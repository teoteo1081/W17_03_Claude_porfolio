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

## 3. Di chuyển và ẩn/hiện các mục trên Portfolio

Trong editor Portfolio, mỗi mục (Dịch vụ, Dashboard, Website, GA4 Tracking) có thanh nhỏ màu cam ở góc trên bên phải:

- **⬆ Lên / ⬇ Xuống**: đổi chỗ mục với mục bên trên/bên dưới. "Giới thiệu" luôn ở đầu, "Liên hệ" luôn ở cuối.
- **🚫 Ẩn mục / 👁 Hiện mục**: mục bị ẩn **không hiện trên web** và **không có trên menu**; trong editor vẫn thấy mờ mờ có viền cam để bật lại khi cần. Ẩn không xóa nội dung.
- Menu (máy tính và điện thoại) tự đổi theo ngay.
- Tải lại trang vẫn giữ thay đổi (bản nháp). Bấm **🚀 Lưu & đăng lên web** để đưa lên web.

## 3b. Chuyển giữa Portfolio và CV

Cả hai trang có nút **`Portfolio | CV`** ở góc trên bên trái; nấc đang xem được tô xanh. Gửi link trang nào cũng được, người nhận tự chuyển sang trang kia.

## 3c. Lưu vào máy và Đăng lên web khác nhau thế nào

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

## 6. Đo lượt truy cập bằng GA4

- GA4 property: **TJ Portfolio & CV** (trong tài khoản "TJ Sai Gon Project"). Measurement ID `G-501ZEXPEVQ` nằm ở ⚙ Cài đặt; để trống ô đó = tắt đo lường.
- Chỉ đo khi mở **trang web thật**. Sửa trong editor, mở bằng MO_EDITOR hay bấm đúp file thì **không** đếm.
- **Xem ngay có hoạt động không:** mở trang thật kèm đuôi `?ga_debug=1`, ví dụ `https://teoteo1081.github.io/W17_03_Claude_porfolio/?ga_debug=1`, bấm vài nút; trong GA4 vào **Quản trị → DebugView** sẽ thấy sự kiện sau vài giây. Hoặc xem **Báo cáo → Thời gian thực**.
- **Tách Portfolio và CV trong báo cáo:** dùng chiều **Nhóm nội dung** (`portfolio` / `cv`).
- **Sự kiện có sẵn:** bấm số điện thoại / email / Zalo, sang CV, sang Portfolio, GitHub, xem demo dự án, mở chi tiết dịch vụ, bấm Tải CV (PDF), mở ứng dụng email từ form liên hệ, đổi ngôn ngữ. Đây là **lượt bấm**, không phải kết quả (bấm Zalo chưa chắc đã nhắn).
- **Quyền riêng tư:** khách ở châu Âu/Anh/Thụy Sĩ mặc định không bị đo cho tới khi bấm Đồng ý; nút **Quyền riêng tư & cookie** ở chân trang để bất kỳ ai đổi lựa chọn. Vì vậy GA4 đếm **ít hơn** số khách thật.

## 7. Tạo link có UTM (biết khách đến từ kênh nào)

Thêm đuôi vào địa chỉ khi đăng link ở một kênh, ví dụ đăng trên LinkedIn:

`https://teoteo1081.github.io/W17_03_Claude_porfolio/?utm_source=linkedin&utm_medium=social&utm_campaign=profile`

- `utm_source`: nơi đăng (linkedin, facebook, email_signature…), `utm_medium`: loại kênh (social, email, referral…), `utm_campaign`: tên đợt.
- Chỉ viết chữ thường, không dấu, không khoảng trắng; **không** đưa tên/email/số điện thoại vào đuôi.
- Không gắn UTM cho link giữa Portfolio và CV (làm GA4 tách phiên sai). PDF và QR đã có sẵn UTM riêng.
- Kết quả xem ở **Báo cáo → Thu nạp → Thu nạp lưu lượng truy cập**, chiều "Nguồn/phương tiện của phiên".

## 8. Kiểm tra mã QR

Mở camera điện thoại, quét mã QR trên PDF (trên màn hình hoặc bản in giấy). Điện thoại phải mở đúng trang Portfolio. Nếu in giấy, in ở cỡ thật (100%), không thu nhỏ trang.

## 9. Sao lưu và khôi phục

- Mỗi lần lưu, máy chủ tự giữ **5 bản cũ gần nhất** trong thư mục ẩn `.w17_backups`.
- Mọi lần đăng lên web đều là một commit trên GitHub, nên luôn quay lại được bản cũ (nhờ Claude hoặc dùng lịch sử GitHub).

## 10. Khi gặp lỗi

| Thông báo | Cách xử lý |
|---|---|
| "Trên GitHub có bản mới hơn" | Nội dung đã lưu và commit trên máy. Nhờ Claude gộp rồi đăng lại. |
| "còn mã do tiện ích trình duyệt chèn vào" | Bấm Ctrl+F5 rồi lưu lại; nên tắt eJOY/Grammarly khi sửa. |
| "Cài đặt dùng chung vừa được đổi…" | Bấm F5 ở tab đó rồi sửa lại. |
| Nút ⚙ báo "Chỉ đổi được khi mở editor bằng MO_EDITOR.bat" | Đóng trang, bấm đúp `MO_EDITOR.bat` để mở lại. |

## 11. Hết lượt dùng Claude thì sao

Mọi việc ở mục 1–9 tự làm được, không cần Claude. Cần Claude khi: đổi bố cục/màu, thêm loại nội dung mới chưa có mẫu, gộp bản khi GitHub có bản mới hơn, sửa lỗi máy chủ.

## Chưa có (đang trong kế hoạch)

Di chuyển từng thẻ bên trong một mục (ở Portfolio), thêm thẻ mới, kinh nghiệm làm việc, dịch tự động bằng Gemini, Search Console. Khi làm xong phần nào, sổ tay này sẽ thêm hướng dẫn phần đó.

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
| GA4 | Google Analytics 4 — công cụ đếm lượt truy cập và lượt bấm |
| Consent | Sự đồng ý của khách cho phép đo lường |
| DebugView | Màn hình trong GA4 xem sự kiện gần như ngay lập tức để kiểm tra |
| QR | Mã vuông quét bằng camera để mở link |
| PDF hyperlink | Link bấm được bên trong file PDF |
