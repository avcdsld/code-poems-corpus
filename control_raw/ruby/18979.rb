def hierarchical_clusterization(no_clusters = 0, distance_method = 0,
                                    vec = @values, debug = false)
      clusters = []
      vec = vec.sort

      if vec.length == 1
        hash    = { vec[0] => 1 }
        cluster = Cluster.new(hash)
        clusters.push(cluster)
        clusters
      end

      # Thresholds
      threshold_distance = (0.25 * (vec.max - vec.min))
      threshold_density  = (0.5 * vec.length).to_i

      # make a histogram from the input vector
      histogram = Hash[vec.group_by { |x| x }.map { |k, vs| [k, vs.length] }]

      # clusters = array of clusters
      # initially each length belongs to a different cluster
      histogram.sort_by { |a| a[0] }.each do |elem|
        warn "len #{elem[0]} appears #{elem[1]} times" if debug
        hash = { elem[0] => elem[1] }
        cluster = Cluster.new(hash)
        clusters.push(cluster)
      end

      clusters.each(&:print) if debug

      return clusters if clusters.length == 1

      # each iteration merge the closest two adiacent cluster
      # the loop stops according to the stop conditions
      iteration = 0
      loop do
        # stop condition 1
        break if no_clusters != 0 && clusters.length == no_clusters

        iteration += iteration
        warn "\nIteration #{iteration}" if debug

        min_distance = 100_000_000
        cluster      = 0
        density      = 0

        clusters[0..clusters.length - 2].each_with_index do |_item, i|
          dist = clusters[i].distance(clusters[i + 1], distance_method)
          warn "distance btwn clusters #{i} and #{i + 1} is #{dist}" if debug
          current_density = clusters[i].density + clusters[i + 1].density
          if dist < min_distance
            min_distance = dist
            cluster = i
            density = current_density
          elsif dist == min_distance && density < current_density
            cluster = i
            density = current_density
          end
        end

        # stop condition 2
        # the distance between the closest clusters exceeds the threshold
        if no_clusters == 0 && (clusters[cluster].mean - clusters[cluster + 1].mean).abs > threshold_distance
          break
        end

        # merge clusters 'cluster' and 'cluster'+1
        warn "clusters to merge #{cluster} and #{cluster + 1}" if debug

        clusters[cluster].add(clusters[cluster + 1])
        clusters.delete_at(cluster + 1)

        if debug
          clusters.each_with_index do |elem, i|
            warn "cluster #{i}"
            elem.print
          end
        end

        # stop condition 3
        # the density of the biggest clusters exceeds the threshold
        if no_clusters == 0 && clusters[cluster].density > threshold_density
          break
        end
      end

      @clusters = clusters
    end