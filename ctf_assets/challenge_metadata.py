class ChallenteMetadata:
    def __init__(self):
        """Initialize metadata with default values and store a backup for resets."""
        self.default_metadata = {
            "role": "cybersecurity_assistant",
            "task": "generate_ctf_flags",
            "audience": "high_school_students",
            "language": "es-PR",
            "tone": "",
            "theme": "",
            "constraints": {
                "format": "ctf{..}",
                "flag_count": 1,
                "uniqueness": True,
                "coherence": True,
                "accuracy": True,
                "no_fabrication": True
            },
            "ethical_constraints": {
                "no_illegal_content": True,
                "no_inappropriate_material": True,
                "under_18_safe": True
            },
            "output_format": "json",
            "response_constraints": "only return flags, no additional information"
        }
        self.metadata = self.default_metadata.copy()

    def reset_metadata(self):
        """Resets metadata back to its default values."""
        self.metadata = self.default_metadata.copy()

    def update_metadata(self, **kwargs):
        """
        Update metadata values using simple keyword arguments.
        
        Args:
            **kwargs: Key-value pairs of metadata fields to update.

        Returns:
            dict: Updated metadata dictionary.
        """
        # Maps simple keyword argument to their actual JSON path
        mapping = {
            "theme": ["theme"],
            "tone": ["tone"],
            "flag_count": ["constraints", "flag_count"],
            "format": ["constraints", "format"],
            "language": ["language"],
            "output_format": ["output_format"],
            "under_18_safe": ["ethical_constraints", "under_18_safe"],
            "no_illegal_content": ["ethical_constraints", "no_illegal_content"],
            "no_inappropriate_material": ["ethical_constraints", "no_inappropriate_material"],
        }

        for key, value in kwargs.items():
            if key in mapping:
                temp = self.metadata
                path = mapping[key]

                for subkey in path[:-1]:  # Traverse to the correct dictionary level
                    temp = temp.setdefault(subkey, {})  # Ensure key exists

                temp[path[-1]] = value  # Update value

        return self.metadata  # Return the updated metadata

