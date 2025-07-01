def resolve(self, other: Type) -> Type:
        """See ``PlaceholderType.resolve``"""
        if not isinstance(other, NltkComplexType):
            return None
        resolved_second = NUMBER_TYPE.resolve(other.second)
        if not resolved_second:
            return None
        return CountType(other.first)