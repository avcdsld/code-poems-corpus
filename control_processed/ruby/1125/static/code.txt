def resources(name)
      get "#{name}", to: "#{name}#index"
      get "#{name}/new", to: "#{name}#new" unless api_mode?
      get "#{name}/:id", to: "#{name}#show"
      post "#{name}", to: "#{name}#create"
      get "#{name}/:id/edit", to: "#{name}#edit" unless api_mode?
      put "#{name}/:id", to: "#{name}#update"
      post "#{name}/:id", to: "#{name}#update" # for binary uploads
      patch "#{name}/:id", to: "#{name}#update"
      delete "#{name}/:id", to: "#{name}#delete"
    end