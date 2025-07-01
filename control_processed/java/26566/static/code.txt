private String createHandler(TypeElement type, ExecutableElement execute, String[] paths, boolean isRest) {
        FieldSpec hostField = FieldSpec.builder(Object.class, "mHost").addModifiers(Modifier.PRIVATE).build();

        MethodSpec rootMethod = MethodSpec.constructorBuilder()
            .addModifiers(Modifier.PUBLIC)
            .addParameter(Object.class, "host")
            .addParameter(mMapping, "mapping")
            .addParameter(mAddition, "addition")
            .addParameter(boolean.class, "isRest")
            .addStatement("super(host, mapping, addition, isRest)")
            .addStatement("this.mHost = host")
            .build();

        CodeBlock.Builder handleCode = CodeBlock.builder()
            .addStatement("$T context = $T.getContext()", mContext, mAndServer)
            .addStatement("String httpPath = request.getPath()")
            .addStatement("$T httpMethod = request.getMethod()", mHttpMethod)
            .add("\n")
            .addStatement("Object converterObj = request.getAttribute($T.HTTP_MESSAGE_CONVERTER)", mRequest)
            .addStatement("$T converter = null", mConverter)
            .beginControlFlow("if (converterObj != null && converterObj instanceof $T)", mConverter)
            .addStatement("converter = ($T)converterObj", mConverter)
            .endControlFlow()
            .add("\n")
            .addStatement("$T multiRequest = null", mRequestMultipart)
            .beginControlFlow("if (request instanceof $T)", mRequestMultipart)
            .addStatement("multiRequest = ($T) request", mRequestMultipart)
            .endControlFlow()
            .add("\n")
            .addStatement("$T requestBody = null", mRequestBody)
            .beginControlFlow("if (httpMethod.allowBody())")
            .addStatement("requestBody = request.getBody()")
            .endControlFlow()
            .add("\n")
            .addStatement("$T<String, String> pathMap = getPathVariable(httpPath)", Map.class)
            .add("\n")
            .add("/** ---------- Building Parameters ---------- **/ ")
            .add("\n");

        String host = type.getQualifiedName().toString() + "#" + execute.getSimpleName().toString() + "()";
        StringBuilder paramBuild = new StringBuilder();
        List<? extends VariableElement> parameters = execute.getParameters();
        if (!parameters.isEmpty()) {
            for (int i = 0; i < parameters.size(); i++) {
                VariableElement parameter = parameters.get(i);

                TypeName typeName = TypeName.get(parameter.asType());
                if (mContext.equals(typeName)) {
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append("context");
                    continue;
                }

                if (mRequest.equals(typeName)) {
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append("request");
                    continue;
                }

                if (mResponse.equals(typeName)) {
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append("response");
                    continue;
                }

                if (mSession.equals(typeName)) {
                    handleCode.add("\n").addStatement("$T session$L = request.getValidSession()", mSession, i);
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format("session%s", i));
                    continue;
                }

                if (mRequestBody.equals(typeName)) {
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append("requestBody");
                    continue;
                }

                RequestHeader requestHeader = parameter.getAnnotation(RequestHeader.class);
                if (requestHeader != null) {
                    Validate.isTrue(isBasicType(typeName),
                        "The RequestHeader annotation only supports [String, int, long, float, double, boolean] on %s.",
                        host);

                    String name = requestHeader.name();
                    if (StringUtils.isEmpty(name)) name = requestHeader.value();
                    Validate.isTrue(!StringUtils.isEmpty(name), "The name of param is null on %s.", host);

                    handleCode.add("\n").addStatement("String header$LStr = request.getHeader($S)", i, name);
                    if (requestHeader.required()) {
                        handleCode.beginControlFlow("if ($T.isEmpty(header$LStr))", mStringUtils, i)
                            .addStatement("throw new $T($S)", mHeaderMissing, name)
                            .endControlFlow();
                    } else {
                        handleCode.beginControlFlow("if ($T.isEmpty(header$LStr))", mStringUtils, i)
                            .addStatement("header$LStr = $S", i, requestHeader.defaultValue())
                            .endControlFlow();
                    }

                    createParameter(handleCode, typeName, "header", i);
                    assignmentParameter(handleCode, typeName, "header", i, "header", i);

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "header%d", i));
                    continue;
                }

                CookieValue cookieValue = parameter.getAnnotation(CookieValue.class);
                if (cookieValue != null) {
                    Validate.isTrue(mString.equals(typeName), "CookieValue can only be used with [String] on %s.",
                        host);

                    String name = cookieValue.name();
                    if (StringUtils.isEmpty(name)) name = cookieValue.value();
                    Validate.notEmpty(name, "The name of cookie is null on %s.", host);

                    handleCode.add("\n").addStatement("String cookie$L = request.getCookieValue($S)", i, name);
                    if (cookieValue.required()) {
                        handleCode.beginControlFlow("if ($T.isEmpty(cookie$L))", mStringUtils, i)
                            .addStatement("throw new $T($S)", mCookieMissing, name)
                            .endControlFlow();
                    }

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "cookie%d", i));
                    continue;
                }

                PathVariable pathVariable = parameter.getAnnotation(PathVariable.class);
                if (pathVariable != null) {
                    Validate.isTrue(isBasicType(typeName),
                        "The PathVariable annotation only supports [String, int, long, float, double, boolean] on %s.",
                        host);

                    String name = pathVariable.name();
                    if (StringUtils.isEmpty(name)) name = pathVariable.value();
                    Validate.isTrue(!StringUtils.isEmpty(name), "The name of path is null on %s.", host);

                    boolean isBlurred = false;
                    for (String path : paths) {
                        if (path.matches(PATH_BLURRED) && !path.matches(PATH)) {
                            isBlurred = true;
                        }
                    }
                    Validate.isTrue(isBlurred,
                        "The PathVariable annotation must have a blurred path, for example [/project/{name}]. The " +
                            "error occurred on %s.", host);

                    handleCode.add("\n").addStatement("String path$LStr = pathMap.get($S)", i, name);

                    if (pathVariable.required()) {
                        handleCode.beginControlFlow("if ($T.isEmpty(path$LStr))", mStringUtils, i)
                            .addStatement("throw new $T($S)", mPathMissing, name)
                            .endControlFlow();
                    } else {
                        handleCode.beginControlFlow("if ($T.isEmpty(path$LStr))", mStringUtils, i)
                            .addStatement("path$LStr = $S;", i, pathVariable.defaultValue())
                            .endControlFlow();
                    }

                    createParameter(handleCode, typeName, "path", i);
                    assignmentParameter(handleCode, typeName, "path", i, "path", i);

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "path%d", i));
                    continue;
                }

                QueryParam queryParam = parameter.getAnnotation(QueryParam.class);
                if (queryParam != null) {
                    Validate.isTrue(isBasicType(typeName),
                        "The QueryParam annotation only supports [String, int, long, float, double, " +
                            "boolean] on %s.", host);

                    String name = queryParam.name();
                    if (StringUtils.isEmpty(name)) name = queryParam.value();
                    Validate.isTrue(!StringUtils.isEmpty(name), "The name of param is null on %s.", host);

                    handleCode.add("\n").addStatement("String param$LStr = request.getQuery($S)", i, name);
                    if (queryParam.required()) {
                        handleCode.beginControlFlow("if ($T.isEmpty(param$LStr))", mStringUtils, i)
                            .addStatement("throw new $T($S)", mParamMissing, name)
                            .endControlFlow();
                    } else {
                        handleCode.beginControlFlow("if ($T.isEmpty(param$LStr))", mStringUtils, i)
                            .addStatement("param$LStr = $S", i, queryParam.defaultValue())
                            .endControlFlow();
                    }

                    createParameter(handleCode, typeName, "param", i);
                    assignmentParameter(handleCode, typeName, "param", i, "param", i);

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "param%d", i));
                    continue;
                }

                RequestParam requestParam = parameter.getAnnotation(RequestParam.class);
                if (requestParam != null) {
                    boolean valid = mMultipart.equals(typeName) || isBasicType(typeName);
                    Validate.isTrue(valid,
                        "The RequestParam annotation only supports [MultipartFile, String, int, long, float, double, " +
                            "boolean] on %s.", host);

                    String name = requestParam.name();
                    if (StringUtils.isEmpty(name)) name = requestParam.value();
                    Validate.isTrue(!StringUtils.isEmpty(name), "The name of param is null on %s.", host);

                    handleCode.add("\n");
                    if (mMultipart.equals(typeName)) {
                        handleCode.addStatement("$T param$L = null", mMultipart, i)
                            .beginControlFlow("if (multiRequest != null)")
                            .addStatement("param$L = multiRequest.getFile($S)", i, name)
                            .endControlFlow();
                        if (requestParam.required()) {
                            handleCode.beginControlFlow("if (param$L == null)", i)
                                .addStatement("throw new $T($S)", mParamMissing, name)
                                .endControlFlow();
                        }
                    } else {
                        handleCode.addStatement("String param$LStr = request.getParameter($S)", i, name);

                        if (requestParam.required()) {
                            handleCode.beginControlFlow("if ($T.isEmpty(param$LStr))", mStringUtils, i)
                                .addStatement("throw new $T($S)", mParamMissing, name)
                                .endControlFlow();
                        } else {
                            handleCode.beginControlFlow("if ($T.isEmpty(param$LStr))", mStringUtils, i)
                                .addStatement("param$LStr = $S", i, requestParam.defaultValue())
                                .endControlFlow();
                        }

                        createParameter(handleCode, typeName, "param", i);
                        assignmentParameter(handleCode, typeName, "param", i, "param", i);
                    }

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "param%d", i));
                    continue;
                }

                FormPart formPart = parameter.getAnnotation(FormPart.class);
                if (formPart != null) {
                    String name = formPart.name();
                    if (StringUtils.isEmpty(name)) name = formPart.value();
                    Validate.isTrue(!StringUtils.isEmpty(name), "The name of param is null on %s.", host);

                    handleCode.add("\n");
                    if (mMultipart.equals(typeName)) {
                        handleCode.addStatement("$T param$L = null", mMultipart, i)
                            .beginControlFlow("if (multiRequest != null)")
                            .addStatement("param$L = multiRequest.getFile($S)", i, name)
                            .endControlFlow();
                        if (formPart.required()) {
                            handleCode.beginControlFlow("if (param$L == null)", i)
                                .addStatement("throw new $T($S)", mParamMissing, name)
                                .endControlFlow();
                        }
                    } else {
                        TypeName wrapperType = ParameterizedTypeName.get(mTypeWrapper, typeName);
                        handleCode.addStatement("$T param$L = null", typeName, i)
                            .addStatement("$T param$LType = new $T(){}.getType()", Type.class, i, wrapperType)
                            .beginControlFlow("if (converter != null && multiRequest != null)")
                            .addStatement("$T param$LFile = multiRequest.getFile($S)", mMultipart, i, name)
                            .beginControlFlow("if (param$LFile != null)", i)
                            .addStatement("$T stream = param$LFile.getStream()", InputStream.class, i)
                            .addStatement("$T mimeType = param$LFile.getContentType()", mMediaType, i)
                            .addStatement("param$L = converter.convert(stream, mimeType, param$LType)", i, i)
                            .endControlFlow()
                            .beginControlFlow("if (param$L == null)", i)
                            .addStatement("String param$LStr = multiRequest.getParameter($S)", i, name)
                            .beginControlFlow("if (!$T.isEmpty(param$LStr))", mStringUtils, i)
                            .addStatement("$T stream = new $T(param$LStr.getBytes())", InputStream.class,
                                ByteArrayInputStream.class, i)
                            .addStatement("$T mimeType = $T.TEXT_PLAIN", mMediaType, mMediaType)
                            .addStatement("param$L = converter.convert(stream, mimeType, param$LType)", i, i)
                            .endControlFlow()
                            .endControlFlow()
                            .endControlFlow();

                        if (formPart.required()) {
                            handleCode.beginControlFlow("if (param$L == null)", i)
                                .addStatement("throw new $T($S)", mParamMissing, name)
                                .endControlFlow();
                        }
                    }
                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "param%d", i));
                    continue;
                }

                RequestBody requestBody = parameter.getAnnotation(RequestBody.class);
                if (requestBody != null) {
                    handleCode.add("\n");

                    if (mString.equals(typeName)) {
                        handleCode.addStatement("String body$L = requestBody.string()", i);
                    } else {
                        TypeName wrapperType = ParameterizedTypeName.get(mTypeWrapper, typeName);
                        handleCode.addStatement("$T body$L = null", typeName, i)
                            .beginControlFlow("if (converter != null && requestBody != null)")
                            .addStatement("$T body$LType = new $T(){}.getType()", Type.class, i, wrapperType)
                            .addStatement("$T stream = requestBody.stream()", InputStream.class)
                            .addStatement("$T mimeType = requestBody.contentType()", mMediaType)
                            .addStatement("body$L = converter.convert(stream, mimeType, body$LType)", i, i)
                            .endControlFlow();
                    }

                    if (requestBody.required()) {
                        handleCode.beginControlFlow("if (body$L == null)", i)
                            .addStatement("throw new $T()", mBodyMissing)
                            .endControlFlow();
                    }

                    if (paramBuild.length() > 0) paramBuild.append(", ");
                    paramBuild.append(String.format(Locale.getDefault(), "body%d", i));
                    continue;
                }

                throw new IllegalStateException(
                    String.format("The parameter type [%s] is not supported on %s.", typeName, host));
            }
        }

        String executeName = execute.getSimpleName().toString();
        TypeMirror returnMirror = execute.getReturnType();
        handleCode.add("\n").addStatement("Object o = null", type, executeName).beginControlFlow("try");
        if (!TypeKind.VOID.equals(returnMirror.getKind())) {
            handleCode.addStatement("o = (($T)mHost).$L($L)", type, executeName, paramBuild.toString());
        } else {
            handleCode.addStatement("(($T)mHost).$L($L)", type, executeName, paramBuild.toString());
        }
        handleCode.endControlFlow().beginControlFlow("catch (Throwable e)").addStatement("throw e").endControlFlow();
        handleCode.addStatement("return new $T($L, o)", mViewObject, isRest);

        MethodSpec handleMethod = MethodSpec.methodBuilder("handle")
            .addAnnotation(Override.class)
            .addModifiers(Modifier.PUBLIC)
            .returns(mView)
            .addParameter(mRequest, "request")
            .addParameter(mResponse, "response")
            .addException(IOException.class)
            .addCode(handleCode.build())
            .build();


        String packageName = MoreElements.getPackage(type).getQualifiedName().toString();
        executeName = StringUtils.capitalize(executeName);
        String className = String.format("%s%sHandler%s", type.getSimpleName(), executeName, "");
        int i = 0;
        while (mHashCodes.contains(className.hashCode())) {
            i++;
            className = String.format("%s%sHandler%s", type.getSimpleName(), executeName, i);
        }
        mHashCodes.add(className.hashCode());

        TypeSpec handlerClass = TypeSpec.classBuilder(className)
            .addJavadoc(Constants.DOC_EDIT_WARN)
            .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
            .superclass(mMappingHandler)
            .addField(hostField)
            .addMethod(rootMethod)
            .addMethod(handleMethod)
            .build();

        JavaFile javaFile = JavaFile.builder(packageName, handlerClass).build();
        try {
            javaFile.writeTo(mFiler);
            return className;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }