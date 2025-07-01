public static void main(String[] args) throws Exception {

		final ParameterTool params = ParameterTool.fromArgs(args);

		// set up the execution environment
		final ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();

		// make parameters available in the web interface
		env.getConfig().setGlobalJobParameters(params);

		// get input data
		DataSet<String> text;
		if (params.has("input")) {
			// read the text file from given input path
			text = env.readTextFile(params.get("input"));
		} else {
			// get default test text data
			System.out.println("Executing WordCount example with default input data set.");
			System.out.println("Use --input to specify file input.");
			text = WordCountData.getDefaultTextLineDataSet(env);
		}

		DataSet<Tuple2<String, Integer>> counts =
				// split up the lines in pairs (2-tuples) containing: (word,1)
				text.flatMap(new Tokenizer())
				// group by the tuple field "0" and sum up tuple field "1"
				.groupBy(0)
				.sum(1);

		// emit result
		if (params.has("output")) {
			counts.writeAsCsv(params.get("output"), "\n", " ");
			// execute program
			env.execute("WordCount Example");
		} else {
			System.out.println("Printing result to stdout. Use --output to specify output path.");
			counts.print();
		}

	}