function(seg, poly)
{
    var arr = [];

    var planes = poly.tPlanes;
    var numVerts = planes.length;
    
    var segD = vdot(seg.tn, seg.ta);
    var minNorm = poly.valueOnAxis(seg.tn, segD) - seg.r;
    var minNeg = poly.valueOnAxis(vneg(seg.tn), -segD) - seg.r;
    if(minNeg > 0 || minNorm > 0) return NONE;
    
    var mini = 0;
    var poly_min = segValueOnAxis(seg, planes[0].n, planes[0].d);
    if(poly_min > 0) return NONE;
    for(var i=0; i<numVerts; i++){
        var dist = segValueOnAxis(seg, planes[i].n, planes[i].d);
        if(dist > 0){
            return NONE;
        } else if(dist > poly_min){
            poly_min = dist;
            mini = i;
        }
    }
    
    var poly_n = vneg(planes[mini].n);
    
    var va = vadd(seg.ta, vmult(poly_n, seg.r));
    var vb = vadd(seg.tb, vmult(poly_n, seg.r));
    if(poly.containsVert(va.x, va.y))
        arr.push(new Contact(va, poly_n, poly_min, hashPair(seg.hashid, 0)));
    if(poly.containsVert(vb.x, vb.y))
        arr.push(new Contact(vb, poly_n, poly_min, hashPair(seg.hashid, 1)));
    
    // Floating point precision problems here.
    // This will have to do for now.
//  poly_min -= cp_collision_slop; // TODO is this needed anymore?
    
    if(minNorm >= poly_min || minNeg >= poly_min) {
        if(minNorm > minNeg)
            findPointsBehindSeg(arr, seg, poly, minNorm, 1);
        else
            findPointsBehindSeg(arr, seg, poly, minNeg, -1);
    }
    
    // If no other collision points are found, try colliding endpoints.
    if(arr.length === 0){
        var mini2 = mini * 2;
        var verts = poly.tVerts;

        var poly_a = new Vect(verts[mini2], verts[mini2+1]);
        
        var con;
        if((con = circle2circleQuery(seg.ta, poly_a, seg.r, 0, arr))) return [con];
        if((con = circle2circleQuery(seg.tb, poly_a, seg.r, 0, arr))) return [con];

        var len = numVerts * 2;
        var poly_b = new Vect(verts[(mini2+2)%len], verts[(mini2+3)%len]);
        if((con = circle2circleQuery(seg.ta, poly_b, seg.r, 0, arr))) return [con];
        if((con = circle2circleQuery(seg.tb, poly_b, seg.r, 0, arr))) return [con];
    }

//  console.log(poly.tVerts, poly.tPlanes);
//  console.log('seg2poly', arr);
    return arr;
}