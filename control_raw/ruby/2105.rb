def update_ptr_record(record_name, ip_address)
      reverse_domain = reverse_domain(ip_address)
      reverse_host = reverse_host(ip_address)

      rdomain = Models::Dns::Domain.safe_find_or_create(name: reverse_domain, type: 'NATIVE')

      Models::Dns::Record.find_or_create(
        domain: rdomain,
        name: reverse_domain,
        type: 'SOA', content: SOA,
        ttl: TTL_4H
      )

      Models::Dns::Record.find_or_create(
        domain: rdomain,
        name: reverse_domain,
        type: 'NS', ttl: TTL_4H,
        content: "ns.#{@domain_name}"
      )

      record = Models::Dns::Record.find_or_create(content: record_name, type: 'PTR')
      record.update(
        domain: rdomain,
        name: reverse_host,
        content: record_name,
        type: 'PTR',
        ttl: TTL_5M,
        change_date: Time.now.to_i
      )
    end