def upcase_local_patient_ids
      self.local_patient_id = local_patient_id.upcase if local_patient_id.present?
      (2..5).each{ |index| upcase_local_patient_id(index) }
    end