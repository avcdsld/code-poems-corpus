function positionRoot(wt) {
    wt.prelim = ( wt.children[0].prelim + 
                  wt.children[0].mod -
                  wt.children[0].x_size/2 +
                  wt.children[wt.num_children - 1].mod + 
                  wt.children[wt.num_children - 1].prelim +
                  wt.children[wt.num_children - 1].x_size/2) / 2;
  }