protected void updateOrdersAndFireNotification(int startingRow) {
        for (int i = startingRow; i < getElements().size(); i++) {
            getElement(i).setOrder(i + 1);
        }

        fireTableDataChanged();
    }