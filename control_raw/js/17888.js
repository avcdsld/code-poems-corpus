function extractMetaNodes(profile) {
        const topLevelNodes = profile.resultRoot.children;
        for (let i = 0; i < topLevelNodes.length && !(profile.gcNode && profile.programNode && profile.idleNode); i++) {
            const node = topLevelNodes[i];
            if (node.functionName === '(garbage collector)')
                profile.gcNode = node;
            else if (node.functionName === '(program)')
                profile.programNode = node;
            else if (node.functionName === '(idle)')
                profile.idleNode = node;
        }
    }