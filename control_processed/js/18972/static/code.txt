function processGetStats(req,res){

    processAuth(req,res).then(function (authResult){
        if(!authResult){
            return;
        }
        res.status(200);
        if(('sws-auth' in req) && req['sws-auth']){
            res.setHeader('x-sws-authenticated','true');
        }
        res.json( processor.getStats( req.query ) );
    });

    /*
    if(!processAuth(req,res)) {
        return;
    }

    if(('sws-auth' in req) && req['sws-auth']){
        res.setHeader('x-sws-authenticated','true');
    }

    res.status(200).json( processor.getStats( req.query ) );
    */
}