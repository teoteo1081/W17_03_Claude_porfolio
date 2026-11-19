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

Trạng thái khi commit (ghi thẳng, không tuyên bố một lần chạy sạch toàn bộ):

| Kiểm tra | Kết quả |
|---|---|
| `python tools/sync_creators.py --check` | OK cho cả hai Creator |
| `grep w17_02` trong 2 Final + 2 Creator | 0 dòng (đã đổi sang `w17_03_`) |
| Lệnh grep ở A2 | Không còn tuyên bố bị cấm; chỉ còn `CPA/EA` hợp lệ |
| `run_all.py --quick`, lần 1 (sau sửa vòng 2) | 35 PASS, 1 FAIL: `R3-01..05` do chuỗi ES `Landing Page` trong tên dịch vụ 3. **Đã sửa** về "Página de Aterrizaje" |
| `run_all.py --quick`, lần 2 (sau sửa ES) | 27 PASS, 4 FAIL, đều là timeout (`Page.goto` 30s, chờ `download` 8s) hoặc ghi file ở F07/F09/F10/N; R3 đã PASS. Các nhóm này PASS ở lần 1, máy đang thiếu RAM |
| `run_all.py --quick --only F07,F09,F10,N` | **11/11 PASS** (chạy riêng, máy rảnh hơn) |
| `run_all.py` (đầy đủ), `native_zoom.py` | Chưa chạy |
| So sánh thị giác 320–1440px, zoom 200% | Chưa làm |

Kết luận có giới hạn: chưa có một lượt `--quick` nào xanh toàn bộ liên tục. Các lỗi còn lại ở lần 2 giải thích được bằng timeout khi máy chậm và PASS khi chạy riêng, nhưng đó là suy luận, không phải bằng chứng. Codex nên chạy lại `run_all.py` đầy đủ trên máy rảnh RAM.

Lỗi F05 migration ở một lần chạy sớm hơn đã được xử lý: bài test sửa nút `hero_badge` (nội dung đã đổi nên migration từ chối đúng thiết kế) nay sửa nút `eco_title` (không đổi), và fixture Creator cũ đổi tiền tố khóa sang `w17_03_`; F05 PASS ở lần 1.

Thay đổi test ngoài chuỗi kỳ vọng: thêm `tests/fixtures/legacy_ad92e4b/` (bản Creator cũ của W17_02, đổi tiền tố khóa) vì repo này không có lịch sử Git của W17_02; `run_all.py`/`extra_cases.py` đọc fixture thay vì `git show`.

Ghi chú công cụ: Codex CLI không chạy được test trên ổ mạng (`CreateProcessWithLogonW failed: 267`, thư mục UNC), nên test được chạy bởi Claude.


## Vòng 3: rà soát theo yêu cầu của chủ hồ sơ (2026-11-18)

Chủ hồ sơ yêu cầu: số liệu hiển thị đúng bản chất, nhận freelance và remote cho thị trường nước ngoài, bỏ chữ khó hiểu ("Hồ sơ trình diễn", "CV Interactive"). Vòng này **thay đổi một phần phạm vi cũ** (trước đây "số liệu GA4 không đổi"); quyết định mới của chủ hồ sơ thay thế.

| Đổi | Vì sao |
|---|---|
| Bỏ biểu đồ xu hướng theo ngày, tab 3 trong popup, bộ chọn 7 ngày, thư viện Chart.js | Chuỗi số theo ngày không có nguồn trong `ga4_metrics_live.json`. Cộng 28 ngày ra 1.684 nhưng 7 ngày cuối ra 388 (thẻ 7 ngày ghi 269); Mỹ + Việt Nam không bằng "Tất cả" theo từng ngày; Mỹ cộng ra 332 lượt xem (thẻ ghi 312), Việt Nam 1.226 (thẻ ghi 1.245). Số "14m 15s" và "1.840 sự kiện" của 7 ngày cũng không có nguồn, còn script ghi "5,000+ sự kiện" cho cùng 7 ngày |
| Thêm khối "Cách đọc số liệu" | Hoa Kỳ có 80 người dùng nhưng 41 phiên (người dùng nhiều hơn phiên là bất thường) và 11 giây mỗi người dùng; ghi rõ chưa lọc, 174 người dùng không phải quy mô khán giả thật |
| Bỏ mũi tên ▲ ở "163 người dùng mới", bỏ emoji trang trí, đổi nhãn thẻ thứ 3 thành "Tương tác TB / người dùng" | ▲ gợi ý tăng trưởng nhưng không có kỳ so sánh |
| Sửa 21,46 thành 21,47 lượt xem/người dùng của Việt Nam | 1.245 / 58 = 21,4655 |
| Chân bảng quốc gia ghi "Top 10: 168/174 người dùng, 10.229/10.465 sự kiện" | Phép cộng 10 dòng ra 168 và 10.229, không phải tổng toàn bộ |
| Bỏ "Power BI Telemetry", "TRỰC TIẾP", "Đồng bộ BigQuery", mã project GCP; ghi "cập nhật thủ công, không phải thời gian thực" | Trang dựng bằng Tailwind, không phải Power BI; số liệu là ảnh chụp, không có kết nối trực tiếp |
| Ngày ghi cố định (14/10 – 10/11/2026) thay cho "28 ngày qua" | "Qua" sai khi số liệu đã cũ |
| `brand_tag`: "Portfolio" (bỏ "Hồ sơ trình diễn (V3)"); CV: bỏ "Tương tác", "Interactive", "V3" | Khách không cần biết số phiên bản nội bộ; "trình diễn" khó hiểu |
| `hero_badge`: "Nhận dự án freelance & remote"; bỏ "(Freelance)" lặp ở định vị | Nhận freelance và remote; badge ngay phía trên đã nói |
| `hero_desc` viết lại: nêu việc làm, remote, bàn giao file chạy được kèm hướng dẫn; giữ "không chạy quảng cáo, không cam kết KPI doanh số" ở cuối; bỏ câu "Digital Marketing đang học" khỏi hero | Câu đang học làm yếu phần chào chính; trạng thái đang học vẫn còn ở `eco_property`, `skill_grp_1`, `modal_pkg_note` |
| `hero_title` về chữ thường theo câu, thêm dấu phẩy | Viết hoa mỗi chữ là kiểu tiếng Anh |
| Nút CV: "Xem CV & hồ sơ năng lực", bỏ ↗ (link mở cùng tab) | ↗ báo hiệu mở tab mới nhưng link không mở tab mới |

Anchor đã đổi: A1 và A5 không còn đòi `hero_desc` chứa chữ "đang học" (vẫn đòi "không cam kết"); A3 chỉ còn đúng với các con số **174 / 1.684 / 10.465** và bảng quốc gia/trang; chuỗi số theo ngày và số liệu 7 ngày đã gỡ.

**Chưa đối soát với GA4 thật (máy này không có thông tin đăng nhập BigQuery):** tất cả số 28 ngày (người dùng, phiên, sự kiện, bảng quốc gia/trang) và lượt xem theo quốc gia (312 Mỹ, 1.245 Việt Nam) lấy từ `ga4_metrics_live.json`, chưa so lại với giao diện GA4. Chủ hồ sơ nên mở GA4 so một lần.

**Kết quả kiểm tra (2026-11-18):** `sync_creators.py --check` OK; `run_all.py --quick` chạy theo ba lượt vì lượt đầu bị đóng trình duyệt thử khi hết thời gian: F01–F05, F03, F08, STATIC PASS; R3, CONTENT, NAV, SAFETY 8/8 PASS; F07, F09, F10, N, RESP 13/13 PASS. Đã chụp màn hình 1440px và 390px (hero, dashboard) và xem bằng mắt; không có lỗi console. `run_all.py` đầy đủ, `native_zoom.py`, ảnh chụp 320/768/1024px chưa chạy. Bản dịch es và zh của chuỗi mới do Claude viết, chưa có người bản ngữ rà.


### Vòng 3b (2026-11-19): quyết định thêm của chủ hồ sơ

| Đổi | Vì sao |
|---|---|
| Ngôn ngữ mặc định lấy theo trình duyệt (vi/en/es/zh; ngôn ngữ khác dùng en); lựa chọn đã lưu luôn được ưu tiên. Áp dụng cho trang chính và CV | Chủ hồ sơ nhắm thị trường nước ngoài; trước đây khách nào cũng thấy tiếng Việt trước |
| Bộ kiểm thử: mọi `new_context` đặt `locale="vi-VN"`; thêm test R3-09 cho ngôn ngữ mặc định | Các test cũ giả định trang mở bằng tiếng Việt; trình duyệt thử mặc định là en-US |
| CV `pill_lang`: "TOEIC ~700+" → "Business English" (es "Inglés de negocios", zh "商务英语") | Chủ hồ sơ chọn; "~700+" nghe thiếu chắc chắn. Không ghi điểm vì không có chứng chỉ kèm theo |
| CV `hero_bio` viết lại giống trang chính; bỏ "(Freelance)" lặp ở `hero_title`; "Xem GitHub"; sửa "gởi" → "gửi" | Đồng bộ với trang chính |
| Khối mô phỏng phễu: nhãn "Dữ liệu mẫu • Mô phỏng"; chú thích nói rõ toàn bộ số là dữ liệu mẫu, không phải kết quả của khách nào (chữ lớn hơn, màu amber) | ROI 3.4x, +24.8%, 78.4% là số minh họa nhưng trước chỉ có một dòng chữ nhỏ |
| Phần trăm trong bảng GA4 dùng dấu phẩy ở vi/es | Thống nhất với các số khác (9,68; 93,7%) |

**Chủ hồ sơ giữ nguyên (không sửa):** chữ "Hệ sinh thái"; trong CV, "Power BI (Nâng cao)" và "Báo cáo thời gian thực". Đây là lời tự nhận của chủ hồ sơ; Claude không kiểm chứng.

**Kết quả kiểm tra (2026-11-19):** `sync_creators.py --check` OK. `run_all.py --quick` chạy theo nhóm: STATIC, F01, F02, F04, F05, F06, F08, R3 (gồm R3-09), CONTENT, NAV 22/22 PASS; F03 và F09 PASS (lượt đó bị lệnh `timeout` cắt sau F09); F07, F10, N, RESP 11/11 PASS khi chạy riêng. Ảnh chụp: trang chính và CV với trình duyệt en-US và vi-VN, không lỗi console.


### Vòng 3c (2026-11-19): editor đơn giản — mở, sửa, lưu & đăng lên web

Chủ hồ sơ thấy editor phức tạp và "sửa xong lại quay về như cũ". Nguyên nhân (đọc từ mã): chữ sửa chỉ nằm trong bộ nhớ trình duyệt; trang Final cùng trình duyệt cũng đọc bộ nhớ đó nên tưởng đã lưu; nút Lưu chỉ ghi vào thư mục khi mở qua `dev_server.py`; web thật chỉ đổi khi commit + push; file editor không được sinh lại sau khi lưu.

| Đổi | Vì sao |
|---|---|
| `MO_EDITOR.bat` + `dev_server.py --open` (tự mở editor, tự đổi cổng nếu bận, mở lại nếu máy chủ của thư mục này đang chạy) | Một cú bấm đúp, không phải gõ lệnh |
| `/api/save` sinh lại file Creator từ Final vừa lưu (`tools/sync_creators.py` có `creator_for(root)`) | Lần mở editor sau là bản vừa lưu |
| `/api/publish`: commit đúng 4 file trang (`--only`), push `main`; không force, không tự gộp; remote mới hơn/sai nhánh/không có Git → lỗi rõ | Đăng lên web từ nút bấm, an toàn |
| Nút **🚀 Lưu & đăng lên web** (lưu → đăng → dọn nháp → tải lại editor, hiện kết quả); nút cũ đổi tên **💾 Chỉ lưu vào máy** (giữ hành vi cũ) | Luồng một nút cho người không rành kỹ thuật |
| Web công khai (không phải localhost/file) không đọc bản nháp trong trình duyệt; editor ở đó hiện dòng nhắc "bản xem thử" và nút đăng chỉ nhắc mở bằng `MO_EDITOR.bat` | Thứ thấy trên web luôn là thứ đã đăng |
| Editor mở tiếng Việt khi chưa chọn ngôn ngữ (trang Final vẫn theo trình duyệt) | Tránh sửa nhầm bản tiếng Anh |
| File lưu ra luôn ở dạng chuẩn: chữ tĩnh tiếng Việt, `<html lang="vi" class="dark scroll-smooth">` dù đang xem EN/giao diện sáng | Giữ khung xem trước tiếng Việt; công cụ sinh Creator không lỗi |
| Bỏ khối `<style>` Tailwind CDN tự chèn khỏi file lưu | Lỗi có từ trước: mỗi lần lưu file phình ~38KB (đo được 238KB → 329 → 367 → 405KB) |

**Kiểm tra (2026-11-19):** R4-01..04 PASS (lưu sinh lại Creator; publish với remote Git trần tạm; web công khai không hiện nháp; chạy thật trên giao diện 2 vòng liên tiếp, không phình file). Các nhóm cũ: STATIC…NAV 22/22, F03+F09 6/6, F10/N/RESP 9/9 PASS; F07 lần đầu quá thời gian chờ 8s khi chạy chung nhóm, chạy lại riêng 3/3 PASS. Chưa có test giao diện end-to-end cho nút đăng ở trang CV (CV được kiểm ở R4-01 và R4-03).
