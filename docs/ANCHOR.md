# ANCHOR — W17_03_Claude_porfolio

> Mốc chuẩn (anchor) để Codex kiểm. Mọi mục dưới đây đều kiểm được bằng lệnh hoặc bằng việc mở file; mục nào chưa kiểm được ghi rõ ở phần "Chưa kiểm".

## 0. Nguồn gốc và phạm vi

| Mục | Giá trị |
|---|---|
| Nguồn | `W17_02` tại commit `9a37799` (nhánh `main`) |
| Bản này | `W17_03_Claude_porfolio`, repo Git độc lập, lịch sử bắt đầu từ commit khởi tạo của bản này |
| Mục tiêu | Đổi định vị từ "ứng viên có nhiều dịch vụ" sang **freelancer về dữ liệu, nhận ít dịch vụ, làm được và chứng minh được** |
| Quyết định của chủ hồ sơ (vòng 2) | Dịch vụ là **dữ liệu**; Digital Marketing **đang học**, không nhận chạy quảng cáo. Nhận làm website, không cam kết doanh thu. Được dùng tên công ty cũ. Xóa số điện thoại. Dữ liệu demo và GA4 (trang do chính chủ làm) dùng bình thường |
| Phạm vi sửa (vòng 2–3) | Chỉ **nội dung chữ** (4 locale `vi/en/es/zh`) trong 2 file Final, hai file Creator sinh lại từ Final, và chuỗi kỳ vọng trong `tests/regression/run_all.py` |
| Phạm vi sửa (vòng 4, từ 2026-11-20) | Theo từng phase của Master Upgrade Spec đã được chủ hồ sơ duyệt; được sửa `server.py`, `tools/`, logic JS, bố cục trong phạm vi phase đó. Số liệu GA4 trưng bày, dữ liệu phễu mẫu, ảnh đại diện vẫn **không đổi** nếu chưa được duyệt riêng |

Lý do từng thay đổi nằm ở `docs/CHANGE_RATIONALE.md`.

## 1. Anchor định vị (A1–A3)

**A1 (cập nhật vòng 4). Sáu dịch vụ** — chính: `1. Tự động hóa Vận hành`, `2. Phân tích Dữ liệu & Dashboard BI`; chuyên ngành: `3. Hỗ trợ văn phòng thuế Mỹ (1040)`, `4. Lương thưởng, hoa hồng & KPI`; nhận làm: `5. Website & Trang đích`, `6. Đo lường hiệu suất quảng cáo`. Khóa cũ `eco_card3/4`, `modal_p3/p4` hiển thị số 5/6; khóa mới `eco_card5/6`, `modal_p5/p6`. Kiểm: test CONTENT. Nội dung A1 gốc bên dưới chỉ còn giá trị lịch sử (vòng 3d đã bỏ "đang học").

**A1 gốc (vòng 2, không còn áp dụng). Dữ liệu là chính; website nhận làm; đo lường theo yêu cầu; Digital Marketing đang học.**
- Chính: `1. Tự động hóa Vận hành`, `2. Phân tích Dữ liệu & Dashboard BI`.
- Nhận làm: `3. Website & Trang đích` (không cam kết doanh thu hay lượng khách).
- Theo yêu cầu: `4. Kiểm lỗi Đo lường` (GA4/GTM, chỉ phần kỹ thuật).
- Digital Marketing: ghi rõ **đang học**, không nhận chạy quảng cáo (`hero_bio`, `hero_desc`, `eco_property`, `modal_pkg_note`, `skill_grp_1`).
- Kiểm: khóa `eco_badge_1..4`, `modal_p1..4_badge`, `modal_pkg_heading` ở đủ 4 locale trong `index.html`.

**A2. Không còn tuyên bố không kiểm chứng được.** Các lệnh sau phải **không** trả kết quả trong nội dung hiển thị của 2 file Final:
```bash
grep -nE "xác thực 100|100% Verified|Verified Specialist|đã xác thực|认证专家|100% 真实|Verificad|verificad" index.html index_portfolio_clean.html
grep -nE "~60%|500\+|12 Vùng|12 Regions|12 Regiones|12 个战区|80–90%" index.html index_portfolio_clean.html
grep -nE "ROAS|CPA|CVR" index.html index_portfolio_clean.html
grep -nE "Google Ads|Meta Ads|TikTok" index.html index_portfolio_clean.html
```
Ghi chú: lệnh `ROAS|CPA|CVR` còn trả vài dòng `CPA/EA` trong mô tả WRP Tax Services (Certified Public Accountant / Enrolled Agent, không phải chỉ số quảng cáo) và một dòng nằm trong chuỗi ảnh nhúng base64; cả hai chấp nhận được. Tên Prudential, Chubb Life, AIA **được phép** xuất hiện (chủ hồ sơ cho phép ở vòng 2); chúng chỉ nằm trong `sol_desc` của CV.

**A3. Số liệu GA4 là của các trang do chính chủ hồ sơ xây.** Nguồn ghi là "thuộc tính GA4 của các trang do TJ xây dựng"; `hub_desc` nói số liệu lấy từ chính các trang này. Các con số (174 người dùng, 1.684 lượt xem, 10.465 sự kiện) và dữ liệu phễu mẫu **không đổi**.

## 2. Anchor nội dung dịch vụ (A4–A5)

**A4. Mỗi dịch vụ có đúng 3 đầu việc; dịch vụ 1–4 đều ghi sản phẩm bàn giao.** Mỗi `modal_pN_itemM` (N = 1..4, M = 1..3) chứa cụm "Bàn giao:" (vi), "Delivered:" (en), "Entrega:" (es), "交付：" (zh). Riêng `modal_p3_item*` vẫn là 3 mục.

**A5. Câu "không cam kết" còn đúng ở chỗ cần thiết.** Còn trong: `hero_desc`/`hero_bio`, `eco_card4_desc` (đúng cụm kiểm thử: `không cam kết doanh thu/lead`, `no revenue/lead KPI commitments`, `sin compromiso de ingresos/leads`, `不承诺获客或营收 KPI`), `modal_p4_item3`, `footer_desc`. Không lặp ở mọi khối như bản W17_02.

## 3. Anchor riêng tư (A6)

**A6 (cập nhật vòng 4). Số điện thoại ĐƯỢC công khai** theo quyết định mới của chủ hồ sơ (2026-11-20), nhưng **chỉ** khi chủ hồ sơ xác nhận số và định dạng (phase P0-2); số được quản lý trong khối `w17-site-config`, không tự lấy số trong link Zalo. Tới khi đó trang vẫn chưa hiển thị số. Nội dung A6 gốc bên dưới là lịch sử.

**A6 gốc (vòng 2). Số điện thoại không còn hiển thị.** Dòng điện thoại ở hero CV và khóa `hero_phone` đã bị xóa; nhãn Zalo không còn ghi số. Kiểm: `grep -n "855" index.html index_portfolio_clean.html` chỉ được trả các liên kết `https://zalo.me/…`. **Giới hạn cần biết:** số Zalo trùng số điện thoại nên địa chỉ liên kết `zalo.me` vẫn chứa số; chỉ ẩn được khỏi chữ hiển thị. Email công khai giữ nguyên.

## 4. Anchor kỹ thuật (A7–A9)

**A7. Quy tắc `AGENTS.md` vẫn đúng.** Không thêm màu/font/spacing mới. Chuỗi mới có `text-balance`/`inline-block` bảo vệ hai chữ cuối ở các tiêu đề và mô tả đã có (`hero_title`, `hub_title`, `contact_section_sub`, `footer_title`). Không dùng `innerHTML` với chuỗi thô mới ngoài cơ chế sẵn có.

**A8. Từ điển và HTML tĩnh đồng bộ.** Mọi khóa sửa có đủ 4 locale. Giá trị `vi` trong từ điển khớp văn bản tĩnh của phần tử `data-i18n` tương ứng.

**A9. Creator ↔ Final không lệch.**
```bash
python -X utf8 tools/sync_creators.py --check   # phải in OK cho cả hai Creator
```

**A10. Cấu hình dùng chung một nguồn (vòng 4).** Email, link Zalo, link GitHub (trang cá nhân) và địa chỉ web công khai nằm trong khối `<script type="application/json" id="w17-site-config">` **giống hệt nhau** ở hai file Final. Đổi qua nút ⚙ Cài đặt của editor (`POST /api/settings`) thì server thay giá trị cũ → mới ở mọi chỗ của cả hai file (giữ nguyên link repo `github.com/<tên>/<repo>`), đặt lại canonical/og:url, sinh lại Creator. `/api/save` trả 409 nếu bản lưu mang cấu hình khác bản trên đĩa (trang mở trước khi đổi cài đặt). Canonical Portfolio = địa chỉ web; canonical CV = địa chỉ web + `index_portfolio_clean.html`; không còn `og:url` trỏ `https://teoteo1081.github.io/` (404). Kiểm: `python -X utf8 tools/site_config.py --check`, test R6-01..03, R6-05.

**A11. Khôi phục bản nháp CV không làm mất thẻ mới (vòng 4).** Bản nháp lưu `knownIds` (mọi mã thẻ/tag từng thấy). Khi khôi phục: thẻ có trong `knownIds` mà không có trong thứ tự → đã bị xóa → xóa; thẻ không có trong `knownIds` → thẻ mới thêm vào file → giữ, đặt cuối nhóm. Bản nháp cũ không có `knownIds` giữ cách xử lý cũ. Kiểm: test R6-04.

## 5. Lệnh kiểm tổng

```bash
python -X utf8 tools/sync_creators.py --check
python -X utf8 tools/site_config.py --check
python -X utf8 tests/regression/run_all.py --quick
python -X utf8 tests/regression/native_zoom.py
```
Kết quả đã chạy khi tạo bản này được ghi ở `docs/CHANGE_RATIONALE.md`, mục "Kết quả kiểm tra".

## 6. Chưa kiểm (ghi thẳng, không tuyên bố PASS)

- Chưa mở site đã deploy; chỉ kiểm trên file trong repo.
- Chất lượng bản dịch `es` và `zh` do Claude viết, **chưa có người bản ngữ rà**.
- Chưa so sánh thị giác từng viewport 320/375/390/768/1024/1440 bằng ảnh chụp mới cho các đoạn chữ vừa đổi; chuỗi mới dài hơn ở một số khối (modal dịch vụ có thêm "Bàn giao: …"). Codex nên chụp modal dịch vụ ở 375px và 720×450.
- Việc nêu tên công ty cũ do chủ hồ sơ xác nhận bằng lời; chưa có tài liệu nào chứng minh quyền đó.

## 7. Cập nhật vòng 3 (2026-11-18)

Xem `docs/CHANGE_RATIONALE.md`, mục "Vòng 3". Tóm tắt các anchor bị ảnh hưởng: A1/A5 (`hero_desc` bỏ câu "đang học", vẫn giữ "không cam kết"), A3 (đã gỡ chuỗi số theo ngày và số liệu 7 ngày; chỉ còn các số 28 ngày trong `ga4_metrics_live.json`, chưa đối soát với GA4 thật). Kiểm: `grep -nE "Chart|trend28d|airy-web|Telemetry" index.html` phải không trả kết quả hiển thị.

Vòng 3b (2026-11-19): ngôn ngữ mặc định theo trình duyệt (kiểm bằng R3-09), CV ghi "Business English", khối phễu ghi rõ dữ liệu mẫu. Giữ nguyên theo chủ hồ sơ: "Hệ sinh thái", "Power BI (Nâng cao)", "Báo cáo thời gian thực" trong CV.

Vòng 3d (2026-11-19): A1/A5 thay đổi theo chủ hồ sơ — trang không còn câu "đang học" / "không cam kết"; dịch vụ 4 là "Đo lường hiệu suất quảng cáo". Chi tiết ở CHANGE_RATIONALE.md, mục Vòng 3d.

## 8. Vòng 4 (2026-11-20) — Master Upgrade, phase P0-1

Chủ hồ sơ duyệt phase P0-1 và việc cập nhật Anchor. Thay đổi so với anchor cũ:
- A1 → sáu dịch vụ (đã thực hiện ở vòng 3e, nay ghi lại vào anchor).
- A6 → số điện thoại được phép công khai sau khi chủ hồ sơ xác nhận số (P0-2).
- Phạm vi "ngoài phạm vi: `server.py`, `tools/`, logic JS" không còn đúng; phạm vi theo từng phase được duyệt.
- Thêm A10 (cấu hình dùng chung) và A11 (khôi phục bản nháp CV).
- Các phase sau (P0-2 CV/PDF/QR, P0-3 GA4, P0-4 sắp xếp Portfolio, P1…) chưa được duyệt; chưa làm.
