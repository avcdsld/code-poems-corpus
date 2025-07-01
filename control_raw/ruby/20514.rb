def gzip
      @assets.map! do |asset|
        gzip_content = Zlib::Deflate.deflate(asset.content)
        [
          asset,
          ::JekyllAssetPipeline::Asset
            .new(gzip_content, "#{asset.filename}.gz", asset.dirname)
        ]
      end.flatten!
    end