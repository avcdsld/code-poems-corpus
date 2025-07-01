def set_will(topic, payload, retain = false, qos = 0)
      self.will_topic = topic
      self.will_payload = payload
      self.will_retain = retain
      self.will_qos = qos
    end