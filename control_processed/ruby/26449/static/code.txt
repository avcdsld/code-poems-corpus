def phi_z(alpha)
      # If the ray is orthogonal on the z axis, the evaluation will yield NaN, and
      # we return the index k which corresponds to the source's z position instead.
      (((@p2.z - @p1.z == 0 ? @p1.z : pz(alpha)) - bz) / @vs.delta_z).floor
    end