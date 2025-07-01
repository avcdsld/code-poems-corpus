public final void parseSingleTableWithoutAlias(final SQLStatement sqlStatement) {
        int beginPosition = lexerEngine.getCurrentToken().getEndPosition() - lexerEngine.getCurrentToken().getLiterals().length();
        String literals = lexerEngine.getCurrentToken().getLiterals();
        int skippedSchemaNameLength = 0;
        lexerEngine.nextToken();
        if (lexerEngine.skipIfEqual(Symbol.DOT)) {
            skippedSchemaNameLength = literals.length() + Symbol.DOT.getLiterals().length();
            literals = lexerEngine.getCurrentToken().getLiterals();
            lexerEngine.nextToken();
        }
        sqlStatement.addSQLToken(new TableToken(beginPosition, literals, QuoteCharacter.getQuoteCharacter(literals), skippedSchemaNameLength));
        sqlStatement.getTables().add(new Table(SQLUtil.getExactlyValue(literals), null));
    }