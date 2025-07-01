private void checkChoices(Option o, Map<String, String> data) throws RequiredParametersException {
		if (o.getChoices().size() > 0 && !o.getChoices().contains(data.get(o.getName()))) {
			throw new RequiredParametersException("Value " + data.get(o.getName()) +
					" is not in the list of valid choices for key " + o.getName());
		}
	}