def blocked?(user)
      (blocked_friend_ids + blocked_inverse_friend_ids + blocked_pending_inverse_friend_ids).include?(user.id) or user.blocked_pending_inverse_friend_ids.include?(self.id)
    end