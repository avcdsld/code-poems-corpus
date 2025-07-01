public String[] getIndexArr() {
		String[] indexArr = new String[this.from.size()];
		for (int i = 0; i < indexArr.length; i++) {
			indexArr[i] = this.from.get(i).getIndex();
		}
		return indexArr;
	}