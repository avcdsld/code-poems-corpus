def remount(from, to)
      client.post("/v1/sys/remount", JSON.fast_generate(
        from: from,
        to:   to,
      ))
      return true
    end