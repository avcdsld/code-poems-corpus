def create_redis_client(self):
        """Create a redis client."""
        return ray.services.create_redis_client(
            self._redis_address, self._ray_params.redis_password)