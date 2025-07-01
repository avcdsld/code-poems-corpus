function _doesEventContainsNestedStackId(stack) {
    if (stack.ResourceType !== 'AWS::CloudFormation::Stack') {
        return false;
    }
    if (stack.ResourceStatusReason !== 'Resource creation Initiated') {
        return false;
    }
    if (stack.ResourceStatus !== 'CREATE_IN_PROGRESS') {
        return false;
    }
    if (_.isNil(stack.PhysicalResourceId)) {
        return false;
    }

    return _hasLabelNestedStackName(stack.PhysicalResourceId);
}