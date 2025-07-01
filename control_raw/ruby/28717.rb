def newest(versions)
      versions.sort { |x,y| compare(x,y) }.last
    end