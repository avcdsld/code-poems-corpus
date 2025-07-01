def update_copyright_policies(data=nil,generate_objects=false)
            uri = URI.parse(@uri + "/CopyrightPolicies")
            put(uri,data,generate_objects)
        end