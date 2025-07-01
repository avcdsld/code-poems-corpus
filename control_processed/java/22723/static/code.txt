public void createOrUpdate(SystemParameter systemParameter) {
        Assert.assertNotNull(systemParameter);
        try {
            SystemParameterDO systemParameterDo = modelToDo(systemParameter);
            systemParameterDo.setId(1L);
            systemParameterDao.insert(systemParameterDo); // 底层使用merge sql，不需要判断update
        } catch (Exception e) {
            logger.error("ERROR ## create SystemParameter has an exception!");
            throw new ManagerException(e);
        }
    }