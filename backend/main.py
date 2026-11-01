import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

# ดึงค่า Environment Variables จาก Docker Compose (ถ้าไม่มี จะใช้ค่าดีฟอลต์สำหรับรันโลคัล)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")

# สร้าง Database URL สำหรับ MySQL (ใช้ pymysql เป็น Driver)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# สร้าง SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    try:
        # เปิด Connection และ Query ข้อมูล
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM users"))
            # แปลงผลลัพธ์ที่เป็น Row ให้เป็น Dictionary
            users = [dict(row._mapping) for row in result]
            return {"users": users}
    except SQLAlchemyError as e:
        # กรณีเชื่อมต่อไม่ได้ หรือตาราง users ยังไม่ถูกสร้าง
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")