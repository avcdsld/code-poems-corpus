def other_args(cls):
        ''' Return args for ``-o`` / ``--output`` to specify where output
        should be written, and for a ``--args`` to pass on any additional
        command line args to the subcommand.

        Subclasses should append these to their class ``args``.

        Example:

            .. code-block:: python

                class Foo(FileOutputSubcommand):

                    args = (

                        FileOutputSubcommand.files_arg("FOO"),

                        # more args for Foo

                    ) + FileOutputSubcommand.other_args()

        '''
        return (
            (('-o', '--output'), dict(
                metavar='FILENAME',
                action='append',
                type=str,
                help="Name of the output file or - for standard output."
            )),

            ('--args', dict(
                metavar='COMMAND-LINE-ARGS',
                nargs=argparse.REMAINDER,
                help="Any command line arguments remaining are passed on to the application handler",
            )),
        )