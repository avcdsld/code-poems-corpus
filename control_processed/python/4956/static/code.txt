def infer_game_name_from_filenames(data_dir, snake_case=True):
  """Infer name from filenames."""
  names = os.listdir(data_dir)
  game_names = [re.findall(pattern=r"^Gym(.*)NoFrameskip", string=name)
                for name in names]
  assert game_names, "No data files found in {}".format(data_dir)
  game_names = sum(game_names, [])
  game_name = game_names[0]
  assert all(game_name == other for other in game_names), \
      "There are multiple different game names in {}".format(data_dir)
  if snake_case:
    game_name = camelcase_to_snakecase(game_name)
  return game_name