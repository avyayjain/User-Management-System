import os

TEST_URL="http://0.0.0.0:8000"

DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_DB = os.getenv("DATABASE_DB")
DATABASE_URL = os.getenv("DATABASE_URL")
DB_CONNECTION_LINK = "postgresql://{}:{}@{}/{}".format(
    DATABASE_USER,
    DATABASE_PASS,
    DATABASE_URL,
    DATABASE_DB,
)
ASYNC_DB_CONNECTION_LINK = "postgresql+asyncpg://{}:{}@{}/{}".format(
    DATABASE_USER,
    DATABASE_PASS,
    DATABASE_URL,
    DATABASE_DB,
)

BYTES_PER_CHUNK = 1000

FILE_FOLDER_PATH = os.path.join(os.getcwd(), 'files')