from app.database import engine, Base
from app.models.receipt import Receipt

# from app.models.gemini_message import Base ---> tire essa linha quando der commit

Base.metadata.create_all(bind=engine)
