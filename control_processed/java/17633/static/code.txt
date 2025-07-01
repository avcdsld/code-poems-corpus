public void computeNonEdgeForces(int pointIndex, double theta, INDArray negativeForce, AtomicDouble sumQ) {
        // Make sure that we spend no time on empty nodes or self-interactions
        if (cumSize == 0 || (isLeaf() && size == 1 && index[0] == pointIndex))
            return;


        // Compute distance between point and center-of-mass
        buf.assign(data.slice(pointIndex)).subi(centerOfMass);

        double D = Nd4j.getBlasWrapper().dot(buf, buf);

        // Check whether we can use this node as a "summary"
        if (isLeaf || FastMath.max(boundary.getHh(), boundary.getHw()) / FastMath.sqrt(D) < theta) {

            // Compute and add t-SNE force between point and current node
            double Q = 1.0 / (1.0 + D);
            double mult = cumSize * Q;
            sumQ.addAndGet(mult);
            mult *= Q;
            negativeForce.addi(buf.mul(mult));

        } else {

            // Recursively apply Barnes-Hut to children
            northWest.computeNonEdgeForces(pointIndex, theta, negativeForce, sumQ);
            northEast.computeNonEdgeForces(pointIndex, theta, negativeForce, sumQ);
            southWest.computeNonEdgeForces(pointIndex, theta, negativeForce, sumQ);
            southEast.computeNonEdgeForces(pointIndex, theta, negativeForce, sumQ);
        }
    }