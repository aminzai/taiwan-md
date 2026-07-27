---
title: 'Mini Taiwan Pulse: Dùng con mắt giám tuyển để vẽ Đài Loan thành một tấm bản đồ biết thở'
description: 'Năm 2026, nhà phân tích dữ liệu Migu đã chồng các nguồn dữ liệu mở rời rạc của Đài Loan—máy bay, tàu thủy, tàu hỏa, xe buýt và xe thu gom rác—thành một tấm bản đồ biết thở. Công việc nặng nhọc là thu thập dữ liệu được giao cho AI, nhưng việc quyết định những lớp nào nên đặt cạnh nhau, dùng màu gì và làm nổi bật lớp nào lại dựa vào con mắt giám tuyển được rèn luyện qua ngành quy hoạch đô thị.'
date: 2026-04-19
author: 'Taiwan.md'
category: 'Technology'
subcategory: '公民科技'
tags:
  [
    'Công nghệ',
    'Công nghệ công dân',
    'Dữ liệu mở',
    'Trực quan hóa dữ liệu',
    'Dự án nguồn mở',
    'TDX',
    'Three.js',
    'Trí tuệ nhân tạo',
    'AI Agent',
    'GIS',
  ]
readingTime: 20
lastVerified: 2026-06-25
lastHumanReview: true
featured: false
translatedFrom: 'Technology/mini-taiwan-pulse.md'
sourceCommitSha: 'da22dc5b'
sourceContentHash: 'sha256:b4fa10553d998dfa'
sourceBodyHash: 'sha256:6475e91be41d93b4'
translatedAt: '2026-07-18T18:59:51+08:00'
image: '/article-images/technology/mini-taiwan-pulse-map-2026.webp'
imageCredit: 'Migu / sciwork 2026'
---

# Mini Taiwan Pulse: Dùng con mắt giám tuyển để vẽ Đài Loan thành một tấm bản đồ biết thở

Một ngày đầu năm 2026, nhà phân tích dữ liệu có tên Migu chuyển một tệp CSV thành GeoJSON rồi kéo nó vào công cụ Kepler.gl trong trình duyệt. Không viết lấy nửa dòng mã, anh đã thấy tấm bản đồ Đài Loan đầu tiên hiện lên màn hình.

Migu từng học quy hoạch đô thị ở đại học và tiếp xúc đôi chút với GIS—hệ thống thông tin địa lý, nói đơn giản là công cụ đưa dữ liệu lên bản đồ. Sau khi đi làm và theo đuổi con đường phân tích dữ liệu, anh đã lâu không còn đụng tới bản đồ. Khoảnh khắc kéo tệp CSV vào Kepler.gl và nhìn Đài Loan dần hiện ra trên màn hình hôm ấy, trong đầu anh bật lên một niềm kinh ngạc rất đỗi giản dị:

> “Hóa ra Đài Loan có nhiều dữ liệu đến vậy; hóa ra chuyển chúng thành bản đồ không hề khó.”[^1]

Câu nói nghe qua không có gì đặc biệt. Về sau, nó trở thành hạt giống của cả một hệ thống.

> **Tổng quan trong 30 giây:** Từ cuối năm 2025, Migu (GitHub `ianlkl11234s`) đã dùng dữ liệu mở của Đài Loan để thực hiện hơn mười dự án trực quan hóa. Nổi tiếng nhất là mini-taiwan-pulse, tích lũy 375 sao trên GitHub và chồng năm loại dữ liệu thời gian thực—bầu trời, biển cả, mặt đất, đường phố và hoạt động thu gom rác—thành một tấm bản đồ chuyển động[^2]. Tuy nhiên, trong một bài diễn thuyết dành cho cộng đồng sciwork vào tháng 6/2026, anh chỉ ra thẳng vấn đề: riêng chính quyền trung ương Đài Loan đã có khoảng 50.000 bộ dữ liệu mở, còn dữ liệu của hơn 20 huyện, thành phố lại phân tán trên những nền tảng khác nhau; “bộ não con người không thể duyệt hết”. Câu trả lời của anh không phải là huy động thêm người, mà là giao toàn bộ dữ liệu cho một hệ thống do các AI Agent điều phối, có khả năng tự phát triển; con người chỉ chịu trách nhiệm đặt bài toán và nghiệm thu[^3].

Bài viết này kể về hành trình một người đi từ sự ngây thơ khi kéo một tệp CSV đến chỗ buông tay để hệ thống tự trưởng thành thay mình.

## GitHub của một người đã phát triển thành cả thiên hà như thế nào

Nếu chỉ nhìn vào mini-taiwan-pulse, người ta rất dễ hình dung Migu là một kỹ sư nghiệp dư làm dự án cho vui: cuối tuần nổi hứng dựng một bản demo, rồi tình cờ trở nên nổi tiếng.

Có hai điểm không đúng trong hình dung ấy.

Thứ nhất, anh làm nhiều hơn một dự án rất nhiều. Mở trang GitHub của anh, từ tháng 12/2025 trở đi là hàng loạt dự án trực quan hóa dữ liệu mở Đài Loan: đầu tiên là một bản chứng minh ý tưởng về phạm vi xe buýt; cuối tháng 12, dự án học tập `mini-taiwan-learning-project` nổi tiếng trước và đến nay đạt 189 sao; tháng 2 có bản đồ vị trí thời gian thực của tàu thủy qua AIS và `flight-arc-graph`, dự án vẽ từng chặng cất, hạ cánh thành đường cung, đạt 56 sao; cuối tháng 2 mới đến mini-taiwan-pulse, rồi atlas đường sắt Đài Loan, quỹ đạo vệ tinh, hình ảnh CCTV thời gian thực và bảng thông tin tình hình `mini-taiwan-info` tập hợp toàn bộ dữ liệu… Chuỗi dự án kéo dài tới tháng 6[^2]. Hơn mười kho mã nối lại thành một vùng rộng lớn mà anh tự đặt tên là thiên hà “Mini Taiwan”.

![Bảng thông tin tình hình Mini Taiwan Info tập hợp dữ liệu mở về nhiều chủ đề như dân số, vận tải đường sắt, hàng hải, tài nguyên nước, cứu hỏa và y tế thành các bảng giám sát, mỗi trang một chủ đề](/article-images/technology/mini-taiwan-info-dashboard-2026.webp)

_Một thành viên khác trong thiên hà, Mini Taiwan Info: dữ liệu mở phân tán được tập hợp thành bảng giám sát tình hình, với mỗi trang dành cho một chủ đề—dân số, vận tải đường sắt, hàng hải, tài nguyên nước, cứu hỏa và y tế. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Xếp các dự án theo số sao cho thấy không chỉ một dự án trở nên nổi tiếng.

```tw-bars
GitHub của Migu: không chỉ một repo nổi tiếng (số sao GitHub)
*mini-taiwan-pulse | 375 | Dự án chủ lực
mini-taiwan-learning-project | 189 | Nổi tiếng trước pulse
flight-arc-graph | 56 | Đường bay
tw-ship-viz | 11 | Tàu thủy
mini-tw-cctv | 6 | Hình ảnh thời gian thực
satellite-arc | 6 | Vệ tinh
Nguồn: GitHub API, 2026-06-25
```

Điểm không đúng thứ hai ẩn trong ba chữ “một người”; phần sau sẽ trở lại phân tích điều này. Trước hết, hãy xem thiên hà ấy hình thành ra sao.

```tw-timeline
2025-12 | Thử nghiệm đầu tiên | Bản PoC phạm vi xe buýt, thử nghiệm sớm nhất với dữ liệu mở Đài Loan
2025-12 | learning-project nổi tiếng trước | Trực quan hóa đường sắt Đài Bắc, nổi tiếng trước dự án chủ lực (189★)
2026-02 | Dự án chủ lực ra đời | mini-taiwan-pulse khai trương, tiến hóa từ JSON tĩnh thành cơ sở dữ liệu không-thời gian
2026-06 | Công bố toàn bộ hệ thống | Diễn thuyết sciwork 2026: giao dữ liệu mở cho một hệ thống được Agent nuôi dưỡng
```

## Cùng một phương pháp, từ tàu điện ngầm đến Hệ Mặt Trời

Bản thân dự án chủ lực cũng không ngừng phát triển. Phiên bản mini-taiwan-pulse đầu tiên gồm ba lớp: bầu trời, biển cả và mặt đất. Đến phiên bản được giới thiệu trong bài diễn thuyết, nó đã trở thành “năm mạch cùng chuyển động”: máy bay trên trời, tàu thủy trên biển, tàu hỏa trên mặt đất, xe buýt ngoài đường và xe thu gom rác, với năm loại dữ liệu thời gian thực có tần suất khác nhau được chồng lên cùng một tấm bản đồ biết thở. Migu cho biết đây là lần đầu dự án “tiến hóa từ JSON tĩnh thành cơ sở dữ liệu không-thời gian”[^3]. Chỉ riêng lớp đường phố đã kết nối hơn 5.700 xe buýt trên TDX, cập nhật vị trí mỗi 30 giây.

![DAY 0, tấm bản đồ đầu tiên: chuyển một tệp CSV thành GeoJSON rồi kéo vào Kepler.gl; không cần viết mã, tấm bản đồ Đài Loan đầu tiên đã xuất hiện](/article-images/technology/mini-taiwan-kepler-day0-2026.webp)

_“DAY 0” trong bài diễn thuyết: chuyển một tệp CSV thành GeoJSON rồi kéo vào Kepler.gl, không cần một dòng mã vẫn có được tấm bản đồ Đài Loan đầu tiên—điểm khởi đầu của cả thiên hà. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Tia lửa đầu tiên của thiên hà là bản trực quan hóa đường sắt Đài Bắc mang tên “Mini Taipei”. Migu chồng ba hệ thống—tàu điện ngầm, đường sắt Đài Loan và đường sắt cao tốc—lên một tấm bản đồ chuyển động; các đoàn tàu chạy theo thời gian biểu. Anh nói chính khoảnh khắc ấy mình mới “cảm nhận được sức hấp dẫn của chuyển động”, khi hơn 300 chuyến tàu đồng thời di chuyển trên màn hình[^3]. Một thời gian biểu tĩnh như vậy đã biến thành nhịp thở của cả thành phố.

![Mini Taipei chồng ba hệ thống tàu điện ngầm, đường sắt Đài Loan và đường sắt cao tốc thành một tấm bản đồ chuyển động, với hơn 300 chuyến tàu chạy theo thời gian biểu](/article-images/technology/mini-taiwan-taipei-rail-2026.webp)

_Mini Taipei: tàu điện ngầm, đường sắt Đài Loan và đường sắt cao tốc xuất hiện trong cùng một khung hình; hơn 300 chuyến tàu chạy theo thời gian biểu. Migu nói đây là lần đầu anh “cảm nhận được sức hấp dẫn của chuyển động”. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Từ đó, như bị cuốn vào niềm say mê, anh áp dụng cùng một phương pháp “biến dữ liệu thành chuyển động” ở những quy mô ngày càng lớn. Trên biển, anh kết nối dữ liệu vị trí AIS thời gian thực của Cục Hàng hải và Cảng vụ, dùng các quả cầu ánh sáng xanh lam-lục cùng vệt chuyển sắc kéo dài 30 phút để thể hiện hướng đi của tàu thuyền quanh vùng biển Đài Loan.

![Tàu thuyền quanh vùng biển Đài Loan được vẽ từ dữ liệu vị trí AIS thời gian thực của Cục Hàng hải và Cảng vụ, với các quả cầu sáng xanh lam-lục cùng vệt chuyển sắc kéo dài 30 phút](/article-images/technology/mini-taiwan-ships-ais-2026.webp)

_Mạch đại dương: dữ liệu vị trí AIS thời gian thực của Cục Hàng hải và Cảng vụ, các quả cầu sáng xanh lam-lục cùng vệt chuyển sắc kéo dài 30 phút, thể hiện tàu thuyền quanh vùng biển Đài Loan. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Sau đó, anh đưa cùng một phương pháp ra ngoài Trái Đất. Từ các tham số quỹ đạo TLE công khai, Migu tính vị trí vệ tinh, vẽ quỹ đạo vệ tinh bay qua Đài Loan rồi mở rộng tới toàn bộ Hệ Mặt Trời. Trong bài thuyết trình, anh nói thẳng: “Cùng một phương pháp, miễn có dữ liệu là có thể mở rộng vô hạn.”[^3] Chính lúc ấy, người ta nhận ra điều thực sự mê hoặc anh là việc “biến dữ liệu thành thứ có thể nhìn thấy”; bản đồ chỉ là hình hài đầu tiên của nó.

![Trực quan hóa quỹ đạo vệ tinh được tính từ dữ liệu TLE công khai, với cùng một phương pháp mở rộng từ bề mặt Đài Loan đến không gian](/article-images/technology/mini-taiwan-satellite-2026.webp)

_Cùng một phương pháp được đưa ra ngoài Trái Đất: dùng TLE công khai để tính quỹ đạo vệ tinh, rồi mở rộng đến toàn bộ Hệ Mặt Trời. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

## Chồng các ốc đảo dữ liệu lên nhau: khoảng trống tự hiện ra

Dần dần, điều đáng chú ý không còn chỉ là “các điểm thời gian thực đang chuyển động”, mà là “khi chồng những dữ liệu vốn không liên quan lên nhau, khoảng trống sẽ tự hiện ra”. Một số dự án trong thiên hà của Migu chuyên thực hiện việc này. Một dự án mang tên “Nông nghiệp × Nước” chồng ba ốc đảo dữ liệu riêng biệt của các cơ quan nông nghiệp, thủy lợi và phòng chống thiên tai lên cùng một bản đồ: ruộng nông nghiệp, sông ngòi, kênh mương, đê điều và nguy cơ ngập lụt cùng xuất hiện. Để bản đồ tổng hợp này có thể chạy trong trình duyệt, anh dùng định dạng PMTiles kết hợp HTTP range request, giảm dữ liệu ban đầu từ 400MB xuống mức trình duyệt chỉ cần tải khoảng 5MB[^3].

![Bản đồ tích hợp Nông nghiệp × Nước: chồng dữ liệu mở về ruộng nông nghiệp, sông ngòi, kênh mương, đê điều và nguy cơ ngập lụt vốn phân tán tại nhiều cơ quan lên cùng một bản đồ](/article-images/technology/mini-taiwan-farm-water-2026.webp)

_Nông nghiệp × Nước: chồng các ốc đảo dữ liệu riêng biệt của ba cơ quan nông nghiệp, thủy lợi và phòng chống thiên tai lên cùng một bản đồ; ruộng nông nghiệp, sông ngòi, kênh mương, đê điều và nguy cơ ngập lụt xuất hiện trong cùng khung hình. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Một dự án khác chồng vị trí bệnh viện, phòng khám, nhà thuốc, máy AED và cơ sở chăm sóc dài hạn lên dữ liệu mật độ dân số, sau đó vẽ các vùng đồng thời gian tiếp cận. Theo Migu, cách này giúp “nhìn thấy khả năng tiếp cận, đồng thời nhìn thấy sa mạc y tế”—những nơi người dân phải đi xa một cách bất hợp lý mới tiếp cận được nguồn lực y tế gần nhất.

![Bản đồ khả năng tiếp cận nguồn lực y tế: chồng vị trí bệnh viện, phòng khám, nhà thuốc, AED và cơ sở chăm sóc dài hạn lên dữ liệu dân số rồi vẽ vùng đồng thời gian, qua đó các sa mạc y tế tự hiện ra](/article-images/technology/mini-taiwan-medical-2026.webp)

_Nguồn lực y tế: chồng vị trí bệnh viện, phòng khám, nhà thuốc, AED và cơ sở chăm sóc dài hạn lên dữ liệu dân số rồi vẽ vùng đồng thời gian để “nhìn thấy khả năng tiếp cận, đồng thời nhìn thấy sa mạc y tế”. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Ở mảng thiên tai, anh triển khai chi tiết hơn: dữ liệu phản hồi radar, mực nước hồ chứa, lượng mưa và cảnh báo thiên tai—vốn có tần suất cập nhật khác nhau—được chuẩn hóa ở tầng dưới thành cùng một trục thời gian. Người dùng chỉ cần kéo trục này là tất cả lớp dữ liệu cùng phát lại đồng bộ. Một trận mưa lớn bắt đầu từ đâu, mực nước hồ dâng ra sao và cảnh báo được phát lúc nào sẽ nối thành một chuỗi nhân quả trên cùng màn hình.

![Trục thời gian mưa lớn và thiên tai: phản hồi radar, hồ chứa, lượng mưa và cảnh báo thiên tai có tần suất khác nhau được thống nhất trên một trục thời gian để phát lại đồng bộ](/article-images/technology/mini-taiwan-disaster-2026.webp)

_Mưa lớn và thiên tai: phản hồi radar, hồ chứa, lượng mưa và cảnh báo thiên tai được chuẩn hóa ở tầng dưới thành cùng một trục thời gian; chỉ cần kéo là tất cả cùng phát lại đồng bộ. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Còn có flight-arc, dự án vẽ mỗi chặng cất và hạ cánh thành một đường cung. Khi cùng một API được cấp dữ liệu của những sân bay khác nhau, mỗi sân bay hiện ra với một “dấu vân tay” riêng: Đào Viên, Haneda ở Tokyo và Frankfurt đều có hình dạng khác nhau. Migu đặc biệt lấy sân bay Atlanta—bận rộn nhất thế giới—làm ví dụ: năm đường băng song song cùng các đường bay chờ chồng lên thành một cấu trúc hình học “giống đường đua”; anh cho biết bản đồ này gồm 1.839 đường bay[^3].

![Bản đồ đường bay tạo từ toàn bộ lượt cất và hạ cánh tại sân bay Atlanta trong một khoảng thời gian, với năm đường băng song song cùng các đường bay chờ chồng thành hình học giống đường đua](/article-images/technology/mini-taiwan-flight-arc-atlanta-2026.webp)

_Dự án flight-arc chồng toàn bộ lượt cất và hạ cánh tại sân bay Atlanta trong một khoảng thời gian lên cùng một bản đồ: năm đường băng song song và các đường bay chờ tạo nên cấu trúc hình học giống đường đua. Migu nói bản thân lưu lượng cũng là một hình dạng. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

> 📝 **Ghi chú của người giám tuyển**
> Hai năm trước, nếu ai đó nói “một người đã làm tấm bản đồ dữ liệu mở thời gian thực đầy đủ nhất Đài Loan”, câu tiếp theo có lẽ sẽ là “chắc hẳn người ấy kiệt sức”. Trực giác này trói quy mô với nhân lực: làm càng nhiều, con người càng bị vắt kiệt. Thiên hà của Migu đáng để dừng lại quan sát chính vì nó nới lỏng mối ràng buộc ấy. Một người đồng thời thúc đẩy hơn mười repo, trong khi dự án chủ lực vẫn liên tục có chức năng mới; phía sau là một thay đổi căn bản hơn: ở giai đoạn sau, ngày càng nhiều commit không do chính tay anh viết. “Một người” ấy đã được tạo ra như thế nào mới là chủ đề thực sự của bài viết này.

## 52.891 bộ dữ liệu, bộ não con người không thể duyệt hết

Đến đây, câu chuyện vẫn khá suôn sẻ: một người có năng lực ngày càng làm nhiều hơn và tốt hơn. Bước ngoặt xuất hiện ở giữa bài diễn thuyết, khi Migu thôi nói “tôi đã làm gì” và bắt đầu nói “tôi đã đâm phải bức tường nào”.

Anh trình chiếu một trang có tiêu đề “Vì sao cần Agentic OSINT”. Trên đó là một con số lớn: data.gov.tw có khoảng 52.891 bộ dữ liệu; cộng thêm các nền tảng dữ liệu mở của 22 huyện, thành phố, kể cả phần trùng lặp, tổng số có thể lên tới 60.000–70.000; chưa tính dữ liệu của khu vực tư nhân, các tổ chức phi chính phủ và cơ sở học thuật không có trong danh mục chính phủ. Kết luận của anh rất ngắn:

> “Bộ não của bạn không thể duyệt hết.”[^3]

Đây là trục xoay của toàn bộ câu chuyện. Người từng kéo một tệp CSV rồi kinh ngạc rằng “hóa ra có nhiều dữ liệu đến vậy” giờ đối diện mặt kia của chính sự phong phú ấy: chỉ hơn 50.000 bộ dữ liệu trên data.gov.tw, dù mỗi ngày đọc 100 bộ, một người vẫn cần hơn 500 ngày liên tục mới xem hết một lượt—và đây mới chỉ là danh mục trung ương. Dữ liệu nhiều đến mức một người dành cả đời cũng không đọc hết, chưa nói đến việc khiến chúng đối thoại với nhau. Nỗ lực cá nhân chạm trần tại đây.

Điều Migu thực sự lĩnh hội là câu tiếp theo. Với anh, lượng dữ liệu quá lớn để duyệt hết là tín hiệu cho thấy cần thay đổi công cụ:

> “Chỉ khi LLM có thể nhìn thấy dữ liệu, Agent mới giúp bạn phát hiện ‘những dữ liệu nào nên được đặt cạnh nhau để xem’.”[^3]

Từ khóa là “đặt cạnh nhau để xem”. Ngay cả khi một người thuộc tên của cả 50.000 bộ dữ liệu, trí nhớ cũng khó giúp họ nghĩ ra rằng “bản đồ nguy cơ hỏa hoạn” nên đi cùng “khu vực khó cứu hộ”, hay phải chồng “vị trí bệnh viện” lên “mật độ dân số” mới nhận ra sa mạc y tế. Giá trị của dữ liệu không nằm ở từng bộ riêng lẻ mà ở sự kết hợp; số tổ hợp có thể tạo ra từ 50.000 bộ dữ liệu đạt quy mô thiên văn. Đây chính là nơi bộ não con người không thể duyệt hết nhưng máy móc lại có ưu thế.

> 📝 **Ghi chú của người giám tuyển**
> Câu chuyện quen thuộc về dữ liệu mở có một đường phân công rõ ràng. Sau cuộc thi hackathon “Viết chương trình để cải tạo xã hội” tại Viện Nghiên cứu Trung ương năm 2012, g0v đã minh họa rất đẹp: chính phủ chịu trách nhiệm mở dữ liệu, cộng đồng công dân chịu trách nhiệm giúp dữ liệu được nhìn thấy. Năm 2020, Ngô Triển Vĩ và các cộng sự dùng 72 giờ để biến dữ liệu tồn kho khẩu trang của Cơ quan Bảo hiểm Y tế thành bản đồ mà mọi người đều có thể tra cứu; đó là một trong những khoảnh khắc cảm động nhất của mô hình này[^4]. Cách kể cũ sẽ đặt Migu vào phần kéo dài của đường thẳng ấy: g0v là tập thể, còn anh là cá nhân—một phiên bản bản đồ khẩu trang do một người thực hiện.
>
> Nhưng cách đối chiếu đó chỉ dừng ở bề mặt và còn đảo ngược quan hệ nhân quả. Migu có thể một mình tiến gần đến quy mô của “cả một thiên hà dữ liệu” hoàn toàn không phải nhờ sức người. Ngay từ đầu, anh đã không định lấy lao động cặm cụi để đấu sức với biển dữ liệu. Thay vì đọc câu “bộ não con người không thể duyệt hết” như lời nhận thua, nên xem đó là khởi điểm của việc thay đổi toàn bộ phương thức làm việc. Hình thái mới thực sự không phải “cá nhân đối đầu tập thể”, mà là “cá nhân × Agent”: một người đạt tới quy mô thiên hà chính vì không phải mọi commit đều do chính tay người ấy viết. Dưới đây là cách hệ thống này vận hành.

## Tôi không viết một chữ nào: pipeline về hỏa hoạn tự chạy đến cuối

Để hiểu “giao cho Agent” nghĩa là gì, lát cắt rõ nhất là ví dụ về hỏa hoạn trong bài diễn thuyết.

Migu cho biết anh chỉ đưa cho hệ thống một câu: “Phân tích dữ liệu công khai liên quan đến hỏa hoạn tại Đài Loan.” Sau đó anh để mặc nó vận hành.

Hệ thống bắt đầu tự mở rộng phạm vi tìm kiếm. Migu mô tả quá trình này bằng một chuỗi số tăng dần qua từng vòng: từ 582 kết quả khớp từ khóa, mở rộng bằng từ đồng nghĩa và chủ đề lên 1.945, tiếp tục tìm kiếm toàn văn, bổ sung và loại trùng, cuối cùng hội tụ thành một danh mục thống nhất gồm 73.900 mục trên 21 nền tảng[^3]. Một câu được đưa vào, bản kiểm kê hơn 70.000 mục dữ liệu được đưa ra.

```tw-figure
Một câu → 73.900 mục
Anh đưa vào câu “Phân tích dữ liệu công khai liên quan đến hỏa hoạn tại Đài Loan”; hệ thống tự mở rộng tìm kiếm và hội tụ thành một danh mục thống nhất trên 21 nền tảng
Theo bài thuyết trình của anh tại sciwork 2026
```

Thu thập vẫn chưa phải là kết thúc. Pipeline tiếp tục tự chia hỏa hoạn thành sáu giai đoạn—phòng ngừa, ứng phó, thông báo, phân tích nguyên nhân phát cháy, thiệt hại và báo cáo—rồi kết hợp với 22 huyện, thành phố để tạo một ma trận bao phủ. Ngay cả các bản kiểm kê cấp địa phương như bản đồ nguy cơ hỏa hoạn tại Tân Trúc, khu vực khó cứu hộ tại Đài Bắc hay hoạt động cứu hộ quanh ao hồ ở Đào Viên cũng được tìm ra. Hệ thống còn thành thật đánh dấu các khoảng trống: không có API hỏa hoạn thời gian thực, tọa độ ở cấp sự kiện rất hiếm và dữ liệu theo dõi sau thiên tai không được công khai.

Tiếp theo là phân tích. Migu đưa ra một báo cáo nguyên nhân hỏa hoạn do hệ thống tự thực hiện: dựa trên 15.405 bản ghi toàn quốc của năm Dân Quốc 113 (2024), nguyên nhân gây cháy lớn nhất tại thành phố Tân Bắc là yếu tố điện, chiếm 30,9%; tại huyện Bình Đông là tàn thuốc, chiếm 35,2%[^3]. Những con số này là kết quả do Agent kết nối API của nhiều đơn vị rồi tạo ra trong ảnh chụp bài thuyết trình, không phải do anh tự tra từng bảng và tính toán.

Đến đây, Migu đặt trên trang trình chiếu một dòng chữ với khoảng cách cố ý giữa từng từ, như sợ người xem chưa đọc rõ:

> “Pipeline tự động tạo ra. Tôi　không　viết　một　chữ　nào.”[^3]

Đây là điểm bùng nổ của cả bài diễn thuyết. Nó biến khẩu hiệu có phần trừu tượng “giao cho Agent” thành một thực tế cụ thể đến mức gần như gây bất an: từ một câu, đến danh mục hơn 70.000 mục dữ liệu, rồi một báo cáo nguyên nhân phân theo huyện, thành phố—vị trí trung gian vốn thường cần con người ra lệnh, viết kịch bản, làm sạch dữ liệu và chạy phân tích nay để trống.

![Kết quả của pipeline phân tích chủ đề hỏa hoạn: hệ thống tự động kiểm kê dữ liệu mở liên quan đến hỏa hoạn trên nhiều nền tảng, liệt kê các bộ dữ liệu ứng viên và ma trận bao phủ](/article-images/technology/mini-taiwan-fire-pipeline-2026.webp)

_Kết quả kiểm kê chủ đề hỏa hoạn được Migu trình bày tại sciwork 2026: khi nhận câu “Phân tích dữ liệu công khai liên quan đến hỏa hoạn tại Đài Loan”, hệ thống tự mở rộng tìm kiếm và hội tụ dữ liệu đa nền tảng thành một danh mục thống nhất. Anh nói về pipeline này: “Tôi không viết một chữ nào.” Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

## Bốn bước có thể tháo rời: dữ liệu đi vào, báo cáo tự gửi đi

Pipeline hỏa hoạn chỉ là một lát cắt, phía sau là hình ảnh thu nhỏ của toàn bộ hệ thống. Hệ thống gồm bốn bước: tiếp nhận dữ liệu, tích hợp tri thức, tạo phân tích và kích hoạt hành động. Migu đặc biệt nhấn mạnh rằng “mỗi bước đều có thể thay thế độc lập, không cần xây lại toàn bộ hệ thống”. Ngay cả tầng tiếp nhận dữ liệu thấp nhất cũng trải qua một quá trình tiến hóa. Ban đầu, anh vào data.gov.tw tải Excel theo cách thủ công, tự đọc và tự lưu; nút thắt nằm ở “trí nhớ con người”. Ở giai đoạn giữa, anh chuyển sang tìm API trên mạng, lấy báo cáo PDF và thu thập dữ liệu từ nền tảng của các huyện, thành phố, nhưng vấn đề là “không có chỉ mục”. Hiện nay, siêu dữ liệu của từng mục đều được chuẩn hóa và lưu trong một danh mục SQLite, cho phép truy vấn và mở rộng tự động[^3].

Phía sau hệ thống là hơn 40 bộ thu thập dữ liệu, từ YouBike, xe buýt và lưu lượng giao thông trên quốc lộ đến thời gian biểu đường sắt Đài Loan, AIS tàu thủy, vệ tinh khí tượng, động đất, mực nước hồ chứa và chất lượng không khí. Migu cho biết nếu kết nối lỗi ba lần liên tiếp, hệ thống lập tức gửi cảnh báo qua Telegram; mỗi sáng lúc 9 giờ, một bản Daily Review được gửi đến hộp thư của anh[^3].

Ở bước cuối cùng, “kích hoạt hành động”, anh mô tả vai trò của con người rõ ràng nhất: “Agent chạy trọn chu trình. Vai trò của con người: đặt mục tiêu, nhận báo cáo. Năm bánh răng ở giữa tự quay: phát hiện, thu thập, tích hợp, tạo sản phẩm, giám sát.” Hệ thống thậm chí tự tạo một bản tin hằng tuần mang tên “Dữ liệu mở mới trong tuần”. Theo cách nói của anh: “Chủ đề tự xuất hiện, báo cáo tự gửi đến hộp thư.”[^3]

## Một người chỉ huy, một nhóm tab: hạm đội Claude trong tmux

Cụm từ “Agent tự chạy trọn chu trình” rất dễ bị nghe như một khẩu hiệu tiếp thị. Ở phần cuối bài diễn thuyết, Migu hiếm hoi mở nắp hệ thống để người nghe nhìn thấy các bánh răng bên dưới. Cấu trúc ấy cụ thể hơn nhiều so với khẩu hiệu, đồng thời cũng trung thực hơn.

Trước tiên là toàn cảnh của chu trình. Migu cho biết hệ thống GIS của anh là “một trung tâm điều phối kết nối một vòng các repo độc lập, Agent lần lượt ghé từng trạm”: trước hết đến repo phụ trách khám phá để tìm dữ liệu đáng thực hiện, sau đó vào repo phụ trách thu thập để lấy dữ liệu, cuối cùng đi vào các repo trình bày như mini-taiwan-pulse hoặc mini-taiwan-info để vẽ bản đồ. Anh mô tả rất chính xác: “Mỗi trạm là một repo độc lập; tầng điều phối chỉ quản lý tiến độ và quyết định, còn công việc đều nằm trong tay worker của từng repo.”[^3]

Trung tâm điều phối này được anh gọi là Orchestrator, về bản chất là “một Claude Session”. Agent chính hoạt động giống một quản đốc: đọc tài liệu proposal, chia nhỏ nhiệm vụ, sắp xếp quan hệ phụ thuộc rồi bắt đầu công việc.

Cách khởi công là bước then chốt nhất trong kiến trúc. Anh không để một AI duy nhất làm mọi việc từ đầu đến cuối, mà dùng tmux—một công cụ lâu đời cho phép chia thiết bị đầu cuối thành nhiều tab độc lập—để cô lập công việc. Nguyên văn lời anh: “Một Orchestrator, một nhóm Worker. Agent chính là một Claude Session; tmux chịu trách nhiệm cô lập, mỗi Worker là một tab độc lập, một Session độc lập.” Định nghĩa ngắn gọn hơn là: “Một Worker = một tab tmux + Session độc lập + một PR.”[^3]

Nói cách khác, thứ anh chỉ huy thực chất là một hạm đội AI. Mỗi worker là một Claude được cô lập trong tab riêng, thực hiện nhiệm vụ riêng và nộp pull request riêng mà không can thiệp lẫn nhau.

![Màn hình vận hành thực tế của hệ thống điều phối Agent: một Claude session đóng vai trò orchestrator, đọc nhiệm vụ, phân rã công việc và chỉ huy các worker bên dưới](/article-images/technology/mini-taiwan-agent-orchestrator-2026.webp)

_Trung tâm điều phối được Migu công khai trong bài thuyết trình: một Claude session làm orchestrator, phân chia nhiệm vụ cho một nhóm worker được cô lập trong các tab tmux riêng; mỗi worker làm việc và nộp một PR. Ảnh: Migu / sciwork 2026 (sử dụng hợp lý cho mục đích bình luận biên tập)._

Vậy làm thế nào nhóm worker làm việc riêng mà không xung đột? Câu trả lời là một bộ nhớ chung. Theo Migu, toàn bộ tiến độ và quyết định đều được ghi thành tài liệu, tập trung trên bảng `SESSION_BOARD.md`, cùng nguyên tắc “mỗi Session một báo cáo”, nhờ đó “không cần đoán ý nhau” và “mỗi người một tệp, không xung đột”[^3]. Ngay cả việc bàn giao nhiệm vụ cũng được ghi thành tài liệu: anh dùng `HANDOFF.md` để chuẩn bị “bản nhiệm vụ cho chặng tiếp theo”, giúp Agent ở vòng kế tiếp tiếp quản mà không cần hỏi lại từ đầu. Anh mô tả cửa kiểm soát cuối cùng một cách thận trọng: “Nghiệm thu: Orchestrator đối chiếu tài liệu để nghiệm thu PR; việc merge do con người quyết định. Chỉ khi đó chu trình mới khép lại.”

Trải phẳng quy trình này, có thể thấy một hình dạng gọn gàng: một người ra lệnh; một nhóm AI được cô lập tự làm việc và tự ghi lại những gì mình đã làm; một trung tâm đối chiếu sổ sách theo tài liệu; cuối cùng, người quyết định “có tiếp nhận thành quả này hay không” vẫn là Migu. Trở lại trục chính của bài viết: dữ liệu nhiều đến mức không thể duyệt hết, nên toàn bộ việc duyệt dữ liệu được giao cho hạm đội; con người lùi về chỉ còn hai động tác—đặt bài toán và nghiệm thu. Trong bài thuyết trình, anh diễn đạt điều này bằng một câu gần như tuyên ngôn:

> “Khi Agent có thể tự chạy trọn chu trình, công việc của con người chỉ còn lại—đặt bài toán và nghiệm thu.”[^3]

Đây cũng chính là ý nghĩa tiêu đề bài diễn thuyết: “Giao dữ liệu mở của Đài Loan cho Agent, nuôi dưỡng thành một hệ thống biết tự phát triển.” Dữ liệu tự lưu chuyển, trang mới tự hình thành; con người chỉ cần đặt đúng bài toán và nghiệm thu tốt kết quả.

## Cùng một mảnh đất, cùng một bộ khung hình thành

Đến đây, nếu biết Taiwan.md—dự án giám tuyển tri thức về Đài Loan do AI duy trì mà bạn đang đọc—có thể bạn sẽ thấy phần mô tả vừa rồi khá quen thuộc.

Đó không phải là ảo giác.

Taiwan.md cũng vận hành theo cách này: một session chính làm trung tâm điều phối, chia công việc cho một nhóm worker được cô lập và có tệp bộ nhớ độc lập; tiến độ được phối hợp bằng tài liệu bàn giao; người cuối cùng quyết định thay đổi nào được đưa vào nhánh chính là nhà sáng lập Ngô Triết Vũ. Luận đề của chúng tôi là “giao tri thức về Đài Loan cho một Semiont biết tự phát triển”; luận đề của Migu là “giao dữ liệu mở của Đài Loan cho một hệ thống biết tự phát triển”. Hai câu gần như có thể hoán đổi chủ ngữ.

Điều đáng suy ngẫm hơn là hai kiến trúc này đã tự hình thành độc lập. Hồ sơ công khai cho thấy một chi tiết nhỏ: dự án Taiwan.md ra đời vào giữa tháng 3/2026; năm ngày sau, trên GitHub của Migu xuất hiện một fork[^5]. Nhưng điều đó nhiều nhất chỉ chứng minh anh biết có dự án này tồn tại. Một fork không thể giải thích toàn bộ hệ thống trong đó orchestrator chỉ huy hạm đội tmux, bảng công việc lưu giữ bộ nhớ chung, còn con người chỉ đặt bài toán và nghiệm thu. Đó là thứ anh từng bước xây dựng để giải quyết vấn đề “không thể duyệt hết 50.000 bộ dữ liệu”.

> 📝 **Ghi chú của người giám tuyển**
> Sinh học có một thuật ngữ là tiến hóa hội tụ: cá heo và cá mập không phải họ hàng gần, nhưng đều phát triển thân hình thuôn và vây lưng vì chúng đối diện cùng một đại dương. Quan hệ giữa Migu và Taiwan.md gần với kiểu hội tụ này hơn là quan hệ huyết thống. Chúng tôi sử dụng cùng nền tảng công cụ—Claude Code—và đối diện cùng hoàn cảnh—một người hoặc một hệ thống phải nắm giữ lượng thông tin về Đài Loan vượt xa dung lượng bộ não cá nhân. Vì vậy, qua những con đường tự khám phá riêng, cả hai cùng đi đến một bộ khung: một trung tâm, một nhóm lao động được cô lập, một bộ nhớ chung và một con người chịu trách nhiệm quyết định.
>
> Tín hiệu thực sự thú vị không phải là “anh ấy đã fork chúng tôi”. Đó là việc hai builder Đài Loan độc lập, trong cùng nửa đầu năm 2026, đều đồng thời tái hình dung AI từ “một công cụ thông minh hơn” thành “một đội ngũ có thể được điều phối”. Khi kiến trúc này bắt đầu mọc từ đầu óc người thứ nhất sang người thứ hai, thứ ba, nó không còn là tuyệt chiêu riêng của một cá nhân mà trở thành hình thái mới đang nảy sinh trên mảnh đất này vào thời điểm này. Builder Đài Loan tiếp theo tự dựng nên hệ thống như vậy rất có thể chưa từng nghe đến hai người trước đó.

## Chưa hoàn thành, nhưng hình dạng đã xuất hiện

Nếu bài viết kết thúc ở đoạn trên, đây sẽ là một câu chuyện quá đẹp, đẹp đến mức đáng ngờ: một người nhờ hạm đội AI đã giải quyết thanh thoát bài toán 50.000 bộ dữ liệu.

Chính Migu không để câu chuyện dừng lại ở đó. Trang áp chót trong bài thuyết trình của anh mang tiêu đề: “Tiến độ thử nghiệm, khoảng một nửa”.

Anh thẳng thắn liệt kê ba vấn đề chưa được điều chỉnh ổn thỏa. Thứ nhất là độ ổn định: harness này “vẫn chưa được điều chỉnh đến mức lý tưởng”; Agent dễ đi chệch hướng và dễ bị gián đoạn. Thứ hai, bản thân dữ liệu mở quá hỗn tạp: “Vẫn còn nhiều trường hợp cần con người phán đoán dữ liệu có khả thi hay không, không thể giao hoàn toàn cho nó.” Thứ ba là sự can thiệp thủ công: trên thực tế, ở từng giai đoạn vẫn cần có người đứng bên cạnh quan sát. Chú thích của anh cho toàn bộ công việc là: “Khả thi thì có khả thi, nhưng chưa ổn định; bản thân tôi cũng vẫn suy nghĩ xem có thực sự nên làm theo cách này hay không.”[^3]

Việc chủ động công khai một nửa thất bại ngay trên sân khấu chính là tín hiệu mạnh nhất về chất lượng. Trong thời đại bản demo AI thường được đóng gói thành “hoàn toàn tự động” và “không cần nhân lực”, một người sẵn sàng viết lên trang trình chiếu rằng “khoảng một nửa”, “chưa ổn định”, “vẫn cần con người” lại càng khiến người ta tin rằng nửa còn lại mà anh đã làm được là thật.

> 📝 **Ghi chú của người giám tuyển**
> Phần đáng tin nhất của bài diễn thuyết thực ra không phải pipeline hỏa hoạn “tôi không viết một chữ nào”, mà là bốn chữ “khoảng một nửa”. Người muốn thuyết phục bạn sẽ làm tròn tỷ lệ thành công thành “gần như hoàn toàn tự động”; chỉ người đang tiến hành thí nghiệm mới thành thật cho biết hệ thống có thể hỏng trong một nửa thời gian. Người trước bán kết luận, người sau cung cấp hiện trường. Migu cung cấp hiện trường. Đó cũng là lý do khi anh nói mình “không viết một chữ nào” trong pipeline ấy, người nghe lựa chọn tin anh. Nếu che giấu một nửa xấu xí, nửa đẹp đẽ cũng trở nên không đáng tin; chỉ khi sẵn sàng bày ra một nửa chưa hoàn hảo, nửa còn lại mới đứng vững.

Hãy trở lại tấm bản đồ ấy.

Người từng kéo một tệp CSV vào Kepler.gl rồi kinh ngạc rằng “hóa ra chuyển thành bản đồ không hề khó”, nửa năm sau đứng trên sân khấu sciwork đã không còn bàn về việc làm bản đồ dễ hay khó. Anh nói về một hệ thống biết tự tìm dữ liệu, tự kết hợp và tự phát triển thành những trang mới. Niềm kinh ngạc ngây thơ năm ấy—“hóa ra Đài Loan có nhiều dữ liệu đến vậy”—trong nửa năm đã lật sang mặt còn lại: dữ liệu nhiều đến mức một người không thể duyệt hết, vì thế cách để chúng được nhìn thấy cũng phải phát triển thành một hình thái mới.

Dữ liệu mở của Đài Loan vẫn luôn ở đó. data.gov.tw hoạt động từ năm 2013; TDX hợp nhất năm nền tảng về đường bộ, đường sắt, hàng không, hàng hải và xe đạp vào năm 2022; Bộ Nội chính có dữ liệu dân số tới cấp thôn, làng; Cơ quan Khí tượng có API mở[^6]. Dữ liệu chưa bao giờ thiếu. Điều khó là làm sao để lượng dữ liệu khổng lồ ấy đối thoại với nhau và được con người nhìn thấy. g0v từng trả lời một lần bằng sức mạnh tập thể; Migu, với một cá nhân cộng một hạm đội AI, đang thử trả lời lần thứ hai—và anh hào phóng thừa nhận mình mới chỉ trả lời đúng một nửa.

Nhưng hình dạng đã xuất hiện. Phía sau một người, một câu lệnh và một tấm bản đồ biết thở là một hệ thống đang học cách tự trưởng thành. Nửa còn lại dành cho người tiếp theo kéo vào một tệp CSV rồi không thể dừng lại.

---

## Đọc thêm

- [Ngô Triết Vũ](/people/吳哲宇): Nhà sáng lập Taiwan.md, cũng dùng lập trình và công cụ tạo sinh để tiến gần tới “thứ biết tự phát triển”
- [Cộng đồng nguồn mở và g0v](/technology/開源社群與g0v): Bối cảnh tập thể của tinh thần “viết chương trình để cải tạo xã hội”, một đối chứng với hình thái cá nhân × Agent của Migu
- [Tinh thần nguồn mở của Đài Loan](/technology/台灣開源精神): Từ “cứu nước bằng bàn phím” đến dữ liệu mở, nền văn hóa cơ sở của công nghệ công dân Đài Loan
- [Thẻ căn cước số và chính phủ số](/technology/數位身分證與數位政府): Một mặt khác của hạ tầng dữ liệu mở chính phủ

## Liên kết dự án

**Thiên hà “Mini Taiwan”** (trực quan hóa dữ liệu mở Đài Loan, đều là dự án nguồn mở cá nhân của Migu)

- **mini-taiwan-pulse**: Dự án chủ lực, bản đồ thời gian thực với năm mạch cùng chuyển động (375★)—<https://github.com/ianlkl11234s/mini-taiwan-pulse>
- **mini-taiwan-learning-project**: Dự án học tập về đường sắt Đài Bắc nổi tiếng sớm nhất (189★)—<https://github.com/ianlkl11234s/mini-taiwan-learning-project>
- **flight-arc-graph**: Quỹ đạo cất và hạ cánh, “dấu vân tay” của từng sân bay (56★)—<https://github.com/ianlkl11234s/flight-arc-graph>
- **mini-taiwan-info**: Bảng giám sát tình hình Đài Loan theo bảy chủ đề—<https://github.com/ianlkl11234s/mini-taiwan-info>
- **tw-ship-viz**: Trực quan hóa vị trí AIS thời gian thực của tàu thủy (11★)—<https://github.com/ianlkl11234s/tw-ship-viz>
- **satellite-arc**: Trực quan hóa quỹ đạo và các lần vệ tinh bay qua—<https://github.com/ianlkl11234s/satellite-arc>
- **mini-tw-cctv**: Hình ảnh thời gian thực trên toàn Đài Loan—<https://github.com/ianlkl11234s/mini-tw-cctv>
- **mini-tw-tra-atlas**: Atlas mạng lưới đường sắt Đài Loan—<https://github.com/ianlkl11234s/mini-tw-tra-atlas>
- **taiwan-weather-timelapse**: Video tua nhanh thời tiết—<https://github.com/ianlkl11234s/taiwan-weather-timelapse>
- **gis-data-collectors**: Xương sống của hơn 40 bộ thu thập dữ liệu phía sau hệ thống—<https://github.com/ianlkl11234s/gis-data-collectors>

**Bài diễn thuyết và tác giả**

- **Bản trình chiếu trực tuyến của bài diễn thuyết sciwork 2026**: <https://sciwork-showcase.zeabur.app>
- **Mã nguồn bài diễn thuyết sciwork 2026**: <https://github.com/ianlkl11234s/0613-sci-work-share>
- **GitHub của nhà phát triển Migu**: <https://github.com/ianlkl11234s>
- **Threads**: [@ianlkl1314](https://www.threads.net/@ianlkl1314)

## Tài liệu tham khảo

- Migu, “Mini Taiwan! Giao dữ liệu mở của Đài Loan cho Agent, nuôi dưỡng thành một hệ thống biết tự phát triển”, sciwork 2026 / SCIWORK SEMINAR, ngày 13/6/2026.
- Nền tảng Dữ liệu mở Chính phủ data.gov.tw (do Hội đồng Phát triển Quốc gia vận hành, hoạt động từ năm 2013).
- Nền tảng Dịch vụ Lưu thông Dữ liệu Giao thông TDX (Bộ Giao thông, hợp nhất năm nền tảng vận tải vào năm 2022).
- Cộng đồng g0v—Chính phủ Số Không—và hồ sơ các kỳ hackathon.

## Nguồn hình ảnh

Tất cả hình ảnh trong bài được lưu đệm tại `public/article-images/technology/`, không liên kết nóng đến máy chủ nguồn.

**Sử dụng hợp lý cho mục đích bình luận biên tập**: Tất cả hình ảnh trong bài đều được trích từ bản trình chiếu công khai của Migu tại sciwork 2026 (xem mã nguồn và bản trình chiếu trực tuyến trong mục “Liên kết dự án” phía trên). Theo Điều 65 Luật Bản quyền và bốn yếu tố sử dụng hợp lý tại 17 U.S.C. § 107—mục đích giáo dục phi thương mại, tác phẩm đã được công bố, tỷ lệ trích dẫn nhỏ và không thay thế đáng kể thị trường—các hình ảnh được sử dụng để bình luận biên tập về công việc trực quan hóa dữ liệu mở của tác giả. © Migu / sciwork 2026.

Phạm vi gồm: bản đồ 3D Mini Taiwan Pulse (ảnh tiêu đề), điểm khởi đầu Kepler.gl, đường sắt Đài Bắc (Mini Taipei), AIS tàu thủy, quỹ đạo vệ tinh, bản đồ tích hợp Nông nghiệp × Nước và nguồn lực y tế, trục thời gian mưa lớn và thiên tai, dấu vân tay đường bay Atlanta, kết quả pipeline chủ đề hỏa hoạn, bảng thông tin Mini Taiwan Info và màn hình vận hành hệ thống điều phối Agent.

---

[^1]: Nhà phát triển Migu Cheng, tài khoản GitHub `ianlkl11234s` (tạo vào tháng 3/2020). Đến tháng 6/2026, phần giới thiệu GitHub của anh được cập nhật thành “Building GIS visualizations from Taiwan open data · Exploring AI automation in daily work”, thay cho nội dung trước đó “nhà phân tích dữ liệu cao cấp, khám phá tự động hóa AI trong công việc hằng ngày”, với ý mới là “dùng dữ liệu mở Đài Loan để trực quan hóa GIS”. Câu “Hóa ra Đài Loan có nhiều dữ liệu đến vậy; hóa ra chuyển chúng thành bản đồ không hề khó” là nguyên văn trên trang trình chiếu “DAY 0, tấm bản đồ đầu tiên” trong bài diễn thuyết sciwork 2026. Nguồn dữ liệu: thu thập qua GitHub API, 2026-06-25; mã nguồn bài trình chiếu `ianlkl11234s/0613-sci-work-share`.

[^2]: Số sao, số fork, thời điểm cập nhật gần nhất và nguồn fork của mini-taiwan-pulse cùng các dự án trong thiên hà “Mini Taiwan” đều được Taiwan.md thu thập qua GitHub API vào ngày 2026-06-25. Khi đó, mini-taiwan-pulse có 375 sao / 26 fork và vẫn được push trong ngày 2026-06-25; mini-taiwan-learning-project có 189 sao; flight-arc-graph có 56 sao. Thiên hà gồm hơn mười repo liên quan đến dữ liệu mở Đài Loan như poc-bus-range, gis-data-collectors, tw-ship-viz, satellite-arc, mini-tw-cctv và mini-taiwan-info.

[^3]: Migu, “Mini Taiwan! Giao dữ liệu mở của Đài Loan cho Agent, nuôi dưỡng thành một hệ thống biết tự phát triển”, sciwork 2026 / SCIWORK SEMINAR, ngày 13/6/2026. Mã nguồn bài diễn thuyết: <https://github.com/ianlkl11234s/0613-sci-work-share>; bản trình chiếu trực tuyến: <https://sciwork-showcase.zeabur.app>. Tất cả số liệu được trích trong bài—data.gov.tw có khoảng 52.891 bộ dữ liệu; pipeline hỏa hoạn tăng từ 582 → 1.945 → 2.404 → 73.900 mục; 21 nền tảng; 15.405 vụ hỏa hoạn trên toàn quốc năm Dân Quốc 113; yếu tố điện chiếm 30,9% tại thành phố Tân Bắc; tàn thuốc chiếm 35,2% tại huyện Bình Đông; hơn 5.700 xe buýt; hơn 40 bộ thu thập; hơn 300 chuyến tàu; 1.839 đường bay tại sân bay Atlanta; dữ liệu Nông nghiệp × Nước giảm từ 400MB xuống khoảng 5MB—cùng tất cả câu trích dẫn như “Bộ não con người không thể duyệt hết”, “Chỉ khi LLM có thể nhìn thấy dữ liệu, Agent mới giúp bạn phát hiện những dữ liệu nào nên được đặt cạnh nhau để xem”, “Pipeline tự động tạo ra. Tôi không viết một chữ nào”, “đặt mục tiêu, nhận báo cáo”, “Khi Agent có thể tự chạy trọn chu trình, công việc của con người chỉ còn lại—đặt bài toán và nghiệm thu”, “Một Worker = một tab tmux + Session độc lập + một PR”, “Mỗi trạm là một repo độc lập; tầng điều phối chỉ quản lý tiến độ và quyết định”, “Tiến độ thử nghiệm khoảng một nửa”—đều là phát biểu và nguyên văn trang trình chiếu của Migu. Đây là tuyên bố cá nhân của diễn giả và kết quả do hệ thống của anh tạo ra, không phải thống kê chính phủ được Taiwan.md kiểm chứng độc lập.

[^4]: Cộng đồng g0v—Chính phủ Số Không—khởi nguồn năm 2012 từ tinh thần của cuộc thi hackathon “Viết chương trình để cải tạo xã hội” tại Viện Nghiên cứu Trung ương. Trong đại dịch COVID-19 năm 2020, Ngô Triển Vĩ cùng các cộng sự đã dùng dữ liệu tồn kho khẩu trang do Cơ quan Bảo hiểm Y tế công bố để xây dựng “Bản đồ cung cầu khẩu trang thời gian thực” chỉ trong vài chục giờ; đây là một trường hợp tiêu biểu cho tinh thần “cứu nước bằng bàn phím” của công nghệ công dân Đài Loan.

[^5]: Theo GitHub API (thu thập ngày 2026-06-25), `ianlkl11234s/taiwan-md` là fork của `frank890417/taiwan-md`—dự án Taiwan.md—được tạo ngày 22/3/2026. Taiwan.md ra đời vào giữa tháng 3/2026. Hệ thống cộng tác của Migu dùng Claude Code làm nền tảng công cụ—mã nguồn bài diễn thuyết có tệp CLAUDE.md và orchestrator là “một Claude Session”—giống Taiwan.md.

[^6]: Nền tảng Dữ liệu mở Chính phủ data.gov.tw do Hội đồng Phát triển Quốc gia vận hành và hoạt động từ năm 2013; Nền tảng Dịch vụ Lưu thông Dữ liệu Giao thông TDX được Bộ Giao thông thành lập năm 2022 bằng cách hợp nhất năm nền tảng vận tải đường bộ, đường sắt, hàng không, hàng hải và xe đạp; Nền tảng Dịch vụ Dữ liệu Kinh tế-Xã hội của Bộ Nội chính (SEGIS) cung cấp dữ liệu dân số tới cấp thôn, làng; Cơ quan Khí tượng Trung ương thuộc Bộ Giao thông cung cấp API mở. Tổng số bộ dữ liệu thời gian thực trên data.gov.tw không thể được kiểm chứng độc lập qua API trong lần này; con số “khoảng 50.000” sử dụng trong bài là số liệu được trình bày trong bài diễn thuyết của Migu.

_Xác minh lần cuối: 2026-06-25_
