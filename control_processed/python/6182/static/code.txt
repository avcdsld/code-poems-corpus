def _choice(num_words: int, num_samples: int) -> Tuple[np.ndarray, int]:
    """
    Chooses ``num_samples`` samples without replacement from [0, ..., num_words).
    Returns a tuple (samples, num_tries).
    """
    num_tries = 0
    num_chosen = 0

    def get_buffer() -> np.ndarray:
        log_samples = np.random.rand(num_samples) * np.log(num_words + 1)
        samples = np.exp(log_samples).astype('int64') - 1
        return np.clip(samples, a_min=0, a_max=num_words - 1)

    sample_buffer = get_buffer()
    buffer_index = 0
    samples: Set[int] = set()

    while num_chosen < num_samples:
        num_tries += 1
        # choose sample
        sample_id = sample_buffer[buffer_index]
        if sample_id not in samples:
            samples.add(sample_id)
            num_chosen += 1

        buffer_index += 1
        if buffer_index == num_samples:
            # Reset the buffer
            sample_buffer = get_buffer()
            buffer_index = 0

    return np.array(list(samples)), num_tries