def benchmark_command(cmd, progress):
    """Benchmark one command execution"""
    full_cmd = '/usr/bin/time --format="%U %M" {0}'.format(cmd)
    print '{0:6.2f}% Running {1}'.format(100.0 * progress, full_cmd)
    (_, err) = subprocess.Popen(
        ['/bin/sh', '-c', full_cmd],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate('')

    values = err.strip().split(' ')
    if len(values) == 2:
        try:
            return (float(values[0]), float(values[1]))
        except:  # pylint:disable=I0011,W0702
            pass  # Handled by the code after the "if"

    print err
    raise Exception('Error during benchmarking')