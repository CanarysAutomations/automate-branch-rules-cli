"""Importing GitHub Module."""
from github import Github


def add(orgname, pat, reponame, branchname):
    """Add or Update CODEOWNERS."""
    g = Github(pat)
    repo = g.get_organization(orgname).get_repo(reponame)
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file)
                             .replace('ContentFile(path="', '')
                             .replace('")', ''))

    with open('./CODEOWNERS', 'r') as file:
        content = file.read()

    # Upload to github
    git_prefix = '.github/'
    git_file = git_prefix + 'CODEOWNERS'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path,
                         "updating CODEOWNERS",
                         content,
                         contents.sha,
                         branch=branchname)
        print(git_file + ' updated for: ' + reponame)
    else:
        repo.create_file(git_file,
                         "adding CODEOWNERS",
                         content,
                         branch=branchname)
        print(git_file + ' created for: ' + reponame)
