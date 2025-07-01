def fire_phantom
      Process::detach fork { Phantom.new(@request.url.sub(%r{\.pdf$}, ''), @options, @request.cookies).to_pdf(render_to) }
    end