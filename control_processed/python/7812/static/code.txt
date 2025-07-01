def sentence(self, padding=75):
        """
        Get sentence
        """
        vec = word_to_vector(self.sentence_str)
        vec += [-1] * (padding - self.sentence_length)
        return np.array(vec, dtype=np.int32)