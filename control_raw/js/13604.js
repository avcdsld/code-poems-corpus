function (lightGroup) {
        var prevLightNumber = this._previousLightNumber;
        var currentLightNumber = this._lightNumber;
        // PENDING Performance
        for (var type in currentLightNumber[lightGroup]) {
            if (!prevLightNumber[lightGroup]) {
                return true;
            }
            if (currentLightNumber[lightGroup][type] !== prevLightNumber[lightGroup][type]) {
                return true;
            }
        }
        for (var type in prevLightNumber[lightGroup]) {
            if (!currentLightNumber[lightGroup]) {
                return true;
            }
            if (currentLightNumber[lightGroup][type] !== prevLightNumber[lightGroup][type]) {
                return true;
            }
        }
        return false;
    }