def update
      @sub_tenant = MnoEnterprise::SubTenant.find(params[:id])

      if @sub_tenant.update(sub_tenant_params)
        @sub_tenant_clients = @sub_tenant.clients
        @sub_tenant_account_managers = @sub_tenant.account_managers
        render :show
      else
        render json: @sub_tenant.errors, status: :bad_request
      end
    end