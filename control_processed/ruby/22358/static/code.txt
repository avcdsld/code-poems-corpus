def call
      list = []

      @activity.audiences.each do |audience|
        if audience.public?
          message = I18n.t("tooltip.public",
                           scope: "socializer.activities.audiences.index")
          return [message]
        end

        list.concat(audience_list(audience: audience))
      end

      list.unshift(@activity.activitable_actor.activitable.display_name)
    end