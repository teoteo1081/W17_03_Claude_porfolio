# Sổ tay tự sửa Portfolio & CV

Dành cho chủ website, không cần biết lập trình. Chỉ ghi những việc **đã làm được**; phần nào chưa có sẽ ghi "chưa có".

Hai trang trên web:
- **Portfolio**: https://teoteo1081.github.io/W17_03_Claude_porfolio/
- **CV**: https://teoteo1081.github.io/W17_03_Claude_porfolio/index_portfolio_clean.html

---

## 1. Mở editor

1. Bấm đúp **`MO_EDITOR.bat`** trong thư mục dự án. Một cửa sổ đen hiện ra — **giữ nó mở** trong lúc sửa.
2. Trình duyệt tự mở trang Portfolio có thanh công cụ ở trên cùng. Sang CV: bấm "CV" trên menu.

Mở file HTML bằng cách bấm đúp, hoặc mở editor trên web thật, thì chỉ là **bản xem thử** (có dòng nhắc màu vàng): không lưu, không đăng được.

## 2. Sửa chữ tiếng Việt

1. Bấm **✏️ Bật sửa chữ**.
2. Bấm vào chữ muốn sửa và gõ trực tiếp.
3. Bấm **🚀 Lưu & đăng lên web**. Khoảng 1–2 phút sau web cập nhật (bấm Ctrl+F5 để xem).

Sửa ở tiếng Việt thì chỉ bản tiếng Việt đổi. Bản EN/ES/ZH: đổi ngôn ngữ trong editor rồi sửa tay, hoặc nhờ Claude dịch (chức năng dịch tự động chưa có).

## 3. Lưu vào máy và Đăng lên web khác nhau thế nào

| Nút | Làm gì |
|---|---|
| 💾 **Chỉ lưu vào máy** | Ghi file trong thư mục dự án. Web **chưa** đổi. |
| 🚀 **Lưu & đăng lên web** | Ghi file, rồi đẩy lên GitHub. Web đổi sau 1–2 phút. |

## 4. Đổi email, số điện thoại, Zalo, GitHub, địa chỉ web

1. Bấm **⚙ Cài đặt** trên thanh công cụ (ở trang Portfolio hay CV đều được).
2. Sửa ô cần đổi rồi bấm **Lưu cài đặt**. Trang tự tải lại.
3. Bấm **🚀 Lưu & đăng lên web**.

Đổi một lần là cả Portfolio và CV, cả 4 ngôn ngữ, cả link bấm gọi/gửi mail đều đổi theo.

- **Số điện thoại** ghi dạng quốc tế: `+84 855 239 805` (có `+84`, bỏ số 0 đầu).
- **Link GitHub** chỉ là trang cá nhân `https://github.com/<tên>`; link tới từng dự án giữ nguyên.
- **Địa chỉ web công khai** là địa chỉ trang Portfolio, kết thúc bằng dấu `/`. Không dùng `localhost`. Khi có tên miền riêng, đổi ở đây; link trong PDF, mã QR và thẻ canonical (cho Google) đổi theo.
- Nếu một tab editor khác (mở từ trước) báo **"Cài đặt dùng chung vừa được đổi"**: bấm F5 ở tab đó rồi sửa lại. Đây là cơ chế chống ghi đè cài đặt mới bằng bản cũ.

## 5. Xuất CV ra PDF (có mã QR)

1. Mở **trang CV trên web thật** (không phải editor) — khuyến nghị.
2. Bấm **📄 Tải CV (PDF)** ở thanh trên cùng → hộp thoại in hiện ra.
3. Ở "Máy in / Destination" chọn **Lưu thành PDF / Save as PDF**. Nên bật **Đồ họa nền / Background graphics**.
4. Bấm Lưu.

Bản PDF có:
- Link bấm được: Zalo, GitHub, **Xem Portfolio**, email, số điện thoại (tùy trình đọc PDF có hỗ trợ hay không).
- Khối **"Quét để xem Portfolio"**: mã QR + tên miền dễ đọc + email + số điện thoại.
- Không có nút của editor.

Link "Xem Portfolio" trong PDF có đuôi `?utm_source=cv_pdf&utm_medium=pdf…`, mã QR có `…utm_medium=qr…`: để sau này (khi cài GA4) phân biệt khách đến từ bấm link PDF hay quét QR. Đuôi này không chứa thông tin cá nhân.

**Lưu ý:** PDF đã gửi đi **không tự cập nhật**. Đổi số điện thoại hay địa chỉ web thì chỉ những bản PDF xuất **sau đó** mới mang thông tin mới.

## 6. Kiểm tra mã QR

Mở camera điện thoại, quét mã QR trên PDF (trên màn hình hoặc bản in giấy). Điện thoại phải mở đúng trang Portfolio. Nếu in giấy, in ở cỡ thật (100%), không thu nhỏ trang.

## 7. Sao lưu và khôi phục

- Mỗi lần lưu, máy chủ tự giữ **5 bản cũ gần nhất** trong thư mục ẩn `.w17_backups`.
- Mọi lần đăng lên web đều là một commit trên GitHub, nên luôn quay lại được bản cũ (nhờ Claude hoặc dùng lịch sử GitHub).

## 8. Khi gặp lỗi

| Thông báo | Cách xử lý |
|---|---|
| "Trên GitHub có bản mới hơn" | Nội dung đã lưu và commit trên máy. Nhờ Claude gộp rồi đăng lại. |
| "còn mã do tiện ích trình duyệt chèn vào" | Bấm Ctrl+F5 rồi lưu lại; nên tắt eJOY/Grammarly khi sửa. |
| "Cài đặt dùng chung vừa được đổi…" | Bấm F5 ở tab đó rồi sửa lại. |
| Nút ⚙ báo "Chỉ đổi được khi mở editor bằng MO_EDITOR.bat" | Đóng trang, bấm đúp `MO_EDITOR.bat` để mở lại. |

## 9. Hết lượt dùng Claude thì sao

Mọi việc ở mục 1–7 tự làm được, không cần Claude. Cần Claude khi: đổi bố cục/màu, thêm loại nội dung mới chưa có mẫu, gộp bản khi GitHub có bản mới hơn, sửa lỗi máy chủ.

## Chưa có (đang trong kế hoạch)

Di chuyển/ẩn mục và thẻ ở Portfolio, thêm thẻ mới, kinh nghiệm làm việc, dịch tự động bằng Gemini, đo lượt truy cập GA4, Search Console. Khi làm xong phần nào, sổ tay này sẽ thêm hướng dẫn phần đó.

## Giải thích từ ngữ

| Từ | Nghĩa |
|---|---|
| Hero | Khối đầu trang (tên, chức danh, nút liên hệ) |
| Section | Một mục lớn của trang (Giới thiệu, Dịch vụ, Liên hệ…) |
| Card / thẻ | Một ô nội dung trong mục (một dịch vụ, một dự án…) |
| CTA | Nút kêu gọi hành động ("Liên hệ Zalo", "Xem Portfolio") |
| UI / UX | Giao diện / trải nghiệm người dùng |
| i18n | Hệ thống đa ngôn ngữ (VI/EN/ES/ZH) |
| Canonical | Thẻ báo cho Google "đây là địa chỉ chính thức của trang" |
| UTM | Đuôi gắn sau link để biết khách đến từ đâu (vd. từ PDF, từ QR) |
| QR | Mã vuông quét bằng camera để mở link |
| PDF hyperlink | Link bấm được bên trong file PDF |
