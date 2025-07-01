public static <IN> CassandraSinkBuilder<IN> addSink(DataStream<IN> input) {
		TypeInformation<IN> typeInfo = input.getType();
		if (typeInfo instanceof TupleTypeInfo) {
			DataStream<Tuple> tupleInput = (DataStream<Tuple>) input;
			return (CassandraSinkBuilder<IN>) new CassandraTupleSinkBuilder<>(tupleInput, tupleInput.getType(), tupleInput.getType().createSerializer(tupleInput.getExecutionEnvironment().getConfig()));
		}
		if (typeInfo instanceof RowTypeInfo) {
			DataStream<Row> rowInput = (DataStream<Row>) input;
			return (CassandraSinkBuilder<IN>) new CassandraRowSinkBuilder(rowInput, rowInput.getType(), rowInput.getType().createSerializer(rowInput.getExecutionEnvironment().getConfig()));
		}
		if (typeInfo instanceof PojoTypeInfo) {
			return new CassandraPojoSinkBuilder<>(input, input.getType(), input.getType().createSerializer(input.getExecutionEnvironment().getConfig()));
		}
		if (typeInfo instanceof CaseClassTypeInfo) {
			DataStream<Product> productInput = (DataStream<Product>) input;
			return (CassandraSinkBuilder<IN>) new CassandraScalaProductSinkBuilder<>(productInput, productInput.getType(), productInput.getType().createSerializer(input.getExecutionEnvironment().getConfig()));
		}
		throw new IllegalArgumentException("No support for the type of the given DataStream: " + input.getType());
	}