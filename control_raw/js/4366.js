function _onClick(event) {
            var $scope = $(event.delegateTarget).parent();
            _openEditorForContext({
                path: $scope.data("path"),
                paneId: $scope.data("paneId"),
                cursor: $scope.data("cursor"),
                hideOnOpenFile: true
            });
        }