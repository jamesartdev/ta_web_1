คำสั่งลง Python เฉพาะใน Project ไม่ใช่ Golbal

 python -m venv .venv

 ต่อมาคือพอลงเสร็จแล้วเราต้องเรียกใช้ด้วยคำสั่งนี้

 source .venv/bin/activate

 พอไม่ใช้แล้วจะกลับไป Gobal ให้ใช้คำสั่ง

 deactivate


 การสร้าง requirements
 python -m pip freeze > requirements.txt

แล้วก็เวลาคนอื่นเอาไฟล์ไปใช้ต่อเขาต้องลง File even ก่อน จากนั้นก็สั่ง
python -m pip install -r requirements.txt   // คือ -r คือให้ไปอ่านทั้งหมดของไฟล์ requirements.txt