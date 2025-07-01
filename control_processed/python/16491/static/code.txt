def debugDumpString(output, str):
    """Dumps informations about the string, shorten it if necessary """
    if output is not None: output.flush()
    libxml2mod.xmlDebugDumpString(output, str)