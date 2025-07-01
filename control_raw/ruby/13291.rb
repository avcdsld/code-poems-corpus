def to_html(style="")
      html = @groups.map do |group|
        [
          "<h3>#{group['title']}</h3>",
          "<ul>",
          flatten_subgroups(group["items"]).map {|g| "<li><a href='#!/guide/#{g['name']}'>#{g['title']}</a></li>" },
          "</ul>",
        ]
      end.flatten.join("\n")

      return <<-EOHTML
        <div id='guides-content' style='#{style}'>
            #{html}
        </div>
      EOHTML
    end