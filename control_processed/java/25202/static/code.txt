public void waitUntilAllWritten(int timeout) throws ExternalFrameConfirmationException {
        final AutoBuffer confirmAb = new AutoBuffer(channel);
        try {
            byte flag = ExternalFrameConfirmationCheck.getConfirmation(confirmAb, timeout);
            assert (flag == ExternalFrameHandler.CONFIRM_WRITING_DONE);
        } catch (TimeoutException ex) {
            throw new ExternalFrameConfirmationException("Timeout for confirmation exceeded!");
        } catch (InterruptedException e) {
            throw new ExternalFrameConfirmationException("Confirmation thread interrupted!");
        } catch (ExecutionException e) {
            throw new ExternalFrameConfirmationException("Confirmation failed!");
        }
    }