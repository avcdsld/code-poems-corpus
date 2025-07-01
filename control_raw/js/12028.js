function(poly1, poly2, n, dist)
{
    var arr = [];

    var verts1 = poly1.tVerts;
    for(var i=0; i<verts1.length; i+=2){
        var vx = verts1[i];
        var vy = verts1[i+1];
        if(poly2.containsVert(vx, vy)){
            arr.push(new Contact(new Vect(vx, vy), n, dist, hashPair(poly1.hashid, i>>1)));
        }
    }
    
    var verts2 = poly2.tVerts;
    for(var i=0; i<verts2.length; i+=2){
        var vx = verts2[i];
        var vy = verts2[i+1];
        if(poly1.containsVert(vx, vy)){
            arr.push(new Contact(new Vect(vx, vy), n, dist, hashPair(poly2.hashid, i>>1)));
        }
    }
    
    return (arr.length ? arr : findVertsFallback(poly1, poly2, n, dist));
}