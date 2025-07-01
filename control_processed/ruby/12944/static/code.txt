def file
      contents = certificates.map { |cert| cert.to_pem }.join
      write_file("chain-#{domain}.pem", contents)
    end