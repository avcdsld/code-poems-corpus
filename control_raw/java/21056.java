private void initialize() {
		this.setLayout(new CardLayout());
		this.setSize(474, 251);
		this.setName(Constant.messages.getString("httpsessions.panel.title"));
		this.setIcon(new ImageIcon(HttpSessionsPanel.class.getResource("/resource/icon/16/session.png")));
		this.setDefaultAccelerator(extension.getView().getMenuShortcutKeyStroke(
				KeyEvent.VK_H, KeyEvent.ALT_DOWN_MASK | KeyEvent.SHIFT_DOWN_MASK, false));
		this.setMnemonic(Constant.messages.getChar("httpsessions.panel.mnemonic"));
		this.add(getPanelCommand(), getPanelCommand().getName());
	}