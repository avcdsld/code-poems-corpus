def invalid_request_content(message):
        """
        Creates a Lambda Service InvalidRequestContent Response

        Parameters
        ----------
        message str
            Message to be added to the body of the response

        Returns
        -------
        Flask.Response
            A response object representing the InvalidRequestContent Error
        """
        exception_tuple = LambdaErrorResponses.InvalidRequestContentException

        return BaseLocalService.service_response(
            LambdaErrorResponses._construct_error_response_body(LambdaErrorResponses.USER_ERROR, message),
            LambdaErrorResponses._construct_headers(exception_tuple[0]),
            exception_tuple[1]
        )