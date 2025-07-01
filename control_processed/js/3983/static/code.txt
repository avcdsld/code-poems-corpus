function showStatusInfo(statusObj) {
        if (statusObj.target === "initial-download") {
            HealthLogger.sendAnalyticsData(
                autoUpdateEventNames.AUTOUPDATE_DOWNLOAD_START,
                "autoUpdate",
                "download",
                "started",
                ""
            );
            UpdateStatus.modifyUpdateStatus(statusObj);
        }
        UpdateStatus.displayProgress(statusObj);
    }