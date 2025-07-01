private void initialize() {
		this.setLayout(new CardLayout());
		this.setName(buildName(getContextIndex()));
		this.setLayout(new GridBagLayout());
		this.setBorder(new EmptyBorder(2, 2, 2, 2));

		this.add(new JLabel(LABEL_DESCRIPTION), LayoutHelper.getGBC(0, 0, 1, 1.0D));

		// Method type combo box
		this.add(new JLabel(FIELD_LABEL_TYPE_SELECT),
				LayoutHelper.getGBC(0, 1, 1, 1.0D, new Insets(20, 0, 5, 5)));
		this.add(getAuthenticationMethodsComboBox(), LayoutHelper.getGBC(0, 2, 1, 1.0D));

		// Method config panel container
		this.add(getConfigContainerPanel(), LayoutHelper.getGBC(0, 3, 1, 1.0d, new Insets(10, 0, 10, 0)));

		// Logged In/Out indicators
		this.add(new JLabel(FIELD_LABEL_LOGGED_IN_INDICATOR), LayoutHelper.getGBC(0, 4, 1, 1.0D));
		this.add(getLoggedInIndicaterRegexField(), LayoutHelper.getGBC(0, 5, 1, 1.0D));
		this.add(new JLabel(FIELD_LABEL_LOGGED_OUT_INDICATOR), LayoutHelper.getGBC(0, 6, 1, 1.0D));
		this.add(getLoggedOutIndicaterRegexField(), LayoutHelper.getGBC(0, 7, 1, 1.0D));

		// Padding
		this.add(new JLabel(), LayoutHelper.getGBC(0, 99, 1, 1.0D, 1.0D));
	}