public static OCSPResp request(URI uri, OCSPReq request, long timeout, TimeUnit unit) throws IOException {
        byte[] encoded = request.getEncoded();

        URL url = uri.toURL();
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        try {
            connection.setConnectTimeout((int) unit.toMillis(timeout));
            connection.setReadTimeout((int) unit.toMillis(timeout));
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestMethod("POST");
            connection.setRequestProperty("host", uri.getHost());
            connection.setRequestProperty("content-type", OCSP_REQUEST_TYPE);
            connection.setRequestProperty("accept", OCSP_RESPONSE_TYPE);
            connection.setRequestProperty("content-length", String.valueOf(encoded.length));

            OutputStream out = connection.getOutputStream();
            try {
                out.write(encoded);
                out.flush();

                InputStream in = connection.getInputStream();
                try {
                    int code = connection.getResponseCode();
                    if (code != HttpsURLConnection.HTTP_OK) {
                        throw new IOException("Unexpected status-code=" + code);
                    }

                    String contentType = connection.getContentType();
                    if (!contentType.equalsIgnoreCase(OCSP_RESPONSE_TYPE)) {
                        throw new IOException("Unexpected content-type=" + contentType);
                    }

                    int contentLength = connection.getContentLength();
                    if (contentLength == -1) {
                        // Probably a terrible idea!
                        contentLength = Integer.MAX_VALUE;
                    }

                    ByteArrayOutputStream baos = new ByteArrayOutputStream();
                    try {
                        byte[] buffer = new byte[8192];
                        int length = -1;

                        while ((length = in.read(buffer)) != -1) {
                            baos.write(buffer, 0, length);

                            if (baos.size() >= contentLength) {
                                break;
                            }
                        }
                    } finally {
                        baos.close();
                    }
                    return new OCSPResp(baos.toByteArray());
                } finally {
                    in.close();
                }
            } finally {
                out.close();
            }
        } finally {
            connection.disconnect();
        }
    }