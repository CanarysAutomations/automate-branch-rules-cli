"""Importing necessary libraries."""
from github import Github
from github import GithubException
import sys
from stdiomask import getpass
from config import branches
from config import branch_rules
from config import signed_commit
from config import add_codeowners_file
import codeowners


def add_all(pat):
    """Add all function."""
    print("")
    for repo in git.get_organization(org_name).get_repos():
        for branch_name in branches:
            try:
                repo.get_branch(branch_name)
            except GithubException:
                print("Error:", repo.name, ",",
                      branch_name, "-->", sys.exc_info()[1])
            else:
                branch = repo.get_branch(branch_name)
                if(add_codeowners_file):
                    codeowners.add(org_name, pat, repo.name, branch_name)
                branch.edit_protection(**branch_rules)
                if(signed_commit):
                    branch.add_required_signatures()
                else:
                    branch.remove_required_signatures()
                print("Edited the branch protection rules for: "
                      + repo.name + "," + branch_name)


def add_one(pat):
    """Add one function."""
    repo_name = input("\nRepository: ")
    repo = git.get_repo(org_name+"/"+repo_name)
    for branch_name in branches:
        try:
            repo.get_branch(branch_name)
        except GithubException:
            print("Error:", repo.name, ",", branch_name, "-->",
                  sys.exc_info()[1])
        else:
            branch = repo.get_branch(branch_name)
            if(add_codeowners_file):
                codeowners.add(org_name, pat, repo_name, branch_name)
            branch.edit_protection(**branch_rules)
            if(signed_commit):
                branch.add_required_signatures()
            else:
                branch.remove_required_signatures()
            print("Edited the branch protection rules for: "
                  + repo.name + "," + branch_name)


def remove_one():
    """Remove One Function."""
    repo_name = input("\nRepository: ")
    repo = git.get_repo(org_name+"/"+repo_name)
    for branch_name in branches:
        try:
            repo.get_branch(branch_name)
        except GithubException:
            print("Error:", repo.name, ",",
                  branch_name, "-->", sys.exc_info()[1])
        else:
            branch = repo.get_branch(branch_name)
            if (branch.protected):
                branch.remove_protection()
                print("Removed branch protection rules for: "
                      + repo.name + "," + branch_name)
            else:
                print("No branch protection rules for: "
                      + repo.name + "," + branch.name)


def remove_all():
    """Remove all function."""
    print("")
    for repo in git.get_organization(org_name).get_repos():
        for branch_name in branches:
            try:
                repo.get_branch(branch_name)
            except GithubException:
                print("Error:", repo.name, ",",
                      branch_name, "-->", sys.exc_info()[1])
            else:
                branch = repo.get_branch(branch_name)
                if (branch.protected):
                    branch.remove_protection()
                    print("Removed branch protection rules for: "
                          + repo.name + "," + branch_name)
                else:
                    print("No branch protection rules for: "
                          + repo.name + "," + branch.name)


header = open("header.txt", "r")
print(header.read())
org_name = input("\nGitHub Organization name: ")
pat = getpass("PAT: ")
print("")
print("Where do you want to add/remove rules?")
exec_type = input("Add One Repository [O] , Add All Repositories [A] ,"
                  + "Remove Single Repository [S] ,"
                  + "Remove All Repositories [R]: ").upper()
git = Github(pat)

if (exec_type == 'O'):
    add_one(pat)
elif (exec_type == 'A'):
    add_all(pat)
elif (exec_type == 'S'):
    remove_one()
elif (exec_type == 'R'):
    remove_all()
else:
    print("Invalid input. Re-run")
