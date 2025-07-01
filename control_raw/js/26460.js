function(e, ui) {
      var logEntry = {
        ID: $scope.sortingLog.length + 1,
        Text: 'Moved element: ' + ui.item.scope().item.text
      };
      $scope.sortingLog.push(logEntry);
    }