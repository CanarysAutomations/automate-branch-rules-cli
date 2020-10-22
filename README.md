# Automate Branch Rules

**This tool will bulk add, remove or modify branch protection rules for every repo or a single repo in any GitHub organization.**

The tool can:
- Add or Update branch rules for a single repository.
- Add or Update branch rules for all repositories in the organization.
- Remove branch rules for a single repository.
- Remove branch rules for all repositories in the organization.

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
