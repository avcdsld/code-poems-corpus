def num_rewards(self):
    """Returns the number of distinct rewards.

    Returns:
      Returns None if the reward range is infinite or the processed rewards
      aren't discrete, otherwise returns the number of distinct rewards.
    """

    # Pre-conditions: reward range is finite.
    #               : processed rewards are discrete.
    if not self.is_reward_range_finite:
      tf.logging.error("Infinite reward range, `num_rewards returning None`")
      return None
    if not self.is_processed_rewards_discrete:
      tf.logging.error(
          "Processed rewards are not discrete, `num_rewards` returning None")
      return None

    min_reward, max_reward = self.reward_range
    return max_reward - min_reward + 1