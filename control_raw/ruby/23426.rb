def connec_version(organization)
      @@connec_version = Rails.cache.fetch("connec_version_#{organization.tenant}", namespace: 'maestrano', expires_in: 1.day) do
        response = get_client(organization).class.get("#{Maestrano[organization.tenant].param('connec.host')}/version", headers: {'Accept' => 'application/json'})
        response = JSON.parse(response.body)
        @@connec_version = response['ci_branch'].delete('v')
      end
      @@connec_version
    end