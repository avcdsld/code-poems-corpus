public static <T> TupleDomain<T> columnWiseUnion(List<TupleDomain<T>> tupleDomains)
    {
        if (tupleDomains.isEmpty()) {
            throw new IllegalArgumentException("tupleDomains must have at least one element");
        }

        if (tupleDomains.size() == 1) {
            return tupleDomains.get(0);
        }

        // gather all common columns
        Set<T> commonColumns = new HashSet<>();

        // first, find a non-none domain
        boolean found = false;
        Iterator<TupleDomain<T>> domains = tupleDomains.iterator();
        while (domains.hasNext()) {
            TupleDomain<T> domain = domains.next();
            if (!domain.isNone()) {
                found = true;
                commonColumns.addAll(domain.getDomains().get().keySet());
                break;
            }
        }

        if (!found) {
            return TupleDomain.none();
        }

        // then, get the common columns
        while (domains.hasNext()) {
            TupleDomain<T> domain = domains.next();
            if (!domain.isNone()) {
                commonColumns.retainAll(domain.getDomains().get().keySet());
            }
        }

        // group domains by column (only for common columns)
        Map<T, List<Domain>> domainsByColumn = new LinkedHashMap<>(tupleDomains.size());

        for (TupleDomain<T> domain : tupleDomains) {
            if (!domain.isNone()) {
                for (Map.Entry<T, Domain> entry : domain.getDomains().get().entrySet()) {
                    if (commonColumns.contains(entry.getKey())) {
                        List<Domain> domainForColumn = domainsByColumn.get(entry.getKey());
                        if (domainForColumn == null) {
                            domainForColumn = new ArrayList<>();
                            domainsByColumn.put(entry.getKey(), domainForColumn);
                        }
                        domainForColumn.add(entry.getValue());
                    }
                }
            }
        }

        // finally, do the column-wise union
        Map<T, Domain> result = new LinkedHashMap<>(domainsByColumn.size());
        for (Map.Entry<T, List<Domain>> entry : domainsByColumn.entrySet()) {
            result.put(entry.getKey(), Domain.union(entry.getValue()));
        }
        return withColumnDomains(result);
    }