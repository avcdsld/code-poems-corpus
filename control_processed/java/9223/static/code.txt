@Override
    public void disconnect() {
        if (kafkaConsumer != null) {
            kafkaConsumer.close();
            kafkaConsumer = null;
        }
        if (kafkaConsumer2 != null) {
            kafkaConsumer2.close();
            kafkaConsumer2 = null;
        }

        connected = false;
    }