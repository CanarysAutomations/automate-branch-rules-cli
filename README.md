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

## Prerequisites

The tool can be executed as a CLI app inside a **docker container** or directly using **python**. Refer the below sections for prerequisites in both cases.

### Running as a docker container.

- A GitHub organization with permissions to update branch protection rules.<br>

  *Note: The tool is not developed for personal accounts in GitHub*

- Docker installed in your machine. To download and install docker for Mac, Linux or windows [click here.](https://docs.docker.com/get-docker/)

### Running using Python

- A GitHub organization with permissions to update branch protection rules.<br>

  *Note: The tool is not developed for personal accounts in GitHub*

- Python 3.8 or above installed in your machine. To download [click here](https://www.python.org/downloads/)

- Latest version of pip. Run the following command as root user or in admin command prompt if windows.

  ```python -m pip install --upgrade pip```

- Python library **stdiomask** installed in your machine. Run the following command as root user or in admin command prompt if windows.

  ```pip install stdiomask```

- Python library **PyGithub** installed in your machine. Run the following command as root user or in admin command prompt if windows.

  ```pip install pygithub```

**To learn how to setup and use the tool [click here](https://github.com/CanarysDevOps/GitHub-Branch-Protector/wiki/Configure-&-Execute).**
