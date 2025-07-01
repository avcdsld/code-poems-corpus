def _merge_float64(lhs, rhs, type_):  # pylint: disable=unused-argument
    """Helper for '_merge_by_type'."""
    lhs_kind = lhs.WhichOneof("kind")
    if lhs_kind == "string_value":
        return Value(string_value=lhs.string_value + rhs.string_value)
    rhs_kind = rhs.WhichOneof("kind")
    array_continuation = (
        lhs_kind == "number_value"
        and rhs_kind == "string_value"
        and rhs.string_value == ""
    )
    if array_continuation:
        return lhs
    raise Unmergeable(lhs, rhs, type_)