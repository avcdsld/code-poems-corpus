def user_filters
      @user_filters ||= begin
        conditions = ['model_class_name = ?', self.model_class_name]

        if WillFilter::Config.user_filters_enabled?
          conditions[0] << ' and user_id = ? '
          if WillFilter::Config.current_user and WillFilter::Config.current_user.id
            conditions << WillFilter::Config.current_user.id
          else
            conditions << '0'
          end
        end

        if WillFilter::Config.project_filters_enabled?
          conditions[0] << ' and project_id = ? '
          if WillFilter::Config.current_project and WillFilter::Config.current_project.id
            conditions << WillFilter::Config.current_project.id
          else
            conditions << '0'
          end
        end

        WillFilter::Filter.where(conditions)
      end
    end