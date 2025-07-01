function GLTFParser( json, extensions, options ) {

    this.json = json || {};
    this.extensions = extensions || {};
    this.options = options || {};

    // loader object cache
    this.cache = new GLTFRegistry();

    // BufferGeometry caching
    this.primitiveCache = [];

    this.textureLoader = new THREE.TextureLoader( this.options.manager );
    this.textureLoader.setCrossOrigin( this.options.crossOrigin );

    this.fileLoader = new THREE.FileLoader( this.options.manager );
    this.fileLoader.setResponseType( 'arraybuffer' );

}