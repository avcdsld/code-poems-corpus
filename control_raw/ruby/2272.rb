def random_score(seed = Time.now, options = {})
      scoring = options.merge(random_score: {seed: seed.to_i})
      chain { criteria.update_scores scoring }
    end