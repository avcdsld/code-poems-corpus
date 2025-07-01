def super_lm_moe():
  """Add mixture of experts with ~1B params."""
  hparams = super_lm_base()
  hparams.layers = (
      ("n,att,m,d,a," "n,moe,m,d,a,") * 4 + "n,ffn,d")
  hparams.moe_num_experts = 32
  hparams.moe_hidden_sizes = "1024"
  return hparams