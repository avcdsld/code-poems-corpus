function(props) {
            var entityNamespace = utils.namespaceFromProperties(props);
            return new root.StoragePassword(this.service, props.name, entityNamespace);
        }