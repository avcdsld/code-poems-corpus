def format_issue(issue)
      t(config.format == 'one-line' ? 'issue.oneline' : 'issue.details',
        key: issue.key,
        summary: issue.summary,
        status: issue.status.name,
        assigned: optional_issue_property('unassigned') { issue.assignee.displayName },
        fixVersion: optional_issue_property('none') { issue.fixVersions.first['name'] },
        priority: optional_issue_property('none') { issue.priority.name },
        url: format_issue_link(issue.key))
    end