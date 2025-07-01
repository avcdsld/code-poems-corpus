def ensure_exposed(cidr)
      # configure new address
      # these will be added alongside any existing addresses
      if @executor_pool.expose(cidr)
        info "Exposed host node at cidr=#{cidr}"
      else
        error "Failed to expose host node at cidr=#{cidr}"
      end

      # cleanup any old addresses
      @executor_pool.ps('weave:expose') do |name, mac, *cidrs|
        cidrs.each do |exposed_cidr|
          if exposed_cidr != cidr
            warn "Migrating host node from cidr=#{exposed_cidr}"
            @executor_pool.hide(exposed_cidr)
          end
        end
      end
    end