def friendshiped_with?(user)
      (friend_ids + inverse_friend_ids + pending_friend_ids + pending_inverse_friend_ids + blocked_friend_ids).include?(user.id)
    end