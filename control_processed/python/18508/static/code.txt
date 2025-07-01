def setup(app):
    ''' Required Sphinx extension setup function. '''
    app.add_config_value('bokeh_gallery_dir', join("docs", "gallery"), 'html')
    app.connect('config-inited', config_inited_handler)
    app.add_directive('bokeh-gallery', BokehGalleryDirective)