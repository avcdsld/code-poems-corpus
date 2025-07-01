private void setHelpEnabled(boolean enabled) {
		if (getView() == null) {
			return;
		}

		JRootPane rootPane = getView().getMainFrame().getRootPane();
		if (enabled && findHelpSetUrl() != null) {
			createHelpBroker();

			loadAddOnHelpSets(ExtensionFactory.getAddOnLoader().getAddOnCollection().getInstalledAddOns());

			getMenuHelpZapUserGuide().addActionListener(showHelpActionListener);
			getMenuHelpZapUserGuide().setToolTipText(null);
			getMenuHelpZapUserGuide().setEnabled(true);

			// Enable the top level F1 help key
			hb.enableHelpKey(rootPane, "zap.intro", hs, "javax.help.SecondaryWindow", null);

			for (Entry<JComponent, String> entry : componentsWithHelp.entrySet()) {
				hb.enableHelp(entry.getKey(), entry.getValue(), hs);
			}

			getHelpButton().setToolTipText(Constant.messages.getString("help.button.tooltip"));
			getHelpButton().setEnabled(true);

		} else {
			String toolTipNoHelp = Constant.messages.getString("help.error.nohelp");
			getMenuHelpZapUserGuide().setEnabled(false);
			getMenuHelpZapUserGuide().setToolTipText(toolTipNoHelp);
			getMenuHelpZapUserGuide().removeActionListener(showHelpActionListener);

			rootPane.unregisterKeyboardAction(KeyStroke.getKeyStroke(KeyEvent.VK_HELP, 0));
			rootPane.unregisterKeyboardAction(KeyStroke.getKeyStroke(KeyEvent.VK_F1, 0));
			removeHelpProperties(rootPane);

			for (JComponent component : componentsWithHelp.keySet()) {
				removeHelpProperties(component);
			}

			getHelpButton().setEnabled(false);
			getHelpButton().setToolTipText(toolTipNoHelp);

			hb = null;
			hs = null;
			showHelpActionListener = null;
		}
	}