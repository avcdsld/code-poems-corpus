def process_experiences(self, current_info: AllBrainInfo, next_info: AllBrainInfo):
        """
        Checks agent histories for processing condition, and processes them as necessary.
        Processing involves calculating value and advantage targets for model updating step.
        :param current_info: Current AllBrainInfo
        :param next_info: Next AllBrainInfo
        """
        info_teacher = next_info[self.brain_to_imitate]
        for l in range(len(info_teacher.agents)):
            teacher_action_list = len(self.demonstration_buffer[info_teacher.agents[l]]['actions'])
            horizon_reached = teacher_action_list > self.trainer_parameters['time_horizon']
            teacher_filled = len(self.demonstration_buffer[info_teacher.agents[l]]['actions']) > 0
            if (info_teacher.local_done[l] or horizon_reached) and teacher_filled:
                agent_id = info_teacher.agents[l]
                self.demonstration_buffer.append_update_buffer(
                    agent_id, batch_size=None, training_length=self.policy.sequence_length)
                self.demonstration_buffer[agent_id].reset_agent()

        super(OnlineBCTrainer, self).process_experiences(current_info, next_info)