def get_pom_from_heuristic(filename)
      begin
        log.debug("Attempting heuristic POM search for #{filename}")
        site = MavenWebsite.new
        filename = cleanup_name(filename)
        version_matcher = VersionMatcher.new
        my_artifact_id, my_version = version_matcher.split_version(filename)
        log.debug("Guessed artifact id: #{my_artifact_id}, version: #{my_version}")

        result = site.search_by_name(my_artifact_id).first
        log.debug("Artifact id search result: #{result}")
        unless result.nil?
          group_id, artifact_id, = site.get_maven_id_from result
          results = site.search_by_group_id_and_artifact_id(group_id, artifact_id)
          log.debug("All versions: #{results}")
          their_versions = results.map { |doc| doc["v"] }
          best_matched_version = (
            if !my_version.nil?
              version_matcher.best_match(my_version, their_versions)
            else
              their_versions.max
            end
          )
          best_matched_result = (results.select { |r| r["v"] == best_matched_version }).first

          group_id, artifact_id, version = site.get_maven_id_from(best_matched_result)
          log.warn("pom.xml for #{filename} found on search.maven.org with heuristic search\
            (#{group_id}:#{artifact_id}:#{version})"
                  )

          return site.download_pom(group_id, artifact_id, version), :found_via_heuristic
        end
      rescue NotFoundOnMavenWebsiteError
        log.warn("Got a 404 error while looking for #{filename} heuristically in search.maven.org")
      end
      nil
    end