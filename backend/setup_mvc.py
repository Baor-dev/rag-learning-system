import os

# Định nghĩa các thư mục kiến trúc lõi
folders = ["models", "controllers", "services", "utils"]

# Định nghĩa các file logic theo chuẩn đã chốt
files = [
    "server.py",
    ".env",
    "models/__init__.py", "models/document.py", "models/chat.py",
    "controllers/__init__.py", "controllers/document_controller.py", "controllers/chat_controller.py",
    "services/__init__.py", "services/rag_service.py", "services/document_service.py",
    "utils/__init__.py", "utils/file_validator.py"
]

# Tự động tạo thư mục
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Tự động tạo file rỗng
for file in files:
    with open(file, 'a') as f:
        pass

print("✅ Đã khởi tạo thành công cấu trúc MVC cho dự án!")