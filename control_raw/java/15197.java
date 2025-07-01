public PopulateResult populate(final ByteSource source, final Map<K, V> map) throws IOException
  {
    return source.asCharSource(StandardCharsets.UTF_8).readLines(
        new LineProcessor<PopulateResult>()
        {
          private int lines = 0;
          private int entries = 0;

          @Override
          public boolean processLine(String line)
          {
            if (lines == Integer.MAX_VALUE) {
              throw new ISE("Cannot read more than %,d lines", Integer.MAX_VALUE);
            }
            final Map<K, V> kvMap = parser.parseToMap(line);
            map.putAll(kvMap);
            lines++;
            entries += kvMap.size();
            return true;
          }

          @Override
          public PopulateResult getResult()
          {
            return new PopulateResult(lines, entries);
          }
        }
    );
  }