USE CongDangKyDN;

-- 1. Thống kê số hồ sơ theo từng trạng thái
SELECT 
    t.ten_trang_thai AS TrangThai,
    COUNT(h.id) AS SoLuong
FROM HoSo h
JOIN TrangThaiHoSo t ON h.trang_thai_id = t.id
GROUP BY t.ten_trang_thai;

-- 2. Danh sách doanh nghiệp có nhiều hồ sơ nhất (top 5)
SELECT 
    d.ten_doanh_nghiep,
    COUNT(h.id) AS SoLuongHoSo
FROM DoanhNghiep d
JOIN TaiKhoan tk ON d.tai_khoan_id = tk.id
JOIN HoSo h ON tk.id = h.tai_khoan_id
GROUP BY d.ten_doanh_nghiep
ORDER BY SoLuongHoSo DESC
LIMIT 5;

-- 3. Số hồ sơ đã nộp theo tháng trong năm hiện tại
SELECT 
    MONTH(h.ngay_nop) AS Thang,
    COUNT(*) AS SoLuongHoSo
FROM HoSo h
WHERE YEAR(h.ngay_nop) = YEAR(NOW())
GROUP BY MONTH(h.ngay_nop)
ORDER BY Thang;

-- 4. Số lần gửi bổ sung hồ sơ theo từng doanh nghiệp
SELECT 
    d.ten_doanh_nghiep,
    COUNT(p.id) AS SoLanBoSung
FROM PhanHoiHoSo p
JOIN HoSo h ON p.ho_so_id = h.id
JOIN TaiKhoan tk ON h.tai_khoan_id = tk.id
JOIN DoanhNghiep d ON d.tai_khoan_id = tk.id
GROUP BY d.ten_doanh_nghiep;

-- 5. Số lượng thông báo đã gửi theo loại
SELECT 
    loai_thong_bao,
    COUNT(*) AS SoThongBao
FROM ThongBao
GROUP BY loai_thong_bao;

-- 6. Số OTP đã gửi và tỷ lệ dùng thành công
SELECT 
    COUNT(*) AS TongOTP,
    SUM(CASE WHEN da_su_dung = TRUE THEN 1 ELSE 0 END) AS DaDung,
    SUM(CASE WHEN da_su_dung = FALSE THEN 1 ELSE 0 END) AS ChuaDung,
    ROUND(SUM(CASE WHEN da_su_dung = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS TiLeDaDung
FROM OTP;
