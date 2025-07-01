function (sNamespace) {
				if (!sNamespace) {
					return "";
				}
				if (sNamespace[0] === "/") {
					var sNamespaceWithoutLeadingSlash = sNamespace.substring(1, sNamespace.length);
					return this.cleanLeadingAndTrailingSlashes(sNamespaceWithoutLeadingSlash);
				}
				if (sNamespace[sNamespace.length - 1] === "/") {
					var sNamespaceWithoutTrailingSlash = sNamespace.substring(0, sNamespace.length - 1);
					return this.cleanLeadingAndTrailingSlashes(sNamespaceWithoutTrailingSlash);
				}
				return sNamespace;
			}