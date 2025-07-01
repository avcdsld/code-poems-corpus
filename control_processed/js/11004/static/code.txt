function(p1,p2,p3,p4) {
      var denom = (p4.y-p3.y)*(p2.x-p1.x)-(p4.x-p3.x)*(p2.y-p1.y);
      if(denom===0.0) { return false; } // parallel lines
      var ua = ((p4.x-p3.x)*(p1.y-p3.y)-(p4.y-p3.y)*(p1.x-p3.x))/denom;
      var ub = ((p2.x-p1.x)*(p1.y-p3.y)-(p2.y-p1.y)*(p1.x-p3.x))/denom;
      if(ua>0.0&&ua<1.0&&ub>0.0&&ub<1.0) {
        var up = new Vec(p1.x+ua*(p2.x-p1.x), p1.y+ua*(p2.y-p1.y));
        return {ua:ua, ub:ub, up:up}; // up is intersection point
      }
      return false;
    }