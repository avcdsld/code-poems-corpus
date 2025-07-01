function isArray(choices)
        {
            choices = (angular.isUndefined(choices)) ? lxSelectChoices.parentCtrl.choices : choices;

            return angular.isArray(choices);
        }