def merge_copyright_holders(target,source)
            uri = URI.parse(@uri + "/CopyrightHolders")
            merge(uri,target,source)
        end