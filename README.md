# Automate :curly_loop: Branch Rules

The tool lets you automate the addition, removal or alteration of the branch protection rules for 1 or more branches & repositories in one go. This helps users to bulk update the branch rules which saves lot of time when you have hundreds of branches and repositories in your organization. 

## Supported branch protection rules

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

### Prerequisites

You can run the tool as **Docker Container** or cli using **Python**. Refer to the below sections in both cases.
- A GitHub organization with permissions to update the branch protection rules
- Git installed on your machine.[Click here](https://git-scm.com/downloads) to get the latest version of Git.

#### Run as a Docker Container :whale:

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

#### Run using Python :snake:

- [Python 3.8](https://www.python.org/downloads/) or above installed on your machine

- Install the latest version of pip

  ```python -m pip install --upgrade pip```

- Install the Python library **stdiomask**

  ```pip install stdiomask```

- Install the Python library **PyGithub**

  ```pip install pygithub```

**Note** :warning: Run the above commands as a root user **(linux)** or as an administrator mode in command prompt **(windows).**

### Usage Instructions :memo:

To learn how to setup and use the tool [click here](https://github.com/CanarysDevOps/GitHub-Branch-Protector/wiki/Configure).

### Current limitations :x: :x:

- The tool does not support for [Personal user accounts](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/types-of-github-accounts) <br/>
- **Allow force pushes**, **Allow deletions** and **Require linear history** rules are not supported

## 💝 Who's using Upptime

<!-- start: readme-repos-list -->
<!-- end: readme-repos-list -->

## License

The scripts and documentation in this project are released under the [MIT License](./LICENSE)
