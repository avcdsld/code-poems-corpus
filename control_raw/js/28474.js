function(props) {
            var entityNamespace = utils.namespaceFromProperties(props);
            return new root.FiredAlertGroup(this.service, props.name, entityNamespace);
        }