def chip_select_active_low(active_low, chip=nil)
      chip = @chip if @chip
      chip = CHIP_SELECT_0 unless chip

      PiPiper.driver.spi_chip_select_polarity(chip, active_low ? 0 : 1)
    end