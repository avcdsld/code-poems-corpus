def next_frame_glow_bair_qual():
  """Hparams for qualitative video generation results."""
  hparams = next_frame_glow_bair_quant()
  hparams.coupling = "additive"
  hparams.temperature = 0.5
  hparams.coupling_width = 392
  return hparams