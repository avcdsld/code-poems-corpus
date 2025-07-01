@Override
    public ValNums apply(Env env, Env.StackHelp stk, AstRoot asts[]) {
        Frame fr = stk.track(asts[1].exec(env)).getFrame();
        String type = stk.track(asts[2].exec(env)).getStr();
        DType dtype;
        switch (type) {
            case "numeric": // Numeric, but not categorical or time
                dtype = DType.Numeric;
                break;
            case "categorical": // Integer, with a categorical/factor String mapping
                dtype = DType.Categorical;
                break;
            case "string": // String
                dtype = DType.String;
                break;
            case "time": // Long msec since the Unix Epoch - with a variety of display/parse options
                dtype = DType.Time;
                break;
            case "uuid": // UUID
                dtype = DType.UUID;
                break;
            case "bad": // No none-NA rows (triple negative! all NAs or zero rows)
                dtype = DType.Bad;
                break;
            default:
                throw new IllegalArgumentException("unknown data type to filter by: " + type);
        }
        Vec vecs[] = fr.vecs();
        ArrayList<Double> idxs = new ArrayList<>();
        for (double i = 0; i < fr.numCols(); i++)
            if (dtype.equals(DType.Numeric) && vecs[(int) i].isNumeric()){
                    idxs.add(i);
            }
            else if (dtype.equals(DType.Categorical) && vecs[(int) i].isCategorical()){
                idxs.add(i);
            }
            else if (dtype.equals(DType.String) && vecs[(int) i].isString()){
                idxs.add(i);
            }
            else if (dtype.equals(DType.Time) && vecs[(int) i].isTime()){
                idxs.add(i);
            }
            else if (dtype.equals(DType.UUID) && vecs[(int) i].isUUID()){
                idxs.add(i);
            } else if (dtype.equals(DType.Bad) && vecs[(int) i].isBad()){
                idxs.add(i);
            }

        double[] include_cols = new double[idxs.size()];
        int i = 0;
        for (double d : idxs)
            include_cols[i++] = (int) d;
        return new ValNums(include_cols);
    }