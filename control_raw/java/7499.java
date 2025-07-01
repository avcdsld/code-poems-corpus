@Override
	public void endElement(String uri, String localName, String qName) throws SAXException {
		final String contentStr = StrUtil.trim(lastContent);

		if (T_ELEMENT.equals(qName)) {
			// type标签
			rowCellList.add(curCell++, contentStr);
		} else if (C_ELEMENT.equals(qName)) {
			// cell标签
			Object value = ExcelSaxUtil.getDataValue(this.cellDataType, contentStr, this.sharedStringsTable, this.numFmtString);
			// 补全单元格之间的空格
			fillBlankCell(preCoordinate, curCoordinate, false);
			rowCellList.add(curCell++, value);
		} else if (ROW_ELEMENT.equals(qName)) {
			// 如果是row标签，说明已经到了一行的结尾
			// 最大列坐标以第一行的为准
			if (curRow == 0) {
				maxCellCoordinate = curCoordinate;
			}

			// 补全一行尾部可能缺失的单元格
			if (maxCellCoordinate != null) {
				fillBlankCell(curCoordinate, maxCellCoordinate, true);
			}

			rowHandler.handle(sheetIndex, curRow, rowCellList);

			// 一行结束
			// 清空rowCellList,
			rowCellList.clear();
			// 行数增加
			curRow++;
			// 当前列置0
			curCell = 0;
			// 置空当前列坐标和前一列坐标
			curCoordinate = null;
			preCoordinate = null;
		}
	}