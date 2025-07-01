private ValFrame slow_table(Vec v1, Vec v2, String[] colnames, boolean dense) {


    // For simplicity, repeat v1 if v2 is missing; this will end up filling in
    // only the diagonal of a 2-D array (in what is otherwise a 1-D array).
    // This should be nearly the same cost as a 1-D array, since everything is
    // sparsely filled in.

    // If this is the 1-column case (all counts on the diagonals), just build a
    // 1-d result.
    if (v2 == null) {


      // Slow-pass group counting, very sparse hashtables.  Note that Vec v2 is
      // used as the left-most arg, or OUTER dimension - which will be columns in
      // the final result.
      AstTable.SlowCnt sc = new AstTable.SlowCnt().doAll(v1, v1);

      // Get the column headers as sorted doubles
      double dcols[] = collectDomain(sc._col0s);

      Frame res = new Frame();
      Vec rowlabel = Vec.makeVec(dcols, Vec.VectorGroup.VG_LEN1.addVec());
      rowlabel.setDomain(v1.domain());
      res.add(colnames[0], rowlabel);
      long cnts[] = new long[dcols.length];
      for (int col = 0; col < dcols.length; col++) {
        long lkey = Double.doubleToRawLongBits(dcols[col]);
        NonBlockingHashMapLong<AtomicLong> colx = sc._col0s.get(lkey);
        AtomicLong al = colx.get(lkey);
        cnts[col] = al.get();
      }
      Vec vec = Vec.makeVec(cnts, null, Vec.VectorGroup.VG_LEN1.addVec());
      res.add("Counts", vec);
      return new ValFrame(res);
    }

    // 2-d table result.
    Frame res = new Frame();
    if (!dense) {

      // Slow-pass group counting, very sparse hashtables.  Note that Vec v2 is
      // used as the left-most arg, or OUTER dimension - which will be columns in
      // the final result.
      AstTable.SlowCnt sc = new AstTable.SlowCnt().doAll(v2, v1);

      // Get the column headers as sorted doubles
      double dcols[] = collectDomain(sc._col0s);

      // Need the row headers as sorted doubles also, but these are scattered
      // throughout the nested tables.  Fold 'em into 1 table.
      NonBlockingHashMapLong<AtomicLong> rows = new NonBlockingHashMapLong<>();
      for (NonBlockingHashMapLong.IteratorLong i = iter(sc._col0s); i.hasNext(); )
        rows.putAll(sc._col0s.get(i.nextLong()));
      double drows[] = collectDomain(rows);

      // Now walk the columns one by one, building a Vec per column, building a
      // Frame result.  Rowlabel for first column.

      Vec rowlabel = Vec.makeVec(drows, Vec.VectorGroup.VG_LEN1.addVec());
      rowlabel.setDomain(v1.domain());
      res.add(colnames[0], rowlabel);
      long cnts[] = new long[drows.length];
      for (int col = 0; col < dcols.length; col++) {
        NonBlockingHashMapLong<AtomicLong> colx = sc._col0s.get(Double.doubleToRawLongBits(dcols[col]));
        for (int row = 0; row < drows.length; row++) {
          AtomicLong al = colx.get(Double.doubleToRawLongBits(drows[row]));
          cnts[row] = al == null ? 0 : al.get();
        }
        Vec vec = Vec.makeVec(cnts, null, Vec.VectorGroup.VG_LEN1.addVec());
        res.add(v2.isCategorical() ? v2.domain()[col] : Double.toString(dcols[col]), vec);
      }
    } else {

      AstTable.SlowCnt sc = new AstTable.SlowCnt().doAll(v1, v2);

      double dcols[] = collectDomain(sc._col0s);

      NonBlockingHashMapLong<AtomicLong> rows = new NonBlockingHashMapLong<>();
      for (NonBlockingHashMapLong.IteratorLong i = iter(sc._col0s); i.hasNext(); )
        rows.putAll(sc._col0s.get(i.nextLong()));
      double drows[] = collectDomain(rows);

      int x = 0;
      int sz = 0;
      for (NonBlockingHashMapLong.IteratorLong i = iter(sc._col0s); i.hasNext(); ) {
        sz += sc._col0s.get(i.nextLong()).size();
      }
      long cnts[] = new long[sz];
      double[] left_categ = new double[sz];
      double[] right_categ = new double[sz];

      for (double dcol : dcols) {
        NonBlockingHashMapLong<AtomicLong> colx = sc._col0s.get(Double.doubleToRawLongBits(dcol));
        for (double drow : drows) {
          AtomicLong al = colx.get(Double.doubleToRawLongBits(drow));
          if (al != null) {
            left_categ[x] = dcol;
            right_categ[x] = drow;
            cnts[x] = al.get();
            x++;
          }
        }
      }

      Vec vec = Vec.makeVec(left_categ, Vec.VectorGroup.VG_LEN1.addVec());
      if (v1.isCategorical()) vec.setDomain(v1.domain());
      res.add(colnames[0], vec);
      vec = Vec.makeVec(right_categ, Vec.VectorGroup.VG_LEN1.addVec());
      if (v2.isCategorical()) vec.setDomain(v2.domain());
      res.add(colnames[1], vec);
      vec = Vec.makeVec(cnts, null, Vec.VectorGroup.VG_LEN1.addVec());
      res.add("Counts", vec);
    }
    return new ValFrame(res);
  }