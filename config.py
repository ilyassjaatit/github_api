import environ

env = environ.Env()
environ.Env.read_env()

GITHUB_ACCESS_TOKEN = env('GITHUB_ACCESS_TOKEN')
