from app.database import engine, Base
from app.models.receipt import Receipt

Base.metadata.create_all(bind=engine)
