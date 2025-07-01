def error(self, msg):
        '''
        error(msg : string)

        Print a usage message incorporating 'msg' to stderr and exit.
        This keeps option parsing exit status uniform for all parsing errors.
        '''
        self.print_usage(sys.stderr)
        self.exit(salt.defaults.exitcodes.EX_USAGE, '{0}: error: {1}\n'.format(self.get_prog_name(), msg))