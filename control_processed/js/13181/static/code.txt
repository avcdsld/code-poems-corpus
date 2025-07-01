function(json, md, element) {
        var toinsert = this.create_output_subarea(md, CLASS_NAME, MIME_TYPE);
        this.keyboard_manager.register_events(toinsert);
        render(this, json, toinsert[0]);
        element.append(toinsert);
        return toinsert;
    }