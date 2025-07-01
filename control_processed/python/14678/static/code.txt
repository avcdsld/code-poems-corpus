def asset_path(cls, organization, asset):
        """Return a fully-qualified asset string."""
        return google.api_core.path_template.expand(
            "organizations/{organization}/assets/{asset}",
            organization=organization,
            asset=asset,
        )