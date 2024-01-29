from github import Github

g = Github("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")

repo = g.get_repo("mouredev/retos-programacion-2023")

commits = repo.get_commits()[:10]

for i, commit in enumerate(commits, start=1):
    git_commit = commit.commit

    hash = commit.sha
    author = git_commit.author.name
    message = git_commit.message
    date = git_commit.author.date

    date_str = date.strftime("%d/%m/%Y %H:%M")

    print(f"Commit {i} | {hash} | {author} | {message} | {date_str}")
