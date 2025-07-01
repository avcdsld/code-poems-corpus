public static void transform(Parser parser, CompilationUnitDeclaration ast) {
		if (disableLombok) return;
		
		if (Symbols.hasSymbol("lombok.disable")) return;
		
		// Do NOT abort if (ast.bits & ASTNode.HasAllMethodBodies) != 0 - that doesn't work.
		
		if (Boolean.TRUE.equals(LombokConfiguration.read(ConfigurationKeys.LOMBOK_DISABLE, EclipseAST.getAbsoluteFileLocation(ast)))) return;
		
		try {
			DebugSnapshotStore.INSTANCE.snapshot(ast, "transform entry");
			long histoToken = lombokTracker == null ? 0L : lombokTracker.start();
			EclipseAST existing = getAST(ast, false);
			new TransformEclipseAST(existing).go();
			if (lombokTracker != null) lombokTracker.end(histoToken);
			DebugSnapshotStore.INSTANCE.snapshot(ast, "transform exit");
		} catch (Throwable t) {
			DebugSnapshotStore.INSTANCE.snapshot(ast, "transform error: %s", t.getClass().getSimpleName());
			try {
				String message = "Lombok can't parse this source: " + t.toString();
				
				EclipseAST.addProblemToCompilationResult(ast.getFileName(), ast.compilationResult, false, message, 0, 0);
				t.printStackTrace();
			} catch (Throwable t2) {
				try {
					error(ast, "Can't create an error in the problems dialog while adding: " + t.toString(), t2);
				} catch (Throwable t3) {
					//This seems risky to just silently turn off lombok, but if we get this far, something pretty
					//drastic went wrong. For example, the eclipse help system's JSP compiler will trigger a lombok call,
					//but due to class loader shenanigans we'll actually get here due to a cascade of
					//ClassNotFoundErrors. This is the right action for the help system (no lombok needed for that JSP compiler,
					//of course). 'disableLombok' is static, but each context classloader (e.g. each eclipse OSGi plugin) has
					//it's own edition of this class, so this won't turn off lombok everywhere.
					disableLombok = true;
				}
			}
		}
	}