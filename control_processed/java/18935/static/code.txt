public void format(PatriciaTrie<V> trie, File file, boolean formatBitString) throws FileNotFoundException {
        PrintWriter writer = new PrintWriter(new FileOutputStream(file));
        writer.println(format(trie, formatBitString));
        writer.close();
    }