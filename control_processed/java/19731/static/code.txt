public TupleDomain<T> intersect(TupleDomain<T> other)
    {
        if (this.isNone() || other.isNone()) {
            return none();
        }

        Map<T, Domain> intersected = new LinkedHashMap<>(this.getDomains().get());
        for (Map.Entry<T, Domain> entry : other.getDomains().get().entrySet()) {
            Domain intersectionDomain = intersected.get(entry.getKey());
            if (intersectionDomain == null) {
                intersected.put(entry.getKey(), entry.getValue());
            }
            else {
                intersected.put(entry.getKey(), intersectionDomain.intersect(entry.getValue()));
            }
        }
        return withColumnDomains(intersected);
    }