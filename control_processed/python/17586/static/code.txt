def on_action_end(self, action, logs={}):
        """ Called at end of each action for each callback in callbackList"""
        for callback in self.callbacks:
            if callable(getattr(callback, 'on_action_end', None)):
                callback.on_action_end(action, logs=logs)