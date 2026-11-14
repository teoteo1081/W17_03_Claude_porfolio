# W17_03_Claude_porfolio — Portfolio Freelancer: Vận hành & Dữ liệu (V3)

Hệ sinh thái **Portfolio Showcase & Hồ Sơ Năng Lực Tương Tác (Version 3)** của **Thao Nguyen (TJ)** — *Freelance Vận hành & Phân tích Dữ liệu • Tự động hóa Quy trình • Dashboard BI*.

> Bản W17_03 phái sinh từ W17_02 (commit `9a37799`): chỉ đổi **nội dung** để định vị freelancer, gồm 2 dịch vụ chính và 2 dịch vụ nhận theo yêu cầu. Mốc kiểm tra nằm ở [`docs/ANCHOR.md`](docs/ANCHOR.md), lý do từng thay đổi ở [`docs/CHANGE_RATIONALE.md`](docs/CHANGE_RATIONALE.md).

---

## 📁 Cấu Trúc Thư Mục Chuẩn (V3)

```text
W17_03_Claude_porfolio/
├── index.html                  # [Final] Portfolio Showcase V3 (Dịch vụ + dashboard GA4 minh họa)
├── index_portfolio_clean.html  # [Final] Hồ Sơ Năng Lực / Interactive CV V3 (Bản sạch sẵn sàng deploy & in PDF)
├── editor_workspace/           # Không gian soạn thảo trực quan (Visual Editor)
│   ├── editor_portfolio.html   # Bản Editor của Portfolio Showcase (Có thanh công cụ sửa chữ & xuất bản Final)
│   └── editor_cv.html          # Bản Editor của Hồ Sơ Năng Lực (Có nút [⬆][⬇], kéo thả, đổi màu, đổi ảnh)
├── ga4_metrics_live.json       # Dữ liệu đo lường thực tế từ Google Analytics 4 & BigQuery (airy-web-503408-c6)
├── fetch_ga4_bigquery.py       # Script Python truy vấn dữ liệu GA4 từ Google BigQuery
├── dev_server.py               # Local Dev Server hỗ trợ xem trực tiếp & lưu file sạch tự động qua /api/save
└── server.py                   # Core HTTP handler cho Visual Editor
```

---

## 🚀 Điểm Nổi Bật (Key Features)

1. **`index.html` — Portfolio Showcase V3**:
   - **Mô phỏng Phễu & Hiệu suất (Interactive Funnel Simulation)**: Lọc KPI động theo khu vực/kênh bán hàng.
   - **GA4 & Power BI Telemetry Dashboard**:
     - Tích hợp **Chart.js** biểu đồ đường & miền (Line & Area Chart) xu hướng 28 ngày (`1.684 lượt xem`, `174 người dùng`, `10.465 sự kiện`, `12m 30s tương tác TB`).
     - Bộ lọc Slicer tương tác (`[Tất cả]`, `[🇺🇸 Hoa Kỳ]`, `[🇻🇳 Việt Nam]`, chuyển đổi `28 ngày` / `7 ngày`).
     - **Interactive Drill-down Modal (Popup)**: Xem chi tiết Top 10 Quốc gia và Top 10 Tiêu đề trang kèm thanh tiến độ Data Bar.
   - **4 Dự Án Cá Nhân**: Liên kết trực tiếp tới Live Demo & GitHub của *WRP Tax Services*, *Operation 0 — 1,000 Chunks Engine*, *TJ WordLoop Multiplayer Game*, và *TJ Courses Hub*.

2. **`index_portfolio_clean.html` — Hồ Sơ Năng Lực / Interactive CV V3**:
   - Giao diện Executive Dark/Light Mode với 4 bảng màu chủ đạo (*Ocean, Emerald, Royal Gold, Midnight Indigo*).
   - Tối ưu hóa CSS in ấn (`@media print`) xuất PDF chuẩn màu 100%.
   - Liên kết điều hướng 2 chiều mượt mà giữa **Portfolio Showcase (`./index.html`)** và **Hồ Sơ Năng Lực (`./index_portfolio_clean.html`)**.

---

## 💻 Cách Chạy Thử Nhanh Trên Máy Khác

### Cách 1: Mở trực tiếp (Zero-Config)
- Chỉ cần **double-click** mở trực tiếp file `index.html` hoặc `index_portfolio_clean.html` trên bất kỳ trình duyệt nào (mọi thư viện Tailwind CSS, Lucide Icons, Chart.js và Google Fonts đều hoạt động độc lập qua CDN và đường dẫn tương đối).

### Cách 2: Chạy qua Local Dev Server (Hỗ trợ tự động lưu file sạch từ Visual Editor)
```bash
python dev_server.py
```
Sau đó mở trình duyệt tại địa chỉ:
- **Portfolio Showcase (Final)**: `http://localhost:8000/index.html`
- **Hồ Sơ Năng Lực (Final)**: `http://localhost:8000/index_portfolio_clean.html`
- **Visual Editor Workspace**: `http://localhost:8000/editor_workspace/editor_portfolio.html`

### Bảo vệ endpoint lưu file (`/api/save`)
- Server chỉ bind `127.0.0.1`, **không bật CORS**; trang trong editor tự lấy token phiên ngẫu nhiên qua `GET /api/session` (chỉ trả cho đúng origin của dev server) rồi gửi kèm header `X-W17-Token`.
- Chỉ ghi `index.html` và `index_portfolio_clean.html`, body tối đa 12MB, HTML phải đủ các thành phần đặc trưng của trang, đủ kích thước và không còn trạng thái editor; ghi nguyên tử, tuần tự hóa các lần ghi đồng thời và tự sao lưu bản cũ vào `.w17_backups/` (giữ 5 bản, đã `.gitignore`).
- Chỉ phục vụ file tĩnh có đuôi trong allowlist; đường dẫn được kiểm sau khi giải mã percent-encoding; không liệt kê thư mục, không phục vụ `*.py` hay thư mục ẩn.
- Mở file bằng `file://` vẫn tải được file sạch về máy nhưng **không** ghi trực tiếp vào dự án; hãy dùng `python dev_server.py`.

### Creator ↔ Final (một nguồn duy nhất)
`index.html` và `index_portfolio_clean.html` là nguồn; hai file trong `editor_workspace/` được **sinh** từ chúng:
```bash
python tools/sync_creators.py          # ghi lại hai Creator sau khi sửa Final
python tools/sync_creators.py --check  # báo lệch (dùng trong kiểm thử)
```
Dữ liệu chỉnh sửa được lưu theo schema (không còn snapshot `innerHTML`) và được nhúng vào file Final khi xuất, nên mở lại bằng cache trống vẫn đủ nội dung.

### Kiểm thử hồi quy
```bash
pip install playwright && python -m playwright install chromium
python -X utf8 tests/regression/run_all.py --quick   # nhanh
python -X utf8 tests/regression/run_all.py           # đầy đủ 6 viewport x 4 locale
python -X utf8 tests/regression/native_zoom.py       # zoom trình duyệt 200% (native)
```
Bộ kiểm thử chạy trên bản sao tạm của repo và server thật trỏ vào thư mục tạm; không ghi file làm việc thật.
