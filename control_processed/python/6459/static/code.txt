def interpret_element(element_type: str, text: str, span: str) -> Element:
    """
    Construct an Element instance from regexp
    groups.
    """
    return Element(element_type,
                   interpret_span(span),
                   text)