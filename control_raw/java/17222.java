public void validate(boolean allowDisconnected, boolean allowNoOutput){

        if (networkInputs == null || networkInputs.isEmpty()) {
            throw new IllegalStateException( "Invalid configuration: network has no inputs. " +
                    "Use .addInputs(String...) to label (and give an ordering to) the network inputs");
        }
        if ((networkOutputs == null || networkOutputs.isEmpty()) && !allowNoOutput) {
            throw new IllegalStateException("Invalid configuration: network has no outputs." +
                    "Use .setOutput(String...) to specify (and give an ordering to) the output vertices, " +
                    "or use allowNoOutputs(true) to disable this check");
        }

        //Check uniqueness of names for inputs, layers, GraphNodes
        for (String s : networkInputs) {
            if (vertices.containsKey(s)) {
                throw new IllegalStateException("Invalid configuration: name \"" + s
                                + "\" is present in both network inputs and graph vertices/layers");
            }
        }

        //Check: each layer & node has at least one input
        for (Map.Entry<String, List<String>> e : vertexInputs.entrySet()) {
            String nodeName = e.getKey();
            if (e.getValue() == null || e.getValue().isEmpty()) {
                throw new IllegalStateException("Invalid configuration: vertex \"" + nodeName + "\" has no inputs");
            }
            for (String inputName : e.getValue()) {
                if (!vertices.containsKey(inputName) && !networkInputs.contains(inputName)) {
                    throw new IllegalStateException("Invalid configuration: Vertex \"" + nodeName + "\" has input \""
                                    + inputName + "\" that does not exist");
                }
            }
        }

        //Check output names:
        if(networkOutputs != null) {
            for (String s : networkOutputs) {
                if (!vertices.containsKey(s)) {
                    throw new IllegalStateException(
                            "Invalid configuration: Output name \"" + s + "\" is not a valid vertex");
                }
            }
        }

        //Check that there aren't any disconnected vertices
        if(!allowDisconnected){
            //A vertex is considered disconnected if it is (a) not an output vertex, and (b) isn't used an as input
            // to another layer

            Set<String> seenAsInput = new HashSet<>();
            seenAsInput.addAll(networkOutputs);
            for(Map.Entry<String,List<String>> e : vertexInputs.entrySet()){
                seenAsInput.addAll(e.getValue());
            }

            Set<String> disconnected = new HashSet<>();
            disconnected.addAll(networkInputs);
            disconnected.addAll(vertices.keySet());
            disconnected.removeAll(seenAsInput);
            if(!disconnected.isEmpty() && !allowNoOutput){  //If allowing no output: by definition we have disconnected vertices
                throw new IllegalStateException("Invalid configuration: disconnected vertices found - " + disconnected
                        + ". Disconnected vertices are those that do not connect to either another vertex, and are also"
                        + " not a network output. To disable this error (i.e., allow network configurations with" +
                        " disconnected vertices) use GraphBuilder.allowDisconnected(true)");
            }
        }

        //Check for no graph cycles: done in ComputationGraph.init()
    }