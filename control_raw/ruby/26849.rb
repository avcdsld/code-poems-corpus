def generate(driver, _options = {})
      round = guess_round driver

      teams_padded = Algorithm::Util.padd_teams_pow2 driver.seeded_teams
      teams_seeded = Algorithm::DoubleBracket.seed teams_padded

      teams = if driver.matches.empty?
                teams_seeded
              else
                get_round_teams driver, round, teams_seeded
              end

      driver.create_matches Algorithm::GroupPairing.adjacent(teams)
    end