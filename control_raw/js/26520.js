function getMemberName(member) {
            if (!member) return null;

            switch (member.type) {
                case "ExportDefaultDeclaration":
                case "ExportNamedDeclaration": {
                    // export statements (e.g. export { a };)
                    // have no declarations, so ignore them
                    return member.declaration
                        ? getMemberName(member.declaration)
                        : null;
                }
                case "DeclareFunction":
                case "FunctionDeclaration":
                case "TSNamespaceFunctionDeclaration":
                case "TSEmptyBodyFunctionDeclaration":
                case "TSEmptyBodyDeclareFunction": {
                    return member.id && member.id.name;
                }
                case "TSMethodSignature": {
                    return (
                        (member.key && (member.key.name || member.key.value)) ||
                        (member.name && (member.name.name || member.name.value))
                    );
                }
                case "TSCallSignature": {
                    return "call";
                }
                case "TSConstructSignature": {
                    return "new";
                }
                case "MethodDefinition": {
                    return member.key.name || member.key.value;
                }
                default: {
                    return null;
                }
            }
        }