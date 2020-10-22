from github import Github
from stdiomask import getpass
from config import branch_name
from config import branch_rules
from config import signed_commit
from config import add_codeowners_file
import codeowners

def add_all(pat):
    print("")
    for repo in git.get_organization(org_name).get_repos():
        branch = repo.get_branch(branch_name)
        if(add_codeowners_file):
            codeowners.add(org_name,pat,repo.name,branch_name)
        branch.edit_protection(**branch_rules)
        if(signed_commit):
            branch.add_required_signatures()
        else:
            branch.remove_required_signatures()
        print("Edited the branch protection rules for: " + repo.name)

def add_one(pat):
    repo_name = input("\nRepository: ")
    repo = git.get_repo(org_name+"/"+repo_name)
    branch = repo.get_branch(branch_name)
    if(add_codeowners_file):
        codeowners.add(org_name,pat,repo_name,branch_name)
    branch.edit_protection(**branch_rules)
    if(signed_commit):
        branch.add_required_signatures()
    else:
        branch.remove_required_signatures()
    print("Edited the branch protection rules for: " + repo.name)  

def remove_one():
    repo_name = input("\nRepository: ")
    repo = git.get_repo(org_name+"/"+repo_name)
    branch = repo.get_branch(branch_name)
    if (branch.protected):
        branch.remove_protection()
        print("Removed branch protection rules for: " + repo.name)
    else:
        print("No branch protection rules for: " + repo.name + "," + branch.name)    

def remove_all():
    print("")
    for repo in git.get_organization(org_name).get_repos():
        branch = repo.get_branch(branch_name)
        if (branch.protected):
            branch.remove_protection()
            print("Removed branch protection rules for: " + repo.name)
        else:
            print("No branch protection rules for: " + repo.name + "," + branch.name)

print("   ___        _                        _         ______                      _       ______      _           ")
print("  / _ \      | |                      | |        | ___ \                    | |      | ___ \    | |          ")
print(" / /_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___   | |_/ /_ __ __ _ _ __   ___| |__    | |_/ /   _| | ___  ___ ")
print(" |  _  | | | | __/ _ \| '_ ` _ \ / _` | __/ _ \  | ___ \ '__/ _` | '_ \ / __| '_ \   |    / | | | |/ _ \/ __|")
print(" | | | | |_| | || (_) | | | | | | (_| | ||  __/  | |_/ / | | (_| | | | | (__| | | |  | |\ \ |_| | |  __/\__ \\")
print(" \_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|  \____/|_|  \__,_|_| |_|\___|_| |_|  \_| \_\__,_|_|\___||___/\n")

org_name = input("\nGitHub Organization name: ")
pat = getpass("PAT: ")
print("")
print("Where do you want to add/remove rules?")
exec_type = input("Add One Repository [O] , Add All Repositories [A] , Remove Single Repository [S] , Remove All Repositories [R]: ").upper()
git = Github(pat)

if (exec_type=='O'):
    add_one(pat)
elif (exec_type=='A'):
    add_all(pat)
elif (exec_type=='S'):
    remove_one()
elif (exec_type=='R'):
    remove_all()
else:
    print("Invalid input. Re-run")
