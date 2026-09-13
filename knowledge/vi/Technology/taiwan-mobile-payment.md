---
title: 'Thanh toán di động tại Đài Loan: Tại sao dù điện thoại có nhiều loại thanh toán, người ta vẫn mang theo tiền mặt khi ra ngoài?'
description: 'Trong mẫu khảo sát trực tuyến của MIC (Hiệp hội Nghiên cứu Kinh tế) quý III năm 2024, 92% đã từng sử dụng và 84% thường xuyên dùng thanh toán di động. Tuy nhiên, một cuộc điều tra quốc gia khác của Ngân hàng Trung ương lại cho thấy 73.8% người trưởng thành vẫn kết hợp dùng tiền mặt và phi tiền mặt. Bài viết này phân tích các công cụ, hợp đồng và quy trình xác nhận khác nhau đằng sau thanh toán bằng điện thoại, trả lời tại sao sự phổ biến cao chưa đủ để loại bỏ tiền mặt, và chỉ ra những gì TWQR đã giải quyết cũng như những trường hợp ngoại lệ còn tồn tại.'
date: 2026-09-01
category: 'Technology'
tags:
  [
    'Thanh toán di động',
    'Thanh toán điện tử',
    'TWQR',
    'Taiwan Pay',
    'Mã QR',
    'Tiền mặt',
    'Công nghệ tài chính',
  ]
subcategory: '數位與網路'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-09-01
lastHumanReview: false
researchReport: 'reports/research/2026-09/台灣行動支付.md'
image: '/article-images/technology/taiwan-mobile-payments-merchant-2026.webp'
imageCredit: '財金資訊股份有限公司（TWQR 官方網站）'
imageLicense: 'Fair use editorial commentary'
imageSource: 'https://www.twqr.com.tw/'
translatedFrom: 'Technology/台灣行動支付.md'
sourceCommitSha: '574b1a339'
sourceContentHash: 'sha256:1e2fca6dab4c2f1c'
sourceBodyHash: 'sha256:62d9c6127e29bebe'
translatedAt: '2026-09-13T00:44:02+08:00'
---

# Thanh toán di động tại Đài Loan: Tại sao dù điện thoại có nhiều loại thanh toán, người ta vẫn mang theo tiền mặt khi ra ngoài?

![Ảnh cửa hàng trong cuộc phỏng vấn chính thức TWQR](/article-images/technology/taiwan-mobile-payments-merchant-2026.webp)
_Ảnh minh họa từ cuộc phỏng vấn chính thức của các đối tác TWQR, chỉ dùng để phân tích tài liệu tuyên truyền hệ thống. Hình ảnh chỉ đại diện cho cửa hàng được phỏng vấn và không thể là bằng chứng thực địa độc lập về tình hình áp dụng tại các cửa hàng nhỏ trên toàn đảo. Ảnh: Công ty Thông tin Tài chính (Trang web chính thức TWQR), sử dụng hợp lý trong bài bình luận._

> **Tóm tắt 30 giây:** Trong mẫu khảo sát trực tuyến quý III năm 2024 của MIC, 92% đã từng dùng thanh toán di động. Tuy nhiên, một cuộc điều tra do Ngân hàng Trung ương ủy thác lại cho thấy 73.8% người trưởng thành vẫn sử dụng cả tiền mặt và phi tiền mặt. Hai bộ số liệu này đến từ các mẫu và câu hỏi khác nhau, nhưng chúng đều chỉ ra cùng một vấn đề: việc thanh toán bằng điện thoại, khả năng giao dịch ở nhiều nơi, và sự an tâm không cần mang theo tiền mặt là ba rào cản khác biệt. Nhiều ứng dụng đôi khi bù đắp thiếu sót về kênh, đôi khi cung cấp chức năng phản hồi và thành viên. TWQR đang tích hợp Mã QR chung, nhưng vẫn chưa tổng hợp được tất cả các nguồn vốn, hợp đồng cửa hàng và tình huống lỗi thành một loại thanh toán duy nhất.

Vào tháng 9 năm 2025, nhà phân tích ngành kỳ cựu Hồ TựLập (Hu Zili) của MIC đã công bố một cuộc khảo sát người tiêu dùng về thanh toán di động. Ông quan sát thấy, những người dùng tích cực cài đặt hơn năm công cụ "chủ yếu là để sử dụng thanh toán di động ở các kênh khác nhau".[^1] Câu nói này rất giống với hành động mà nhiều người đã làm trước quầy thu ngân: nhìn xem trên cửa kính hoặc quầy có logo nào, rồi quyết định mở ứng dụng nào. Nếu không tìm thấy biểu tượng quen thuộc, họ mới ngẩng đầu hỏi một câu: "Ở đây nhận loại nào?".

Tùy chọn trong điện thoại ngày càng nhiều, nhưng ví tiền vẫn còn vài tờ tiền giấy. Bức tranh song hành này dễ bị hiểu là thị trường thanh toán Đài Loan quá phân mảnh, hoặc cũng dễ bị cho là sự lựa chọn ưu đãi đơn thuần. Hai cách giải thích đều nắm bắt được một phần vấn đề. Sự ma sát về hệ thống chấp nhận và tương thông thực sự khiến người ta cài nhiều công cụ và giữ lại tiền mặt; các yếu tố như phản hồi, thành viên, chuyển khoản, thói quen, sở thích cá nhân và dự phòng lỗi cũng cùng tác động. Để nhìn rõ vấn đề này, cần phải tách ba rào cản ra: liệu con người có áp dụng hay không, giao dịch có thể dùng chung qua nhiều kịch bản hay không, và khi giao dịch thất bại thì có thể khôi phục để người dùng dám để lại tờ tiền cuối cùng ở nhà hay không.

## Thanh toán bằng điện thoại không có nghĩa là chỉ cần mang điện thoại là đủ

Tỷ lệ 92% "đã từng sử dụng" và 84% "thường xuyên sử dụng" do MIC công bố, dựa trên mẫu khảo sát trực tuyến kéo dài hai tháng trong quý III năm 2024. Trang công khai không liệt kê đầy đủ khung mẫu, phạm vi tuổi tác và phương pháp trọng số hóa, vì vậy hai tỷ lệ này chỉ mô tả mẫu khảo sát đó chứ không thể được coi là tỷ lệ phổ biến của toàn bộ dân số Đài Loan.[^2] Ngay cả khi giữ lại giới hạn này, nó vẫn cho thấy trong nhóm người tiêu dùng điền vào bảng câu hỏi trực tuyến, thanh toán bằng điện thoại đã vượt qua giai đoạn công nghệ xa lạ.

Một cuộc điều tra khác do Ngân hàng Trung ương ủy thác Viện Nghiên cứu Kinh tế Đài Loan thực hiện, hỏi về cách thức sử dụng tiền mặt và phi tiền mặt hàng ngày của người dân từ 18 tuổi trở lên. Cuộc khảo sát chủ yếu dựa trên phương ngữ địa phương, điện thoại di động và bổ sung bằng internet, bao gồm 22 thành phố, và được trọng số hóa theo cơ cấu dân số, với mẫu hiệu quả là 4.234 phiếu. Kết quả cho thấy 73.8% sử dụng đồng thời tiền mặt và phi tiền mặt, 25% chỉ dùng tiền mặt, và chỉ 1.2% chỉ dùng phi tiền mặt.[^3] Ở đây, "phi tiền mặt" còn bao gồm thẻ tín dụng, thẻ tài chính và thẻ nạp tiền, không thể dùng để đo thị phần thanh toán di động, nhưng rất phù hợp để mô tả hình dáng ví tiền ngày nay.

```tw-waffle
Sử dụng hỗn hợp là thói quen của đa số (%)
Dùng cả tiền mặt và phi tiền mặt | 73.8
Chỉ dùng tiền mặt | 25
Chỉ dùng phi tiền mặt | 1.2
Nguồn: Khảo sát công cụ thanh toán ủy thác của Ngân hàng Trung ương, công bố năm 2024
```

Do đó, việc một người sử dụng cảm ứng điện thoại tại quán cà phê chuỗi vào buổi sáng, quét mã để tích điểm vào bữa trưa, và chuyển sang trả tiền mặt ở chợ vào buổi tối không hề mâu thuẫn. Người này đã vượt qua rào cản đầu tiên là "con người có dùng", nhưng vẫn phải thay đổi công cụ tùy theo địa điểm, cửa hàng và thiết bị. Cụm từ "vẫn mang theo tiền mặt" trong tiêu đề chỉ có thể được hiểu là sự dự phòng ở quy mô lớn, chứ không thể mở rộng thành một điều cần thiết đối với mọi người Đài Loan mỗi ngày.

Thói quen thanh toán đã thay đổi, nhưng các trường hợp ngoại lệ vẫn còn trên đường. Việc cài thêm vài ứng dụng dường như có thể bù đắp từng ngoại lệ, nhưng để hiểu tại sao nó có thể bù đắp, trước hết phải thừa nhận rằng những ứng dụng đó không phải là một thứ duy nhất. Khoảnh khắc mở điện thoại rất giống nhau, nhưng con đường giao dịch đi tiếp sau đó có thể hoàn toàn khác biệt.

## Nhiều ứng dụng trông như đang thanh toán, nhưng chúng lại đi trên các con đường khác nhau

Bộ Giáo dục Tài chính (Jinbanhui) phân loại thanh toán di động theo công cụ liên kết, công nghệ và quy định áp dụng thành: thẻ tín dụng di động, thẻ tài chính di động, quét mã QR, tổ chức thanh toán điện tử và phiếu điện tử.[^4]

Hành động người tiêu dùng thực hiện ở giao diện trước có thể chỉ là một lần chạm, một lần quét, hoặc một lần xác nhận, nhưng ở hậu trường, nó có thể được hoàn thành bởi các công cụ liên kết khác nhau, công nghệ khác nhau, đầu cuối nhận tiền và quy tắc khác nhau. Cùng thanh toán trên điện thoại, có cái sử dụng thẻ liên kết, có cái sử dụng tài khoản thanh toán điện tử. Đầu cuối nhận tiền và thông số kỹ thuật mà cửa hàng chấp nhận sẽ quyết định những sự kết hợp nào có thể dùng được. Do đó, LINE Pay, Street, Apple Pay, AllPay và Taiwan Pay không thể chỉ xếp logo thành năm chiếc ví đồng nhất. Một số cạnh tranh lẫn nhau, một số hợp tác phân tầng trong cùng một giao dịch, và một số bù đắp cho nhau ở các kênh khác nhau.

Để xem các nền tảng như PChome, Shopee và Coupang đã thay đổi kịch bản mua sắm trực tuyến như thế nào, có thể đọc thêm [Hệ sinh thái Thương mại điện tử và Thanh toán Kỹ thuật số Đài Loan](/vi/technology/e-commerce-and-digital-payment-ecosystem). Bài viết này chỉ dừng lại ở chặng cuối của thanh toán tại cửa hàng thực tế.

Vì vậy, việc một thương hiệu tồn tại trong điện thoại chỉ trả lời được liệu phía người dùng có nhận được công cụ hay không, chứ không thể trực tiếp trả lời liệu cửa hàng có chấp nhận đầu cuối tương thích hay không. Việc nhìn thấy cùng một Mã QR cũng không có nghĩa là mọi ứng dụng, hướng quét và nguồn vốn đều có thể hoàn thành giao dịch. Từ biểu tượng trên điện thoại nhảy thẳng đến "toàn đảo sử dụng được" đã bỏ qua ít nhất ba tầng: công cụ liên kết, hợp đồng cửa hàng và thông số kỹ thuật giao dịch.

Số lượng ứng dụng cũng cần phải điều chỉnh lại con số phóng đại là "trung bình năm loại". Mẫu khảo sát trực tuyến của MIC năm 2024 cho thấy 86% sử dụng dưới năm loại, trong đó 61% sử dụng ba loại trở xuống, và 14% sử dụng sáu loại trở lên. Dữ liệu công khai không có giá trị trung bình hay trung vị, cũng không có phân bố đầy đủ của một đến năm loại.[^5] Nó hỗ trợ việc sử dụng đa ứng dụng, nhưng không thể tạo ra một "người dùng điển hình" chính xác là năm loại.

Bảng tháng 6 năm 2026 của Bộ Giáo dục Tài chính tổng hợp số lượng tổ chức thanh toán điện tử được báo cáo lên thành 41,129,000. Đây là tổng cộng các tổ chức, chứ không phải số người dùng đã khử trùng lặp qua nhiều tổ chức. Nó đo lường một ảnh chụp nhanh về hợp đồng, chứ không thể trả lời được một người dùng điển hình cài bao nhiêu công cụ.

> **📝 Ghi chú của Biên tập viên**
> Logo trên quầy là thương hiệu, giao diện hiển thị trong điện thoại là giao diện, còn số liệu tích lũy trong bảng của Bộ Giáo dục Tài chính là các hợp đồng tài khoản chưa kết thúc. Nếu gọi cả ba thứ này thành một loại "số lượng người dùng", chúng ta sẽ làm phẳng tầng bậc quan trọng nhất của thị trường thanh toán.

Giao diện trước có vẻ giống nhau, nhưng khi giao dịch đi đến đầu kia, sự khác biệt mới hiện ra. Người dùng tải bao nhiêu ứng dụng cũng không thể thay cửa hàng hoàn thành đăng ký, xác nhận và đối soát. Rào cản thứ hai nằm ở phía sau quầy.

## Người tiêu dùng thấy một lần quét mã, còn cửa hàng phải kết nối toàn bộ quy trình

Một cửa hàng muốn chấp nhận Taiwan Pay trước tiên phải nộp đơn xin trở thành cửa hàng đặc biệt đã ký hợp đồng với tổ chức tài chính nhận thanh toán, lấy mã ngân hàng nhận tiền, mã cửa hàng đặc biệt và mã thiết bị đầu cuối, sau đó hoàn thành đăng ký dịch vụ.[^7] Sau khi bắt đầu nhận thanh toán, thiết bị và mạng phải hoạt động, nhân viên cần biết cách xác nhận thông báo, xử lý hoàn tiền, và hậu trường phải hoàn thành đối soát và chuyển tiền. Đối với các cửa hàng nhỏ, việc dán mã nhận tiền chỉ là khởi đầu, phía sau nó là một quy trình vận hành bắt buộc phải kết thúc mỗi ngày.

Các câu hỏi thường gặp về Taiwan Pay mô tả rất cụ thể khoảnh khắc dễ bị che khuất bởi một Mã QR: khi thiết bị ngoại tuyến, cửa hàng vẫn có thể tạo ra Mã QR không kèm số tiền trên trang đăng nhập để người tiêu dùng quét mã, nhưng điện thoại của cửa hàng lại không nhận được thông báo giao dịch.[^8] Giao diện khách hàng hiển thị đã thanh toán, nhưng đầu cuối nhận tiền tạm thời thiếu thông báo, quầy thu ngân phải quyết định có cho hàng hay không và tra cứu giao dịch này ở đâu. Quét mã chỉ là điểm khởi đầu của hành động, việc xác nhận tại chỗ và đối soát sau đó mới khiến giao dịch thực sự thành công.

Taiwan Pay quy định phí giao dịch theo hợp đồng giữa cửa hàng và ngân hàng nhận tiền, giải thích chính thức là "phí xử lý giao dịch được thỏa thuận bởi cả hai bên: cửa hàng (người nhận) và ngân hàng nhận tiền". Các phương án công khai của các nền tảng khác, sự thương lượng của chuỗi cửa hàng và các nguồn thanh toán khác nhau đều có điều kiện riêng.[^9] Phí dịch vụ sẽ nằm trong quyết định của cửa hàng, thời gian chuyển tiền, hoàn tiền, mạng, thiết bị, đối tượng khách hàng, học hỏi và đối soát cũng sẽ được đưa vào.

Nghiên cứu học thuật về các cửa hàng ở khu thương mại Đài Nam thậm chí còn phát hiện ra mối tương quan thuận giữa tính hữu dụng cảm nhận, tính dễ sử dụng, sự chấp nhận của người tiêu dùng và khả năng tương thích, trong khi chi phí cảm nhận không có mối quan hệ đáng kể trong mẫu đó.[^10] Điều này cũng cho thấy cửa hàng không chỉ gánh chịu chi phí, mà còn đánh giá công cụ có tốt hay không, khách hàng đã áp dụng chưa. Nghiên cứu địa phương này không thể ngoại suy ra toàn đảo, nhưng đủ để ngăn chặn cách giải thích đơn lẻ rằng "cửa hàng không nhận vì sợ mất phí".

Cuộc điều tra ủy thác của Ngân hàng Trung ương đã đưa ra quy mô khác biệt về sự chấp nhận. Trong 611 mẫu người bán hàng rong, 76.1% chỉ nhận tiền mặt. Trong 1.436 mẫu cửa hàng, tỷ lệ này là 46.8%. Báo cáo liên kết tỷ lệ cao hơn của người bán hàng rong với địa điểm, thiết bị và quy mô.[^11] "Chỉ nhận tiền mặt" ở đây tương đối so với tất cả các công cụ phi tiền mặt, không thể suy ngược thành tỷ lệ chấp nhận thanh toán di động, cũng không thể dùng để chỉ trích người bán hàng rong thiếu ý chí tiến bộ.

```tw-bars
Điều kiện chấp nhận tại quầy và cửa hàng (Chỉ nhận tiền mặt, %)
Mẫu người bán hàng rong | 76.1 | 611 phiếu
Mẫu cửa hàng | 46.8 | 1,436 phiếu
Nguồn: Khảo sát công cụ thanh toán ủy thác của Ngân hàng Trung ương, công bố năm 2024
```

Tính phổ quát của việc thanh toán phải được hoàn thành bởi cả hai phía: người tiêu dùng có công cụ, và cửa hàng cũng có quy trình để tiếp tục nhận tiền, xác nhận, hoàn tiền và đối soát. Sự ma sát về hệ thống đến đây đã có hình dáng, nhưng nó chỉ giải thích một phần sự tồn tại song song của nhiều ứng dụng và tiền mặt. Ứng dụng tiếp theo đôi khi là phương án dự phòng, đôi khi giống như một thẻ thành viên hơn.

## Cài thêm một ứng dụng, đôi khi để sử dụng, đôi khi chỉ muốn tốt hơn

Khi hỏi về những khó khăn trong việc sử dụng thanh toán di động, 18.9% chọn cửa hàng không chấp nhận, 12.0% chọn cửa hàng không chấp nhận công cụ quen dùng, và 7.6% mới là do quá nhiều loại trên thị trường. Tín hiệu mạng kém chiếm 6.5%, hết pin điện thoại chiếm 3.4%.[^12] Đây đều là tự báo cáo đa lựa chọn, không thể được coi là tỷ lệ nhân quả của từng yếu tố gây ra giao dịch bằng tiền mặt, nhưng nó cho thấy thực sự có sự chênh lệch giữa "có ứng dụng" và "ứng dụng này trên tay có thể dùng".

"Các kênh khác nhau" mà Hồ TựLập đề cập, hoàn toàn tương ứng với động cơ bù đắp này. Một cửa hàng không nhận công cụ quen dùng, người dùng có thể cài thêm một loại. Khi tụ tập bạn bè cần chia hóa đơn, hoặc gia đình muốn chuyển tặng điểm thưởng, họ cũng có thể giữ lại một loại khác. Nghiên cứu cùng loạt của MIC chỉ ra rằng 57% người dùng đã sử dụng các dịch vụ tài chính ngoài tiêu dùng, phổ biến nhất là chuyển khoản và chuyển tặng điểm thưởng, chiếm 38%.[^13] Những chức năng này đưa ứng dụng thanh toán vào cuộc sống xã hội và thành viên, lý do sở hữu đã vượt ra ngoài khả năng quét của quầy thu ngân.

Trong nghiên cứu liên vùng mà Visa ủy thác năm 2022, họ phỏng vấn 1.000 người Đài Loan trong độ tuổi từ 18 đến 55, trong đó 40% thường xuyên theo dõi điểm thưởng tiêu dùng, và 22% tính toán kỹ lưỡng vì phần thưởng tốt nhất.[^14] Dữ liệu này không thể ước tính "bao nhiêu người cài thêm ứng dụng vì phần thưởng", mà chỉ cho thấy một số người được phỏng vấn sẽ theo dõi điểm thưởng và tính toán ưu đãi. Hệ sinh thái thành viên bán lẻ cũng tạo ra công cụ thanh toán của riêng mình. Để xem cách Wanhua (Juanlian) chuyển từ mạng lưới cửa hàng và quản lý thành viên sang nền tảng sống tần suất cao, có thể tham khảo [Trung tâm Phúc lợi Juanlian](/vi/economy/pxmart-supermarket), bài viết này không tái hiện lịch sử doanh nghiệp và tranh cãi.

Cuộc điều tra của Bộ Kinh tế về ngành bán lẻ cung cấp một sự thay đổi dài hơn. Tính theo số tiền thanh toán trong mẫu trả lại, tỷ trọng người tiêu dùng sử dụng thanh toán di động đã tăng từ 0.6% năm 2017 lên 11.2% năm 2023, trong khi tiền mặt giảm từ 41.1% xuống 23.0%. Cơ quan chính thức cho rằng sự thay đổi của ngành bán lẻ hàng hóa tổng hợp và mỹ phẩm một phần là do hệ sinh thái thành viên và công cụ thanh toán tự xây dựng bởi doanh nghiệp.[^15] Tỷ trọng thanh toán di động tăng lên, trong khi tỷ trọng tiền mặt giảm. Sự cạnh tranh đa thương hiệu cũng thực sự tạo ra lựa chọn. Nếu chỉ chẩn đoán nhiều ứng dụng là sự thất bại của hệ thống, thì quỹ đạo tăng trưởng này và sở thích chủ động của người dùng đều bị bỏ qua.

```tw-slope
Tỷ trọng giá trị thanh toán bán lẻ: Thanh toán di động tăng, tiền mặt giảm (%)
2017 | 2023
*Thanh toán di động | 0.6 | 11.2
Tiền mặt | 41.1 | 23.0
Nguồn: Cục Thống kê Kinh tế, Khảo sát tình hình kinh doanh bán buôn, bán lẻ và ăn uống
```

Các công cụ đa dạng đóng hai vai trò: một là bù đắp thiếu sót về sự chấp nhận và nguồn vốn, hai là mang theo chiết khấu, điểm thưởng, thành viên và chuyển khoản. Số lượng ứng dụng tự nó không thể đo lường được khoảng cách của sự phổ biến, tính phổ quát hay việc không cần tiền mặt. Khi cạnh tranh và bù đắp rối rắm lại với nhau, vấn đề nằm ở mức độ tích hợp đã đạt được.

## TWQR tích hợp Mã QR chung, nhưng chưa tổng hợp tất cả thanh toán thành một

TWQR là phản ứng thực tế đối với "quá nhiều thông số thanh toán, quá nhiều biển hiệu cửa hàng". Bộ tiêu chuẩn Mã QR chung này kết nối các tổ chức tài chính và tổ chức thanh toán điện tử tham gia. Đến cuối năm 2025, dữ liệu của Ngân hàng Trung ương liệt kê 44 tổ chức tài chính, 10 tổ chức thanh toán điện tử và 678.000 cửa hàng đặc biệt hợp tác. Trong năm 2025, tổng giao dịch là 146,73 triệu, trị giá 713.6 tỷ Đài tệ.[^16] "Thanh toán QR Đài Loan hoàn toàn không tương thông" đã không còn phù hợp với thực tế.

![Hình minh họa hệ thống thanh toán đa dạng của TWQR](/article-images/technology/taiwan-mobile-payments-single-contract-2026.webp)
_Tài liệu tuyên truyền chính thức về "Một hợp đồng, thanh toán đa dạng" của TWQR, thể hiện phương thức kết nối cửa hàng do công ty tài chính chủ trương. Đây là hình ảnh tuyên truyền hệ thống, không thể chứng minh độc lập rằng mỗi cửa hàng hợp tác đều hoạt động, mỗi giao dịch thành công hoặc tất cả các nguồn thanh toán đều tương thông._

Mã QR chung đã giải quyết một tầng quan trọng, nhưng trang nhận tiền của tổ chức tài chính hợp tác cũng cho thấy ranh giới vẫn còn. Danh sách "Quét chính" trên trang liệt kê 11 loại công cụ như Taiwan Pay, Street, AllPay, EasyPay, iCard. Danh sách "Được quét" thì ngắn hơn và bị giới hạn bởi thông số QR Auth. AllPay, EasyCard và AllingPay xuất hiện trong danh sách quét chính, nhưng không có trong danh sách được quét của trang đó.[^17] Hướng quét, thông số kỹ thuật và sự tham gia của tổ chức sẽ thay đổi các sự kết hợp khả dụng, và cửa hàng vẫn phải nộp đơn xin TWQR với tổ chức nhận tiền.

678.000 là số lượng cửa hàng đặc biệt hợp tác, dữ liệu công khai này của Ngân hàng Trung ương không cung cấp bao nhiêu cửa hàng hoạt động liên tục, cũng như tỷ lệ thị trường toàn bộ và tỷ lệ thành công tại chỗ. Mã QR chung cũng không tự động thống nhất các nguồn vốn như thẻ tín dụng hoặc tài khoản, điểm thưởng thành viên, phản hồi, hợp đồng cửa hàng, phí dịch vụ và quy trình hoàn tiền. Nó đưa biển hiệu và thông số kỹ thuật về cùng một tầng, chứ không xóa nhòa toàn bộ thế giới thương mại của mỗi ứng dụng.

> **📝 Ghi chú của Biên tập viên**
> Thành tựu đáng nhận biết nhất của TWQR nằm trong phạm vi "chung": Mã QR chung và thông báo liên cơ quan đã tạo thành một nền tảng quy mô lớn, nhưng việc sử dụng hàng ngày của các cửa hàng hợp tác, mỗi nguồn vốn và mỗi bộ quy tắc thành viên vẫn do các tầng khác quyết định. Tính phổ quát đang được xây dựng từng lớp một.

Rào cản tương thông đã tiến lên phía trước, nhưng số lượng cửa hàng hợp tác sẽ không tự động trở thành thứ mà mọi người, mọi giao dịch, mọi nguồn vốn đều có thể sử dụng. Khi công trình tích hợp vẫn đang trên đường, việc giữ lại tiền mặt lại có một lời giải thích khác.

## Tiền mặt không chứng minh thanh toán di động thất bại, nó thường không cần hỏi trước xem có dùng được hay không

Khả năng một công cụ nào đó có thể dùng chung, ít nhất phải khiến người dùng nhận được, khiến cửa hàng nhận diện và xác nhận, và để giao dịch hoàn thành, cũng phải có một phương pháp khôi phục có thể dự đoán được khi điện thoại hết pin, mạng không ổn định hoặc thông báo thất bại. Điều này có nghĩa là cả hai bên đều biết tìm nơi nào để tra cứu, khi nào thử lại, và con đường nào có thể đi sau khi thất bại. Việc cả hai bên có thể kiểm tra cùng một bản ghi sau khi giao dịch hoàn thành cũng là một phần của việc khôi phục.

Với thước đo này, thanh toán di động đã rút ngắn quy trình thanh toán trong nhiều giao dịch nhỏ hàng ngày, nhưng vẫn chưa cung cấp một con đường giống nhau cho mọi kịch bản. Trong hầu hết các giao dịch nhỏ trực tiếp, tiền mặt không cần đăng ký, không cần thiết bị, việc trao và xác nhận xảy ra đồng thời, do đó nó tiếp tục đóng vai trò là giao diện chung tối thiểu. Nó cũng có chi phí thối tiền, bảo quản và kiểm kê; ở đây so sánh rào cản chấp nhận và lỗi, chứ không phải tổng chi phí vận hành.

Cuộc điều tra ủy thác của Ngân hàng Trung ương đã đưa sự khác biệt của con người vào vai trò của tiền mặt: tỷ lệ người trên 40 tuổi và cư dân vùng xa chỉ dùng tiền mặt cao hơn. Dữ liệu hỗ trợ sự khác biệt về xu hướng, không thể mở rộng thành một hình ảnh duy nhất cho tất cả người già hoặc cư dân nông thôn.[^18] Nghiên cứu lần này cũng không có đủ dữ liệu để điền tỷ lệ hay tạo ra tiếng nói cho trẻ vị thành niên, người khuyết tật, lao động nhập cư và khách du lịch ngắn ngày. Các công cụ phổ biến rất tiện lợi cho một số người, nhưng điều đó không có nghĩa là mọi người đều có thể sở hữu cùng một tài khoản, thẻ, điện thoại hoặc mạng.

Người dùng nặng trong các chuỗi cửa hàng quen thuộc và vòng đời sống thực sự có thể không chạm vào tiền giấy trong thời gian dài. Người khác giữ lại tiền mặt cũng có thể chỉ vì thói quen, sở thích riêng tư hoặc kiểm soát chi tiêu, chứ không phải vì giao dịch đã thất bại trước đó. Sự ma sát về hệ thống, sự chấp nhận của cửa hàng, phản hồi, thành viên, thói quen, sở thích và khả năng phục hồi cùng tác động, các cuộc điều tra hiện tại không thể xếp hạng nguyên nhân đơn lẻ cho chúng.

Rào cản phổ biến hỏi bao nhiêu người sử dụng. Rào cản tương thông hỏi liệu những người và cửa hàng khác nhau có thể hoàn thành qua nhiều kịch bản hay không. Việc không cần tiền mặt lại phải hỏi, sau khi thất bại thì có thể khôi phục được không. Hai rào cản đầu tiên càng tiến lên, số người mang tiền mặt càng ít, nhưng tờ tiền cuối cùng rời khỏi ví vào lúc nào phụ thuộc vào việc ngoại lệ đã ít đến mức không đáng để dự phòng hay chưa.

Phần dưới đây là một kịch bản giả định dựa trên giới hạn ngoại tuyến của FAQ chính thức, và không phải là trường hợp thực tế: Điện thoại cửa hàng ngoại tuyến, trang đăng nhập vẫn hiển thị Mã QR không kèm số tiền. Khách hàng quét mã, nhưng cửa hàng lại không nhận được thông báo ghi sổ. Cả hai đều nhìn vào màn hình của mình, giao dịch bị kẹt giữa "có thể thanh toán" và "có thể xác nhận ngay lập tức". Cuối cùng khách hàng cất điện thoại đi, lấy ra một tờ tiền giấy. Tờ tiền đó đã không phán xét công nghệ, nó chỉ là trong kịch bản này, vẫn không cần hỏi trước: "Ở đây nhận loại nào?".

## Đọc thêm

- [Hệ sinh thái Thương mại điện tử và Thanh toán Kỹ thuật số Đài Loan](/vi/technology/e-commerce-and-digital-payment-ecosystem) — Xem lại cuộc chiến nền tảng và các nhà cung cấp dịch vụ logistics của thương mại điện tử Đài Loan trong hai mươi năm.
- [Phát triển Công nghệ Tài chính Đài Loan](/vi/economy/taiwan-fintech-development) — Đặt trường hợp thanh toán vào bối cảnh phát triển công nghệ tài chính Đài Loan trong một thập kỷ giữa sự cởi mở và kiểm soát rủi ro.
- [Trung tâm Phúc lợi Juanlian](/vi/economy/pxmart-supermarket) — Xem cách Wanhua (Juanlian) chuyển từ mạng lưới cửa hàng và quản lý thành viên sang nền tảng sống tần suất cao.

## Nguồn hình ảnh

- Ảnh chính: Công ty Thông tin Tài chính (Trang web chính thức TWQR), [Nguồn gốc](https://www.twqr.com.tw/), Bình luận sử dụng hợp lý. Hình gốc là ảnh thu nhỏ video chính thức "Lời tâm sự của người chủ | Nhật Nguyệt Hương Thịt Xốt", bài viết này chỉ được dùng để bình luận về hệ thống tuyên truyền TWQR.
- Ảnh trong bài: Công ty Thông tin Tài chính (Trang web chính thức TWQR), [Nguồn gốc](https://www.twqr.com.tw/), Bình luận sử dụng hợp lý. Hình gốc là ảnh minh họa tài liệu chính thức "Một hợp đồng, thanh toán đa dạng".

## Tài liệu tham khảo

[^1]: [MIC: Khảo sát người tiêu dùng thanh toán di động năm 2025](https://mic.iii.org.tw/research.aspx?id=730) — Hồ TựLập giải thích việc người dùng tích cực cài đặt nhiều công cụ cho các kênh khác nhau, và công bố phương pháp khảo sát, tỷ lệ áp dụng và phạm vi số lượng.

[^2]: [MIC: Khảo sát người tiêu dùng thanh toán di động năm 2025](https://mic.iii.org.tw/research.aspx?id=730) — Dữ liệu được thu thập trong quý III năm 2024, với mẫu trực tuyến là 5.000 phiếu. Tỷ lệ 92% đã từng sử dụng và 84% thường xuyên sử dụng đều giới hạn trong mẫu này.

[^3]: [Ngân hàng Trung ương: Kết quả khảo sát ủy thác về chủ đề CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Giải thích phương pháp, mẫu và trọng số hóa, cùng kết quả 73.8% sử dụng hỗn hợp, 25% chỉ dùng tiền mặt, và 1.2% chỉ dùng phi tiền mặt của người dân.

[^4]: [Trang web trí tuệ tài chính Jinbanhui: Tài liệu thanh toán di động](https://moneywise.fsc.gov.tw/uploaddowndoc?file=financeroom%2F202001131202240.pdf&filedisplay=%E6%96%B0%E5%A2%9E%E6%95%99%E6%9D%90PPT-+%E8%A1%8C%E5%8B%95%E6%94%AF%E4%BB%98-%E5%AE%9A%E7%A8%BF.pdf&flag=doc) — Phân loại thẻ tín dụng di động, thẻ tài chính di động, quét mã QR, tổ chức thanh toán điện tử và phiếu điện tử theo công cụ liên kết, công nghệ và quy định.

[^5]: [MIC: Khảo sát người tiêu dùng thanh toán di động năm 2025](https://mic.iii.org.tw/research.aspx?id=730) — Công bố phân bố phạm vi dưới năm loại, ba loại trở xuống và sáu loại trở lên của năm 2024, không công bố giá trị trung bình hoặc trung vị.

[^6]: [Cục Ngân hàng Jinbanhui: Thông tin quan trọng về tài khoản thanh toán điện tử tháng 6 năm 115](https://www.fsc.gov.tw/userfiles/file/BB-1156_%E9%9B%BB%E5%AD%90%E6%94%AF%E4%BB%98%E5%B8%B3%E6%88%B6%E9%87%8D%E8%A6%81%E8%B3%87%E8%A8%8A%E6%8F%AD%E9%9C%B2.pdf) — Tổng cộng là 41.128.870, chú thích định nghĩa là số người dùng đã đăng ký mở tài khoản và chưa kết thúc hợp đồng của mỗi tổ chức.

[^7]: [Thanh toán di động Đài Loan: FAQ vận hành cửa hàng đặc biệt](https://www.twmp.com.tw/Faq?n=95c7608a1dfc4fa1834f4467d41a32d1) — Giải thích rằng cửa hàng phải ký hợp đồng với tổ chức tài chính nhận thanh toán và lấy mã ngân hàng, mã cửa hàng đặc biệt và mã thiết bị đầu cuối.

[^8]: [Thanh toán di động Đài Loan: FAQ nhận tiền của cửa hàng](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Giải thích rằng khi thiết bị ngoại tuyến vẫn có thể tạo ra Mã QR không kèm số tiền, nhưng không thể đăng nhập hoặc nhận thông báo giao dịch.

[^9]: [Thanh toán di động Đài Loan: FAQ nhận tiền của cửa hàng](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Cơ quan chính thức nêu rõ phí xử lý giao dịch do cả hai bên là cửa hàng và ngân hàng nhận tiền thỏa thuận, không thể suy ra tỷ lệ phí thống nhất toàn thị trường.

[^10]: [Đại học Thành Công: Nghiên cứu về việc áp dụng thanh toán di động tại khu thương mại Đài Nam](https://researchoutput.ncku.edu.tw/en/studentTheses/what-factors-affect-stores-willingness-to-adopt-mobile-payment-de/) — Tóm tắt luận án tiến sĩ liệt kê các yếu tố có ý nghĩa và không có ý nghĩa đối với ý định áp dụng, phạm vi nghiên cứu giới hạn trong mẫu khu thương mại Đài Nam.

[^11]: [Ngân hàng Trung ương: Kết quả khảo sát ủy thác về chủ đề CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Mẫu 611 người bán hàng rong và 1.436 cửa hàng, và liên kết sự khác biệt chỉ nhận tiền mặt với địa điểm, thiết bị và quy mô.

[^12]: [Ngân hàng Trung ương: Khảo sát công cụ thanh toán trong Báo cáo ổn định tài chính](https://www.cbc.gov.tw/tw/dl-207586-2f35d674d8a34ee09d1d1c0fd68a6fea.html) — Biểu đồ liệt kê các khó khăn đa lựa chọn như cửa hàng không chấp nhận, không chấp nhận công cụ quen dùng, quá nhiều loại, tín hiệu và pin điện thoại.

[^13]: [MIC: Khảo sát người tiêu dùng thanh toán di động năm 2025](https://mic.iii.org.tw/research.aspx?id=730) — Cuộc khảo sát liệt kê các dịch vụ tài chính ngoài tiêu dùng, trong đó chuyển khoản và chuyển tặng điểm thưởng là loại phổ biến nhất.

[^14]: [Visa Đài Loan: Nghiên cứu người tiêu dùng ví điện tử và thanh toán điện tử năm 2022](https://www.visa.com.tw/about-visa/newsroom/press-releases/nr-tw-230310.html) — Tiết lộ tỷ lệ 1.000 mẫu từ 18 đến 55 tuổi tại Đài Loan và việc theo dõi phản hồi, tính toán ưu đãi.

[^15]: [Cục Thống kê Kinh tế: Bản PDF khảo sát lại tỷ trọng thanh toán di động bán lẻ](https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=116845) — Tỷ lệ giá trị thanh toán năm 2017 và 2023 của ngành bán buôn, bán lẻ và ăn uống và giải thích bằng hệ sinh thái thành viên.

[^16]: [Ngân hàng Trung ương: Báo cáo thường niên năm 2025](https://www.cbc.gov.tw/tw/dl-225165-b56d9b5e547843a4822acd679cb4868e.html) — Liệt kê các tổ chức tham gia TWQR, cửa hàng đặc biệt hợp tác vào cuối năm 2025, và số lượng giao dịch cũng như giá trị trong cả năm.

[^17]: [Tổ chức tài chính hợp tác: Dịch vụ nhận thanh toán liên cơ quan TWQR](https://www.tcb-bank.com.tw/company-banking/credit-card/special-store/twqr) — Phân loại các tổ chức có thể quét chính và được quét, thông số kỹ thuật QR Auth và phương thức đăng ký cửa hàng, cho thấy sự phân tầng theo hướng và thông số.

[^18]: [Ngân hàng Trung ương: Kết quả khảo sát ủy thác về chủ đề CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Báo cáo thể hiện sự khác biệt về xu hướng theo tuổi tác và khu vực, bài viết này không hư cấu tỷ lệ hoặc tiếng nói của một nhóm cụ thể dựa trên đó.
