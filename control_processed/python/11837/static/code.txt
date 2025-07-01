def activation_atlas(
    model,
    layer,
    grid_size=10,
    icon_size=96,
    number_activations=NUMBER_OF_AVAILABLE_SAMPLES,
    icon_batch_size=32,
    verbose=False,
):
    """Renders an Activation Atlas of the given model's layer."""

    activations = layer.activations[:number_activations, ...]
    layout, = aligned_umap(activations, verbose=verbose)
    directions, coordinates, _ = bin_laid_out_activations(
        layout, activations, grid_size
    )
    icons = []
    for directions_batch in chunked(directions, icon_batch_size):
        icon_batch, losses = render_icons(
            directions_batch, model, layer=layer.name, size=icon_size, num_attempts=1
        )
        icons += icon_batch
    canvas = make_canvas(icons, coordinates, grid_size)

    return canvas