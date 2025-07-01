private void constructFailureStates()
    {
        Queue<State> queue = new LinkedBlockingDeque<State>();

        // 第一步，将深度为1的节点的failure设为根节点
        for (State depthOneState : this.rootState.getStates())
        {
            depthOneState.setFailure(this.rootState);
            queue.add(depthOneState);
        }
        this.failureStatesConstructed = true;

        // 第二步，为深度 > 1 的节点建立failure表，这是一个bfs
        while (!queue.isEmpty())
        {
            State currentState = queue.remove();

            for (Character transition : currentState.getTransitions())
            {
                State targetState = currentState.nextState(transition);
                queue.add(targetState);

                State traceFailureState = currentState.failure();
                while (traceFailureState.nextState(transition) == null)
                {
                    traceFailureState = traceFailureState.failure();
                }
                State newFailureState = traceFailureState.nextState(transition);
                targetState.setFailure(newFailureState);
                targetState.addEmit(newFailureState.emit());
            }
        }
    }