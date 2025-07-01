public INDArray symmetrized(INDArray rowP, INDArray colP, INDArray valP) {
        INDArray rowCounts = Nd4j.create(N);

        MemoryWorkspace workspace =
                workspaceMode == WorkspaceMode.NONE ? new DummyWorkspace()
                        : Nd4j.getWorkspaceManager().getWorkspaceForCurrentThread(
                        workspaceConfigurationExternal,
                        workspaceExternal);

        try (MemoryWorkspace ws = workspace.notifyScopeEntered()) {
            for (int n = 0; n < N; n++) {
                int begin = rowP.getInt(n);
                int end = rowP.getInt(n + 1);
                for (int i = begin; i < end; i++) {
                    boolean present = false;
                    for (int m = rowP.getInt(colP.getInt(i)); m < rowP.getInt(colP.getInt(i) + 1); m++)
                        if (colP.getInt(m) == n) {
                            present = true;
                        }


                    if (present)
                        rowCounts.putScalar(n, rowCounts.getDouble(n) + 1);

                    else {
                        rowCounts.putScalar(n, rowCounts.getDouble(n) + 1);
                        rowCounts.putScalar(colP.getInt(i), rowCounts.getDouble(colP.getInt(i)) + 1);
                    }
                }
            }


            int numElements = rowCounts.sum(Integer.MAX_VALUE).getInt(0);
            INDArray offset = Nd4j.create(N);
            INDArray symRowP = Nd4j.create(N + 1);
            INDArray symColP = Nd4j.create(numElements);
            INDArray symValP = Nd4j.create(numElements);

            for (int n = 0; n < N; n++)
                symRowP.putScalar(n + 1, symRowP.getDouble(n) + rowCounts.getDouble(n));


            for (int n = 0; n < N; n++) {
                for (int i = rowP.getInt(n); i < rowP.getInt(n + 1); i++) {
                    boolean present = false;
                    for (int m = rowP.getInt(colP.getInt(i)); m < rowP.getInt(colP.getInt(i)) + 1; m++) {
                        if (colP.getInt(m) == n) {
                            present = true;
                            if (n < colP.getInt(i)) {
                                // make sure we do not add elements twice
                                symColP.putScalar(symRowP.getInt(n) + offset.getInt(n), colP.getInt(i));
                                symColP.putScalar(symRowP.getInt(colP.getInt(i)) + offset.getInt(colP.getInt(i)), n);
                                symValP.putScalar(symRowP.getInt(n) + offset.getInt(n),
                                        valP.getDouble(i) + valP.getDouble(m));
                                symValP.putScalar(symRowP.getInt(colP.getInt(i)) + offset.getInt(colP.getInt(i)),
                                        valP.getDouble(i) + valP.getDouble(m));
                            }
                        }
                    }

                    // If (colP[i], n) is not present, there is no addition involved
                    if (!present) {
                        int colPI = colP.getInt(i);
                        if (n < colPI) {
                            symColP.putScalar(symRowP.getInt(n) + offset.getInt(n), colPI);
                            symColP.putScalar(symRowP.getInt(colP.getInt(i)) + offset.getInt(colPI), n);
                            symValP.putScalar(symRowP.getInt(n) + offset.getInt(n), valP.getDouble(i));
                            symValP.putScalar(symRowP.getInt(colPI) + offset.getInt(colPI), valP.getDouble(i));
                        }

                    }

                    // Update offsets
                    if (!present || (present && n < colP.getInt(i))) {
                        offset.putScalar(n, offset.getInt(n) + 1);
                        int colPI = colP.getInt(i);
                        if (colPI != n)
                            offset.putScalar(colPI, offset.getDouble(colPI) + 1);
                    }
                }
            }

            // Divide the result by two
            symValP.divi(2.0);
            return symValP;

        }


    }