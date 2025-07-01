function doCommand(cmd) {
    //console.log("COMMAND",cmd);
    if (cmd.hasOwnProperty("clear")) {
        doTidyUp(cmd.clear);
    }
    if (cmd.hasOwnProperty("panit")) {
        if (cmd.panit == "true") { panit = true; }
        else { panit = false; }
        document.getElementById("panit").checked = panit;
    }
    if (cmd.hasOwnProperty("hiderightclick")) {
        if (cmd.hiderightclick == "true" || cmd.hiderightclick == true) { hiderightclick = true; }
        else { hiderightclick = false; }
    }
    if (cmd.hasOwnProperty("showmenu")) {
        if ((cmd.showmenu === "hide") && (showUserMenu === true)) {
            showUserMenu = false;
            if (inIframe) {
                if (menuButton) {
                    try { map.removeControl(menuButton); }
                    catch(e) {}
                }
            }
            else { document.getElementById("bars").style.display="none"; }
        }
        else if ((cmd.showmenu === "show") && (showUserMenu === false)) {
            showUserMenu = true;
            if (inIframe) { map.addControl(menuButton); }
            else { document.getElementById("bars").style.display="unset";  }
        }
    }
    if (cmd.hasOwnProperty("showlayers")) {
        if ((cmd.showlayers === "hide") && (showLayerMenu === true)) {
            showLayerMenu = false;
            layercontrol.removeFrom(map);
        }
        else if ((cmd.showlayers === "show") && (showLayerMenu === false)) {
            showLayerMenu = true;
            layercontrol = L.control.layers(basemaps, overlays).addTo(map);
        }
    }
    if (cmd.hasOwnProperty("grid")) {
        if (cmd.grid.hasOwnProperty("showgrid")) {
            var changed = false;
            if ((cmd.grid.showgrid == "true" || cmd.grid.showgrid == true ) && !showGrid) { changed = true; }
            if ((cmd.grid.showgrid == "false" || cmd.grid.showgrid == false ) && showGrid) { changed = true; }
            if (changed) {
                showGrid = !showGrid;
                if (showGrid) { Lgrid.addTo(map); }
                else { Lgrid.removeFrom(map); }
            }
        }
        if (cmd.grid.hasOwnProperty("opt")) {
            Lgrid.initialize(cmd.grid.opt);
            if (showGrid) {
                Lgrid.removeFrom(map);
                Lgrid.addTo(map);
            }
        }
    }
    if (cmd.hasOwnProperty("button")) {
        if (cmd.button.icon) {
            if (!buttons[cmd.button.name]) {
                buttons[cmd.button.name] = L.easyButton( cmd.button.icon, function() {
                    ws.send(JSON.stringify({action:"button",name:cmd.button.name}));
                }, cmd.button.name, { position:cmd.button.position||'topright' }).addTo(map);
            }
        }
        else {
            if (buttons[cmd.button.name]) {
                buttons[cmd.button.name].removeFrom(map);
                delete buttons[cmd.button.name];
            }
        }
    }
    if (cmd.hasOwnProperty("contextmenu")) {
        if (typeof cmd.contextmenu === "string") {
            addmenu = cmd.contextmenu;
            rightmenuMap.setContent(addmenu);
        }
    }
    if (cmd.hasOwnProperty("coords")) {
        try { coords.removeFrom(map); }
        catch(e) {}
        if (cmd.coords == "dms") {
            coords.options.useDMS = true;
            showMouseCoords = "dms";
            coords.addTo(map);
        }
        if (cmd.coords == "deg") {
            coords.options.useDMS = false;
            showMouseCoords = "deg";
            coords.addTo(map);
        }
    }

    var existsalready = false;
    // Add a new base map layer
    if (cmd.map && cmd.map.hasOwnProperty("name") && cmd.map.hasOwnProperty("url") && cmd.map.hasOwnProperty("opt")) {
        console.log("BASE",cmd.map);
        if (basemaps.hasOwnProperty(cmd.map.name)) { existsalready = true; }
        if (cmd.map.hasOwnProperty("wms")) {   // special case for wms
            console.log("New WMS:",cmd.map.name);
            if (cmd.map.wms === "grey") {
                basemaps[cmd.map.name] = L.tileLayer.graywms(cmd.map.url, cmd.map.opt);
            }
            else {
                basemaps[cmd.map.name] = L.tileLayer.wms(cmd.map.url, cmd.map.opt);
            }
        }
        else {
            console.log("New Map:",cmd.map.name);
            basemaps[cmd.map.name] = L.tileLayer(cmd.map.url, cmd.map.opt);
        }
        //if (!existsalready && !inIframe) {
        if (!existsalready) {
            layercontrol.addBaseLayer(basemaps[cmd.map.name],cmd.map.name);
        }
    }
    // Remove one or more map layers (base or overlay)
    if (cmd.map && cmd.map.hasOwnProperty("delete")) {
        if (!Array.isArray(cmd.map.delete)) { cmd.map.delete = [cmd.map.delete]; }
        for (var a=0; a < cmd.map.delete.length; a++) {
            if (basemaps.hasOwnProperty(cmd.map.delete[a])) { delete basemaps[cmd.map.delete[a]]; }
            if (overlays.hasOwnProperty(cmd.map.delete[a])) { delete overlays[cmd.map.delete[a]]; }
        }
        if (showLayerMenu) {
            map.removeControl(layercontrol);
            layercontrol = L.control.layers(basemaps, overlays).addTo(map);
        }
    }
    // Add a new geojson overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("geojson") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        var opt = cmd.map.opt || { style:function(feature) {
            var st = { stroke:true, weight:2, fill:true };
            if (feature.hasOwnProperty("properties")) {
                st.color = feature.properties.color||feature.properties.roofColor||"black";
                if (feature.properties.hasOwnProperty("color")) { delete feature.properties.color; }
                if (feature.properties.hasOwnProperty("roofColor")) { delete feature.properties.roofColor; }
            }
            if (feature.hasOwnProperty("properties") && feature.properties.hasOwnProperty('style')) {
                if (feature.properties.style.hasOwnProperty('stroke')) {
                    st.color = feature.properties.style.stroke;
                }
                if (feature.properties.style.hasOwnProperty('stroke-width')) {
                    st.weight = feature.properties.style["stroke-width"];
                }
                if (feature.properties.style.hasOwnProperty('stroke-opacity')) {
                    st.opacity = feature.properties.style["stroke-opacity"];
                }
                if (feature.properties.style.hasOwnProperty('fill')) {
                    if (feature.properties.style.fill == "none") { st.fill = false; }
                    else { st.fillColor = feature.properties.style.fill; }
                }
                if (feature.properties.style.hasOwnProperty('fill-opacity')) {
                    st.fillOpacity = feature.properties.style["fill-opacity"];
                }
            }
            delete feature.properties.style;
            return st;
        }};
        opt.onEachFeature = function (f,l) {
            l.bindPopup('<pre>'+JSON.stringify(f.properties,null,' ').replace(/[\{\}"]/g,'')+'</pre>');
        }
        overlays[cmd.map.overlay] = L.geoJson(cmd.map.geojson,opt);
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    // Add a new NVG XML overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("nvg") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        var parser = new NVG(cmd.map.nvg);
        var geoj = parser.toGeoJSON();

        overlays[cmd.map.overlay] = L.geoJson(geoj,{
            style: function(feature) {
                var st = { stroke:true, color:"black", weight:2, fill:true };
            	if (feature.hasOwnProperty("properties") && feature.properties.hasOwnProperty('style')) {
                    if (feature.properties.style.hasOwnProperty('stroke')) {
                        st.color = feature.properties.style.stroke;
                    }
                    if (feature.properties.style.hasOwnProperty('stroke-width')) {
                        st.weight = feature.properties.style["stroke-width"];
                    }
                    if (feature.properties.style.hasOwnProperty('stroke-opacity')) {
                        st.opacity = feature.properties.style["stroke-opacity"];
                    }
                    if (feature.properties.style.hasOwnProperty('fill')) {
                        if (feature.properties.style.fill == "none") { st.fill = false; }
                        else { st.fillColor = feature.properties.style.fill; }
                    }
                    if (feature.properties.style.hasOwnProperty('fill-opacity')) {
                        st.fillOpacity = feature.properties.style["fill-opacity"];
                    }
                }
                return st;
            }
        });
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    var custIco = function() {
        var customLayer = L.geoJson();
        if (cmd.map.hasOwnProperty("icon")) {
            var col = cmd.map.iconColor || "#910000";
            var myMarker = L.divIcon({
                className:"faicon",
                html: '<center><i class="fa fa-fw '+cmd.map.icon+'" style="color:'+col+'"></i></center>',
                iconSize: [15, 15],
            });
            customLayer = L.geoJson(null, {
                pointToLayer: function(geoJsonPoint, latlng) {
                    return L.marker(latlng, {icon: myMarker, title: geoJsonPoint.properties.name});
                }
            });
        }
        return customLayer;
    }
    // Add a new KML overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("kml") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        //var opt = {async:true};
        overlays[cmd.map.overlay] = omnivore.kml.parse(cmd.map.kml, null, custIco());
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    // Add a new TOPOJSON overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("topojson") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        overlays[cmd.map.overlay] = omnivore.topojson.parse(cmd.map.topojson);
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    // Add a new GPX overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("gpx") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        overlays[cmd.map.overlay] = omnivore.gpx.parse(cmd.map.gpx, null, custIco());

        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    // Add a new velocity overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("velocity") ) {
        if (overlays.hasOwnProperty(cmd.map.overlay)) {
            map.removeLayer(overlays[cmd.map.overlay]);
            existsalready = true;
        }
        overlays[cmd.map.overlay] = L.velocityLayer(cmd.map.velocity);
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
        if (cmd.map.hasOwnProperty("fit")) { map.fitBounds(overlays[cmd.map.overlay].getBounds()); }
    }
    // Add a new overlay layer
    if (cmd.map && cmd.map.hasOwnProperty("overlay") && cmd.map.hasOwnProperty("url") && cmd.map.hasOwnProperty("opt")) {
        console.log("New overlay:",cmd.map.overlay);
        if (overlays.hasOwnProperty(cmd.map.overlay)) { existsalready = true; }
        if (cmd.map.hasOwnProperty("wms")) {   // special case for wms
            if (cmd.map.wms === "grey") {
                overlays[cmd.map.overlay] = L.tileLayer.graywms(cmd.map.url, cmd.map.opt);
            }
            else {
                overlays[cmd.map.overlay] = L.tileLayer.wms(cmd.map.url, cmd.map.opt);
            }
        }
        else if (cmd.map.hasOwnProperty("bounds")) {            //Image Overlay in the bounds specified (2D Array)
            if (cmd.map.bounds.length === 2 && cmd.map.bounds[0].length === 2 && cmd.map.bounds[1].length === 2) {
                overlays[cmd.map.overlay] = new L.imageOverlay(cmd.map.url, L.latLngBounds(cmd.map.bounds), cmd.map.opt);
            }
        }
        else {
            overlays[cmd.map.overlay] = L.tileLayer(cmd.map.url, cmd.map.opt);
        }
        //if (!existsalready && !inIframe) {
        if (!existsalready) {
            layercontrol.addOverlay(overlays[cmd.map.overlay],cmd.map.overlay);
        }
        map.addLayer(overlays[cmd.map.overlay]);
    }
    // Swap a base layer
    if (cmd.layer && basemaps.hasOwnProperty(cmd.layer)) {
        map.removeLayer(basemaps[baselayername]);
        baselayername = cmd.layer;
        basemaps[baselayername].addTo(map);
    }
    if (cmd.layer && (cmd.layer === "none")) {
        map.removeLayer(basemaps[baselayername]);
        baselayername = cmd.layer;
    }
    // Add search command
    if (cmd.hasOwnProperty("search") && (typeof cmd.search === "string")) {
        document.getElementById('search').value = cmd.search;
        if (cmd.search !== "") {
            openMenu();
            doSearch();
        }
        else {
            closeMenu();
            clearSearch();
        }
    }
    // Add side by side control
    if (cmd.side && (cmd.side === "none")) {
        sidebyside.remove();
        map.removeLayer(basemaps[sidebyside.lay]);
        sidebyside = undefined;
    }
    if (cmd.side && basemaps.hasOwnProperty(cmd.side)) {
        if (sidebyside) { sidebyside.remove(); map.removeLayer(basemaps[sidebyside.lay]); }
        basemaps[cmd.side].addTo(map);
        sidebyside = L.control.sideBySide(basemaps[baselayername], basemaps[cmd.side]);
        sidebyside.addTo(map);
        sidebyside.lay = cmd.side;
    }
    if (cmd.split && sidebyside && (cmd.split <= 100) && (cmd.split >= 0)) { sidebyside.setSplit(cmd.split); }
    // Turn on an existing overlay(s)
    if (cmd.hasOwnProperty("showlayer")) {
        if (typeof cmd.showlayer === "string") { cmd.showlayer = [ cmd.showlayer ]; }
        for (var i=0; i < cmd.showlayer.length; i++) {
            if (overlays.hasOwnProperty(cmd.showlayer[i])) {
                map.addLayer(overlays[cmd.showlayer[i]]);
            }
        }
    }
    // Turn off an existing overlay(s)
    if (cmd.hasOwnProperty("hidelayer")) {
        if (typeof cmd.hidelayer === "string") { cmd.hidelayer = [ cmd.hidelayer ]; }
        for (var i=0; i < cmd.hidelayer.length; i++) {
            if (overlays.hasOwnProperty(cmd.hidelayer[i])) {
                map.removeLayer(overlays[cmd.hidelayer[i]]);
            }
        }
    }
    // Lock the pan so map can be moved
    if (cmd.hasOwnProperty("panlock")) {
        if (cmd.panlock == "true" || cmd.panlock == true) { lockit = true; }
        else { lockit = false; doLock(false); }
        document.getElementById("lockit").checked = lockit;
    }
    // move to a new position
    var clat = map.getCenter().lat;
    var clon = map.getCenter().lng;
    var czoom = map.getZoom();
    if (cmd.hasOwnProperty("lat")) { clat = cmd.lat; }
    if (cmd.hasOwnProperty("lon")) { clon = cmd.lon; }
    if (cmd.hasOwnProperty("zoom")) { czoom = cmd.zoom; }
    map.setView([clat,clon],czoom);

    if (cmd.hasOwnProperty("cluster")) {
        clusterAt = cmd.cluster;
        document.getElementById("setclus").value = cmd.cluster;
        setCluster(clusterAt);
    }
    if (cmd.hasOwnProperty("maxage")) {
        document.getElementById("maxage").value = cmd.maxage;
        setMaxAge();
    }
    if (cmd.hasOwnProperty("heatmap")) {
        heat.setOptions(cmd.heatmap);
        document.getElementById("heatall").checked = !!cmd.heatmap;
        heat.redraw();
    }
    if (cmd.hasOwnProperty("panlock") && lockit === true) { doLock(true); }
    if (cmd.hasOwnProperty("zoomlock")) {
        if (cmd.zoomlock == "true" || cmd.zoomlock == true) {
            if (map.doubleClickZoom.enabled()) { map.removeControl(map.zoomControl); }
            map.doubleClickZoom.disable();
            map.scrollWheelZoom.disable();
        }
        else {
            if (!map.doubleClickZoom.enabled()) { map.addControl(map.zoomControl); }
            map.doubleClickZoom.enable();
            map.scrollWheelZoom.enable();
        }
    }
}