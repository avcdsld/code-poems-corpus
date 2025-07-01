@Override
    public List<Team> getBoards() {
        int count = 0;
        int startAt = 0;
        boolean isLast = false;
        List<Team> result = new ArrayList<>();
        while (!isLast) {
            String url = featureSettings.getJiraBaseUrl() + (featureSettings.getJiraBaseUrl().endsWith("/") ? "" : "/")
                    + BOARD_TEAMS_REST_SUFFIX + "?startAt=" + startAt;
            try {
                ResponseEntity<String> responseEntity = makeRestCall(url);
                String responseBody = responseEntity.getBody();
                JSONObject teamsJson = (JSONObject) parser.parse(responseBody);

                if (teamsJson != null) {
                    JSONArray valuesArray = (JSONArray) teamsJson.get("values");
                    if (!CollectionUtils.isEmpty(valuesArray)) {
                        for (Object obj : valuesArray) {
                            JSONObject jo = (JSONObject) obj;
                            String teamId = getString(jo, "id");
                            String teamName = getString(jo, "name");
                            String teamType = getString(jo, "type");
                            Team team = new Team(teamId, teamName);
                            team.setTeamType(teamType);
                            team.setChangeDate("");
                            team.setAssetState("Active");
                            team.setIsDeleted("False");
                            result.add(team);
                            count = count + 1;
                        }
                        isLast = (boolean) teamsJson.get("isLast");
                        LOGGER.info("JIRA Collector collected " + count + " boards");
                        if (!isLast) {
                            startAt += JIRA_BOARDS_PAGING;
                        }
                    } else {
                        isLast = true;
                    }
                } else {
                    isLast = true;
                }
            } catch (ParseException pe) {
                isLast = true;
                LOGGER.error("Parser exception when parsing teams", pe);
            } catch (HygieiaException | HttpClientErrorException | HttpServerErrorException e) {
                isLast = true;
                LOGGER.error("Error in calling JIRA API: " + url , e.getMessage());
            }
        }
        return result;
    }