def wf_distribution_interval?(interval)
      return true if %i[m h d].include?(interval)
      raise Wavefront::Exception::InvalidDistributionInterval
    end