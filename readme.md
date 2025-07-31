# Dự Án Thực Tập FPT

## 1. Giới thiệu

Dự án này là hệ thống quản lý hồ sơ thực tập, hỗ trợ doanh nghiệp, sinh viên và quản trị viên trong việc nộp, xét duyệt, và quản lý hồ sơ thực tập. Dự án gồm hai phần chính:
- **Backend:** Xây dựng bằng Python (FastAPI), quản lý API, xác thực, truy xuất dữ liệu.
- **Frontend:** Xây dựng bằng Vue.js, giao diện người dùng hiện đại, dễ sử dụng.

---

## 2. Tính năng chính

- Đăng nhập, đăng ký cho người dùng và doanh nghiệp
- Quản lý hồ sơ thực tập (tạo, cập nhật, theo dõi trạng thái)
- Quản trị viên duyệt hồ sơ, gửi thông báo
- Quản lý doanh nghiệp, sinh viên, thông báo
- Gửi email tự động khi có thay đổi trạng thái hồ sơ
- Thống kê, báo cáo

---

## 3. Kiến trúc hệ thống

```
mermaid
graph TD
  A[Frontend (Vue.js)] -->|API Request| B[Backend (FastAPI)]
  B -->|ORM Queries| C[(Database)]
  B -->|Send Email| D[Mail Server]
```
<pre lang="markdown"> ```mermaid graph TD A[Frontend (Vue.js)] -->|API Request| B[Backend (FastAPI)] B -->|ORM Queries| C[(Database)] B -->|Send Email| D[Mail Server] ``` </pre>

- **Frontend:** Giao diện người dùng, gọi API qua HTTP.
- **Backend:** Xử lý logic, xác thực, kết nối database, gửi mail.
- **Database:** Lưu trữ dữ liệu (MySQL/PostgreSQL tuỳ cấu hình).
- **Mail Server:** Gửi email thông báo.

---

## 4. Cấu trúc thư mục
```
DuAnThucTapFPT/
│
├── database/              # File SQL: schema, sample data, queries
│   ├── schema.sql
│   ├── sample_data.sql
│   └── report_queries.sql
│
├── FPT_Backend/           # Backend (FastAPI)
│   ├── requirements.txt
│   └── src/
│       ├── main.py
│       ├── models/
│       ├── routes/
│       ├── schemas/
│       └── utils/
│
├── FPT_Frontend/
│   └── Du-an-ftp/
│       ├── src/
│       ├── public/
│       └── package.json
```

---

## 5. Hướng dẫn cài đặt

### 5.1. Cài đặt Database

1. Cài đặt MySQL hoặc PostgreSQL.
2. Tạo database mới, ví dụ: `fpt_internship`.
3. Chạy file `database/schema.sql` để tạo bảng.
4. (Tuỳ chọn) Chạy `database/sample_data.sql` để thêm dữ liệu mẫu.

### 5.2. Cài đặt Backend

**Yêu cầu:** Python 3.8+

```bash
cd FPT_Backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**Cấu hình kết nối database và mail:**
- Sửa file cấu hình (ví dụ: `src/utils/db.py` hoặc file `.env` nếu có) để điền thông tin database, mail server.

**Chạy server:**
```bash
cd src
uvicorn main:app --reload
```
- API docs: http://127.0.0.1:8000/docs

### 5.3. Cài đặt Frontend

**Yêu cầu:** Node.js 16+

```bash
cd FPT_Frontend/Du-an-ftp
npm install
npm run dev
```
- Truy cập: http://localhost:5173

---

## 6. Hướng dẫn cấu hình

### 6.1. Backend

- **Database:** Sửa thông tin kết nối trong file cấu hình backend.
- **Mail:** Sửa thông tin SMTP trong file cấu hình (nếu có).
- **CORS:** Đảm bảo backend cho phép frontend truy cập (CORS).

### 6.2. Frontend

- Nếu cần thay đổi URL API, sửa trong file cấu hình (ví dụ: `src/plugins/index.js`).

---

## 7. Hướng dẫn sử dụng

### 7.1. Đăng nhập/Đăng ký

- Người dùng, doanh nghiệp đăng ký tài khoản.
- Đăng nhập để sử dụng các chức năng.

### 7.2. Nộp hồ sơ 

- Doanh nghiệp tạo và nộp hồ sơ .
- Theo dõi trạng thái hồ sơ.

### 7.3. Quản trị viên

- Duyệt hồ sơ, thay đổi trạng thái.
- Gửi thông báo cho doanh nghiệp.
- Quản lý danh sách doanh nghiệp.

### 7.4. Doanh nghiệp

- Quản lý thông tin doanh nghiệp.
- Xem danh sách hồ sơ.

---

## 8. Đóng góp & phát triển

- Fork repo, tạo branch mới cho tính năng/sửa lỗi.
- Tạo pull request kèm mô tả chi tiết.
- Tuân thủ quy tắc code và chuẩn đặt tên.

---


## 10. License

Dự án sử dụng cho mục đích học tập, nghiên cứu. Vui lòng liên hệ tác giả nếu muốn sử dụng cho mục đích khác.

---

