function afterTarball () {
        if (badDownload) return
        if (extractCount === 0) {
          return cb(new Error('There was a fatal problem while downloading/extracting the tarball'))
        }
        log.verbose('tarball', 'done parsing tarball')
        var async = 0

        if (win) {
          // need to download node.lib
          async++
          downloadNodeLib(deref)
        }

        // write the "installVersion" file
        async++
        var installVersionPath = path.resolve(devDir, 'installVersion')
        fs.writeFile(installVersionPath, gyp.package.installVersion + '\n', deref)

        // Only download SHASUMS.txt if not using tarPath override
        if (!tarPath) {
          // download SHASUMS.txt
          async++
          downloadShasums(deref)
        }

        if (async === 0) {
          // no async tasks required
          cb()
        }

        function deref (err) {
          if (err) return cb(err)

          async--
          if (!async) {
            log.verbose('download contents checksum', JSON.stringify(contentShasums))
            // check content shasums
            for (var k in contentShasums) {
              log.verbose('validating download checksum for ' + k, '(%s == %s)', contentShasums[k], expectShasums[k])
              if (contentShasums[k] !== expectShasums[k]) {
                cb(new Error(k + ' local checksum ' + contentShasums[k] + ' not match remote ' + expectShasums[k]))
                return
              }
            }
            cb()
          }
        }
      }