def one_translation_per_lang_per_key
      translation_exists = Translation.exists?(
        lang: self.lang,
        translator_id: self.translator.id,
        translator_type: self.translator.class.name,
        translation_key_id: self.key.id
      )

      unless translation_exists
        true
      else
        false
        self.errors.add(:lang, I18n.t('.one_translation_per_lang_per_key'))
      end
    end