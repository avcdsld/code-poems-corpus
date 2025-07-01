def _toolkit_serialize_summary_struct(model, sections, section_titles):
    """
      Serialize model summary into a dict with ordered lists of sections and section titles

    Parameters
    ----------
    model : Model object
    sections : Ordered list of lists (sections) of tuples (field,value)
      [
        [(field1, value1), (field2, value2)],
        [(field3, value3), (field4, value4)],

      ]
    section_titles : Ordered list of section titles


    Returns
    -------
    output_dict : A dict with two entries:
                    'sections' : ordered list with tuples of the form ('label',value)
                    'section_titles' : ordered list of section labels
    """
    output_dict = dict()
    output_dict['sections'] = [ [ ( field[0], __extract_model_summary_value(model, field[1]) ) \
                                                                            for field in section ]
                                                                            for section in sections ]
    output_dict['section_titles'] = section_titles
    return output_dict