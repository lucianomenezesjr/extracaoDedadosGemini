from app.database import engine
from app.models.gemini_message import Base

Base.metadata.create_all(bind=engine)
