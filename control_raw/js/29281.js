function(ctx, size, texMeters) {
    // fill all with ground Color
    ctx.fillStyle = this.data.groundColor;
    ctx.fillRect(0, 0, size, size);

    var i, col, col1, col2, im, imdata, numpixels;

    if (this.data.groundTexture == 'none') return;
    switch(this.data.groundTexture) {
      case 'checkerboard': {
        ctx.fillStyle = this.data.groundColor2;
        var num = Math.floor(texMeters / 2);
        var step = size / (texMeters / 2); // 2 meters == <step> pixels
        for (i = 0; i < num + 1; i += 2) {
          for (var j = 0; j < num + 1; j ++) {
            ctx.fillRect(Math.floor((i + j % 2) * step), Math.floor(j * step), Math.floor(step), Math.floor(step));
          }
        }
        break;
      }
      case 'squares': {
        var numSquares = 16;
        var squareSize = size / numSquares;
        col1 = new THREE.Color(this.data.groundColor);
        col2 = new THREE.Color(this.data.groundColor2);
        for (i = 0; i < numSquares * numSquares; i++) {
          col = this.random(i + 3) > 0.5 ? col1.clone() : col2.clone();
          col.addScalar(this.random(i + 3) * 0.1 - 0.05);
          ctx.fillStyle = '#' + col.getHexString();
          ctx.fillRect((i % numSquares) * squareSize, Math.floor(i / numSquares) * squareSize, squareSize, squareSize);
        }
        break;
      }
      case 'noise': {
      // TODO: fix
        imdata = ctx.getImageData(0, 0, size, size);
        im = imdata.data;
        col1 = new THREE.Color(this.data.groundColor);
        col2 = new THREE.Color(this.data.groundColor2);
        var diff = new THREE.Color(col2.r - col1.r, col2.g - col1.g, col2.b - col1.b);
        var perlin = new PerlinNoise();
        for (i = 0, j = 0, numpixels = im.length; i < numpixels; i += 4, j++){
          //console.log( (j % size) / size, j / size)
          var rnd = perlin.noise((j % size) / size * 3, j / size / size * 3, 0);
          im[i + 0] = Math.floor((col1.r + diff.r * rnd) * 255);
          im[i + 1] = Math.floor((col1.g + diff.g * rnd) * 255);
          im[i + 2] = Math.floor((col1.b + diff.b * rnd) * 255);
        }
        ctx.putImageData(imdata, 0, 0);
        break;
      }
      case 'walkernoise': {
        var s = Math.floor(size / 2);
        var tex = document.createElement('canvas');
        tex.width = s;
        tex.height = s;
        var texctx = tex.getContext('2d');
        texctx.fillStyle = this.data.groundColor;
        texctx.fillRect(0, 0, s, s);
        imdata = texctx.getImageData(0, 0, s, s);
        im = imdata.data;
        col1 = new THREE.Color(this.data.groundColor);
        col2 = new THREE.Color(this.data.groundColor2);
        var walkers = [];
        var numwalkers = 1000;
        for (i = 0; i < numwalkers; i++) {
          col = col1.clone().lerp(col2, Math.random());
          walkers.push({
            x: Math.random() * s,
            y: Math.random() * s,
            r: Math.floor(col.r * 255),
            g: Math.floor(col.g * 255),
            b: Math.floor(col.b * 255)
          });
        }
        var iterations = 5000;
        for (var it = 0; it< iterations; it++){
          for (i = 0; i < numwalkers; i++) {
            var walker = walkers[i];
            var pos = Math.floor((walker.y * s + walker.x)) * 4;
            im[pos + 0] = walker.r;
            im[pos + 1] = walker.g;
            im[pos + 2] = walker.b;
            walker.x += Math.floor(Math.random() * 3) - 1;
            walker.y += Math.floor(Math.random() * 3) - 1;
            if (walker.x >= s) walker.x = walker.x - s;
            if (walker.y >= s) walker.y = walker.y - s;
            if (walker.x < 0) walker.x = s + walker.x;
            if (walker.y < 0) walker.y = s + walker.y;
          }
        }
        texctx.putImageData(imdata, 0, 0);
        ctx.drawImage(tex, 0, 0, size, size);
        break;
      }
    }
  }