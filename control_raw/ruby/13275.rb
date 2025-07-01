def export_results(results)
      CSV.open("job_results_#{ruby}_#{servers}s_#{workers}w_v#{version}.csv", 'wb') do |csv|
        csv << results.first.keys
        results.each { |result| csv << result.values }
      end
    end