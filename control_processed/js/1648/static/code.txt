function getPostData(req, res, next) {
    req.body = req.body || {};

    const urlWithoutSubdirectoryWithoutAmp = res.locals.relativeUrl.match(/(.*?\/)amp\/?$/)[1];

    /**
     * @NOTE
     *
     * We have to figure out the target permalink, otherwise it would be possible to serve a post
     * which lives in two collections.
     *
     * @TODO:
     *
     * This is not optimal and caused by the fact how apps currently work. But apps weren't designed
     * for dynamic routing.
     *
     * I think if the responsible, target router would first take care fetching/determining the post, the
     * request could then be forwarded to this app. Then we don't have to:
     *
     * 1. care about fetching the post
     * 2. care about if the post can be served
     * 3. then this app would act like an extension
     *
     * The challenge is to design different types of apps e.g. extensions of routers, standalone pages etc.
     */
    const permalinks = urlService.getPermalinkByUrl(urlWithoutSubdirectoryWithoutAmp, {withUrlOptions: true});

    if (!permalinks) {
        return next(new common.errors.NotFoundError({
            message: common.i18n.t('errors.errors.pageNotFound')
        }));
    }

    // @NOTE: amp is not supported for static pages
    // @TODO: https://github.com/TryGhost/Ghost/issues/10548
    helpers.entryLookup(urlWithoutSubdirectoryWithoutAmp, {permalinks, query: {controller: 'postsPublic', resource: 'posts'}}, res.locals)
        .then((result) => {
            if (result && result.entry) {
                req.body.post = result.entry;
            }

            next();
        })
        .catch(next);
}