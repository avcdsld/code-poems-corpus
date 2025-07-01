function() {
                var a, attachment,
                    e, elements = [],
                    f, filters = new tree.Filterset(),
                    z, zooms = [],
                    segments = 0, conditions = 0;

                while (
                        (e = $(this.element)) ||
                        (z = $(this.zoom)) ||
                        (f = $(this.filter)) ||
                        (a = $(this.attachment))
                    ) {
                    segments++;
                    if (e) {
                        elements.push(e);
                    } else if (z) {
                        zooms.push(z);
                        conditions++;
                    } else if (f) {
                        var err = filters.add(f);
                        if (err) {
                            util.error(env, {
                                message: err,
                                index: i - 1,
                                filename: env.filename
                            });
                            throw new Error('N/A');
                        }
                        conditions++;
                    } else if (attachment) {
                        util.error(env, {
                            message: 'Encountered second attachment name.\n',
                            index: i - 1,
                            filename: env.filename
                        });
                        throw new Error('N/A');
                    } else {
                        attachment = a;
                    }

                    var c = input.charAt(i);
                    if (c === '{' || c === '}' || c === ';' || c === ',') { break; }
                }

                if (segments) {
                    return new tree.Selector(filters, zooms, elements, attachment, conditions, memo);
                }
            }