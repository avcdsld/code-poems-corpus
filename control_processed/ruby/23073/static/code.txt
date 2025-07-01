def get_copyright_holders(query_obj=nil,with_nested_resources=false,use_http_query=false)
            uri = URI.parse(@uri + "/CopyrightHolders")
            handle_get_request(uri,query_obj,with_nested_resources,use_http_query)
        end