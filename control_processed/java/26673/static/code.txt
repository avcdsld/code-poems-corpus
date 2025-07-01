private static Audit getCodeQualityAudit(JSONArray jsonArray, JSONArray global) {

        LOGGER.info("NFRR Audit Collector auditing CODE_QUALITY");
        Audit audit = new Audit();
        audit.setType(AuditType.CODE_QUALITY);
        Audit basicAudit;
        if ((basicAudit = doBasicAuditCheck(jsonArray, global, AuditType.CODE_QUALITY)) != null) {
            return basicAudit;
        }
        audit.setAuditStatus(AuditStatus.OK);
        audit.setDataStatus(DataStatus.OK);
        for (Object o : jsonArray) {
            Optional<Object> urlOptObj = Optional.ofNullable(((JSONObject) o).get(STR_URL));
            urlOptObj.ifPresent(urlObj -> audit.getUrl().add(urlOptObj.get().toString()));
            JSONArray auditJO = (JSONArray) ((JSONObject) o).get(STR_AUDITSTATUSES);
            auditJO.stream().map(aj -> audit.getAuditStatusCodes().add((String) aj));
            boolean ok = false;
            for (Object s : auditJO) {
                String status = (String) s;
                audit.getAuditStatusCodes().add(status);
                if (CodeQualityAuditStatus.CODE_QUALITY_AUDIT_OK.name().equalsIgnoreCase(status)) {
                    ok = true;
                    break;
                }
                if (CodeQualityAuditStatus.CODE_QUALITY_DETAIL_MISSING.name().equalsIgnoreCase(status)) {
                    audit.setAuditStatus(AuditStatus.NA);
                    audit.setDataStatus(DataStatus.NO_DATA);
                    return audit;
                }
            }
            if (!ok) {
                audit.setAuditStatus(AuditStatus.FAIL);
                return audit;
            }
        }
        return audit;
    }