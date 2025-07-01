def star(poly, trans, draw)
      x, y, n = poly.x, poly.y, poly.n
      inner_radius, outer_radius = poly.inner_radius, poly.outer_radius
      use_cairo do |cc|
        cc.rotate_about(x, y, trans.angle)
        cc.move_to(x + outer_radius, y) # i = 0, so cos(0)=1 and sin(0)=0
        theta = Math::PI / n.to_f # i.e. (2*pi) / (2*n)
        0.upto(2 * n) do |i|
            radius = i.even? ? outer_radius : inner_radius
            cc.line_to(x + radius * Math::cos(i * theta),
                       y + radius * Math::sin(i * theta))
        end
        cc.close_path
        cc.fill_n_stroke(draw)
      end
    end