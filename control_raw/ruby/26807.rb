def exchange_typecasting_alias_method_chain attribute, setter=nil
      alias_method :"#{attribute}_without_exchange_typecasting#{setter}", :"#{attribute}#{setter}"
      alias_method :"#{attribute}#{setter}", :"#{attribute}_with_exchange_typecasting#{setter}"
    end