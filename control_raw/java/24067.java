public static SofaResponse buildSofaErrorResponse(String errorMsg) {
        SofaResponse sofaResponse = new SofaResponse();
        sofaResponse.setErrorMsg(errorMsg);

        return sofaResponse;
    }