function createGltf(objData, options) {
    const nodes = objData.nodes;
    let materials = objData.materials;
    const name = objData.name;

    // Split materials used by primitives with different types of attributes
    materials = splitIncompatibleMaterials(nodes, materials, options);

    const gltf = {
        accessors : [],
        asset : {},
        buffers : [],
        bufferViews : [],
        extensionsUsed : [],
        extensionsRequired : [],
        images : [],
        materials : [],
        meshes : [],
        nodes : [],
        samplers : [],
        scene : 0,
        scenes : [],
        textures : []
    };

    gltf.asset = {
        generator : 'obj2gltf',
        version: '2.0'
    };

    gltf.scenes.push({
        nodes : []
    });

    const bufferState = {
        positionBuffers : [],
        normalBuffers : [],
        uvBuffers : [],
        indexBuffers : [],
        positionAccessors : [],
        normalAccessors : [],
        uvAccessors : [],
        indexAccessors : []
    };

    const uint32Indices = requiresUint32Indices(nodes);

    const nodesLength = nodes.length;
    for (let i = 0; i < nodesLength; ++i) {
        const node = nodes[i];
        const meshes = node.meshes;
        const meshesLength = meshes.length;

        if (meshesLength === 1) {
            const meshIndex = addMesh(gltf, materials, bufferState, uint32Indices, meshes[0], options);
            addNode(gltf, node.name, meshIndex, undefined);
        } else {
            // Add meshes as child nodes
            const parentIndex = addNode(gltf, node.name);
            for (let j = 0; j < meshesLength; ++j) {
                const mesh = meshes[j];
                const meshIndex = addMesh(gltf, materials, bufferState, uint32Indices, mesh, options);
                addNode(gltf, mesh.name, meshIndex, parentIndex);
            }
        }
    }

    if (gltf.images.length > 0) {
        gltf.samplers.push({
            magFilter : WebGLConstants.LINEAR,
            minFilter : WebGLConstants.NEAREST_MIPMAP_LINEAR,
            wrapS : WebGLConstants.REPEAT,
            wrapT : WebGLConstants.REPEAT
        });
    }

    addBuffers(gltf, bufferState, name, options.separate);

    if (options.specularGlossiness) {
        gltf.extensionsUsed.push('KHR_materials_pbrSpecularGlossiness');
        gltf.extensionsRequired.push('KHR_materials_pbrSpecularGlossiness');
    }

    if (options.unlit) {
        gltf.extensionsUsed.push('KHR_materials_unlit');
        gltf.extensionsRequired.push('KHR_materials_unlit');
    }

    return gltf;
}