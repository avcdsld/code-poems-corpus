function (renderable) {
                if (!(renderable instanceof WorldWind.Polygon)) {
                    throw new ArgumentError(
                        Logger.logMessage(Logger.LEVEL_SEVERE, "WktExporter", "exportPolygon",
                            "invalidTypeOfRenderable"));
                }

                var sb = WktType.SupportedGeometries.POLYGON + '(';
                if (renderable.boundaries.length > 0 && renderable.boundaries[0].length > 2) {
                    //with holes
                    for (var i = 0; i < renderable.boundaries.length; i++) {
                        sb = sb + '(';
                        for (var j = 0; j < renderable.boundaries[i].length; j++) {
                            sb = sb + renderable.boundaries[i][j].longitude + ' ' +
                                renderable.boundaries[i][j].latitude;
                            sb = sb + ', ';
                        }
                        sb = sb.substring(0, sb.length - 2);
                        sb = sb + ')';
                        sb = sb + ', ';
                    }
                    sb = sb.substring(0, sb.length - 2);
                }
                else {
                    //no holes
                    sb = sb + '(';
                    for (var i = 0; i < renderable.boundaries.length; i++) {
                        sb = sb + renderable.boundaries[i].longitude + ' ' +
                            renderable.boundaries[i].latitude;
                        sb = sb + ', ';
                    }

                    sb = sb.substring(0, sb.length - 2);
                    sb = sb + ')';
                }
                sb = sb + ')';
                return sb;
            }