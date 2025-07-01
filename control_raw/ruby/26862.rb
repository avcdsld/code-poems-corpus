def generate(driver, options = {})
      round = options[:round] || guess_round(driver)

      teams = Algorithm::Util.padd_teams_even(driver.seeded_teams)

      matches = Algorithm::RoundRobin.round_robin_pairing(teams, round)

      create_matches driver, matches, round
    end