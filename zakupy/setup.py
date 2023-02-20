import alembic.config

if __name__ == "__main__":
    # run alembic upgrade head
    alembicArgs = [
        "--raiseerr",
        "upgrade",
        "heads",
    ]
    alembic.config.main(argv=alembicArgs)
