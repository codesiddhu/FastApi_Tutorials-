from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import create_engine

MYSQL_USER = "root"
MYSQL_PASSWORD = "1144"
MYSQL_DATABASE = "fastapi"
MYSQL_PORT = "3306"
MYSQL_HOST = "localhost"


DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

new_engine = create_engine(DATABASE_URL)

session=sessionmaker(autoflush=False,autocommit=False,bind=new_engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
Base = declarative_base()