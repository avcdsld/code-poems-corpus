def register_actor(name, actor_handle):
    """Register a named actor under a string key.

   Args:
       name: The name of the named actor.
       actor_handle: The actor object to be associated with this name
   """
    if not isinstance(name, str):
        raise TypeError("The name argument must be a string.")
    if not isinstance(actor_handle, ray.actor.ActorHandle):
        raise TypeError("The actor_handle argument must be an ActorHandle "
                        "object.")
    actor_name = _calculate_key(name)
    pickled_state = pickle.dumps(actor_handle)

    # Add the actor to Redis if it does not already exist.
    already_exists = _internal_kv_put(actor_name, pickled_state)
    if already_exists:
        # If the registration fails, then erase the new actor handle that
        # was added when pickling the actor handle.
        actor_handle._ray_new_actor_handles.pop()
        raise ValueError(
            "Error: the actor with name={} already exists".format(name))