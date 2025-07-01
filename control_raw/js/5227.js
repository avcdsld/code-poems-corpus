function follow (cid, links, err, obj) {
      if (err) {
        return cb(err)
      }

      if (!links.length) {
        // done tracing, obj is the target node
        return cb(null, cid.buffer)
      }

      const linkName = links[0]
      const nextObj = obj.links.find(link => link.name === linkName)
      if (!nextObj) {
        return cb(new Error(
          `no link named "${linkName}" under ${cid.toBaseEncodedString()}`
        ))
      }

      objectAPI.get(nextObj.cid, follow.bind(null, nextObj.cid, links.slice(1)))
    }