function inverse$15(p) {
        p.x -= this.x0;
        p.y -= this.y0;
        var lon, lat;

        if (this.sphere) {
            lon = adjust_lon(this.long0 + (p.x / this.a) / Math.cos(this.lat_ts));
            lat = Math.asin((p.y / this.a) * Math.cos(this.lat_ts));
        }
        else {
            lat = iqsfnz(this.e, 2 * p.y * this.k0 / this.a);
            lon = adjust_lon(this.long0 + p.x / (this.a * this.k0));
        }

        p.x = lon;
        p.y = lat;
        return p;
    }