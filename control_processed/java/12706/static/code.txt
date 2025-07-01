private boolean isAddToLoadBalancerSuspended(String asgAccountId, String asgName) {
        AutoScalingGroup asg;
        if(asgAccountId == null || asgAccountId.equals(accountId)) {
            asg = retrieveAutoScalingGroup(asgName);
        } else {
            asg = retrieveAutoScalingGroupCrossAccount(asgAccountId, asgName);
        }
        if (asg == null) {
            logger.warn("The ASG information for {} could not be found. So returning false.", asgName);
            return false;
        }
        return isAddToLoadBalancerSuspended(asg);
    }