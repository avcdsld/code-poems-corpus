@Deprecated
	public <L, R> SingleOutputStreamOperator<Either<L, R>> flatSelect(
			final PatternFlatTimeoutFunction<T, L> patternFlatTimeoutFunction,
			final PatternFlatSelectFunction<T, R> patternFlatSelectFunction) {

		final TypeInformation<L> timedOutTypeInfo = TypeExtractor.getUnaryOperatorReturnType(
			patternFlatTimeoutFunction,
			PatternFlatTimeoutFunction.class,
			0,
			1,
			new int[]{2, 0},
			builder.getInputType(),
			null,
			false);

		final TypeInformation<R> mainTypeInfo = TypeExtractor.getUnaryOperatorReturnType(
			patternFlatSelectFunction,
			PatternFlatSelectFunction.class,
			0,
			1,
			new int[]{1, 0},
			builder.getInputType(),
			null,
			false);

		final OutputTag<L> outputTag = new OutputTag<>(UUID.randomUUID().toString(), timedOutTypeInfo);

		final PatternProcessFunction<T, R> processFunction =
			fromFlatSelect(builder.clean(patternFlatSelectFunction))
				.withTimeoutHandler(outputTag, builder.clean(patternFlatTimeoutFunction))
				.build();

		final SingleOutputStreamOperator<R> mainStream = process(processFunction, mainTypeInfo);
		final DataStream<L> timedOutStream = mainStream.getSideOutput(outputTag);
		final TypeInformation<Either<L, R>> outTypeInfo = new EitherTypeInfo<>(timedOutTypeInfo, mainTypeInfo);

		return mainStream
				.connect(timedOutStream)
				.map(new CoMapTimeout<>())
				.returns(outTypeInfo);
	}