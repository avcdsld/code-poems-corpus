def term_frequency(document, term)
      tf = document.term_count(term)
      (tf * 2.2) / (tf + 0.3 + 0.9 * documents.size / @model.average_document_size)
    end