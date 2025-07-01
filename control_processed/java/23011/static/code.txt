public void addError(String message, DiagnosticPosition pos) {
		ast.printMessage(Diagnostic.Kind.ERROR, message, null, pos, true);
	}