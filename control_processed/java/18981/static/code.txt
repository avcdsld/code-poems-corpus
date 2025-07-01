public FeedForwardLayer getLossLayer(InputType type) throws UnsupportedKerasConfigurationException {
        if (type instanceof InputType.InputTypeFeedForward) {
            this.layer = new LossLayer.Builder(loss).name(this.layerName).build();
        }
        else if (type instanceof  InputType.InputTypeRecurrent) {
            this.layer = new RnnLossLayer.Builder(loss).name(this.layerName).build();
        }
        else if (type instanceof InputType.InputTypeConvolutional) {
            this.layer = new CnnLossLayer.Builder(loss).name(this.layerName).build();
        } else {
            throw new UnsupportedKerasConfigurationException("Unsupported output layer type"
                    + "got : " + type.toString());
        }
        return (FeedForwardLayer) this.layer;
    }