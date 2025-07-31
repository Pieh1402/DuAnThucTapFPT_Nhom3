USE CongDangKyDN;

-- 1. Tài khoản doanh nghiệp
INSERT INTO TaiKhoan (ten_dang_nhap, email, mat_khau, so_dien_thoai, trang_thai)
VALUES 
('abc123', 'abcde@company.com', 'mahoa123', '0912345678', 1),
('xyz456', 'xyzzz@biz.vn', 'mahoa456', '0987654321', 1);
-- 2. Doanh nghiệp
INSERT INTO DoanhNghiep (tai_khoan_id, ten_doanh_nghiep, dia_chi, ma_so_thue, loai_hinh)
VALUES 
(1, 'Công ty TNHH ABC', '123 Nguyễn Văn Cừ, Hà Nội', '0101234567', 'TNHH'),
(2, 'Công ty Cổ phần XYZ', '45 Lê Lợi, Đà Nẵng', '0407654321', 'Cổ phần');

-- 3. Trạng thái hồ sơ
INSERT INTO TrangThaiHoSo (ten_trang_thai)
VALUES 
('Đã tiếp nhận'),
('Đang xử lý'),
('Cần bổ sung'),
('Đã duyệt');

-- 4. Hồ sơ
INSERT INTO HoSo (tai_khoan_id, doanh_nghiep_id, ten_ho_so, duong_dan_pdf, duong_dan_xml, da_ky_so, trang_thai_id)
VALUES 
(1, 1, 'Hồ sơ đăng ký ABC', 'files/abc.pdf', 'files/abc.xml', TRUE, 1),
(2, 2, 'Hồ sơ đăng ký XYZ', 'files/xyz.pdf', NULL, FALSE, 3);


-- 5. Phản hồi bổ sung
INSERT INTO PhanHoiHoSo (ho_so_id, ghi_chu, duong_dan_file, da_ky_so)
VALUES 
(2, 'Vui lòng bổ sung giấy tờ chứng nhận vốn', 'files/bosung_xyz.pdf', TRUE);

-- 6. Thông báo
INSERT INTO ThongBao (tai_khoan_id, noi_dung, loai_thong_bao, da_doc)
VALUES 
(1, 'Hồ sơ của bạn đã tiếp nhận', 'trang_thai', FALSE),
(2, 'Cần bổ sung hồ sơ theo yêu cầu', 'bo_sung', FALSE);

-- 7. Tài khoản quản trị
INSERT INTO Admin (email, mat_khau, ho_ten, phan_quyen)
VALUES 
('admin@moit.gov.vn', 'admin123', 'Nguyễn Văn A', 'superadmin');
UPDATE Admin
SET mat_khau = '$2b$12$usTV.wBXdJ1XyrXlJSx00OrURb2gLdez4GwAKxB.21EFx.S6JdZm2'
WHERE email = 'admin@moit.gov.vn';
-- 8. OTP
INSERT INTO OTP (tai_khoan_id, ma_otp, het_han_sau, da_su_dung)
VALUES 
(1, '489512', 300, FALSE),
(2, '103984', 300, TRUE);

