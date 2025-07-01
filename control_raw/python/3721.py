def fave_slices(self, user_id=None):
        """Favorite slices for a user"""
        if not user_id:
            user_id = g.user.id
        qry = (
            db.session.query(
                models.Slice,
                models.FavStar.dttm,
            )
            .join(
                models.FavStar,
                sqla.and_(
                    models.FavStar.user_id == int(user_id),
                    models.FavStar.class_name == 'slice',
                    models.Slice.id == models.FavStar.obj_id,
                ),
            )
            .order_by(
                models.FavStar.dttm.desc(),
            )
        )
        payload = []
        for o in qry.all():
            d = {
                'id': o.Slice.id,
                'title': o.Slice.slice_name,
                'url': o.Slice.slice_url,
                'dttm': o.dttm,
                'viz_type': o.Slice.viz_type,
            }
            if o.Slice.created_by:
                user = o.Slice.created_by
                d['creator'] = str(user)
                d['creator_url'] = '/superset/profile/{}/'.format(
                    user.username)
            payload.append(d)
        return json_success(
            json.dumps(payload, default=utils.json_int_dttm_ser))