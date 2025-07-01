void add_document(Document doc)
    {
        doc.feature().normalize();
        documents_.add(doc);
        composite_.add_vector(doc.feature());
    }