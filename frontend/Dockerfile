FROM node:20-alpine

WORKDIR /app

# ติดตั้ง dependencies ก่อน เพื่อใช้ cache
COPY package*.json ./
RUN npm install

# คัดลอกโค้ดทั้งหมด
COPY . .

EXPOSE 5173

# --host ทำให้เข้าถึงจากนอก container ได้
CMD ["npm", "run", "dev", "--", "--host"]
