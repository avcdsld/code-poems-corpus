def getLocs
      # Calculate the location of the (active) FAT (loc as absolute byte for seek).
      @fatBase = @bs['res_sec'] * @bytesPerSector
      @fatSize = @bs['fat_size32'] * @bytesPerSector
      fu = @bs['fat_usage']
      if fu & FU_ONE_FAT == FU_ONE_FAT
        @fatBase += @fatSize * (fu & FU_MSK_ACTIVE_FAT)
      end
      return false if @fatBase == 0 || @fatSize == 0

      # Calculate the location of the root dir (loc as absolute byte for seek).
      @rootCluster = @bs['root_clus']
      @rootBase = clusToByte(@rootCluster)
      return false if @rootBase == 0
      true
    end