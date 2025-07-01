def list():
  """Print a listing of known running TensorBoard instances.

  TensorBoard instances that were killed uncleanly (e.g., with SIGKILL
  or SIGQUIT) may appear in this list even if they are no longer
  running. Conversely, this list may be missing some entries if your
  operating system's temporary directory has been cleared since a
  still-running TensorBoard instance started.
  """
  infos = manager.get_all()
  if not infos:
    print("No known TensorBoard instances running.")
    return

  print("Known TensorBoard instances:")
  for info in infos:
    template = "  - port {port}: {data_source} (started {delta} ago; pid {pid})"
    print(template.format(
        port=info.port,
        data_source=manager.data_source_from_info(info),
        delta=_time_delta_from_info(info),
        pid=info.pid,
    ))