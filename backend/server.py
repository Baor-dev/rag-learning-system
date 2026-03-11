from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="RAG Learning System API",
    description="Backend API cho hệ thống hỗ trợ học tập dựa trên RAG",
    version="1.0.0"
)

# Cấu hình CORS để Frontend (ReactJS) có thể giao tiếp được với Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép mọi domain gọi API (sau này deploy sẽ siết lại)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint kiểm tra sức khỏe của Server
@app.get("/")
async def root():
    return {"status": "success", "message": "Server FastAPI đang hoạt động trơn tru! Hệ thống RAG đã sẵn sàng."}

# Lệnh chạy server khi gọi trực tiếp file này
if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)