public static boolean checkForServiceAccount(String userLdapDN, ApiSettings settings,Map<String,String> allowedUsers,String author,List<String> commitFiles,boolean isCommit,AuditReviewResponse auditReviewResponse) {
        List<String> serviceAccountOU = settings.getServiceAccountOU();
        boolean isValid = false;
        if(!MapUtils.isEmpty(allowedUsers) && isCommit){
            isValid = isValidServiceAccount(author,allowedUsers,commitFiles);
            if(isValid){
                auditReviewResponse.addAuditStatus(CodeReviewAuditStatus.DIRECT_COMMIT_CHANGE_WHITELISTED_ACCOUNT);
            }
        }
        if (!CollectionUtils.isEmpty(serviceAccountOU) && StringUtils.isNotBlank(userLdapDN) && !isValid) {
            try {
                String userLdapDNParsed = LdapUtils.getStringValue(new LdapName(userLdapDN), "OU");
                List<String> matches = serviceAccountOU.stream().filter(it -> it.contains(userLdapDNParsed)).collect(Collectors.toList());
                isValid =  CollectionUtils.isNotEmpty(matches);
            } catch (InvalidNameException e) {
                LOGGER.error("Error parsing LDAP DN:" + userLdapDN);
            }
        }
        else {
            LOGGER.info("API Settings missing service account RDN");
        }
        return isValid;
    }