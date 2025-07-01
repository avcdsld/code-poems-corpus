public User getUserById(int id) {
		for (User u : users)
			if (u.getId() == id)
				return u;
		return null;
	}