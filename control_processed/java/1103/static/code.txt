public Collection<TermFrequency> top(int N)
    {
        MaxHeap<TermFrequency> heap = new MaxHeap<TermFrequency>(N, new Comparator<TermFrequency>()
        {
            @Override
            public int compare(TermFrequency o1, TermFrequency o2)
            {
                return o1.compareTo(o2);
            }
        });
        heap.addAll(termFrequencyMap.values());
        return heap.toList();
    }