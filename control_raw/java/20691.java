private JPanel getJPanel() {
		if (jPanel == null) {
			GridBagConstraints gridBagConstraints12 = new GridBagConstraints();
			java.awt.GridBagConstraints gridBagConstraints11 = new GridBagConstraints();

			java.awt.GridBagConstraints gridBagConstraints6 = new GridBagConstraints();

			ZapLabel descLabel = new ZapLabel();
			descLabel.setLineWrap(true);
			descLabel.setWrapStyleWord(true);
			descLabel.setText(Constant.messages.getString("history.filter.label.desc"));
			
			jPanel = new JPanel();
			jPanel.setLayout(new GridBagLayout());

			gridBagConstraints6.gridwidth = 3;
			gridBagConstraints6.gridx = 0;
			gridBagConstraints6.gridy = 3;
			gridBagConstraints6.insets = new java.awt.Insets(5,2,5,2);
			gridBagConstraints6.ipadx = 3;
			gridBagConstraints6.ipady = 3;
			gridBagConstraints11.gridx = 0;
			gridBagConstraints11.gridy = 0;
			gridBagConstraints11.insets = new java.awt.Insets(5,10,5,10);
			gridBagConstraints11.weightx = 1.0D;
			gridBagConstraints11.gridwidth = 3;
			gridBagConstraints11.anchor = java.awt.GridBagConstraints.WEST;
			gridBagConstraints11.fill = java.awt.GridBagConstraints.HORIZONTAL;
			gridBagConstraints11.ipadx = 3;
			gridBagConstraints11.ipady = 3;
			gridBagConstraints12.gridx = 0;
			gridBagConstraints12.weighty = 1.0D;
			gridBagConstraints12.gridwidth = 3;
			gridBagConstraints12.gridy = 2;
			gridBagConstraints12.fill = java.awt.GridBagConstraints.BOTH;
			gridBagConstraints12.insets = new java.awt.Insets(2,10,2,10);
			gridBagConstraints12.ipadx = 0;
			gridBagConstraints12.ipady = 1;
			jPanel.add(descLabel, gridBagConstraints11);
			jPanel.add(getJPanel2(), gridBagConstraints12);
			jPanel.add(getJPanel1(), gridBagConstraints6);
		}
		return jPanel;
	}