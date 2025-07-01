public static String getGarbageCollectorStatsAsString(List<GarbageCollectorMXBean> gcMXBeans) {
		StringBuilder bld = new StringBuilder("Garbage collector stats: ");
		
		for (GarbageCollectorMXBean bean : gcMXBeans) {
			bld.append('[').append(bean.getName()).append(", GC TIME (ms): ").append(bean.getCollectionTime());
			bld.append(", GC COUNT: ").append(bean.getCollectionCount()).append(']');
			
			bld.append(", ");
		}
		
		if (!gcMXBeans.isEmpty()) {
			bld.setLength(bld.length() - 2);
		}
		
		return bld.toString();
	}