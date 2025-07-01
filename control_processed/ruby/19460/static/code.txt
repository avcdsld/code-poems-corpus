def parse_series_formula(formula)  # :nodoc:
    encoding = 0
    length   = 0
    count    = 0
    tokens = []

    return [''] if formula.nil?

    # Strip the = sign at the beginning of the formula string
    formula = formula.sub(/^=/, '')

    # In order to raise formula errors from the point of view of the calling
    # program we use an eval block and re-raise the error from here.
    #
    tokens = parser.parse_formula(formula)

    # Force ranges to be a reference class.
    tokens.collect! { |t| t.gsub(/_ref3d/, '_ref3dR') }
    tokens.collect! { |t| t.gsub(/_range3d/, '_range3dR') }
    tokens.collect! { |t| t.gsub(/_name/, '_nameR') }

    # Parse the tokens into a formula string.
    formula = parser.parse_tokens(tokens)

    # Return formula for a single cell as used by title and series name.
    return formula if formula.ord == 0x3A

    # Extract the range from the parse formula.
    if formula.ord == 0x3B
        ptg, ext_ref, row_1, row_2, col_1, col_2 = formula.unpack('Cv5')

        # TODO. Remove high bit on relative references.
        count = row_2 - row_1 + 1
    end

    [formula, count]
  end