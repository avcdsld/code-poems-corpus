public final int compare(MemorySegment seg2, int offset1, int offset2, int len) {
		while (len >= 8) {
			long l1 = this.getLongBigEndian(offset1);
			long l2 = seg2.getLongBigEndian(offset2);

			if (l1 != l2) {
				return (l1 < l2) ^ (l1 < 0) ^ (l2 < 0) ? -1 : 1;
			}

			offset1 += 8;
			offset2 += 8;
			len -= 8;
		}
		while (len > 0) {
			int b1 = this.get(offset1) & 0xff;
			int b2 = seg2.get(offset2) & 0xff;
			int cmp = b1 - b2;
			if (cmp != 0) {
				return cmp;
			}
			offset1++;
			offset2++;
			len--;
		}
		return 0;
	}