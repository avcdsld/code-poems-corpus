def preface_names(clause)
      return if clause.nil?
      @anchors[clause["id"]] =
        { label: nil, level: 1, xref: preface_clause_name(clause), type: "clause" }
      clause.xpath(ns("./clause | ./terms | ./term | ./definitions | ./references")).each_with_index do |c, i|
        preface_names1(c, c.at(ns("./title"))&.text, "#{preface_clause_name(clause)}, #{i+1}", 2)
      end
    end