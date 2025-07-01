def sysctl(command):
    """Run a sysctl command and parse the output.

    Args:
        command: A sysctl command with an argument, for example,
            ["sysctl", "hw.memsize"].

    Returns:
        The parsed output.
    """
    out = subprocess.check_output(command)
    result = out.split(b" ")[1]
    try:
        return int(result)
    except ValueError:
        return result