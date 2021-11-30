from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#url = "mysql+mysqlconnector://root:123456@192.168.60.128:4306/test"
url = "mysql+mysqlconnector://root:123456@192.158.0.5:3306/test"
engine = create_engine(url, pool_size=5)
Session = sessionmaker(bind=engine)
