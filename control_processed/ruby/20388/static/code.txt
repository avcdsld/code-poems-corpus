def render_image(image)
      id_attr = image.id ? %{ id="attachment_#{image.id}"} : ""
      lines = []
      lines << %{<figure#{id_attr} class="image embedded">}
      lines << %{<div class="img"><img src="#{encode(image.url)}" alt="#{encode(image.alt_text)}"></div>}
      lines << image.figcaption_html if image.figcaption?
      lines << '</figure>'
      lines.join
    end