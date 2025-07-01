private void refreshValidIssues(FeatureCollector collector, List<Team> teams, Set<Scope> scopes) {
        long refreshValidIssuesStart = System.currentTimeMillis();
        List<String> lookUpIds = Objects.equals(collector.getMode(), JiraMode.Board) ? teams.stream().map(Team::getTeamId).collect(Collectors.toList()) : scopes.stream().map(Scope::getpId).collect(Collectors.toList());
        lookUpIds.forEach(l -> {
            LOGGER.info("Refreshing issues for " + collector.getMode() + " ID:" + l);
            List<String> issueIds = jiraClient.getAllIssueIds(l, collector.getMode());
            List<Feature> existingFeatures = Objects.equals(collector.getMode(), JiraMode.Board) ? featureRepository.findAllByCollectorIdAndSTeamID(collector.getId(), l) : featureRepository.findAllByCollectorIdAndSProjectID(collector.getId(), l);
            List<Feature> deletedFeatures = existingFeatures.stream().filter(e -> !issueIds.contains(e.getsId())).collect(Collectors.toList());
            deletedFeatures.forEach(d -> {
                LOGGER.info("Deleting Feature " + d.getsId() + ':' + d.getsName());
                featureRepository.delete(d);
            });
        });
        log(collector.getMode() + " Issues Refreshed ", refreshValidIssuesStart);
    }