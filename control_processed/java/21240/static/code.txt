private PopupEncoder2Menu getPopupMenuEncode() {
        if (popupEncodeMenu== null) {
            popupEncodeMenu = new PopupEncoder2Menu();
            popupEncodeMenu.setText(Constant.messages.getString("enc2.popup"));
            popupEncodeMenu.addActionListener(new java.awt.event.ActionListener() {
                @Override
                public void actionPerformed(java.awt.event.ActionEvent e) {
                    showEncodeDecodeDialog(popupEncodeMenu.getLastInvoker());
                    
                }
            });
        }
        return popupEncodeMenu;
    }