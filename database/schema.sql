CREATE DATABASE CongDangKyDN;
USE CongDangKyDN;

-- Bảng TaiKhoan
CREATE TABLE IF NOT EXISTS TaiKhoan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_dang_nhap VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE NOT NULL,
    mat_khau VARCHAR(256) NOT NULL,
    so_dien_thoai VARCHAR(20),
    trang_thai TINYINT DEFAULT 1,
    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Bảng DoanhNghiep
CREATE TABLE IF NOT EXISTS DoanhNghiep (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT ,
    ten_doanh_nghiep VARCHAR(255),
    dia_chi TEXT,
    ma_so_thue VARCHAR(20),
    loai_hinh VARCHAR(100),
    ngay_dang_ky DATE,
    FOREIGN KEY (tai_khoan_id) REFERENCES TaiKhoan(id)
);

-- Bảng TrangThaiHoSo
CREATE TABLE IF NOT EXISTS TrangThaiHoSo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_trang_thai VARCHAR(100) NOT NULL
);

-- Bảng HoSo
CREATE TABLE IF NOT EXISTS HoSo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT,
    doanh_nghiep_id INT,
    ten_ho_so VARCHAR(255),
    duong_dan_pdf VARCHAR(255),
    duong_dan_xml VARCHAR(255),
    da_ky_so BOOLEAN DEFAULT FALSE,
    trang_thai_id INT,
    ngay_nop DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tai_khoan_id) REFERENCES TaiKhoan(id),
    FOREIGN KEY (doanh_nghiep_id) REFERENCES DoanhNghiep(id),
    FOREIGN KEY (trang_thai_id) REFERENCES TrangThaiHoSo(id)
);

-- Bảng PhanHoiHoSo
CREATE TABLE IF NOT EXISTS PhanHoiHoSo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ho_so_id INT,
    ghi_chu TEXT,
    duong_dan_file VARCHAR(255),
    da_ky_so BOOLEAN DEFAULT FALSE,
    thoi_gian_gui DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ho_so_id) REFERENCES HoSo(id)
);

-- Bảng ThongBao
CREATE TABLE IF NOT EXISTS ThongBao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT,
    noi_dung TEXT,
    thoi_gian_gui DATETIME DEFAULT CURRENT_TIMESTAMP,
    loai_thong_bao VARCHAR(50),
    da_doc BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (tai_khoan_id) REFERENCES TaiKhoan(id)
);

-- Bảng Admin
CREATE TABLE IF NOT EXISTS Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    mat_khau VARCHAR(256) NOT NULL,
    ho_ten VARCHAR(100),
    phan_quyen VARCHAR(50)
);

-- Bảng OTP
CREATE TABLE IF NOT EXISTS OTP (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT,
    ma_otp VARCHAR(10),
    thoi_gian_gui DATETIME DEFAULT CURRENT_TIMESTAMP,
    het_han_sau INT DEFAULT 300,
    da_su_dung BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (tai_khoan_id) REFERENCES TaiKhoan(id)
);
