import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# Load .env vào os.environ
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Kết nối thành công!")
        for row in result:
            print("Kết quả test:", row[0])
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print("❌ Kết nối thất bại:", str(e))
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 