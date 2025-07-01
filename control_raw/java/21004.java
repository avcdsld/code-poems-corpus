private JPanel getPanelSession() {
		if (panelSession == null) {

			panelSession = new JPanel();
			panelSession.setLayout(new GridBagLayout());
			panelSession.setName("Ignorespider");

			java.awt.GridBagConstraints gridBagConstraints2 = new GridBagConstraints();
	        java.awt.GridBagConstraints gridBagConstraints1 = new GridBagConstraints();
	        GridBagConstraints gridBagConstraints3 = new GridBagConstraints();

	        javax.swing.JLabel jLabel = new JLabel();

	        jLabel.setText(Constant.messages.getString("session.spider.label.ignore"));
	        gridBagConstraints1.gridx = 0;
	        gridBagConstraints1.gridy = 0;
	        gridBagConstraints1.gridheight = 1;
	        gridBagConstraints1.insets = new java.awt.Insets(10,0,5,0);
	        gridBagConstraints1.anchor = java.awt.GridBagConstraints.NORTHWEST;
	        gridBagConstraints1.fill = java.awt.GridBagConstraints.HORIZONTAL;
	        gridBagConstraints1.weightx = 0.0D;

	        gridBagConstraints2.gridx = 0;
	        gridBagConstraints2.gridy = 1;
	        gridBagConstraints2.weightx = 1.0;
	        gridBagConstraints2.weighty = 1.0;
	        gridBagConstraints2.fill = java.awt.GridBagConstraints.BOTH;
	        gridBagConstraints2.ipadx = 0;
	        gridBagConstraints2.insets = new java.awt.Insets(0,0,0,0);
	        gridBagConstraints2.anchor = java.awt.GridBagConstraints.NORTHWEST;
	        
	        JLabel noteLabel = new JLabel();
	        noteLabel.setText(Constant.messages.getString("options.globalexcludeurl.seeglobalconfig"));

	        gridBagConstraints3.gridx = 0;
	        gridBagConstraints3.gridy = 2;
	        gridBagConstraints3.gridheight = 1;
	        gridBagConstraints3.weightx = 1.0;
	        gridBagConstraints3.weighty = 0.0;
	        gridBagConstraints3.fill = java.awt.GridBagConstraints.HORIZONTAL;
	        gridBagConstraints3.ipadx = 0;
	        gridBagConstraints3.insets = new java.awt.Insets(0,0,0,0);
	        gridBagConstraints3.anchor = java.awt.GridBagConstraints.SOUTH;

	        panelSession.add(jLabel, gridBagConstraints1);
	        panelSession.add(regexesPanel, gridBagConstraints2);
	        panelSession.add(noteLabel, gridBagConstraints3);
		}
		return panelSession;
	}