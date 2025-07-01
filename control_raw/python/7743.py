def run_ut_py3_qemu():
    """Run unit tests in the emulator and copy the results back to the host through the mounted
    volume in /mxnet"""
    from vmcontrol import VM
    with VM() as vm:
        qemu_provision(vm.ssh_port)
        logging.info("execute tests")
        qemu_ssh(vm.ssh_port, "./runtime_functions.py", "run_ut_python3_qemu_internal")
        qemu_rsync_to_host(vm.ssh_port, "*.xml", "mxnet")
        logging.info("copied to host")
        logging.info("tests finished, vm shutdown.")
        vm.shutdown()