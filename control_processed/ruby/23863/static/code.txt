def update_by_person(email, params, person_repo: Person.new)
      person = person_repo.find_exactly_by_email(email)
      deal = get_by_person_id(person[:id], person_repo: person_repo).first
      update(deal[:id], params)
    end