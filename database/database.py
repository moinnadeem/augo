user = os.environ['POSTGRES_USER"]
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB"]
host = 'db'
port = '5432'
engine = create_engine("postgres://{}:{}@{}:{}/{}".format(user, pwd, host, port, db))

Base = declarative_base()

def init_db():
   import models
   Base.metadata.create_all(bind=engine) 
