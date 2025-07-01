function (gl, vertexShaderSource, fragmentShaderSource, attribute) {

            // Call to the superclass, which performs shader program compiling and linking.
            GpuProgram.call(this, gl, vertexShaderSource, fragmentShaderSource, attribute);


            // Frag color mode indicates the atmospheric scattering color components written to the fragment color.
            this.FRAGMODE_SKY = 1;
            this.FRAGMODE_GROUND_PRIMARY = 2;
            this.FRAGMODE_GROUND_SECONDARY = 3;
            this.FRAGMODE_GROUND_PRIMARY_TEX_BLEND = 4;

            /**
             * The globe's atmosphere altitude.
             * @type {Number}
             * @default 160000.0 meters
             */
            this.altitude = 160000;

            /**
             * This atmosphere's Rayleigh scale depth.
             * @type {Number}
             * @default 0.25
             */
            this.rayleighScaleDepth = 0.25;

            /**
             * The WebGL location for this program's 'fragMode' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.fragModeLocation = this.uniformLocation(gl, "fragMode");

            /**
             * The WebGL location for this program's 'mvpMatrix' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.mvpMatrixLocation = this.uniformLocation(gl, "mvpMatrix");

            /**
             * The WebGL location for this program's 'texCoordMatrix' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.texCoordMatrixLocation = this.uniformLocation(gl, "texCoordMatrix");

            /**
             * The WebGL location for this program's 'vertexOrigin' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.vertexOriginLocation = this.uniformLocation(gl, "vertexOrigin");

            /**
             * The WebGL location for this program's 'eyePoint' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.eyePointLocation = this.uniformLocation(gl, "eyePoint");

            /**
             * The WebGL location for this program's 'eyeMagnitude' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.eyeMagnitudeLocation = this.uniformLocation(gl, "eyeMagnitude");

            /**
             * The WebGL location for this program's 'eyeMagnitude2' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.eyeMagnitude2Location = this.uniformLocation(gl, "eyeMagnitude2");

            /**
             * The WebGL location for this program's 'lightDirection' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.lightDirectionLocation = this.uniformLocation(gl, "lightDirection");

            /**
             * The WebGL location for this program's 'atmosphereRadius' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.atmosphereRadiusLocation = this.uniformLocation(gl, "atmosphereRadius");

            /**
             * The WebGL location for this program's 'atmosphereRadius2' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.atmosphereRadius2Location = this.uniformLocation(gl, "atmosphereRadius2");

            /**
             * The WebGL location for this program's 'globeRadius' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.globeRadiusLocation = this.uniformLocation(gl, "globeRadius");

            /**
             * The WebGL location for this program's 'scale' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.scaleLocation = this.uniformLocation(gl, "scale");

            /**
             * The WebGL location for this program's 'scaleDepth' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.scaleDepthLocation = this.uniformLocation(gl, "scaleDepth");

            /**
             * The WebGL location for this program's 'scaleOverScaleDepth' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.scaleOverScaleDepthLocation = this.uniformLocation(gl, "scaleOverScaleDepth");
            
            this.scratchArray9 = new Float32Array(9);
        }