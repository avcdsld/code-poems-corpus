def save_stitch(path, opts = {})
      return @browser.screenshot.save(path) if base64_capable?
      @options = opts
      @path = path
      calculate_dimensions

      return self.save(@path) if (one_shot? || bug_shot?)

      build_canvas
      gather_slices
      stitch_together

      @combined_screenshot.write @path
    end