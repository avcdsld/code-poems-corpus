public void refreshCachedValues() {
        if (noteColumn) {
            note = getHistoryReference().hasNote();
        }
        if (tagsColumn) {
            tags = listToCsv(getHistoryReference().getTags());
        }
        if (highestAlertColumn) {
            alertRiskCellItem = AlertRiskTableCellItem.getItemForRisk(getHistoryReference().getHighestAlert());
        }
    }