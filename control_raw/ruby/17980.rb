def ad_insights(range: Date.today..Date.today, level: 'ad', time_increment: 1)
      ad_campaigns.map do |ad_campaign|
        ad_campaign.ad_insights(range: range, level: level, time_increment: time_increment)
      end.flatten
    end