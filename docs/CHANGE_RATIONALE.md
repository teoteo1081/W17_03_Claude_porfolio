# Lý do thay đổi — W17_03_Claude_porfolio

Tài liệu cho Codex kiểm. Mỗi mục có: **đổi gì**, **vì sao**, **cách kiểm**. Mốc kiểm ở `docs/ANCHOR.md`.

## Bối cảnh quyết định

Đánh giá bản W17_02 theo góc nhìn "doanh nghiệp có thuê không" cho kết quả: nên mời phỏng vấn, chưa thuê ngay. Sau đó chủ hồ sơ nói mục tiêu thật là **làm freelancer**, và muốn học để lấp gap rồi tập trung vào dịch vụ làm được. Từ đó có ba nguyên tắc cho bản này:

1. **Ít dịch vụ, rõ ràng hơn nhiều dịch vụ.** Khách freelance mua một kết quả cụ thể. Bốn dịch vụ ngang hàng làm khách khó nhớ bạn bán gì.
2. **Chỉ nói điều kiểm chứng được.** Với freelancer, một câu bị phát hiện là phóng đại làm mất cả hợp đồng. Những gì chưa có bằng chứng thì hạ xuống "theo yêu cầu" hoặc bỏ.
3. **Bàn giao là thứ khách mua.** Mỗi đầu việc nói rõ khách nhận được gì.

## Vòng 2: điều chỉnh theo phản hồi của chủ hồ sơ

Sau vòng 1, chủ hồ sơ trả lời: dịch vụ là **dữ liệu**, còn digital marketing **đang học**; nhận làm website, không cam kết doanh thu; **tên công ty dùng được**; **xóa số điện thoại**; dữ liệu demo và GA4 là trang chính mình làm nên dùng được. Vòng 2 sửa lại những chỗ vòng 1 đã thận trọng hơn mức cần:

| Vòng 1 | Vòng 2 | Lý do |
|---|---|---|
| Bỏ tên Prudential, Chubb Life, AIA | Khôi phục câu gốc | Chủ hồ sơ xác nhận được dùng |
| Website là "theo yêu cầu, chưa phải dịch vụ chính" | "Nhận làm", badge `Nhận làm • Website`, không cam kết doanh thu | Chủ hồ sơ nói nhận làm được |
| Nhóm kỹ năng "Đo lường (hỗ trợ thêm)" | "Đo lường & Marketing số (đang học)"; ghi rõ không nhận chạy quảng cáo | Phản ánh đúng trạng thái đang học, không tuyên bố năng lực chưa có |
| Câu nhắc "lượng người dùng còn nhỏ, không phải kết quả cho khách" | Bỏ câu đó; ghi số liệu lấy từ chính các trang do TJ xây | Chủ hồ sơ xác nhận đó là dữ liệu của trang chính mình |
| Số điện thoại hiển thị ở hero và nhãn Zalo | Xóa dòng hero, bỏ số khỏi nhãn Zalo | Yêu cầu của chủ hồ sơ; liên kết `zalo.me` còn chứa số (xem A6) |

Những điều **vẫn giữ** từ vòng 1: bỏ các cụm "xác thực 100%", bỏ `~60%`/`500+`/`12 vùng` (chưa có bối cảnh trước/sau), bỏ tuyên bố ROAS/CPA/Ads. Lý do: chưa có ai xác nhận số liệu hoặc năng lực đó, và chủ hồ sơ cũng nói marketing đang học.

## Thay đổi theo nhóm (vòng 1, đã cập nhật theo vòng 2)

### N1. Định vị: 2 dịch vụ chính + 2 dịch vụ theo yêu cầu
- **Đổi:** `hero_title/headline`, `hero_positioning`, `hero_desc`, `eco_property`, `eco_badge_1..4`, `modal_p1..4_badge`, `modal_pkg_heading`, `modal_pkg_note`, tên dịch vụ 1 và 4 (`1. Tự động hóa Vận hành`, `4. Kiểm lỗi Đo lường`), `hero_title/hero_bio` của CV.
- **Vì sao:** Bằng chứng mạnh nhất trong repo là tự động hóa (Python, Playwright, test hồi quy, server lưu file có kiểm soát) và dashboard. Web và theo dõi GA4/GTM chưa có sản phẩm làm cho khách: dữ liệu GA4 hiện có là traffic của dự án cá nhân. "Vận hành Trọn gói A–Z" nghe như thầu toàn bộ vận hành của doanh nghiệp, quá rộng cho một người làm tự do; đổi thành "Tự động hóa Vận hành" đúng cái làm được.
- **Kiểm:** A1.

### N2. Bỏ chữ "xác thực" và nhãn chuyên gia
- **Đổi:** `hero_verified` (thành "Nhận dự án Freelance"), `hero_badge_spec`, `footer_copy`, `spoke_section_badge`, nguồn GA4 ("GA4 đã xác thực" thành "GA4 của các dự án cá nhân").
- **Vì sao:** Không có bên thứ ba nào xác thực. Người đọc có kinh nghiệm xem đây là dấu hiệu né kiểm chứng, và nó gây hại hơn là giúp.
- **Kiểm:** A2.

### N3. Tên công ty cũ (vòng 2: khôi phục)
- **Hiện trạng:** `sol_desc` giữ nguyên câu gốc nêu Prudential, Chubb Life, AIA, vì chủ hồ sơ xác nhận được dùng.
- **Còn thiếu (gợi ý, không bắt buộc):** chức danh, thời gian, phạm vi. Chỉ có tên công ty thì khách khó kiểm chứng; nên thêm khi có thể.
- **Kiểm:** A2.

### N4. Thay 3 chỉ số thành tích bằng 3 bước làm việc
- **Đổi:** `metric_val_1..3`, `metric_title_1..3`, `metric_desc_1..3` của CV. Trước: `~60%`, `500+`, `12 Vùng`. Sau: Bước 1 Khảo sát, Bước 2 Làm thử trên dữ liệu mẫu, Bước 3 Bàn giao và hướng dẫn. Đồng thời bỏ `(~60% thời gian tiết kiệm)` trong sơ đồ quy trình và `80–90%` trong mô tả dịch vụ.
- **Vì sao:** Các con số này không có mốc trước/sau, công ty, vai trò. Người đọc coi như không có, và nếu bị hỏi lại mà chưa có đáp án thì mất uy tín. Quy trình ba bước là thứ kiểm chứng được và giúp khách biết làm việc với bạn sẽ ra sao.
- **Kiểm:** A2.
- **Lưu ý:** Chủ hồ sơ có thể thêm lại từng con số **khi có đủ** (làm ở đâu, trước/sau bao lâu, mình làm phần nào). Đó là mục "case study" trong danh sách cần làm.

### N5. Rút phần quảng cáo/ROAS khỏi tuyên bố năng lực
- **Đổi:** `sol_card1_p4`, `sol_card2_p3`, `skill_grp_1` ("Đo lường (hỗ trợ thêm)"), `skill_tag_cpa`, bỏ hai tag `Google Ads & Meta Ads` và `TikTok & Zalo Ads`, thêm tag `Playwright` và `Google Sheets` vào nhóm ETL, `sol_card2_sub`, các khối demo trong modal giải pháp (`planning`, `bi`, `automation`).
- **Vì sao:** Hồ sơ vừa nói không cam kết doanh thu/lead, vừa liệt kê tối ưu ROAS/CPA/CVR và Google/Meta/TikTok Ads. Hai điều đó mâu thuẫn, và không có bằng chứng nào trong repo cho việc chạy quảng cáo. Playwright và Google Sheets thì có bằng chứng ngay trong repo và trong mô tả dịch vụ.
- **Kiểm:** A2. `CPA/EA` trong mô tả WRP Tax là "Certified Public Accountant / Enrolled Agent", không phải chỉ số quảng cáo; được giữ nguyên.

### N6. Mỗi đầu việc ghi sản phẩm bàn giao
- **Đổi:** 12 mục `modal_pN_itemM` ở 4 locale, thêm "Bàn giao: …". Số đầu việc giữ nguyên 3 mỗi dịch vụ.
- **Vì sao:** Đây là khoảng trống lớn nhất đã chỉ ra khi đánh giá: freelancer cần nói khách nhận gì, không chỉ nói mình làm gì. Chưa ghi giá và tiêu chí nghiệm thu, vì không có số liệu thật để viết (xem mục cần xác nhận).
- **Kiểm:** A4.

### N7. Nhãn dữ liệu GA4 (vòng 2: theo xác nhận của chủ hồ sơ)
- **Đổi:** `hub_title`, `hub_desc`, `pbi_source_footer`, `ga4_modal_footer_source`, `spoke_section_badge`. Số liệu không đổi.
- **Vì sao:** Bản gốc ghi "GA4 đã xác thực", nhưng không có bên thứ ba xác thực. Nay ghi đúng bản chất: GA4 của các trang do TJ xây, số liệu lấy từ chính các trang đó. Chủ hồ sơ xác nhận không có lo ngại về dữ liệu demo.
- **Lưu ý (không sửa theo yêu cầu):** 80 người dùng Mỹ chỉ tương tác trung bình 11 giây là mẫu dễ bị người biết GA4 chất vấn. Chủ hồ sơ nên chuẩn bị câu trả lời nếu bị hỏi.
- **Kiểm:** A3.

### N8. Câu mời liên hệ
- **Đổi:** `contact_section_sub`, `contact_section_desc`, `footer_title`, `footer_desc`. Không hứa thời gian phản hồi.
- **Vì sao:** Bản cũ nói về "tăng trưởng thực chất", "cơ chế khuyến khích", "marketing hiệu suất", không khớp dịch vụ mới. Câu mới mời khách mô tả việc đang làm tay, đó là cách bắt đầu một đơn hàng tự động hóa.
- **Kiểm:** đọc 4 locale.

### N9. Meta, README, khóa cache, kiểm thử
- **Đổi:** `<title>`, `meta description`, `og:*`; README; tiền tố khóa `localStorage` từ `w17_02_` sang `w17_03_`; chuỗi kỳ vọng `BADGES`, `SERVICE_TITLES` trong `tests/regression/run_all.py`.
- **Vì sao:** `meta description` của CV còn ghi "chuyển dịch sang Digital Marketing ... ROAS, CPA", mâu thuẫn định vị. Hai bản W17_02 và W17_03 nếu cùng được phục vụ từ một origin sẽ dùng chung `localStorage`; tiền tố riêng giữ nguyên nguyên tắc cách ly cache mà W17_02 đã sửa ở vòng audit F01. Kiểm thử phải đổi theo vì nó khớp đúng chuỗi cũ.
- **Kiểm:** A8, A9; `grep -rn "w17_02" .` chỉ còn trong tài liệu và ghi chú.

## Những gì cố ý KHÔNG đổi

- Số liệu GA4, dữ liệu phễu minh họa (đã được ghi rõ là dữ liệu mẫu), ảnh đại diện.
- `server.py`, `dev_server.py`, `tools/sync_creators.py` (ngoại trừ tiền tố khóa), bố cục và màu.
- Bốn ứng dụng cá nhân và đường dẫn demo/GitHub của chúng.
- Số điện thoại/Zalo và email công khai (xem dưới).

## Cần chủ hồ sơ xác nhận (Claude không tự quyết được)

1. **Thứ tự ưu tiên giữa hai dịch vụ dữ liệu.** Bản này đặt tự động hóa trước, Dashboard BI sau. Nếu thực tế ngược lại, đảo `eco_badge_*` và thứ tự thẻ.
2. **Zalo và số điện thoại.** Số đã ẩn khỏi chữ hiển thị nhưng liên kết `zalo.me/0855239805` vẫn lộ số. Muốn ẩn hẳn thì phải bỏ hoặc đổi kênh Zalo; đó là quyết định của chủ hồ sơ.
3. **Các con số cũ (60%, 500+, 12 vùng).** Có số liệu thật và được phép nêu thì đưa vào case study kèm bối cảnh, không đưa lại dạng thẻ chỉ số trần.
4. **Giá và tiêu chí nghiệm thu.** Chưa viết vì không có dữ liệu để viết; không nên bịa. Nên làm khi đã có 1–2 đơn thật.
5. **Email.** Email trên hồ sơ là `teoteo1081@gmail.com`; chủ hồ sơ nên xác nhận đúng địa chỉ.
6. **Bản dịch `es`, `zh`** do Claude viết, cần người bản ngữ rà trước khi dùng thật.

## Kết quả kiểm tra

Trạng thái khi commit (ghi thẳng, không tuyên bố PASS toàn bộ):

| Kiểm tra | Kết quả |
|---|---|
| `python tools/sync_creators.py --check` | OK cho cả hai Creator |
| `grep w17_02` trong 2 Final + 2 Creator | 0 dòng (đã đổi sang `w17_03_`) |
| Các lệnh grep ở A2 (Prudential được phép) | Không còn tuyên bố bị cấm; chỉ còn `CPA/EA` hợp lệ |
| `run_all.py --quick` | **CHƯA hoàn tất.** Các lần chạy bị hệ thống dừng vì thiếu bộ nhớ. Lần cuối chỉ đến 3 PASS (nhóm STATIC/F01) trước khi bị dừng, 0 FAIL ở phần đã chạy |
| `run_all.py` (đầy đủ), `native_zoom.py` | Chưa chạy |
| So sánh thị giác 320–1440px, zoom 200% | Chưa làm |

Một lần chạy sớm hơn (trước khi sửa vòng 2) đã báo 1 FAIL ở F05 migration. Nguyên nhân đã xác định: bài test sửa nút `hero_badge`, mà nội dung này đã đổi nên cơ chế migration (chỉ áp khi văn bản gốc khớp) từ chối đúng thiết kế; cộng thêm khóa `w17_02_` trong fixture. Đã sửa test sang nút `eco_title` (không đổi) và đổi tiền tố trong fixture, **nhưng chưa chạy lại để xác nhận**. Codex cần chạy `run_all.py` trên máy đủ bộ nhớ trước khi kết luận.

Thay đổi test ngoài chuỗi kỳ vọng: thêm `tests/fixtures/legacy_ad92e4b/` (bản Creator cũ của W17_02, đổi tiền tố khóa sang `w17_03_`) vì repo này không có lịch sử Git của W17_02; `run_all.py`/`extra_cases.py` đọc fixture thay vì `git show`.
