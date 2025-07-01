def get(remotepath, destpath)
      Kernel.open(destpath, 'w') { |dest|
        readchunks(remotepath) { |chunk|
          dest.write chunk
        }
      }
    end