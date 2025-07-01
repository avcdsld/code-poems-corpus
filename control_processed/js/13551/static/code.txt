function(root, disposeGeometry, disposeTexture) {
        // Dettached from parent
        if (root.getParent()) {
            root.getParent().remove(root);
        }
        var disposedMap = {};
        root.traverse(function(node) {
            var material = node.material;
            if (node.geometry && disposeGeometry) {
                node.geometry.dispose(this);
            }
            if (disposeTexture && material && !disposedMap[material.__uid__]) {
                var textureUniforms = material.getTextureUniforms();
                for (var u = 0; u < textureUniforms.length; u++) {
                    var uniformName = textureUniforms[u];
                    var val = material.uniforms[uniformName].value;
                    var uniformType = material.uniforms[uniformName].type;
                    if (!val) {
                        continue;
                    }
                    if (uniformType === 't') {
                        val.dispose && val.dispose(this);
                    }
                    else if (uniformType === 'tv') {
                        for (var k = 0; k < val.length; k++) {
                            if (val[k]) {
                                val[k].dispose && val[k].dispose(this);
                            }
                        }
                    }
                }
                disposedMap[material.__uid__] = true;
            }
            // Particle system and AmbientCubemap light need to dispose
            if (node.dispose) {
                node.dispose(this);
            }
        }, this);
    }