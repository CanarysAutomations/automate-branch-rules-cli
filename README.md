# Automate :curly_loop: Branch Rules

The tool lets you automate the addition, removal or alteration of the branch protection rules for 1 or more repositories in one go.

The tool currently supports adding or modifying the below branch protection rules-

- Require pull request reviews before merging
  - Dismiss stale pull request approvals when new commits are pushed
  - Require review from Code Owners
  - Restrict who can dismiss pull request reviews
- Require status checks to pass before merging
  - Require branches to be up to date before merging
- Require signed commits
- Include administrators
- Restrict who can push to matching branches
- Add or update CODEOWNERS

## Prerequisites

The tool can be executed as a CLI app inside a **Docker Container** or using **Python**. Refer the below sections for prerequisites in both the cases.

### Run as a Docker Container :whale:

- A GitHub organization with permissions to update the branch protection rules

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

### Run using Python

- A GitHub organization with permissions to update the branch protection rules

- [Python 3.8](https://www.python.org/downloads/) or above installed on your machine

- Latest version of pip. Run the following command as a **root user** (linux) or as an administrator mode in command prompt (windows).

  ```python -m pip install --upgrade pip```

- Python library **stdiomask** installed on your machine. Run the following command as a **root user** (linux) or as an administrator mode in command prompt (windows).

  ```pip install stdiomask```

- Python library **PyGithub** installed on your machine. Run the following command as a **root user** (linux) or as an administrator mode in command prompt (windows).

  ```pip install pygithub```

### Usage Instructions :memo:

To learn how to setup and use the tool [click here](https://github.com/CanarysDevOps/GitHub-Branch-Protector/wiki/Configure-&-Execute).

### Current limitations :x: :x:

- The tool does not support for [Personal user accounts](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/types-of-github-accounts) <br/>
- Allow force pushes, Allow deletions and Require linear history rules are not supported
