def get_json_or_yaml_settings(self, settings_name="zappa_settings"):
        """
        Return zappa_settings path as JSON or YAML (or TOML), as appropriate.
        """
        zs_json = settings_name + ".json"
        zs_yml = settings_name + ".yml"
        zs_yaml = settings_name + ".yaml"
        zs_toml = settings_name + ".toml"

        # Must have at least one
        if not os.path.isfile(zs_json) \
            and not os.path.isfile(zs_yml) \
            and not os.path.isfile(zs_yaml) \
            and not os.path.isfile(zs_toml):
            raise ClickException("Please configure a zappa_settings file or call `zappa init`.")

        # Prefer JSON
        if os.path.isfile(zs_json):
            settings_file = zs_json
        elif os.path.isfile(zs_toml):
            settings_file = zs_toml
        elif os.path.isfile(zs_yml):
            settings_file = zs_yml
        else:
            settings_file = zs_yaml

        return settings_file