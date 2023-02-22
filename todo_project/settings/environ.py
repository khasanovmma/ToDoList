import os, environ


environ.Path(__file__) - 3
env = environ.Env()

ENV_FILE = os.getenv("TODO_PROJECT_ENV", ".env")
environ.Env.read_env(ENV_FILE)
