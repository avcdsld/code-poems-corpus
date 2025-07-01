def get_or_create_head_node(config, config_file, no_restart, restart_only, yes,
                            override_cluster_name):
    """Create the cluster head node, which in turn creates the workers."""
    provider = get_node_provider(config["provider"], config["cluster_name"])
    try:
        head_node_tags = {
            TAG_RAY_NODE_TYPE: "head",
        }
        nodes = provider.non_terminated_nodes(head_node_tags)
        if len(nodes) > 0:
            head_node = nodes[0]
        else:
            head_node = None

        if not head_node:
            confirm("This will create a new cluster", yes)
        elif not no_restart:
            confirm("This will restart cluster services", yes)

        launch_hash = hash_launch_conf(config["head_node"], config["auth"])
        if head_node is None or provider.node_tags(head_node).get(
                TAG_RAY_LAUNCH_CONFIG) != launch_hash:
            if head_node is not None:
                confirm("Head node config out-of-date. It will be terminated",
                        yes)
                logger.info(
                    "get_or_create_head_node: "
                    "Terminating outdated head node {}".format(head_node))
                provider.terminate_node(head_node)
            logger.info("get_or_create_head_node: Launching new head node...")
            head_node_tags[TAG_RAY_LAUNCH_CONFIG] = launch_hash
            head_node_tags[TAG_RAY_NODE_NAME] = "ray-{}-head".format(
                config["cluster_name"])
            provider.create_node(config["head_node"], head_node_tags, 1)

        nodes = provider.non_terminated_nodes(head_node_tags)
        assert len(nodes) == 1, "Failed to create head node."
        head_node = nodes[0]

        # TODO(ekl) right now we always update the head node even if the hash
        # matches. We could prompt the user for what they want to do here.
        runtime_hash = hash_runtime_conf(config["file_mounts"], config)
        logger.info("get_or_create_head_node: Updating files on head node...")

        # Rewrite the auth config so that the head node can update the workers
        remote_key_path = "~/ray_bootstrap_key.pem"
        remote_config = copy.deepcopy(config)
        remote_config["auth"]["ssh_private_key"] = remote_key_path

        # Adjust for new file locations
        new_mounts = {}
        for remote_path in config["file_mounts"]:
            new_mounts[remote_path] = remote_path
        remote_config["file_mounts"] = new_mounts
        remote_config["no_restart"] = no_restart

        # Now inject the rewritten config and SSH key into the head node
        remote_config_file = tempfile.NamedTemporaryFile(
            "w", prefix="ray-bootstrap-")
        remote_config_file.write(json.dumps(remote_config))
        remote_config_file.flush()
        config["file_mounts"].update({
            remote_key_path: config["auth"]["ssh_private_key"],
            "~/ray_bootstrap_config.yaml": remote_config_file.name
        })

        if restart_only:
            init_commands = config["head_start_ray_commands"]
        elif no_restart:
            init_commands = config["head_setup_commands"]
        else:
            init_commands = (config["head_setup_commands"] +
                             config["head_start_ray_commands"])

        updater = NodeUpdaterThread(
            node_id=head_node,
            provider_config=config["provider"],
            provider=provider,
            auth_config=config["auth"],
            cluster_name=config["cluster_name"],
            file_mounts=config["file_mounts"],
            initialization_commands=config["initialization_commands"],
            setup_commands=init_commands,
            runtime_hash=runtime_hash,
        )
        updater.start()
        updater.join()

        # Refresh the node cache so we see the external ip if available
        provider.non_terminated_nodes(head_node_tags)

        if config.get("provider", {}).get("use_internal_ips", False) is True:
            head_node_ip = provider.internal_ip(head_node)
        else:
            head_node_ip = provider.external_ip(head_node)

        if updater.exitcode != 0:
            logger.error("get_or_create_head_node: "
                         "Updating {} failed".format(head_node_ip))
            sys.exit(1)
        logger.info(
            "get_or_create_head_node: "
            "Head node up-to-date, IP address is: {}".format(head_node_ip))

        monitor_str = "tail -n 100 -f /tmp/ray/session_*/logs/monitor*"
        use_docker = bool(config["docker"]["container_name"])
        if override_cluster_name:
            modifiers = " --cluster-name={}".format(
                quote(override_cluster_name))
        else:
            modifiers = ""
        print("To monitor auto-scaling activity, you can run:\n\n"
              "  ray exec {} {}{}{}\n".format(
                  config_file, "--docker " if use_docker else " ",
                  quote(monitor_str), modifiers))
        print("To open a console on the cluster:\n\n"
              "  ray attach {}{}\n".format(config_file, modifiers))

        print("To ssh manually to the cluster, run:\n\n"
              "  ssh -i {} {}@{}\n".format(config["auth"]["ssh_private_key"],
                                           config["auth"]["ssh_user"],
                                           head_node_ip))
    finally:
        provider.cleanup()