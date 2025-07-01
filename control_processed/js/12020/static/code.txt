function(node, a, b)
{
    var idx = 1/(b.x - a.x);
    var tx1 = (node.bb_l == a.x ? -Infinity : (node.bb_l - a.x)*idx);
    var tx2 = (node.bb_r == a.x ?  Infinity : (node.bb_r - a.x)*idx);
    var txmin = min(tx1, tx2);
    var txmax = max(tx1, tx2);
    
    var idy = 1/(b.y - a.y);
    var ty1 = (node.bb_b == a.y ? -Infinity : (node.bb_b - a.y)*idy);
    var ty2 = (node.bb_t == a.y ?  Infinity : (node.bb_t - a.y)*idy);
    var tymin = min(ty1, ty2);
    var tymax = max(ty1, ty2);
    
    if(tymin <= txmax && txmin <= tymax){
        var min_ = max(txmin, tymin);
        var max_ = min(txmax, tymax);
        
        if(0.0 <= max_ && min_ <= 1.0) return max(min_, 0.0);
    }
    
    return Infinity;
}