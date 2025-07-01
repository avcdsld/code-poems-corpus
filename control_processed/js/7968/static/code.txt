function createDefaultToolbar(oCreationRow) {
		return new OverflowToolbar({
			content: [
				new ToolbarSpacer(),
				new Button({
					text: TableUtils.getResourceText("TBL_CREATIONROW_APPLY"),
					type: MLibrary.ButtonType.Emphasized,
					enabled: oCreationRow.getApplyEnabled(),
					press: function() {
						oCreationRow._fireApply();
					}
				})
			],
			style: MLibrary.ToolbarStyle.Clear,
			ariaLabelledBy: [oCreationRow.getId() + "-label"]
		});
	}