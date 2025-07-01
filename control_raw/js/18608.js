function LGraphLensFX() {
            this.addInput("in", "Texture");
            this.addInput("f", "number");
            this.addOutput("out", "Texture");
            this.properties = {
                enabled: true,
                factor: 1,
                precision: LGraphTexture.LOW
            };

            this._uniforms = { u_texture: 0, u_factor: 1 };
        }