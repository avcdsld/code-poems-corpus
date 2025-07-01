private void onProbationHit(Node node) {
    admittor.record(node.key);

    node.remove();
    node.status = Status.PROTECTED;
    node.appendToTail(headProtected);

    sizeProtected++;
    if (sizeProtected > maxProtected) {
      Node demote = headProtected.next;
      demote.remove();
      demote.status = Status.PROBATION;
      demote.appendToTail(headProbation);
      sizeProtected--;
    }
  }