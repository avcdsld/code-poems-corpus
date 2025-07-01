function modelCenter(view, magnet) {

        var model = view.model;
        var bbox = model.getBBox();
        var center = bbox.center();
        var angle = model.angle();

        var portId = view.findAttribute('port', magnet);
        if (portId) {
            var portGroup = model.portProp(portId, 'group');
            var portsPositions = model.getPortsPositions(portGroup);
            var anchor = new g.Point(portsPositions[portId]).offset(bbox.origin());
            anchor.rotate(center, -angle);
            return anchor;
        }

        return center;
    }