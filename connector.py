from github import Github

from config import GITHUB_ACCESS_TOKEN


def get_report_list():
    g = Github(GITHUB_ACCESS_TOKEN)
    repos = []
    for repo in g.get_user().get_repos():
        repos.append(repo)
    return repos