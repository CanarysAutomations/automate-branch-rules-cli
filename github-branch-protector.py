from github import Github
from stdiomask import getpass
from config import branch_name
from config import branch_rules
from config import signed_commit

def add_all():
    print("")
    for repo in git.get_organization(org_name).get_repos():
        branch = repo.get_branch(branch_name)
        branch.edit_protection(**branch_rules)
        if(signed_commit):
            branch.add_required_signatures()
        print("Added branch protection rules for: " + repo.name)

def add_one():
    repo_name = input("\nRepository: ")
    repo = git.get_repo(org_name+"/"+repo_name)
    branch = repo.get_branch(branch_name)
    branch.edit_protection(**branch_rules)
    if(signed_commit):
        branch.add_required_signatures()
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

print("   _____ _ _   _    _       _        ____                       _        _____           _            _")
print("  / ____(_) | | |  | |     | |      |  _ \                     | |      |  __ \         | |          | |")
print(" | |  __ _| |_| |__| |_   _| |__    | |_) |_ __ __ _ _ __   ___| |__    | |__) | __ ___ | |_ ___  ___| |_ ___  _ __")
print(" | | |_ | | __|  __  | | | | '_ \   |  _ <| '__/ _` | '_ \ / __| '_ \   |  ___/ '__/ _ \| __/ _ \/ __| __/ _ \| '__|")
print(" | |__| | | |_| |  | | |_| | |_) |  | |_) | | | (_| | | | | (__| | | |  | |   | | | (_) | ||  __/ (__| || (_) | |")
print("  \_____|_|\__|_|  |_|\__,_|_.__/   |____/|_|  \__,_|_| |_|\___|_| |_|  |_|   |_|  \___/ \__\___|\___|\__\___/|_|\n")        

org_name = input("\nGitHub Organization name: ")
pat = getpass("PAT: ")
print("")
print("Where do u want to add/remove rules?")
exec_type = input("One Repository [O] , All Repositories [A] , Remove Single [S] , Remove All [R]: ")
git = Github(pat)

if (exec_type=='O'):
    add_one()
elif (exec_type=='A'):
    add_all()
elif (exec_type=='S'):
    remove_one()
elif (exec_type=='R'):
    remove_all()
else:
    print("Invalid input. Re-run")
