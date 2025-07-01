function (gl) {
            var vertexShaderSource =
                    //.x = declination
                    //.y = right ascension
                    //.z = point size
                    //.w = magnitude
                    'attribute vec4 vertexPoint;\n' +

                    'uniform mat4 mvpMatrix;\n' +
                    //number of days (positive or negative) since Greenwich noon, Terrestrial Time,
                    // on 1 January 2000 (J2000.0)
                    'uniform float numDays;\n' +
                    'uniform vec2 magnitudeRange;\n' +

                    'varying float magnitudeWeight;\n' +

                    //normalizes an angle between 0.0 and 359.0
                    'float normalizeAngle(float angle) {\n' +
                    '   float angleDivisions = angle / 360.0;\n' +
                    '   return 360.0 * (angleDivisions - floor(angleDivisions));\n' +
                    '}\n' +

                    //transforms declination and right ascension in cartesian coordinates
                    'vec3 computePosition(float dec, float ra) {\n' +
                    '   float GMST = normalizeAngle(280.46061837 + 360.98564736629 * numDays);\n' +
                    '   float GHA = normalizeAngle(GMST - ra);\n' +
                    '   float lon = -GHA + 360.0 * step(180.0, GHA);\n' +
                    '   float latRad = radians(dec);\n' +
                    '   float lonRad = radians(lon);\n' +
                    '   float radCosLat = cos(latRad);\n' +
                    '   return vec3(radCosLat * sin(lonRad), sin(latRad), radCosLat * cos(lonRad));\n' +
                    '}\n' +

                    //normalizes a value between 0.0 and 1.0
                    'float normalizeScalar(float value, float minValue, float maxValue){\n' +
                    '   return (value - minValue) / (maxValue - minValue);\n' +
                    '}\n' +

                    'void main() {\n' +
                    '   vec3 vertexPosition = computePosition(vertexPoint.x, vertexPoint.y);\n' +
                    '   gl_Position = mvpMatrix * vec4(vertexPosition.xyz, 1.0);\n' +
                    '   gl_Position.z = gl_Position.w - 0.00001;\n' +
                    '   gl_PointSize = vertexPoint.z;\n' +
                    '   magnitudeWeight = normalizeScalar(vertexPoint.w, magnitudeRange.x, magnitudeRange.y);\n' +
                    '}',
                fragmentShaderSource =
                    'precision mediump float;\n' +

                    'uniform sampler2D textureSampler;\n' +
                    'uniform int textureEnabled;\n' +

                    'varying float magnitudeWeight;\n' +

                    'const vec4 white = vec4(1.0, 1.0, 1.0, 1.0);\n' +
                    'const vec4 grey = vec4(0.5, 0.5, 0.5, 1.0);\n' +

                    'void main() {\n' +
                    '   if (textureEnabled == 1) {\n' +
                    '       gl_FragColor = texture2D(textureSampler, gl_PointCoord);\n' +
                    '   }\n' +
                    '   else {\n' +
                    //paint the starts in shades of grey, where the brightest star is white and the dimmest star is grey
                    '       gl_FragColor = mix(white, grey, magnitudeWeight);\n' +
                    '   }\n' +
                    '}';

            // Call to the superclass, which performs shader program compiling and linking.
            GpuProgram.call(this, gl, vertexShaderSource, fragmentShaderSource, ["vertexPoint"]);

            /**
             * The WebGL location for this program's 'vertexPoint' attribute.
             * @type {Number}
             * @readonly
             */
            this.vertexPointLocation = this.attributeLocation(gl, "vertexPoint");

            /**
             * The WebGL location for this program's 'mvpMatrix' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.mvpMatrixLocation = this.uniformLocation(gl, "mvpMatrix");

            /**
             * The WebGL location for this program's 'numDays' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.numDaysLocation = this.uniformLocation(gl, "numDays");

            /**
             * The WebGL location for this program's 'magnitudeRangeLocation' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.magnitudeRangeLocation = this.uniformLocation(gl, "magnitudeRange");

            /**
             * The WebGL location for this program's 'textureSampler' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.textureUnitLocation = this.uniformLocation(gl, "textureSampler");

            /**
             * The WebGL location for this program's 'textureEnabled' uniform.
             * @type {WebGLUniformLocation}
             * @readonly
             */
            this.textureEnabledLocation = this.uniformLocation(gl, "textureEnabled");
        }