def update_stack(self, name, working_bucket, wait=False, update_only=False, disable_progress=False):
        """
        Update or create the CF stack managed by Zappa.
        """
        capabilities = []

        template = name + '-template-' + str(int(time.time())) + '.json'
        with open(template, 'wb') as out:
            out.write(bytes(self.cf_template.to_json(indent=None, separators=(',',':')), "utf-8"))

        self.upload_to_s3(template, working_bucket, disable_progress=disable_progress)
        if self.boto_session.region_name == "us-gov-west-1":
            url = 'https://s3-us-gov-west-1.amazonaws.com/{0}/{1}'.format(working_bucket, template)
        else:
            url = 'https://s3.amazonaws.com/{0}/{1}'.format(working_bucket, template)

        tags = [{'Key': key, 'Value': self.tags[key]}
                for key in self.tags.keys()
                if key != 'ZappaProject']
        tags.append({'Key':'ZappaProject','Value':name})
        update = True

        try:
            self.cf_client.describe_stacks(StackName=name)
        except botocore.client.ClientError:
            update = False

        if update_only and not update:
            print('CloudFormation stack missing, re-deploy to enable updates')
            return

        if not update:
            self.cf_client.create_stack(StackName=name,
                                        Capabilities=capabilities,
                                        TemplateURL=url,
                                        Tags=tags)
            print('Waiting for stack {0} to create (this can take a bit)..'.format(name))
        else:
            try:
                self.cf_client.update_stack(StackName=name,
                                            Capabilities=capabilities,
                                            TemplateURL=url,
                                            Tags=tags)
                print('Waiting for stack {0} to update..'.format(name))
            except botocore.client.ClientError as e:
                if e.response['Error']['Message'] == 'No updates are to be performed.':
                    wait = False
                else:
                    raise

        if wait:
            total_resources = len(self.cf_template.resources)
            current_resources = 0
            sr = self.cf_client.get_paginator('list_stack_resources')
            progress = tqdm(total=total_resources, unit='res', disable=disable_progress)
            while True:
                time.sleep(3)
                result = self.cf_client.describe_stacks(StackName=name)
                if not result['Stacks']:
                    continue  # might need to wait a bit

                if result['Stacks'][0]['StackStatus'] in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']:
                    break

                # Something has gone wrong.
                # Is raising enough? Should we also remove the Lambda function?
                if result['Stacks'][0]['StackStatus'] in [
                                                            'DELETE_COMPLETE',
                                                            'DELETE_IN_PROGRESS',
                                                            'ROLLBACK_IN_PROGRESS',
                                                            'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS',
                                                            'UPDATE_ROLLBACK_COMPLETE'
                                                        ]:
                    raise EnvironmentError("Stack creation failed. "
                                           "Please check your CloudFormation console. "
                                           "You may also need to `undeploy`.")

                count = 0
                for result in sr.paginate(StackName=name):
                    done = (1 for x in result['StackResourceSummaries']
                            if 'COMPLETE' in x['ResourceStatus'])
                    count += sum(done)
                if count:
                    # We can end up in a situation where we have more resources being created
                    # than anticipated.
                    if (count - current_resources) > 0:
                        progress.update(count - current_resources)
                current_resources = count
            progress.close()

        try:
            os.remove(template)
        except OSError:
            pass

        self.remove_from_s3(template, working_bucket)