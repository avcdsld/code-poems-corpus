function setMarker(data) {

    var rightmenu = function(m) {
        // customise right click context menu
        var rightcontext = "";
        if (polygons[data.name] == undefined) {
            rightcontext = "<button id='delbutton' onclick='delMarker(\""+data.name+"\",true);'>Delete</button>";
        }
        else if (data.editable) {
            rightcontext = "<button onclick='editPoly(\""+data.name+"\",true);'>Edit</button><button onclick='delMarker(\""+data.name+"\",true);'>Delete</button>";
        }
        if ((data.contextmenu !== undefined) && (typeof data.contextmenu === "string")) {
            rightcontext = data.contextmenu.replace(/\$name/g,data.name);
            delete data.contextmenu;
        }
        if (rightcontext.length > 0) {
            var rightmenuMarker = L.popup({offset:[0,-12]}).setContent("<b>"+data.name+"</b><br/>"+rightcontext);
            if (hiderightclick !== true) {
                m.on('contextmenu', function(e) {
                    L.DomEvent.stopPropagation(e);
                    rightmenuMarker.setLatLng(e.latlng);
                    map.openPopup(rightmenuMarker);
                });
            }
        }
        return m;
    }

    //console.log("DATA" typeof data, data);
    if (data.deleted) { // remove markers we are told to
        delMarker(data.name);
        return;
    }

    var ll;
    var lli = null;
    var opt = {};
    opt.color = data.color || "#910000";
    opt.fillColor = data.fillColor || "#910000";
    opt.stroke = (data.hasOwnProperty("stroke")) ? data.stroke : true;
    opt.weight = data.weight || 2;
    opt.opacity = data.opacity || 1;
    opt.fillOpacity = data.fillOpacity || 0.2;
    opt.clickable = (data.hasOwnProperty("clickable")) ? data.clickable : false;
    opt.fill = (data.hasOwnProperty("fill")) ? data.fill : true;
	if (data.hasOwnProperty("dashArray")) { opt.dashArray = data.dashArray; }

    // Replace building
    if (data.hasOwnProperty("building")) {
        if ((data.building === "") && layers.hasOwnProperty("buildings")) {
            map.removeLayer(layers["buildings"]);
            layercontrol._update();
            layers["buildings"] = overlays["buildings"].set("");
            return;
        }
        //layers["buildings"] = new OSMBuildings(map).set(data.building);
        layers["buildings"] = overlays["buildings"].set(data.building);
        map.addLayer(layers["buildings"]);
        return;
    }

    var lay = data.layer || "unknown";
    if (!data.hasOwnProperty("action") || data.action.indexOf("layer") === -1) {
        if (typeof layers[lay] == "undefined") {  // add layer if if doesn't exist
            if (clusterAt > 0) {
                layers[lay] = new L.MarkerClusterGroup({
                    maxClusterRadius:50,
                    spiderfyDistanceMultiplier:1.8,
                    disableClusteringAtZoom:clusterAt
                    //zoomToBoundsOnClick:false
                });
            }
            else {
                layers[lay] = new L.LayerGroup();
            }
            overlays[lay] = layers[lay];
            if (showLayerMenu !== false) {
                layercontrol.addOverlay(layers[lay],lay);
            }
            map.addLayer(overlays[lay]);
            //console.log("ADDED LAYER",lay,layers);
        }
        if (!allData.hasOwnProperty(data.name)) { allData[data.name] = {}; }
        delete data.action;
        Object.keys(data).forEach(key => {
            if (data[key] == null) { delete allData[data.name][key]; }
            else { allData[data.name][key] = data[key]; }
        });
        data = Object.assign({},allData[data.name]);
    }
    delete data.action;

    if (typeof markers[data.name] != "undefined") {
        if (markers[data.name].lay !== data.layer) {
            delMarker(data.name);
        }
        else {
            try {layers[lay].removeLayer(markers[data.name]); }
            catch(e) { console.log("OOPS"); }
        }
    }
    if (typeof polygons[data.name] != "undefined") { layers[lay].removeLayer(polygons[data.name]); }

    if (data.hasOwnProperty("line") && Array.isArray(data.line)) {
        delete opt.fill;
        if (!data.hasOwnProperty("weight")) { opt.weight = 3; }    //Standard settings different for lines
        if (!data.hasOwnProperty("opacity")) { opt.opacity = 0.8; }
        var polyln = L.polyline(data.line, opt);
        polygons[data.name] = polyln;
    }
    else if (data.hasOwnProperty("area") && Array.isArray(data.area)) {
        var polyarea;
        if (data.area.length === 2) { polyarea = L.rectangle(data.area, opt); }
        else { polyarea = L.polygon(data.area, opt); }
        polygons[data.name] = polyarea;
    }
    else if (data.hasOwnProperty("sdlat") && data.hasOwnProperty("sdlon")) {
        if (!data.hasOwnProperty("iconColor")) { opt.color = "blue"; }     //different standard Color Settings
        if (!data.hasOwnProperty("fillColor")) { opt.fillColor = "blue"; }
        var ellipse = L.ellipse(new L.LatLng((data.lat*1), (data.lon*1)), [200000*data.sdlon*Math.cos(data.lat*Math.PI/180), 200000*data.sdlat], 0, opt);
        polygons[data.name] = ellipse;
    }
    else if (data.hasOwnProperty("radius")) {
        if (data.hasOwnProperty("lat") && data.hasOwnProperty("lon")) {
            var polycirc;
            if (Array.isArray(data.radius)) {
                polycirc = L.ellipse(new L.LatLng((data.lat*1), (data.lon*1)), [data.radius[0]*Math.cos(data.lat*Math.PI/180), data.radius[1]], data.tilt || 0, opt);
            }
            else {
                polycirc = L.circle(new L.LatLng((data.lat*1), (data.lon*1)), data.radius*1, opt);
            }
            polygons[data.name] = polycirc;
        }
    }

    if (polygons[data.name] !== undefined) {
        polygons[data.name].lay = lay;
        if (opt.clickable) {
            var words = "<b>"+data.name+"</b>";
            if (data.popup) { var words = words + "<br/>" + data.popup; }
            polygons[data.name].bindPopup(words, {autoClose:false, closeButton:true, closeOnClick:false, minWidth:200});
        }
        polygons[data.name] = rightmenu(polygons[data.name]);
        layers[lay].addLayer(polygons[data.name]);
    }
    else {
        if (typeof data.coordinates == "object") { ll = new L.LatLng(data.coordinates[1],data.coordinates[0]); }
        else if (data.hasOwnProperty("position") && data.position.hasOwnProperty("lat") && data.position.hasOwnProperty("lon")) {
            data.lat = data.position.lat*1;
            data.lon = data.position.lon*1;
            data.alt = data.position.alt;
            if (parseFloat(data.position.alt) == data.position.alt) { data.alt = data.position.alt + " m"; }
            delete data.position;
            ll = new L.LatLng((data.lat*1), (data.lon*1));
        }
        else if (data.hasOwnProperty("lat") && data.hasOwnProperty("lon")) { ll = new L.LatLng((data.lat*1), (data.lon*1)); }
        else if (data.hasOwnProperty("latitude") && data.hasOwnProperty("longitude")) { ll = new L.LatLng((data.latitude*1), (data.longitude*1)); }
        else { console.log("No location:",data); return; }

        // Adding new L.LatLng object (lli) when optional intensity value is defined. Only for use in heatmap layer
        if (typeof data.coordinates == "object") { lli = new L.LatLng(data.coordinates[2],data.coordinates[1],data.coordinates[0]); }
        else if (data.hasOwnProperty("lat") && data.hasOwnProperty("lon") && data.hasOwnProperty("intensity")) { lli = new L.LatLng((data.lat*1), (data.lon*1), (data.intensity*1)); }
        else if (data.hasOwnProperty("latitude") && data.hasOwnProperty("longitude") && data.hasOwnProperty("intensity")) { lli = new L.LatLng((data.latitude*1), (data.longitude*1), (data.intensity*1)); }
        else { lli = ll }

        // Create the icons... handle plane, car, ship, wind, earthquake as specials
        var marker, myMarker;
        var icon, q;
        var words="";
        var labelOffset = [12,0];
        var drag = false;

        if (data.draggable === true) { drag = true; }
        //console.log("ICON",data.icon);
        if (data.hasOwnProperty("icon")) {
            if (data.icon === "ship") {
                marker = L.boatMarker(ll, {
                    title: data.name,
                    color: (data.iconColor || "blue")
                });
                marker.setHeading(parseFloat(data.hdg || data.bearing || "0"));
                q = 'https://www.bing.com/images/search?q='+data.icon+'%20%2B"'+encodeURIComponent(data.name)+'"';
                words += '<a href=\''+q+'\' target="_thingpic">Pictures</a><br>';
            }
            else if (data.icon === "plane") {
                data.iconColor = data.iconColor || "black";
                if (data.hasOwnProperty("squawk")) { data.iconColor = "red"; }
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="310px" height="310px" viewBox="0 0 310 310">';
                icon += '<path d="M134.875,19.74c0.04-22.771,34.363-22.771,34.34,0.642v95.563L303,196.354v35.306l-133.144-43.821v71.424l30.813,24.072v27.923l-47.501-14.764l-47.501,14.764v-27.923l30.491-24.072v-71.424L3,231.66v-35.306l131.875-80.409V19.74z" fill="'+data.iconColor+'"/></svg>';
                var svgplane = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"planeicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svgplane+'" style="width:32px; height:32px; -webkit-transform:rotate('+dir+'deg); -moz-transform:rotate('+dir+'deg);"/>'
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                //q = 'https://www.bing.com/images/search?q='+data.icon+'%20'+encodeURIComponent(data.name);
                //words += '<a href=\''+q+'\' target="_thingpic">Pictures</a><br>';
            }
            else if (data.icon === "helicopter") {
                data.iconColor = data.iconColor || "black";
                if (data.hasOwnProperty("squawk")) { data.iconColor = "red"; }
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="314" height="314" viewBox="0 0 314.5 314.5">';
                icon += '<path d="M268.8 3c-3.1-3.1-8.3-2.9-11.7 0.5L204.9 55.7C198.5 23.3 180.8 0 159.9 0c-21.9 0-40.3 25.5-45.7 60.2L57.4 3.5c-3.4-3.4-8.6-3.6-11.7-0.5 -3.1 3.1-2.9 8.4 0.5 11.7l66.3 66.3c0 0.2 0 0.4 0 0.6 0 20.9 4.6 39.9 12.1 54.4l-78.4 78.4c-3.4 3.4-3.6 8.6-0.5 11.7 3.1 3.1 8.3 2.9 11.7-0.5l76.1-76.1c3.2 3.7 6.7 6.7 10.4 8.9v105.8l-47.7 32.2v18l50.2-22.3h26.9l50.2 22.3v-18L175.8 264.2v-105.8c2.7-1.7 5.4-3.8 7.8-6.2l73.4 73.4c3.4 3.4 8.6 3.6 11.7 0.5 3.1-3.1 2.9-8.3-0.5-11.7l-74.9-74.9c8.6-14.8 14-35.2 14-57.8 0-1.9-0.1-3.8-0.2-5.8l61.2-61.2C271.7 11.3 271.9 6.1 268.8 3z" fill="'+data.iconColor+'"/></svg>';
                var svgheli = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"heliicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svgheli+'" style="width:32px; height:32px; -webkit-transform:rotate('+dir+'deg); -moz-transform:rotate('+dir+'deg);"/>'
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "uav") {
                data.iconColor = data.iconColor || "black";
                if (data.hasOwnProperty("squawk")) { data.iconColor = "red"; }
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 100">';
                icon+= '<path d="M62 82h-8V64h36c0-5-4-9-9-9H54v-8c0-3 4-5 4-11.1 0-4.4-3.6-8-8-8-4.4 0-8 3.6-8 8 0 5.1 4 8.1 4 11.1V55h-27c-5 0-9 4-9 9h36v18H38c-2.4 0-5 2.3-5 5L50 92l17-5C67 84.3 64.4 82 62 82z" fill="'+data.iconColor+'"/></svg>';
                var svguav = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"uavicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svguav+'" style="width:32px; height:32px; -webkit-transform:rotate('+dir+'deg); -moz-transform:rotate('+dir+'deg);"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "car") {
                data.iconColor = data.iconColor || "black";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="47px" height="47px" viewBox="0 0 47 47">';
                icon += '<path d="M29.395,0H17.636c-3.117,0-5.643,3.467-5.643,6.584v34.804c0,3.116,2.526,5.644,5.643,5.644h11.759   c3.116,0,5.644-2.527,5.644-5.644V6.584C35.037,3.467,32.511,0,29.395,0z M34.05,14.188v11.665l-2.729,0.351v-4.806L34.05,14.188z    M32.618,10.773c-1.016,3.9-2.219,8.51-2.219,8.51H16.631l-2.222-8.51C14.41,10.773,23.293,7.755,32.618,10.773z M15.741,21.713   v4.492l-2.73-0.349V14.502L15.741,21.713z M13.011,37.938V27.579l2.73,0.343v8.196L13.011,37.938z M14.568,40.882l2.218-3.336 h13.771l2.219,3.336H14.568z M31.321,35.805v-7.872l2.729-0.355v10.048L31.321,35.805z" fill="'+data.iconColor+'"/></svg>';
                var svgcar = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"caricon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svgcar+'" style="width:32px; height:32px; -webkit-transform:rotate('+dir+'deg); -moz-transform:rotate('+dir+'deg);"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "arrow") {
                data.iconColor = data.iconColor || "black";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32px" height="32px" viewBox="0 0 32 32">';
                icon += '<path d="m16.2 0.6l-10.9 31 10.7-11.1 10.5 11.1 -10.3-31z" fill="'+data.iconColor+'"/></svg>';
                var svgarrow = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"arrowicon",
                    iconAnchor: [16, 16],
                    html:"'<img src='"+svgarrow+"' style='width:32px; height:32px; -webkit-transform:translate(0px,-16px) rotate("+dir+"deg); -moz-transform:translate(0px,-16px) rotate("+dir+"deg);'/>",
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "wind") {
                data.iconColor = data.iconColor || "black";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32px" height="32px" viewBox="0 0 32 32">';
                icon += '<path d="M16.7 31.7l7-6.9c0.4-0.4 0.4-1 0-1.4 -0.4-0.4-1-0.4-1.4 0l-5.3 5.2V17.3l6.7-6.6c0.2-0.2 0.3-0.5 0.3-0.7v-9c0-0.9-1.1-1.3-1.7-0.7l-6.3 6.2L9.7 0.3C9.1-0.3 8 0.1 8 1.1v8.8c0 0.3 0.1 0.6 0.3 0.8l6.7 6.6v11.3l-5.3-5.2c-0.4-0.4-1-0.4-1.4 0 -0.4 0.4-0.4 1 0 1.4l7 6.9c0.2 0.2 0.5 0.3 0.7 0.3C16.2 32 16.5 31.9 16.7 31.7zM10 9.6V3.4l5 4.9v6.2L10 9.6zM17 8.3l5-4.9v6.2l-5 4.9V8.3z" fill="'+data.iconColor+'"/></svg>';
                var svgwind = "data:image/svg+xml;base64," + btoa(icon);
                var dir = parseFloat(data.hdg || data.bearing || "0");
                myMarker = L.divIcon({
                    className:"windicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svgwind+'" style="width:32px; height:32px; -webkit-transform:rotate('+dir+'deg); -moz-transform:rotate('+dir+'deg);"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "satellite") {
                data.iconColor = data.iconColor || "black";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 100">';
                icon += '<polygon points="38.17 39.4 45.24 32.33 43.34 27.92 24.21 8.78 14.59 18.4 33.72 37.53" fill="'+data.iconColor+'"/>';
                icon += '<path d="M69.22 44.57L54.38 29.73c-1.1-1.1-2.91-1.1-4.01 0L35.53 44.57c-1.1 1.1-1.1 2.91 0 4.01l14.84 14.84c1.1 1.1 2.91 1.1 4.01 0l14.84-14.84C70.32 47.47 70.32 45.67 69.22 44.57z" fill="'+data.iconColor+'"/>';
                icon += '<polygon points="71.04 55.61 66.58 53.75 59.52 60.82 61.42 65.23 80.55 84.36 90.17 74.75" fill="'+data.iconColor+'"/>';
                icon += '<path d="M28.08 55.26l-6.05 0.59C23.11 68.13 32.78 77.94 45 79.22l0.59-6.05C36.26 72.15 28.89 64.66 28.08 55.26z" fill="'+data.iconColor+'"/>';
                icon += '<path d="M15.88 56.54L9.83 57.13c1.67 18.06 16.03 32.43 34.08 34.09l0.59-6.04C29.34 83.76 17.29 71.71 15.88 56.54z" fill="'+data.iconColor+'"/>';
                icon += '</svg>';
                var svgsat = "data:image/svg+xml;base64," + btoa(icon);
                myMarker = L.divIcon({
                    className:"satelliteicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svgsat+'" style="width:32px; height:32px;"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if ((data.icon === "iss") || (data.icon === "ISS")) {
                data.iconColor = data.iconColor || "black";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 48 48">';
                icon += '<path id="iss" d="m4.55 30.97l6.85-12.68 0.59 0.32 -6.85 12.68 4.27 2.3 6.85-12.68 0.49 0.27 -0.81 1.5c-0.26 0.48-0.07 1.1 0.44 1.37l5.09 2.75c0.5 0.27 1.12 0.1 1.38-0.39l0.81-1.5 0.72 0.39 -1.49 2.75c-0.41 0.76-0.38 1.58 0.08 1.82l4.61 2.49c0.45 0.24 1.15-0.18 1.56-0.94l1.49-2.75 0.69 0.37 -6.85 12.68 4.26 2.3 6.85-12.68 0.59 0.32 -6.85 12.69 4.26 2.3 14.46-26.78 -4.26-2.3 -6.88 12.74 -0.59-0.32 6.88-12.74 -4.26-2.3 -6.88 12.74 -0.69-0.37 1.49-2.75c0.41-0.76 ';
                icon += '0.38-1.58-0.08-1.82l-1.4-0.75 0.5-0.92c1.02 0.17 2.09-0.32 2.62-1.3 0.67-1.23 0.22-2.76-0.99-3.42 -1.21-0.65-2.74-0.19-3.4 1.05 -0.53 0.98-0.35 2.14 0.35 2.9l-0.5 0.92 -1.8-0.97c-0.45-0.24-1.15 0.17-1.57 0.94l-1.49 2.75 -0.72-0.39 0.81-1.5c0.26-0.48 0.07-1.1-0.44-1.36l-5.09-2.75c-0.5-0.27-1.12-0.1-1.38 0.39l-0.81 1.5 -0.49-0.27 6.88-12.74 -4.26-2.3 -6.88 12.74 -0.59-0.32 6.88-12.74 -4.26-2.3 -14.46 26.78 4.26 2.3zm14.26-11.72c0.2-0.37 0.68-0.51 1.06-0.3l3.93 ';
                icon += '2.12c0.39 0.21 0.54 0.68 0.34 1.05l-1.81 3.35c-0.2 0.37-0.68 0.51-1.06 0.3l-3.93-2.12c-0.38-0.21-0.53-0.68-0.33-1.05l1.81-3.35zm12.01-1.46c0.45-0.83 1.47-1.14 2.28-0.7 0.81 0.44 1.11 1.46 0.66 2.29 -0.44 0.83-1.47 1.14-2.28 0.7 -0.81-0.44-1.11-1.46-0.66-2.29zm-3.78 4.26c0.35-0.66 0.93-1.04 1.28-0.85l3.57 1.93c0.35 0.19 0.35 0.88-0.01 1.53l-3.19 5.91c-0.35 0.66-0.93 1.04-1.28 0.85l-3.56-1.92c-0.35-0.19-0.35-0.88 0.01-1.53l3.19-5.91zm0.19 7.49c-0.26 0.49-0.87 ';
                icon += '0.67-1.36 0.41 -0.49-0.26-0.67-0.87-0.41-1.36 0.27-0.49 0.87-0.67 1.36-0.4 0.49 0.26 0.67 0.87 0.41 1.36zm-7.46-6.31c-0.26 0.49-0.87 0.67-1.36 0.41s-0.67-0.87-0.41-1.36c0.27-0.49 0.87-0.67 1.36-0.4s0.67 0.87 0.41 1.36zm2.32 1.25c-0.26 0.49-0.87 0.67-1.36 0.41 -0.49-0.26-0.67-0.87-0.41-1.36 0.27-0.49 0.87-0.67 1.36-0.41 0.49 0.26 0.67 0.87 0.41 1.36z" fill="'+data.iconColor+'"/>';
                icon += '</svg>';
                var svgiss = "data:image/svg+xml;base64," + btoa(icon);
                myMarker = L.divIcon({
                    className:"issicon",
                    iconAnchor: [25, 25],
                    html:'<img src="'+svgiss+'" style="width:50px; height:50px;"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
            }
            else if (data.icon === "locate") {
                data.iconColor = data.iconColor || "cyan";
                icon = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="468px" height="468px" viewBox="0 0 468 468">';
                icon += '<polygon points="32 32 104 32 104 0 0 0 0 104 32 104" fill="'+data.iconColor+'"/>';
                icon += '<polygon points="468 0 364 0 364 32 436 32 436 104 468 104" fill="'+data.iconColor+'"/>';
                icon += '<polygon points="0 468 104 468 104 436 32 436 32 364 0 364" fill="'+data.iconColor+'"/>';
                icon += '<polygon points="436 436 364 436 364 468 468 468 468 364 436 364" fill="'+data.iconColor+'"/>';
                //icon += '<circle cx="234" cy="234" r="22" fill="'+data.iconColor+'"/>';
                icon += '</svg>';
                var svglocate = "data:image/svg+xml;base64," + btoa(icon);
                myMarker = L.divIcon({
                    className:"locateicon",
                    iconAnchor: [16, 16],
                    html:'<img src="'+svglocate+'" style="width:32px; height:32px;"/>',
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [12,-4];
            }
            else if (data.icon === "friend") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'circle f', iconSize: [20, 12] }), title: data.name, draggable:drag });
            }
            else if (data.icon === "hostile") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'circle h', iconSize: [16, 16] }), title: data.name, draggable:drag });
            }
            else if (data.icon === "neutral") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'circle n', iconSize: [16, 16] }), title: data.name, draggable:drag });
            }
            else if (data.icon === "unknown") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'circle', iconSize: [16, 16] }), title: data.name, draggable:drag });
            }
            else if (data.icon === "danger") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'up-triangle' }), title: data.name, draggable:drag });
            }
            else if (data.icon === "earthquake") {
                marker = L.marker(ll, { icon: L.divIcon({ className: 'circle e', iconSize: [data.mag*5, data.mag*5] }), title: data.name, draggable:drag });
            }
            else if (data.icon.match(/^:.*:$/g)) {
                var em = emojify(data.icon);
                var col = data.iconColor || "#910000";
                myMarker = L.divIcon({
                    className:"emicon",
                    html: '<center><span style="font-size:2em; color:'+col+'">'+em+'</span></center>',
                    iconSize: [32, 32]
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [12,-4];
            }
            else if (data.icon.match(/^https?:.*$/)) {
                myMarker = L.icon({
                    iconUrl: data.icon,
                    iconSize: [32, 32],
                    iconAnchor: [16, 16],
                    popupAnchor: [0, -16]
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [12,-4];
            }
            else if (data.icon.substr(0,3) === "fa-") {
                var col = data.iconColor || "#910000";
                var imod = "";
                if (data.icon.indexOf(" ") === -1) { imod = "fa-2x "; }
                myMarker = L.divIcon({
                    className:"faicon",
                    html: '<center><i class="fa fa-fw '+imod+data.icon+'" style="color:'+col+'"></i></center>',
                    iconSize: [32, 32],
                    popupAnchor: [0, -16]
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [8,-8];
            }
            else if (data.icon.substr(0,3) === "wi-") {
                var col = data.iconColor || "#910000";
                var imod = "";
                if (data.icon.indexOf(" ") === -1) { imod = "wi-2x "; }
                myMarker = L.divIcon({
                    className:"wiicon",
                    html: '<center><i class="wi wi-fw '+imod+data.icon+'" style="color:'+col+'"></i></center>',
                    iconSize: [32, 32],
                    popupAnchor: [0, -16]
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [16,-16];
            }
            else {
                myMarker = L.VectorMarkers.icon({
                    icon: data.icon || "circle",
                    markerColor: (data.iconColor || "#910000"),
                    prefix: 'fa',
                    iconColor: 'white'
                });
                marker = L.marker(ll, {title:data.name, icon:myMarker, draggable:drag});
                labelOffset = [6,-6];
            }
        }
        if (data.hasOwnProperty("SIDC")) {
            // "SIDC":"SFGPU------E***","name":"1.C2 komp","fullname":"1.C2 komp/FTS/INSS"
            myMarker = new ms.Symbol( data.SIDC.toUpperCase(), { uniqueDesignation:data.name });
            // Now that we have a symbol we can ask for the echelon and set the symbol size
            var opts = data.options || {};
            opts.size = opts.size || iconSz[myMarker.getProperties().echelon] || 30;
            opts.size = opts.size * (opts.scale || 1);
            myMarker = myMarker.setOptions(opts);
            var myicon = L.icon({
                iconUrl: myMarker.toDataURL(),
                iconAnchor: [myMarker.getAnchor().x, myMarker.getAnchor().y],
                className: "natoicon",
            });
            marker =  L.marker(ll, { title:data.name, icon:myicon, draggable:drag });
        }
        marker.name = data.name;

        // var createLabelIcon = function(labelText) {
        //     return L.marker(new L.LatLng(51.05, -1.35), {icon:L.divIcon({ html:labelText })});
        // }

        // send new position at end of move event if point is draggable
        if (data.draggable === true) {
            if (data.icon) { marker.icon = data.icon; }
            if (data.iconColor) { marker.iconColor = data.iconColor; }
            if (data.SIDC) { marker.SIDC = data.SIDC.toUpperCase(); }
            marker.on('dragend', function (e) {
                var l = marker.getLatLng().toString().replace('LatLng(','lat, lon : ').replace(')','')
                marker.setPopupContent(marker.getPopup().getContent().split("lat, lon")[0] + l);
                ws.send(JSON.stringify({action:"move",name:marker.name,layer:marker.lay,icon:marker.icon,iconColor:marker.iconColor,SIDC:marker.SIDC,draggable:true,lat:parseFloat(marker.getLatLng().lat.toFixed(6)),lon:parseFloat(marker.getLatLng().lng.toFixed(6))}));
            });
        }

        // remove icon from list of properties, then add all others to popup
        if (data.hasOwnProperty("SIDC") && data.hasOwnProperty("options")) { delete data.options; }
        if (data.hasOwnProperty("icon")) { delete data.icon; }
        if (data.hasOwnProperty("iconColor")) { delete data.iconColor; }
        if (data.hasOwnProperty("photourl")) {
            words += "<img src=\"" + data.photourl + "\" style=\"width:100%; margin-top:10px;\">";
            delete data.photourl;
        }
        if (data.hasOwnProperty("photoUrl")) {
            words += "<img src=\"" + data.photoUrl + "\" style=\"width:100%; margin-top:10px;\">";
            delete data.photoUrl;
        }
        if (data.hasOwnProperty("videoUrl")) {
            words += '<video controls muted autoplay width="320"><source src="'+data.videoUrl+'" type="video/mp4">Your browser does not support the video tag.</video>';
            delete data.videoUrl;
        }
        if (data.hasOwnProperty("ttl")) {  // save expiry time for this marker
            if (data.ttl != 0) {
                marker.ts = parseInt(Date.now()/1000) + Number(data.ttl);
            }
            delete data.ttl;
        }
        else if (maxage != 0) {
            marker.ts = parseInt(Date.now()/1000) + Number(maxage);
        }
        if (data.hasOwnProperty("weblink")) {
            if (typeof data.weblink === "string") {
                words += "<b><a href='"+ data.weblink + "' target='_new'>more information...</a></b><br/>";
            } else {
                var tgt = data.weblink.target || "_new";
                words += "<b><a href='"+ data.weblink.url + "' target='"+ tgt + "'>" + data.weblink.name + "</a></b><br/>";
            }
            delete data.weblink;
        }
        var p;
        if (data.hasOwnProperty("popped") && (data.popped === true)) {
            p = true;
            delete data.popped;
        }
        if (data.hasOwnProperty("popped") && (data.popped === false)) {
            marker.closePopup();
            p = false;
            delete data.popped;
        }
        // If .label then use that rather than name tooltip
        if (data.label) {
            if (typeof data.label === "boolean" && data.label === true) {
                marker.bindTooltip(data.name, { permanent:true, direction:"right", offset:labelOffset });
            }
            else if (typeof data.label === "string" && data.label.length > 0) {
                marker.bindTooltip(data.label, { permanent:true, direction:"right", offset:labelOffset });
            }
            delete marker.options.title;
            delete data.label;
        }
        // otherwise check for .tooltip then use that rather than name tooltip
        else if (data.tooltip) {
            if (typeof data.tooltip === "string" && data.tooltip.length > 0) {
                marker.bindTooltip(data.tooltip, { direction:"bottom", offset:[0,4] });
                delete marker.options.title;
                delete data.tooltip;
            }
        }

        marker = rightmenu(marker);

        // Add any remaining properties to the info box
        var llc = data.lineColor;
        delete data.lat;
        delete data.lon;
        if (data.layer) { delete data.layer; }
        if (data.lineColor) { delete data.lineColor; }
        if (data.color) { delete data.color; }
        if (data.weight) { delete data.weight; }
        if (data.tracklength) { delete data.tracklength; }
        if (data.dashArray) { delete data.dashArray; }
        if (data.fill) { delete data.fill; }
        if (data.draggable) { delete data.draggable; }
        for (var i in data) {
            if ((i != "name") && (i != "length")) {
                if (typeof data[i] === "object") {
                    words += i +" : "+JSON.stringify(data[i])+"<br/>";
                } else {
                    words += i +" : "+data[i]+"<br/>";
                }
            }
        }
        if (data.popup) { words = data.popup; }
        else { words = words + marker.getLatLng().toString().replace('LatLng(','lat, lon : ').replace(')',''); }
        words = "<b>"+data.name+"</b><br/>" + words; //"<button style=\"border-radius:4px; float:right; background-color:lightgrey;\" onclick='popped=false;popmark.closePopup();'>X</button><br/>" + words;
        marker.bindPopup(words, {autoClose:false, closeButton:true, closeOnClick:false, minWidth:200});
        marker._popup.dname = data.name;
        marker.lay = lay;                       // and the layer it is on

        marker.on('click', function(e) {
            ws.send(JSON.stringify({action:"click",name:marker.name,layer:marker.lay,icon:marker.icon,iconColor:marker.iconColor,SIDC:marker.SIDC,draggable:true,lat:parseFloat(marker.getLatLng().lat.toFixed(6)),lon:parseFloat(marker.getLatLng().lng.toFixed(6))}));
        });
        if ((data.addtoheatmap !== "false") || (!data.hasOwnProperty("addtoheatmap"))) { // Added to give ability to control if points from active layer contribute to heatmap
            if (heatAll || map.hasLayer(layers[lay])) { heat.addLatLng(lli); }
        }
        markers[data.name] = marker;
        layers[lay].addLayer(marker);



        if ((data.hdg != null) && (data.bearing == null)) { data.bearing = data.hdg; delete data.hdg; }
        if (data.bearing != null) {  // if there is a heading
            if (data.speed != null) { data.length = parseFloat(data.speed || "0") * 50; }  // and a speed
            if (data.length != null) {
                if (polygons[data.name] != null) { map.removeLayer(polygons[data.name]); }
                var x = ll.lng * 1; // X coordinate
                var y = ll.lat * 1; // Y coordinate
                var ll1 = ll;
                var angle = parseFloat(data.bearing);
                var lengthAsDegrees = parseFloat(data.length || "0") / 110540; // metres in a degree..ish
                var polygon = null;
                if (data.accuracy != null) {
                    data.accuracy = Number(data.accuracy);
                    var y2 = y + Math.sin((90-angle+data.accuracy)/180*Math.PI)*lengthAsDegrees*Math.cos(y/180*Math.PI);
                    var x2 = x + Math.cos((90-angle+data.accuracy)/180*Math.PI)*lengthAsDegrees;
                    var ll2 = new L.LatLng(y2,x2);
                    var y3 = y + Math.sin((90-angle-data.accuracy)/180*Math.PI)*lengthAsDegrees*Math.cos(y/180*Math.PI);
                    var x3 = x + Math.cos((90-angle-data.accuracy)/180*Math.PI)*lengthAsDegrees;
                    var ll3 = new L.LatLng(y3,x3);
                    polygon = L.polygon([ ll1, ll2, ll3 ], {weight:2, color:llc||'#f30', fillOpacity:0.06, clickable:false});
                } else {
                    var ya = y + Math.sin((90-angle)/180*Math.PI)*lengthAsDegrees*Math.cos(y/180*Math.PI);
                    var xa = x + Math.cos((90-angle)/180*Math.PI)*lengthAsDegrees;
                    var lla = new L.LatLng(ya,xa);
                    polygon = L.polygon([ ll1, lla ], {weight:2, color:llc||'#f30', clickable:false});
                }
                if (typeof layers[lay].getVisibleParent === 'function') {
                    var vis = layers[lay].getVisibleParent(marker);
                    if ((polygon !== null) && (vis !== null) && (!vis.hasOwnProperty("lay"))) {
                        polygon.setStyle({opacity:0});
                    }
                }
                polygons[data.name] = polygon;
                polygons[data.name].lay = lay;
                layers[lay].addLayer(polygon);
            }
        }
        if (panit) { map.setView(ll,map.getZoom()); }
        if (p === true) { marker.openPopup(); }
    }
}