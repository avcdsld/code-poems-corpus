private long decodeMsDosFormatDateTime(long datetime) {
		LocalDateTime localDateTime = LocalDateTime.of(
				(int) (((datetime >> 25) & 0x7f) + 1980), (int) ((datetime >> 21) & 0x0f),
				(int) ((datetime >> 16) & 0x1f), (int) ((datetime >> 11) & 0x1f),
				(int) ((datetime >> 5) & 0x3f), (int) ((datetime << 1) & 0x3e));
		return localDateTime.toEpochSecond(
				ZoneId.systemDefault().getRules().getOffset(localDateTime)) * 1000;
	}