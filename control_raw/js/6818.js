function createPathProxyFromString(data) {
    if (!data) {
        return new PathProxy();
    }

    // var data = data.replace(/-/g, ' -')
    //     .replace(/  /g, ' ')
    //     .replace(/ /g, ',')
    //     .replace(/,,/g, ',');

    // var n;
    // create pipes so that we can split the data
    // for (n = 0; n < cc.length; n++) {
    //     cs = cs.replace(new RegExp(cc[n], 'g'), '|' + cc[n]);
    // }

    // data = data.replace(/-/g, ',-');

    // create array
    // var arr = cs.split('|');
    // init context point
    var cpx = 0;
    var cpy = 0;
    var subpathX = cpx;
    var subpathY = cpy;
    var prevCmd;

    var path = new PathProxy();
    var CMD = PathProxy.CMD;

    // commandReg.lastIndex = 0;
    // var cmdResult;
    // while ((cmdResult = commandReg.exec(data)) != null) {
    //     var cmdStr = cmdResult[1];
    //     var cmdContent = cmdResult[2];

    var cmdList = data.match(commandReg);
    for (var l = 0; l < cmdList.length; l++) {
        var cmdText = cmdList[l];
        var cmdStr = cmdText.charAt(0);

        var cmd;

        // String#split is faster a little bit than String#replace or RegExp#exec.
        // var p = cmdContent.split(valueSplitReg);
        // var pLen = 0;
        // for (var i = 0; i < p.length; i++) {
        //     // '' and other invalid str => NaN
        //     var val = parseFloat(p[i]);
        //     !isNaN(val) && (p[pLen++] = val);
        // }

        var p = cmdText.match(numberReg) || [];
        var pLen = p.length;
        for (var i = 0; i < pLen; i++) {
            p[i] = parseFloat(p[i]);
        }

        var off = 0;
        while (off < pLen) {
            var ctlPtx;
            var ctlPty;

            var rx;
            var ry;
            var psi;
            var fa;
            var fs;

            var x1 = cpx;
            var y1 = cpy;

            // convert l, H, h, V, and v to L
            switch (cmdStr) {
                case 'l':
                    cpx += p[off++];
                    cpy += p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'L':
                    cpx = p[off++];
                    cpy = p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'm':
                    cpx += p[off++];
                    cpy += p[off++];
                    cmd = CMD.M;
                    path.addData(cmd, cpx, cpy);
                    subpathX = cpx;
                    subpathY = cpy;
                    cmdStr = 'l';
                    break;
                case 'M':
                    cpx = p[off++];
                    cpy = p[off++];
                    cmd = CMD.M;
                    path.addData(cmd, cpx, cpy);
                    subpathX = cpx;
                    subpathY = cpy;
                    cmdStr = 'L';
                    break;
                case 'h':
                    cpx += p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'H':
                    cpx = p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'v':
                    cpy += p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'V':
                    cpy = p[off++];
                    cmd = CMD.L;
                    path.addData(cmd, cpx, cpy);
                    break;
                case 'C':
                    cmd = CMD.C;
                    path.addData(
                        cmd, p[off++], p[off++], p[off++], p[off++], p[off++], p[off++]
                    );
                    cpx = p[off - 2];
                    cpy = p[off - 1];
                    break;
                case 'c':
                    cmd = CMD.C;
                    path.addData(
                        cmd,
                        p[off++] + cpx, p[off++] + cpy,
                        p[off++] + cpx, p[off++] + cpy,
                        p[off++] + cpx, p[off++] + cpy
                    );
                    cpx += p[off - 2];
                    cpy += p[off - 1];
                    break;
                case 'S':
                    ctlPtx = cpx;
                    ctlPty = cpy;
                    var len = path.len();
                    var pathData = path.data;
                    if (prevCmd === CMD.C) {
                        ctlPtx += cpx - pathData[len - 4];
                        ctlPty += cpy - pathData[len - 3];
                    }
                    cmd = CMD.C;
                    x1 = p[off++];
                    y1 = p[off++];
                    cpx = p[off++];
                    cpy = p[off++];
                    path.addData(cmd, ctlPtx, ctlPty, x1, y1, cpx, cpy);
                    break;
                case 's':
                    ctlPtx = cpx;
                    ctlPty = cpy;
                    var len = path.len();
                    var pathData = path.data;
                    if (prevCmd === CMD.C) {
                        ctlPtx += cpx - pathData[len - 4];
                        ctlPty += cpy - pathData[len - 3];
                    }
                    cmd = CMD.C;
                    x1 = cpx + p[off++];
                    y1 = cpy + p[off++];
                    cpx += p[off++];
                    cpy += p[off++];
                    path.addData(cmd, ctlPtx, ctlPty, x1, y1, cpx, cpy);
                    break;
                case 'Q':
                    x1 = p[off++];
                    y1 = p[off++];
                    cpx = p[off++];
                    cpy = p[off++];
                    cmd = CMD.Q;
                    path.addData(cmd, x1, y1, cpx, cpy);
                    break;
                case 'q':
                    x1 = p[off++] + cpx;
                    y1 = p[off++] + cpy;
                    cpx += p[off++];
                    cpy += p[off++];
                    cmd = CMD.Q;
                    path.addData(cmd, x1, y1, cpx, cpy);
                    break;
                case 'T':
                    ctlPtx = cpx;
                    ctlPty = cpy;
                    var len = path.len();
                    var pathData = path.data;
                    if (prevCmd === CMD.Q) {
                        ctlPtx += cpx - pathData[len - 4];
                        ctlPty += cpy - pathData[len - 3];
                    }
                    cpx = p[off++];
                    cpy = p[off++];
                    cmd = CMD.Q;
                    path.addData(cmd, ctlPtx, ctlPty, cpx, cpy);
                    break;
                case 't':
                    ctlPtx = cpx;
                    ctlPty = cpy;
                    var len = path.len();
                    var pathData = path.data;
                    if (prevCmd === CMD.Q) {
                        ctlPtx += cpx - pathData[len - 4];
                        ctlPty += cpy - pathData[len - 3];
                    }
                    cpx += p[off++];
                    cpy += p[off++];
                    cmd = CMD.Q;
                    path.addData(cmd, ctlPtx, ctlPty, cpx, cpy);
                    break;
                case 'A':
                    rx = p[off++];
                    ry = p[off++];
                    psi = p[off++];
                    fa = p[off++];
                    fs = p[off++];

                    x1 = cpx, y1 = cpy;
                    cpx = p[off++];
                    cpy = p[off++];
                    cmd = CMD.A;
                    processArc(
                        x1, y1, cpx, cpy, fa, fs, rx, ry, psi, cmd, path
                    );
                    break;
                case 'a':
                    rx = p[off++];
                    ry = p[off++];
                    psi = p[off++];
                    fa = p[off++];
                    fs = p[off++];

                    x1 = cpx, y1 = cpy;
                    cpx += p[off++];
                    cpy += p[off++];
                    cmd = CMD.A;
                    processArc(
                        x1, y1, cpx, cpy, fa, fs, rx, ry, psi, cmd, path
                    );
                    break;
            }
        }

        if (cmdStr === 'z' || cmdStr === 'Z') {
            cmd = CMD.Z;
            path.addData(cmd);
            // z may be in the middle of the path.
            cpx = subpathX;
            cpy = subpathY;
        }

        prevCmd = cmd;
    }

    path.toStatic();

    return path;
}