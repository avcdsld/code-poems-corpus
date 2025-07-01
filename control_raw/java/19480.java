@Deprecated
    @JsonProperty
    public List<ClientTypeSignature> getTypeArguments()
    {
        List<ClientTypeSignature> result = new ArrayList<>();
        for (ClientTypeSignatureParameter argument : arguments) {
            switch (argument.getKind()) {
                case TYPE:
                    result.add(argument.getTypeSignature());
                    break;
                case NAMED_TYPE:
                    result.add(new ClientTypeSignature(argument.getNamedTypeSignature().getTypeSignature()));
                    break;
                default:
                    return new ArrayList<>();
            }
        }
        return result;
    }