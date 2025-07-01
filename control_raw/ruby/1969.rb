def routes(rails_router)
      load!
      Router.new(router: rails_router, namespaces: namespaces).apply
    end