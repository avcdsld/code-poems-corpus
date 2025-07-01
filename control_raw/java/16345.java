@Override
    public void setOrder(char order) {
        Preconditions.checkArgument(order == 'c' || order == 'f', "Order specified must be either c or f: got %s", String.valueOf(order));
        this.order = order;
    }