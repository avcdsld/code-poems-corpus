function (contract, params, funAbi, linkLibraries, linkReferences, callback) {
    this.encodeParams(params, funAbi, (error, encodedParam) => {
      if (error) return callback(error)
      var bytecodeToDeploy = contract.evm.bytecode.object
      if (bytecodeToDeploy.indexOf('_') >= 0) {
        if (linkLibraries && linkReferences) {
          for (var libFile in linkLibraries) {
            for (var lib in linkLibraries[libFile]) {
              var address = linkLibraries[libFile][lib]
              if (!ethJSUtil.isValidAddress(address)) return callback(address + ' is not a valid address. Please check the provided address is valid.')
              bytecodeToDeploy = this.linkLibraryStandardFromlinkReferences(lib, address.replace('0x', ''), bytecodeToDeploy, linkReferences)
            }
          }
        }
      }
      if (bytecodeToDeploy.indexOf('_') >= 0) {
        return callback('Failed to link some libraries')
      }
      return callback(null, { dataHex: bytecodeToDeploy + encodedParam.dataHex, funAbi, funArgs: encodedParam.funArgs, contractBytecode: contract.evm.bytecode.object })
    })
  }