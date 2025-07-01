public List<Writable> execute(List<Writable> input) {
        List<Writable> currValues = input;

        for (DataAction d : actionList) {
            if (d.getTransform() != null) {
                Transform t = d.getTransform();
                currValues = t.map(currValues);

            } else if (d.getFilter() != null) {
                Filter f = d.getFilter();
                if (f.removeExample(currValues))
                    return null;
            } else if (d.getConvertToSequence() != null) {
                throw new RuntimeException(
                        "Cannot execute examples individually: TransformProcess contains a ConvertToSequence operation");
            } else if (d.getConvertFromSequence() != null) {
                throw new RuntimeException(
                        "Unexpected operation: TransformProcess contains a ConvertFromSequence operation");
            } else if (d.getSequenceSplit() != null) {
                throw new RuntimeException(
                        "Cannot execute examples individually: TransformProcess contains a SequenceSplit operation");
            } else {
                throw new RuntimeException("Unknown action: " + d);
            }
        }

        return currValues;
    }