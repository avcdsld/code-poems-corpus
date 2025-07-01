def _digest(x, n)
      # Use 'first' and 'last' instead of min/max because of performance reasons
      # This works because RBTree is sorted
      min = @centroids.first
      max = @centroids.last

      min = min.nil? ? nil : min[1]
      max = max.nil? ? nil : max[1]
      nearest = find_nearest(x)

      @n += n

      if nearest && nearest.mean == x
        _add_weight(nearest, x, n)
      elsif nearest == min
        _new_centroid(x, n, 0)
      elsif nearest == max
        _new_centroid(x, n, @n)
      else
        p = nearest.mean_cumn.to_f / @n
        max_n = (4 * @n * @delta * p * (1 - p)).floor
        if max_n - nearest.n >= n
          _add_weight(nearest, x, n)
        else
          _new_centroid(x, n, nearest.cumn)
        end
      end

      _cumulate(false)

      # If the number of centroids has grown to a very large size,
      # it may be due to values being inserted in sorted order.
      # We combat that by replaying the centroids in random order,
      # which is what compress! does
      compress! if @centroids.size > (@k / @delta)

      nil
    end