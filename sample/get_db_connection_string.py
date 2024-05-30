def get_db_connecion_string():
    # Note: Here is where you would drive this by configuration (local, dev, prod, etc)
    # Note: In the real word, the secret would not be saved in a git repo :)
    return 'postgresql://test_user:test_password@localhost:5432/fastapi_db'
