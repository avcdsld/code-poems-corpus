function(aIssues) {
				var iHighIssues = 0,
					iMediumIssues = 0,
					iLowIssues = 0;
				aIssues.forEach(function(element) {
					switch (element.severity) {
						case constants.SUPPORT_ASSISTANT_ISSUE_SEVERITY_LOW:
							iLowIssues++;
							break;
						case constants.SUPPORT_ASSISTANT_ISSUE_SEVERITY_MEDIUM:
							iMediumIssues++;
							break;
						case constants.SUPPORT_ASSISTANT_ISSUE_SEVERITY_HIGH:
							iHighIssues++;
							break;
					}
				});

				return {high: iHighIssues, medium: iMediumIssues, low: iLowIssues};
			}