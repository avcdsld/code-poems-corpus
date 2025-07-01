function askForMonitoring() {
    if (this.regenerate) return;

    const done = this.async();

    const prompts = [
        {
            type: 'list',
            name: 'monitoring',
            message: 'Do you want to setup monitoring for your applications ?',
            choices: [
                {
                    value: 'no',
                    name: 'No'
                },
                {
                    value: 'elk',
                    name:
                        this.deploymentApplicationType === 'monolith'
                            ? 'Yes, for logs and metrics with the JHipster Console (based on ELK)'
                            : 'Yes, for logs and metrics with the JHipster Console (based on ELK and Zipkin)'
                },
                {
                    value: 'prometheus',
                    name: 'Yes, for metrics only with Prometheus'
                }
            ],
            default: this.monitoring ? this.monitoring : 'no'
        }
    ];

    this.prompt(prompts).then(props => {
        this.monitoring = props.monitoring;
        done();
    });
}