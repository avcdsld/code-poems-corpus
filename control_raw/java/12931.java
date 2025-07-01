public void setResourceNamesOnProcessDefinitions(ParsedDeployment parsedDeployment) {
    for (ProcessDefinitionEntity processDefinition : parsedDeployment.getAllProcessDefinitions()) {
      String resourceName = parsedDeployment.getResourceForProcessDefinition(processDefinition).getName();
      processDefinition.setResourceName(resourceName);
    }
  }