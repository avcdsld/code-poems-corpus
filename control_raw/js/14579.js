function setBlendMode(mode, gl) {
         gl = gl || this.gl;
         gl.enable(gl.BLEND);

         switch (mode) {
           case "multiply":
             gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
             this.currentBlendMode = mode;
             break;

           default:
             gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
             this.currentBlendMode = "normal";
             break;
         }
       }