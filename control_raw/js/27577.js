async function(symbol = false) {
            let parameters = symbol ? {symbol:symbol} : {};
            return await request('/v3/openOrders', parameters, {type: 'SIGNED'});
        }