def dashboard(self, dashboard_id):
        """Server side rendering for a dashboard"""
        session = db.session()
        qry = session.query(models.Dashboard)
        if dashboard_id.isdigit():
            qry = qry.filter_by(id=int(dashboard_id))
        else:
            qry = qry.filter_by(slug=dashboard_id)

        dash = qry.one_or_none()
        if not dash:
            abort(404)
        datasources = set()
        for slc in dash.slices:
            datasource = slc.datasource
            if datasource:
                datasources.add(datasource)

        if config.get('ENABLE_ACCESS_REQUEST'):
            for datasource in datasources:
                if datasource and not security_manager.datasource_access(datasource):
                    flash(
                        __(security_manager.get_datasource_access_error_msg(datasource)),
                        'danger')
                    return redirect(
                        'superset/request_access/?'
                        f'dashboard_id={dash.id}&')

        dash_edit_perm = check_ownership(dash, raise_if_false=False) and \
            security_manager.can_access('can_save_dash', 'Superset')
        dash_save_perm = security_manager.can_access('can_save_dash', 'Superset')
        superset_can_explore = security_manager.can_access('can_explore', 'Superset')
        superset_can_csv = security_manager.can_access('can_csv', 'Superset')
        slice_can_edit = security_manager.can_access('can_edit', 'SliceModelView')

        standalone_mode = request.args.get('standalone') == 'true'
        edit_mode = request.args.get('edit') == 'true'

        # Hack to log the dashboard_id properly, even when getting a slug
        @log_this
        def dashboard(**kwargs):  # noqa
            pass
        dashboard(
            dashboard_id=dash.id,
            dashboard_version='v2',
            dash_edit_perm=dash_edit_perm,
            edit_mode=edit_mode)

        dashboard_data = dash.data
        dashboard_data.update({
            'standalone_mode': standalone_mode,
            'dash_save_perm': dash_save_perm,
            'dash_edit_perm': dash_edit_perm,
            'superset_can_explore': superset_can_explore,
            'superset_can_csv': superset_can_csv,
            'slice_can_edit': slice_can_edit,
        })

        bootstrap_data = {
            'user_id': g.user.get_id(),
            'dashboard_data': dashboard_data,
            'datasources': {ds.uid: ds.data for ds in datasources},
            'common': self.common_bootsrap_payload(),
            'editMode': edit_mode,
        }

        if request.args.get('json') == 'true':
            return json_success(json.dumps(bootstrap_data))

        return self.render_template(
            'superset/dashboard.html',
            entry='dashboard',
            standalone_mode=standalone_mode,
            title=dash.dashboard_title,
            bootstrap_data=json.dumps(bootstrap_data),
        )