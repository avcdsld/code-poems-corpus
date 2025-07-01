def patterns(self):
        """Get all patterns that were added to the entity ruler.

        RETURNS (list): The original patterns, one dictionary per pattern.

        DOCS: https://spacy.io/api/entityruler#patterns
        """
        all_patterns = []
        for label, patterns in self.token_patterns.items():
            for pattern in patterns:
                all_patterns.append({"label": label, "pattern": pattern})
        for label, patterns in self.phrase_patterns.items():
            for pattern in patterns:
                all_patterns.append({"label": label, "pattern": pattern.text})
        return all_patterns