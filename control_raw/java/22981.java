public static <C> Iterable<C> findServices(final Class<C> target, ClassLoader loader) throws IOException {
		if (loader == null) loader = ClassLoader.getSystemClassLoader();
		Enumeration<URL> resources = loader.getResources("META-INF/services/" + target.getName());
		final Set<String> entries = new LinkedHashSet<String>();
		while (resources.hasMoreElements()) {
			URL url = resources.nextElement();
			readServicesFromUrl(entries, url);
		}
		
		final Iterator<String> names = entries.iterator();
		final ClassLoader fLoader = loader;
		return new Iterable<C> () {
			@Override public Iterator<C> iterator() {
				return new Iterator<C>() {
					@Override public boolean hasNext() {
						return names.hasNext();
					}
					
					@Override public C next() {
						try {
							return target.cast(Class.forName(names.next(), true, fLoader).newInstance());
						} catch (Exception e) {
							if (e instanceof RuntimeException) throw (RuntimeException)e;
							throw new RuntimeException(e);
						}
					}
					
					@Override public void remove() {
						throw new UnsupportedOperationException();
					}
				};
			}
		};
	}