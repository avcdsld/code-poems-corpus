def plot_diagrams(results, configs, compiler, out_dir):
    """Plot all diagrams specified by the configs"""
    compiler_fn = make_filename(compiler)
    total = psutil.virtual_memory().total  # pylint:disable=I0011,E1101
    memory = int(math.ceil(byte_to_gb(total)))

    images_dir = os.path.join(out_dir, 'images')

    for config in configs:
        out_prefix = '{0}_{1}'.format(config['name'], compiler_fn)

        plot_diagram(
            config,
            results,
            images_dir,
            os.path.join(images_dir, '{0}.png'.format(out_prefix))
        )

        with open(
            os.path.join(out_dir, '{0}.qbk'.format(out_prefix)),
            'wb'
        ) as out_f:
            qbk_content = """{0}
Measured on a {2} host with {3} GB memory. Compiler used: {4}.

[$images/metaparse/{1}.png [width 100%]]
""".format(config['desc'], out_prefix, platform.platform(), memory, compiler)
            out_f.write(qbk_content)