function checkCacheTRBL(current, cache) {
                    if (cache === undefined)
                        return true;
                    else if (current.t !== cache.t ||
                        current.r !== cache.r ||
                        current.b !== cache.b ||
                        current.l !== cache.l)
                        return true;
                    return false;
                }