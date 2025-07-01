def small_image_url(self):
        """Optional[:class:`str`]: Returns a URL pointing to the small image asset of this activity if applicable."""
        if self.application_id is None:
            return None

        try:
            small_image = self.assets['small_image']
        except KeyError:
            return None
        else:
            return 'https://cdn.discordapp.com/app-assets/{0}/{1}.png'.format(self.application_id, small_image)