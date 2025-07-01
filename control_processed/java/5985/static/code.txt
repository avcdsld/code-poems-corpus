public static String getPlanAsJSON(Plan plan) {
		List<DataSinkNode> sinks = Optimizer.createPreOptimizedPlan(plan);
		return new PlanJSONDumpGenerator().getPactPlanAsJSON(sinks);
	}