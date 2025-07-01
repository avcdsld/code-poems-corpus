def send_keys(self, keysToSend):
        """
        Send Keys to the Alert.

        :Args:
         - keysToSend: The text to be sent to Alert.


        """
        if self.driver.w3c:
            self.driver.execute(Command.W3C_SET_ALERT_VALUE, {'value': keys_to_typing(keysToSend),
                                                              'text': keysToSend})
        else:
            self.driver.execute(Command.SET_ALERT_VALUE, {'text': keysToSend})