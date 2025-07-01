def hierarchical_clusterization_2d(no_clusters = 0, distance_method = 0,
                                       vec = @values, debug = false)
      clusters = []

      if vec.length == 1
        hash = { vec[0] => 1 }
        cluster = PairCluster.new(hash)
        clusters.push(cluster)
        clusters
      end

      # Thresholds
      # threshold_distance = (0.25 * (vec.max-vec.min))
      threshold_density = (0.5 * vec.length).to_i

      # make a histogram from the input vector
      histogram = Hash[vec.group_by { |a| a }.map { |k, vs| [k, vs.length] }]

      # clusters = array of clusters
      # initially each length belongs to a different cluster
      histogram.each do |e|
        warn "pair (#{e[0].x} #{e[0].y}) appears #{e[1]} times" if debug
        hash = { e[0] => e[1] }
        cluster = PairCluster.new(hash)
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
        cluster1     = 0
        cluster2     = 0
        density      = 0

        [*(0..(clusters.length - 2))].each do |i|
          [*((i + 1)..(clusters.length - 1))].each do |j|
            dist = clusters[i].distance(clusters[j], distance_method)
            warn "distance between clusters #{i} and #{j} is #{dist}" if debug
            current_density = clusters[i].density + clusters[j].density
            if dist < min_distance
              min_distance = dist
              cluster1     = i
              cluster2     = j
              density      = current_density
            elsif dist == min_distance && density < current_density
              cluster1 = i
              cluster2 = j
              density  = current_density
            end
          end
        end

        # merge clusters 'cluster1' and 'cluster2'
        warn "clusters to merge #{cluster1} and #{cluster2}" if debug

        clusters[cluster1].add(clusters[cluster2])
        clusters.delete_at(cluster2)

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