public static boolean nodeHasDeprecatedFlag(JCTree node) {
		if (node instanceof JCVariableDecl) return (((JCVariableDecl) node).mods.flags & Flags.DEPRECATED) != 0;
		if (node instanceof JCMethodDecl) return (((JCMethodDecl) node).mods.flags & Flags.DEPRECATED) != 0;
		if (node instanceof JCClassDecl) return (((JCClassDecl) node).mods.flags & Flags.DEPRECATED) != 0;
		return false;
	}