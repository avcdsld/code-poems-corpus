function setObjectMembers (ref, object, metaId, members) {
  if (!Array.isArray(members)) return

  for (const member of members) {
    if (object.hasOwnProperty(member.name)) continue

    const descriptor = { enumerable: member.enumerable }
    if (member.type === 'method') {
      const remoteMemberFunction = function (...args) {
        let command
        if (this && this.constructor === remoteMemberFunction) {
          command = 'ELECTRON_BROWSER_MEMBER_CONSTRUCTOR'
        } else {
          command = 'ELECTRON_BROWSER_MEMBER_CALL'
        }
        const ret = ipcRendererInternal.sendSync(command, contextId, metaId, member.name, wrapArgs(args))
        return metaToValue(ret)
      }

      let descriptorFunction = proxyFunctionProperties(remoteMemberFunction, metaId, member.name)

      descriptor.get = () => {
        descriptorFunction.ref = ref // The member should reference its object.
        return descriptorFunction
      }
      // Enable monkey-patch the method
      descriptor.set = (value) => {
        descriptorFunction = value
        return value
      }
      descriptor.configurable = true
    } else if (member.type === 'get') {
      descriptor.get = () => {
        const command = 'ELECTRON_BROWSER_MEMBER_GET'
        const meta = ipcRendererInternal.sendSync(command, contextId, metaId, member.name)
        return metaToValue(meta)
      }

      if (member.writable) {
        descriptor.set = (value) => {
          const args = wrapArgs([value])
          const command = 'ELECTRON_BROWSER_MEMBER_SET'
          const meta = ipcRendererInternal.sendSync(command, contextId, metaId, member.name, args)
          if (meta != null) metaToValue(meta)
          return value
        }
      }
    }

    Object.defineProperty(object, member.name, descriptor)
  }
}