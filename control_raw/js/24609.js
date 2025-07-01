function addCap (coord, v, normal, type, isBeginning, context) {
    var neg_normal = Vector.neg(normal);
    var has_texcoord = (context.texcoord_index != null);

    switch (type){
    case CAP_TYPE.square:
        var tangent;
        // first vertex on the lineString
        if (isBeginning){
            tangent = [normal[1], -normal[0]];

            addVertex(coord, Vector.add(normal, tangent), normal, 1, v, context, 1);
            addVertex(coord, Vector.add(neg_normal, tangent), normal, 0, v, context, 1);

            if (has_texcoord) {
                // Add length of square cap to texture coordinate
                v += 0.5 * context.texcoord_width * context.v_scale;
            }

            addVertex(coord, normal, normal, 1, v, context, 1);
            addVertex(coord, neg_normal, normal, 0, v, context, 1);

        }
        // last vertex on the lineString
        else {
            tangent = [-normal[1], normal[0]];

            addVertex(coord, normal, normal, 1, v, context, 1);
            addVertex(coord, neg_normal, normal, 0, v, context, 1);

            if (has_texcoord) {
                // Add length of square cap to texture coordinate
                v += 0.5 * context.texcoord_width * context.v_scale;
            }

            addVertex(coord, Vector.add(normal, tangent), normal, 1, v, context, 1);
            addVertex(coord, Vector.add(neg_normal, tangent), normal, 0, v, context, 1);
        }

        indexPairs(1, context);
        break;
    case CAP_TYPE.round:
        // default for end cap, beginning cap will overwrite below (this way we're always passing a non-null value,
        // even if texture coords are disabled)
        var uvA = zero_v, uvB = one_v, uvC = mid_v;
        var nA, nB;

        // first vertex on the lineString
        if (isBeginning) {
            nA = normal;
            nB = neg_normal;

            if (has_texcoord){
                v += 0.5 * context.texcoord_width * context.v_scale;
                uvA = one_v, uvB = zero_v, uvC = mid_v; // update cap UV order
            }
        }
        // last vertex on the lineString - flip the direction of the cap
        else {
            nA = neg_normal;
            nB = normal;
        }

        if (has_texcoord) {
            zero_v[1] = v, one_v[1] = v, mid_v[1] = v; // update cap UV values
        }

        addFan(coord,
            nA, zero_vec2, nB,  // extrusion normal
            normal,             // line normal, for offsets
            uvA, uvC, uvB,      // texture coords (ignored if disabled)
            true, false, context
        );

        break;
    case CAP_TYPE.butt:
        return;
    }
}