public Impl embedded(CharSequence ref, Resource resource) {
        if (StringUtils.isNotEmpty(ref) && resource != null) {
            List<Resource> resources = this.embeddedMap.computeIfAbsent(ref, charSequence -> new ArrayList<>());
            resources.add(resource);
        }
        return (Impl) this;
    }