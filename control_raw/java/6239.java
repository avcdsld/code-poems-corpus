@Override
	protected List<OUT> executeOnCollections(List<IN1> input1, List<IN2> input2, RuntimeContext ctx, ExecutionConfig executionConfig) throws Exception {
		// --------------------------------------------------------------------
		// Setup
		// --------------------------------------------------------------------
		TypeInformation<IN1> inputType1 = getOperatorInfo().getFirstInputType();
		TypeInformation<IN2> inputType2 = getOperatorInfo().getSecondInputType();
		
		// for the grouping / merging comparator
		int[] inputKeys1 = getKeyColumns(0);
		int[] inputKeys2 = getKeyColumns(1);

		boolean[] inputDirections1 = new boolean[inputKeys1.length];
		boolean[] inputDirections2 = new boolean[inputKeys2.length];
		Arrays.fill(inputDirections1, true);
		Arrays.fill(inputDirections2, true);
		
		final TypeSerializer<IN1> inputSerializer1 = inputType1.createSerializer(executionConfig);
		final TypeSerializer<IN2> inputSerializer2 = inputType2.createSerializer(executionConfig);
		
		final TypeComparator<IN1> inputComparator1 = getTypeComparator(executionConfig, inputType1, inputKeys1, inputDirections1);
		final TypeComparator<IN2> inputComparator2 = getTypeComparator(executionConfig, inputType2, inputKeys2, inputDirections2);
		
		final TypeComparator<IN1> inputSortComparator1;
		final TypeComparator<IN2> inputSortComparator2;
		
		if (groupOrder1 == null || groupOrder1.getNumberOfFields() == 0) {
			// no group sorting
			inputSortComparator1 = inputComparator1;
		}
		else {
			// group sorting
			int[] groupSortKeys = groupOrder1.getFieldPositions();
			int[] allSortKeys = new int[inputKeys1.length + groupOrder1.getNumberOfFields()];
			System.arraycopy(inputKeys1, 0, allSortKeys, 0, inputKeys1.length);
			System.arraycopy(groupSortKeys, 0, allSortKeys, inputKeys1.length, groupSortKeys.length);
			
			boolean[] groupSortDirections = groupOrder1.getFieldSortDirections();
			boolean[] allSortDirections = new boolean[inputKeys1.length + groupSortKeys.length];
			Arrays.fill(allSortDirections, 0, inputKeys1.length, true);
			System.arraycopy(groupSortDirections, 0, allSortDirections, inputKeys1.length, groupSortDirections.length);
			
			inputSortComparator1 = getTypeComparator(executionConfig, inputType1, allSortKeys, allSortDirections);
		}
		
		if (groupOrder2 == null || groupOrder2.getNumberOfFields() == 0) {
			// no group sorting
			inputSortComparator2 = inputComparator2;
		}
		else {
			// group sorting
			int[] groupSortKeys = groupOrder2.getFieldPositions();
			int[] allSortKeys = new int[inputKeys2.length + groupOrder2.getNumberOfFields()];
			System.arraycopy(inputKeys2, 0, allSortKeys, 0, inputKeys2.length);
			System.arraycopy(groupSortKeys, 0, allSortKeys, inputKeys2.length, groupSortKeys.length);
			
			boolean[] groupSortDirections = groupOrder2.getFieldSortDirections();
			boolean[] allSortDirections = new boolean[inputKeys2.length + groupSortKeys.length];
			Arrays.fill(allSortDirections, 0, inputKeys2.length, true);
			System.arraycopy(groupSortDirections, 0, allSortDirections, inputKeys2.length, groupSortDirections.length);
			
			inputSortComparator2 = getTypeComparator(executionConfig, inputType2, allSortKeys, allSortDirections);
		}

		CoGroupSortListIterator<IN1, IN2> coGroupIterator =
				new CoGroupSortListIterator<IN1, IN2>(input1, inputSortComparator1, inputComparator1, inputSerializer1,
						input2, inputSortComparator2, inputComparator2, inputSerializer2);

		// --------------------------------------------------------------------
		// Run UDF
		// --------------------------------------------------------------------
		CoGroupFunction<IN1, IN2, OUT> function = userFunction.getUserCodeObject();

		FunctionUtils.setFunctionRuntimeContext(function, ctx);
		FunctionUtils.openFunction(function, parameters);

		List<OUT> result = new ArrayList<OUT>();
		Collector<OUT> resultCollector = new CopyingListCollector<OUT>(result, getOperatorInfo().getOutputType().createSerializer(executionConfig));

		while (coGroupIterator.next()) {
			function.coGroup(coGroupIterator.getValues1(), coGroupIterator.getValues2(), resultCollector);
		}

		FunctionUtils.closeFunction(function);

		return result;
	}