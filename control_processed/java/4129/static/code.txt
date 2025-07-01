public <M> Graph<K, VV, EV> runGatherSumApplyIteration(
			org.apache.flink.graph.gsa.GatherFunction<VV, EV, M> gatherFunction, SumFunction<VV, EV, M> sumFunction,
			ApplyFunction<K, VV, M> applyFunction, int maximumNumberOfIterations) {

		return this.runGatherSumApplyIteration(gatherFunction, sumFunction, applyFunction,
				maximumNumberOfIterations, null);
	}