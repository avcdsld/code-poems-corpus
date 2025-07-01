def new_more_like_this(object, *types, &block)
      types[0] ||= object.class
      mlt = Search::MoreLikeThisSearch.new(
        connection,
        setup_for_types(types),
        Query::MoreLikeThisQuery.new(object, types),
        @config
      )
      mlt.build(&block) if block
      mlt
    end