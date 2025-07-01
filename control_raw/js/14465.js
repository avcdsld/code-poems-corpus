function insertNode(i, x, y, last) {
       var p = new Node(i, x, y);

       if (!last) {
           p.prev = p;
           p.next = p;

       } else {
           p.next = last.next;
           p.prev = last;
           last.next.prev = p;
           last.next = p;
       }
       return p;
   }