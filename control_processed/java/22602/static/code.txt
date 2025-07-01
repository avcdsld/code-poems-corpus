public void create(final Node node) {
        Assert.assertNotNull(node);
        transactionTemplate.execute(new TransactionCallbackWithoutResult() {

            protected void doInTransactionWithoutResult(TransactionStatus status) {

                try {
                    NodeDO nodeDo = modelToDo(node);
                    nodeDo.setId(0L);
                    if (!nodeDao.checkUnique(nodeDo)) {
                        String exceptionCause = "exist the same repeat node in the database.";
                        logger.warn("WARN ## " + exceptionCause);
                        throw new RepeatConfigureException(exceptionCause);
                    }
                    nodeDao.insert(nodeDo);

                } catch (RepeatConfigureException rce) {
                    throw rce;
                } catch (Exception e) {
                    logger.error("ERROR ## create node has an exception!");
                    throw new ManagerException(e);
                }
            }
        });
    }