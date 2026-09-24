---
title: 'Nhìn Đài Loan qua dữ liệu 22 thành phố và huyện: Chênh lệch mật độ 151 lần, chênh lệch thế hệ giữa già nhất và trẻ nhất'
description: 'Cùng một hòn đảo, Thủ đô Đài Bắc có mật độ dân số cao nhất là 8.975 người/km², trong khi Cao Hùng có mức thấp nhất chỉ 59 người; sự khác biệt lên tới 151 lần. Tân Trúc với tỷ lệ già hóa 15,08% và Gia Nghĩa với 24,11% cho thấy khoảng cách gần một thế hệ. Dựa trên dữ liệu chính thức cuối năm 2025 của Cục Hành chính dân sự Bộ Nội vụ, chúng tôi vẽ nên chân dung có thể kiểm chứng của cả hòn đảo: bảy phần dân cư chen chúc trong ba phần đất đai, và ranh giới già hóa không nằm ở đô thị mà ở các vùng phía Đông, đảo xa và nông nghiệp; và tất cả 22 thành phố/huyện đều đã vượt qua ngưỡng sinh bằng tử.'
date: 2026-06-06
category: 'Geography'
tags:
  [
    'thống kê dân số',
    'già hóa dân số',
    'xã hội siêu cao niên',
    'lục đô',
    'chênh lệch thành thị-nông thôn',
    'mật độ dân số',
    'chỉ số lão hóa',
    'tỷ lệ sinh thấp',
    'trực quan hóa dữ liệu',
    '22 thành phố/huyện',
  ]
subcategory: '人口與區域'
author: 'Taiwan.md'
readingTime: 13
featured: false
lastVerified: 2026-06-06
lastHumanReview: false
image: '/article-images/geography/taiwan-island-nasa-mosaic.webp'
imageAlt: 'Ảnh vệ tinh đảo chính Đài Loan nhìn từ không gian, dễ dàng nhận ra đồng bằng phía Tây và dãy núi trung tâm phía Đông'
imageCredit: 'NASA'
imageLicense: 'Public domain（NASA）'
imageSource: 'https://commons.wikimedia.org/wiki/File:Taiwan_Main_Island_Mosaic_NASA_2020.jpg'
translatedFrom: 'Geography/用數據看台灣22縣市.md'
sourceCommitSha: 'b67b190fb'
sourceContentHash: 'sha256:446265901543dd85'
sourceBodyHash: 'sha256:2daf1a831ec93084'
translatedAt: '2026-09-24T22:04:27+08:00'
---

# Nhìn Đài Loan qua dữ liệu 22 thành phố và huyện: Chênh lệch mật độ 151 lần, chênh lệch thế hệ giữa già nhất và trẻ nhất

Lái xe từ khu Thân Nghĩa, Thủ đô Đài Bắc đi về phía Nam, rồi về phía Đông, cuối cùng đến trung tâm thành phố Cao Hùng. Định vị cho thấy hơn ba trăm kilômét, chưa đầy một ngày lái xe. Nhưng nếu bạn tập trung vào một thang đo khác—số người sống trên mỗi kilômét vuông bên ngoài cửa sổ—chặng đường đó sẽ giống như xuyên qua hai quốc gia. Thủ đô Đài Bắc, nơi khu Thân Nghĩa tọa lạc, có mật độ 8.975 người/km². Cao Hùng, nơi thành phố Cao Hùng đặt chân đến, chỉ có 59 người/km². Cùng một hòn đảo, cùng một hộ chiếu, sự chênh lệch về mật độ là trọn vẹn 151 lần.

Con số này không phải là trò ảo thuật của các giá trị cực đoan. Nó là sự khác biệt thực tế bên trong Đài Loan. Chúng ta thường có xu hướng nói về "Đài Loan" như một tổng thể—nói về kinh tế, bầu cử, tỷ lệ sinh thấp của nó—nhưng khi bạn trải ra bộ dữ liệu toàn diện của 22 thành phố và huyện cuối năm 2025 từ Cục Hành chính dân sự Bộ Nội vụ, bạn sẽ nhận ra không hề có một Đài Loan đồng nhất nào. Có người chen chúc trong rừng bê tông chờ đèn đỏ, có người lái xe mười phút mà không thấy chiếc thứ hai. Một số thành phố/huyện vẫn đang phát triển, đa số các thành phố/huyện đang thu hẹp quy mô. Góc độ trẻ nhất và góc độ già nhất cách nhau gần một thế hệ.

```tw-figure
151 倍
Mật độ dân số giữa Thủ đô Đài Bắc và Cao Hùng: 8.975 người/km² so với 59 người
Cục Hành chính dân sự Bộ Nội vụ, cuối năm 2025
```

Bài viết này muốn làm một việc: dùng dữ liệu chính thức để vẽ nên một chân dung có thể kiểm chứng của cả hòn đảo. Sau khi hoàn thành, bạn sẽ thấy một khuôn mặt phân hóa mạnh mẽ và đang già đi nhanh chóng. [^1]

> **Tổng quan 30 giây:** Tổng dân số Đài Loan cuối năm 2025 là 23.299.132 người (khoảng 23.300 nghìn), đã giảm liên tục trong 23 tháng, và tỷ lệ trẻ sơ sinh lần đầu tiên dưới 110.000. Cùng năm, Đài Loan chính thức bước vào "xã hội siêu cao niên", cứ năm người thì có một người trên 65 tuổi. Nhưng mức trung bình toàn quốc đã che giấu sự chênh lệch khổng lồ bên trong: mật độ dân số cao nhất và thấp nhất cách nhau 151 lần, quy mô dân số chênh lệch 297 lần, và mức độ già hóa khác biệt gần một thế hệ. Người đổ về Lục Đô, ranh giới già hóa không nằm ở đô thị mà ở phía Đông, đảo xa và các huyện nông nghiệp; nơi trẻ nhất là Tân Trúc được hỗ trợ bởi thành phố Tân Trúc. Đây là một Đài Loan phân hóa và đang cùng nhau già đi. [^2]

## Bảy phần dân cư, ba phần đất đai

Trước hết hãy xem một sự thật dễ bị bỏ qua: người Đài Loan thực chất sống rất tập trung.

Cuối năm 2025, sáu thành phố trực thuộc tỉnh (Đài Bắc, Tân Bắc, Đào Viên, Đài Trung, Đài Nam, Cao Hùng) cộng lại có 16.278.931 người, chiếm 69,87% tổng dân số toàn đảo. Nói cách khác, cứ mười người Đài Loan thì có gần bảy người sống ở Lục Đô. Nhưng đất đai của sáu thành phố này cộng lại chỉ chiếm 30,12% diện tích toàn đảo. Bảy phần dân cư chen chúc trong ba phần đất đai. Ba phần còn lại của dân cư phân tán trên bảy phần đất đai kia. Đây là cấu trúc đầu tiên về sự phân bố dân số Đài Loan.

```tw-stat
23.300 nghìn | Tổng dân số toàn đảo | Giảm liên tục 23 tháng cuối năm 2025
20,06% | Tỷ lệ dân số từ 65 tuổi trở lên | Vượt ngưỡng siêu cao niên chính thức vào năm 2025
69,87% | Tỷ lệ dân cư Lục Đô so với toàn quốc | Nhưng chỉ sống trên 30% đất đai
```

Cấu trúc tỷ lệ bảy-ba này không tự nhiên hình thành; nó có một điểm khởi đầu thể chế rõ ràng. Ngày 25 tháng 12 năm 2010, Đài Loan đã viết lại bản đồ hành chính: Huyện Đài Bắc được nâng cấp thành Tân Bắc, các thành phố/huyện Đài Trung, Đài Nam và Cao Hùng sáp nhập, cùng với Thủ đô Đài Bắc ban đầu, tạo ra năm thành phố trực thuộc tỉnh đồng thời. Bốn năm sau, ngày 25 tháng 12 năm 2014, Đào Viên được nâng cấp thành thành phố thứ sáu. Chỉ trong bốn năm ngắn ngủi, Đài Loan đã chuyển từ hai thành phố trực thuộc tỉnh ban đầu thành sáu, và cán cân tài nguyên, ngân sách, xây dựng cũng nghiêng theo. [^4]

Việc nâng cấp không chỉ là đổi tên. Các thành phố trực thuộc tỉnh nhận được các khoản phân bổ tập trung, cơ cấu nhân sự và nguồn thu tự chủ cao hơn nhiều so với các huyện/thành phố thông thường. Cơ sở hạ tầng đi về đâu, cơ hội việc làm phát triển theo đó, người trẻ di chuyển đến đó. Thể chế đã vạch ra một đường, và dân số chảy theo con đường đó. Sự tập trung của Lục Đô mà chúng ta thấy ngày nay, ở một mức độ nào đó, là kết quả sau hơn mười năm cải cách từ năm 2010.

Biểu đồ dưới đây phân tách rõ hơn "người Đài Loan sống ở đâu". Tân Bắc một thành phố đã chứa 17,4% dân số toàn quốc, Đài Trung 12,3%, Cao Hùng 11,7%, Đài Bắc 10,5%, Đào Viên 10,1%, Đài Nam 7,9%—sáu thành phố cộng lại gần bảy phần. Còn 16 thành phố/huyện khác phân tán khắp toàn đảo, từ phía Bắc đến các đảo xa, tổng cộng chỉ chiếm 30,1%.

```tw-waffle
Người Đài Loan sống ở đâu (Tỷ lệ % dân số toàn quốc)
Tân Bắc | 17,4
Đài Trung | 12,3
Cao Hùng | 11,7
Đài Bắc | 10,5
Đào Viên | 10,1
Đài Nam | 7,9
16 thành phố/huyện khác | 30,1
Nguồn: Cục Hành chính dân sự Bộ Nội vụ, cuối năm 2025
```

Hãy nhìn kỹ biểu đồ ô vuông này, bạn sẽ nảy sinh một câu hỏi: Những người sống trên 30% đất đai kia sống cuộc sống như thế nào? Câu trả lời nằm ở mật độ.

![Đường chân trời nhà cao tầng khu Thân Nghĩa và Nam Cảng của Thủ đô Đài Bắc, các lớp dân cư và thương mại chồng chất dày đặc](/article-images/society/taipei-skyline-housing-2026.webp)
_Đường chân trời của Thủ đô Đài Bắc. Thành phố/huyện đông đúc nhất toàn đảo, chứa 8.975 người/km². Ảnh: Heeheemalu, CC BY-SA 4.0 qua [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg)._

## Từ đông đúc nhất đến vắng vẻ nhất, chênh lệch 151 lần

Sự tập trung dân số nói về "bao nhiêu người", còn mật độ nói về "có chen chúc không". Điều sau đây mới khiến bạn cảm nhận được khoảng cách giữa hai Đài Loan.

Thủ đô Đài Bắc với 8.975 người/km² là nơi đông đúc nhất toàn đảo. Sự chật chội của Đài Bắc là chuyện thường ngày: tàu điện ngầm đông nghịt vào giờ cao điểm, chờ đèn đỏ phải đợi hai chuyến, nhà cửa xây cao và hẹp. Tiếp theo là thành phố Tân Trúc với 4.376 người/km², chưa bằng một nửa Đài Bắc. Rồi thành phố Cơ Long với 2.710 người. Chỉ riêng ba thành phố đông đúc nhất này, mật độ đã giảm mạnh như vực thẳm.

```tw-bars
Thủ đô Đài Bắc | 8.975 người/km²
Tân Trúc | 4.376 người/km²
Cơ Long | 2.710 người/km²
Huyện Chương Hóa | 1.126 người/km²
Huyện Hoa Liên | 68 người/km²
Cao Hùng | 59 người/km² | Vắng vẻ nhất toàn đảo
Nguồn: Cục Hành chính dân sự Bộ Nội vụ, cuối năm 2025
```

Nhìn sang đầu kia của biểu đồ cột này, sự chênh lệch mới thực sự hiện ra. Huyện Chương Hóa với 1.126 người/km² đã được coi là tương đối đông đúc trong số các huyện nông nghiệp. Đến [Huyện Hoa Liên](/vi/geography/hualien-county/), con số giảm xuống còn 68 người. Cao Hùng, ở dưới cùng, chỉ còn lại 59 người/km². Số người mà một kilômét vuông của Đài Bắc chứa được, tương đương với việc cần 151 kilômét vuông của Cao Hùng mới lấp đầy. Đây chính là diện mạo thực tế của sự chênh lệch 151 lần—bạn lái xe từ khu Thân Nghĩa đi thẳng đến Cao Hùng, tận mắt chứng kiến mật độ dân số thưa dần bên ngoài cửa sổ.

Đằng sau đó còn có một sự thật địa lý đang chống đỡ. Thành phố/huyện có diện tích lớn nhất Đài Loan là Hoa Liên, 4.628 kilômét vuông, gần như toàn bộ phía Đông của dãy núi trung tâm. Diện tích lớn, dân số ít, nhiều núi, mật độ của Hoa Liên và Cao Hùng tự nhiên bị pha loãng xuống mức thấp nhất toàn đảo. Còn [Huyện Liên Giang](/vi/geography/lienchiang-county/) có diện tích nhỏ nhất chỉ 28,8 kilômét vuông. Vấn đề mật độ, một nửa là lựa chọn của con người, một nửa là do điều kiện địa hình bẩm sinh quyết định.

Quan niệm thông thường thường coi "mật độ dân số cao" đồng nghĩa với sự tiến bộ, và "mật độ thấp" đồng nghĩa với sự lạc hậu, nhưng mối quan hệ tương ứng này thực chất đã bị đảo ngược nhân quả. Mật độ thấp của Cao Hùng không phải vì nó không thể phát triển, mà là vì nó dựa vào dãy núi lớn, hướng ra Thái Bình Dương, vốn có điều kiện địa lý rộng đất và thưa dân. Sự "vắng vẻ" của Hoa Liên chứa đựng Thái Lộc, chứa đựng dãy núi ven biển, chứa đựng cảnh quan hậu sơn hoàn chỉnh nhất Đài Loan. Con số mật độ chỉ cho bạn biết người có chen chúc không, nó không nói lên giá trị của mảnh đất đó. Khi xếp 22 thành phố/huyện toàn đảo thành một quang phổ từ đông đúc đến vắng vẻ, bạn thấy được những cách sống khác nhau nảy sinh trên các địa hình khác nhau của hòn đảo này.

![Đường lớn Bách Lãng ở Cao Hùng, con đường nông thôn thẳng khoảng 2,2 kilômét, hai bên là cánh đồng lúa rộng mở, không có cột điện](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_%2828896712393%29.jpg/1280px-29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_%2828896712393%29.jpg)
_Đường lớn Bách Lãng ở Cao Hùng. Thành phố/huyện vắng vẻ nhất toàn đảo, với 59 người/km², bằng một phần một trăm năm mươi mốt của Đài Bắc. Ảnh: Sinchen.Lin, CC BY 2.0 qua [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_(28896712393).\_

## Người khổng lồ và hạt bụi

Nếu mật độ so sánh "có chen chúc không", thì quy mô dân số so sánh "to hay nhỏ". Sự chênh lệch về chiều kích này thậm chí còn khoa trương hơn cả mật độ.

Thành phố có dân số đông nhất toàn đảo là Tân Bắc, với 4.044.831 người, một thành phố đã tương đương với không ít quốc gia. Thành phố có dân số ít nhất là Liên Giang, tức Mỗ Tổ, chỉ có 13.621 người. Dân số của một thành phố Tân Bắc gấp 297 lần Liên Giang. Nếu đưa toàn bộ dân số huyện Liên Giang vào Tân Bắc, vẫn chưa đủ lấp đầy một phần nhỏ. Cùng mang hộ chiếu Trung Hoa Dân Quốc, "toàn thể" của một huyện trong mắt một huyện khác chỉ là một hạt bụi li ti.

Sự chênh lệch về quy mô này trực tiếp trở thành vấn đề quản trị. Tân Bắc phải xử lý giao thông, nhà ở, chăm sóc dài hạn, rác thải cho bốn triệu người; Liên Giang phải suy nghĩ làm thế nào để hòn đảo nhỏ với 13.000 người không tiếp tục mất dân số, làm sao duy trì một bệnh viện, và làm sao chuyến tàu cuối cùng vẫn có thể chạy được. Cùng một bộ luật, cùng một chính sách trung ương, khi áp dụng lên khoảng cách chênh lệch 297 lần về dân số, kết quả thực tế hoàn toàn khác nhau. Khi chúng ta nói về "chính quyền địa phương", trong đầu chúng ta thường mặc định là quy mô đô thị, nhưng Đài Loan có khá nhiều thành phố/huyện vận hành một bộ máy chính phủ với quy mô của hạt bụi.

Tuy nhiên, ở đây cần cẩn thận một cái bẫy trực giác: nhỏ không đồng nghĩa với trẻ. Bạn có thể nghĩ rằng các đảo xa và huyện nhỏ vì người trẻ di cư ra ngoài nên chỉ còn lại người già, do đó vừa nhỏ vừa già; hoặc bạn có thể nghĩ rằng các đô thị lớn có nhiều tài nguyên, cơ hội, nên vừa lớn vừa trẻ. Dữ liệu thực tế đã bác bỏ cả hai giả định này. Liên Giang có dân số ít nhất, tỷ lệ già hóa của nó là 17,14%, ngược lại còn thấp hơn một số huyện lớn; trong khi Thủ đô Đài Bắc, nơi đông đúc thứ tư về dân số và rất phồn hoa, có tỷ lệ già hóa cao nhất toàn đảo là 24,18%. Giữa quy mô và sự lão hóa, căn bản không có một đường tương ứng rõ ràng. Muốn hiểu cách Đài Loan đang già đi, cần phải thay đổi bản đồ.

## Ranh giới già hóa không nằm ở đô thị

Năm 2025, Đài Loan đã vượt qua một ngưỡng: tỷ lệ dân số từ 65 tuổi trở lên toàn quốc đạt 20,06%, chính thức trở thành "xã hội siêu cao niên" theo định nghĩa của Tổ chức Y tế Thế giới. Quy đổi ra, cả đảo có 4,67 triệu người trên 65 tuổi, cứ năm người Đài Loan thì có một người là người cao tuổi. Hơn nữa, trong số 22 thành phố/huyện toàn đảo, đã có 14 nơi vượt qua ngưỡng tỷ lệ già hóa 20%. Già đã trở thành màu nền chung của cả hòn đảo.

Nhưng mức trung bình 20,06% này đã làm phẳng hoàn toàn sự khác biệt kịch liệt bên trong. Bảng dưới đây xếp hàng tỷ lệ già hóa và chỉ số lão hóa của 22 thành phố/huyện, là bảng mà bài viết này cần dừng lại để xem kỹ nhất. Trước hết giải thích cách đọc "chỉ số lão hóa": nó bằng dân số từ 65 tuổi trở lên chia cho dân số từ 0 đến 14 tuổi rồi nhân với 100, bằng 100 nghĩa là người già và trẻ em có số lượng tương đương, con số càng cao thì nơi đó càng "trọng đầu nhẹ chân", người già ngày càng nhiều hơn, trẻ em ngày càng ít đi.

```tw-heatmap
Thành phố/Huyện | Tỷ lệ 65+ (%) | Chỉ số lão hóa
Thủ đô Đài Bắc | 24,18 | 202,06
Tân Bắc | 19,95 | 185,54
Đào Viên | 16,72 | 127,33
Đài Trung | 17,40 | 136,45
Đài Nam | 20,48 | 184,96
Cao Hùng | 20,79 | 192,10
Cơ Long | 22,28 | 240,21
Tân Trúc | 16,16 | 106,59
Gia Nghĩa | 19,90 | 164,47
Huyện Tân Trúc | 15,08 | 101,88
Huyện Miêu Lật | 20,23 | 179,56
Chương Hóa | 20,37 | 178,35
Huyện Nam Đầu | 22,66 | 224,64
Huyện Vân Lâm | 21,76 | 206,78
Gia Nghĩa | 24,11 | 291,69
Huyện Bình Đông | 21,84 | 218,72
Huyện Nghi Lan | 20,77 | 189,67
Hoa Liên | 21,52 | 200,53
Cao Hùng | 20,93 | 194,71
Huyện Bành Hồ | 21,03 | 223,65
Kim Môn | 19,69 | 255,57
Liên Giang | 17,14 | 180,23
Nguồn: Cục Hành chính dân sự Bộ Nội vụ, cuối năm 2025
```

Khi đọc bảng này, hãy đặc biệt chú ý đến cột chỉ số lão hóa. Cao nhất toàn đảo là Gia Nghĩa, với 291,69, điều này có nghĩa là ở Gia Nghĩa, mỗi đứa trẻ tương ứng gần ba người già. Tiếp theo là Kim Môn với 255,57 và Cơ Long với 240,21. Ba nơi này có một đặc điểm chung: tất cả đều là các huyện nông nghiệp, đảo xa hoặc các đô thị cũ do công nghiệp dịch chuyển, không có thành phố nào lọt vào danh sách những thành phố phồn hoa nhất Đài Loan. Ranh giới già hóa sâu sắc nhất nằm ở những góc độ này—những nơi liên tục đối mặt với sự di cư của người trẻ. Khi người trẻ rời đi vì công việc, vì học tập, những người ở lại dần già đi, và số lượng trẻ sơ sinh không bù đắp được, chỉ số lão hóa cứ tăng vọt.

Vậy, góc độ trẻ nhất toàn đảo nằm ở đâu? Câu trả lời sẽ khiến nhiều người ngạc nhiên: không phải ở một vùng đất hẻo lánh nào, mà là bên cạnh các khu công nghiệp công nghệ cao. Tỷ lệ già hóa của Huyện Tân Trúc chỉ là 15,08%, thấp nhất toàn đảo; chỉ số lão hóa 101,88, gần như trạng thái cân bằng một trẻ và một người già, nổi bật trong bối cảnh chung của sự già hóa trên toàn đảo. Đài Trung với 16,72% và Tân Bắc với 16,16% theo sát phía sau. Sự trẻ trung của ba nơi này hầu hết đều gắn liền với cùng một lý do: Khu công nghệ cao (Zhuke). Ngành bán dẫn và công nghệ đã thu hút số lượng lớn kỹ sư, nhân viên trong độ tuổi sinh sản, họ lập gia đình và sinh con ở đây, buộc cấu trúc dân số của các thành phố/huyện này phải kéo về phía trẻ. Tân Trúc không chỉ hỗ trợ con số xuất khẩu của Đài Loan mà còn là khu vực có cấu trúc dân số trẻ nhất của Đài Loan.

Đặt hai thái cực trẻ nhất và già nhất cạnh nhau, sự chênh lệch càng trở nên sắc nét.

```tw-versus
Huyện Tân Trúc (Trẻ nhất toàn đảo) | Gia Nghĩa (Già nhất toàn đảo)
Tỷ lệ 65+ 15,08% | Tỷ lệ 65+ 24,11%
Chỉ số lão hóa 101,88 | Chỉ số lão hóa 291,69
Dân số vẫn đang tăng trưởng | Dân số liên tục suy giảm
Trẻ nhờ Khu công nghệ cao | Ranh giới già hóa của huyện nông nghiệp
Nguồn: Cục Hành chính dân sự Bộ Nội vụ, cuối năm 2025
```

Tỷ lệ 15,08% của Huyện Tân Trúc so với 24,11% của Gia Nghĩa, chênh lệch 9 điểm phần trăm; chỉ số lão hóa 101,88 so với 291,69, chênh lệch gần gấp ba lần. Một nơi vẫn đang tăng trưởng, dân số chảy vào; một nơi liên tục suy giảm, dân số chảy ra. Hai huyện trên cùng một hòn đảo này có mức độ già hóa khác biệt gần một thế hệ. Bạn có thể thấy những bậc cha mẹ trẻ đẩy xe nôi ở công viên Tân Trúc, còn ở nông thôn Gia Nghĩa, cả con phố có thể là người cao tuổi đi chậm rãi. Hai loại Đài Loan này đều được tính toán bằng số liệu của Cục Hành chính dân sự.

Ở đây cần phá vỡ một hiểu lầm phổ biến: nhiều người cho rằng sự già hóa là đặc quyền của nông thôn và đảo xa, còn các đô thị lớn thì miễn nhiễm với sự lão hóa vì có nhiều người trẻ và cơ hội. Dữ liệu nói rằng không có chuyện đó. Thủ đô Đài Bắc với tỷ lệ 24,18% là cao nhất toàn đảo; chỉ số lão hóa 202,06 cũng là cao nhất trong Lục Đô. Thành phố phồn hoa và tập trung tài nguyên nhất này lại là nơi già nhất trong Lục Đô. Lý do không khó hiểu: giá nhà ở Đài Bắc cao, các gia đình trẻ bị đẩy đến Tân Bắc, Đào Viên để lập nghiệp; những người ở lại khu vực thành phố là thế hệ đã định cư từ sớm và đang dần già đi. Sự phồn hoa của đô thị không thể ngăn cản sự lão hóa, nó chỉ già đi bằng một cách khác. Lão hóa không phải là bệnh của một số huyện/thành phố, mà là tình trạng chung của cả hòn đảo, chỉ là tốc độ trước sau khác nhau.

## Một hòn đảo cùng nhau già đi

Khi mở rộng ống kính từ thành phố/huyện ra toàn quốc, câu chuyện lão hóa của Đài Loan còn có một chiều kích đáng cảnh báo hơn: tốc độ.

Đài Loan không mới bắt đầu già đi. Năm 1993, tỷ lệ dân số trên 65 tuổi toàn quốc vượt quá 7%, bước vào "xã hội cao niên" theo định nghĩa quốc tế. Năm 2018, con số này đạt 14,05%, tiến vào "xã hội già". Năm 2025, lại phá vỡ ngưỡng 20%, trở thành "xã hội siêu cao niên". Ba cột mốc thoạt nhìn chỉ là ba năm, nhưng ẩn chứa bên trong là một đường dốc ngày càng nhanh.

```tw-timeline
1993 | Xã hội cao niên | Tỷ lệ 65+ vượt 7%, Đài Loan bắt đầu già đi
2018 | Xã hội già | Tỷ lệ 65+ đạt 14%, đã trải qua giai đoạn trước đó trong 25 năm
2025 | Xã hội siêu cao niên | Tỷ lệ 65+ vượt 20%, chỉ mất 7 năm cho giai đoạn này
```

Hãy nhìn khoảng cách giữa hai mốc thời gian trên trục thời gian. Từ 7% đến 14%, Đài Loan đã mất 25 năm; nhưng từ 14% đến 20%, chỉ mất 7 năm. Đoạn đường sau chỉ tốn chưa đến một phần ba thời gian của đoạn trước. Đài Loan đang già đi, và ngày càng nhanh hơn. Điều này được coi là cấp bách ở nhiều quốc gia trên thế giới; các nước khác có hàng thập kỷ để điều chỉnh hệ thống chăm sóc dài hạn, lương hưu, y tế, còn Đài Loan bị nén lại trong vỏn vẹn bảy năm, buộc phải xây dựng toàn bộ hệ thống chăm sóc người già trong một khoảng thời gian rất ngắn.

```tw-line
Sự tăng trưởng tỷ lệ dân số trên 65 tuổi toàn quốc (%)
Năm | Tỷ lệ 65+
2000 | 8,6
2010 | 10,7
2020 | 16,1
2025 | 20,06
Nguồn: Bộ Nội vụ và Ủy ban Phát triển Quốc gia
```

Đường cong tăng trưởng này cho thấy sự tăng tốc rõ ràng. Năm 2000, tỷ lệ trên 65 tuổi toàn quốc là 8,6%, năm 2010 là 10,7%, mười năm chỉ tăng hơn hai điểm phần trăm; nhưng trong thập kỷ từ 2010 đến 2020, con số đã nhảy vọt từ 10,7% lên 16,1%, và đến mức 20,06% vào năm 2025. Phần đuôi của đường cong rõ ràng dốc hơn phần đầu. Đường cong lão hóa của Đài Loan đang bị uốn cong hướng lên trên.

Mặt khác của sự già hóa là sự sụp đổ ở phía sinh sản. Năm 2025, số trẻ sơ sinh toàn quốc lần đầu tiên dưới 110.000, chỉ có 107.812. Tỷ lệ sinh thấp và lão hóa là hai mặt của một đồng xu: người già ngày càng nhiều hơn, trẻ em bù đắp vào lại ngày càng ít đi, cấu trúc dân số chung cứ thế trở nên nặng đầu nhẹ chân. Đây cũng là lý do tại sao chỉ số lão hóa của các thành phố/huyện trước đó lại cao như vậy: người già tăng lên, còn trẻ em quá ít.

> **📝 Ghi chú biên tập viên**
> Chúng ta dễ dàng hiểu "giảm dân số" là "người trẻ di chuyển từ nông thôn ra đô thị, nên nông thôn giảm, đô thị tăng", giống như một cuộc di cư trong đảo. Nhưng dữ liệu năm 2025 đã tiết lộ một sự thật cơ bản hơn: "tăng trưởng tự nhiên" của tất cả các thành phố/huyện trên toàn quốc đều là âm. Điều này có nghĩa là, ở mỗi thành phố/huyện Đài Loan, bất kể là đô thị hay nông thôn, lớn hay nhỏ, số người chết đã vượt quá số người sinh ra. Đây không còn là vấn đề dân cư chảy đi đâu, mà là cả hòn đảo đang sống không bằng cái chết. Người di cư vào và ra chỉ là sự phân bổ lại dân số vốn đã thu hẹp, nó không tạo ra bất kỳ người mới nào.

Sự thật này đáng để suy nghĩ kỹ. Năm 2025, chỉ còn bốn thành phố/huyện toàn đảo vẫn đang tăng trưởng: Đào Viên, Tân Trúc, Đài Trung và Tân Trúc. Và sự tăng trưởng của chúng đều đến từ "tăng trưởng xã hội", tức là người dân từ nơi khác di cư vào, dựa vào việc thu hút người từ các huyện/thành phố khác, chứ không phải nhờ tự sinh sôi. Ngoài bốn nơi này, 18 thành phố/huyện còn lại đều có dân số giảm. Những nơi giảm mạnh nhất là Kim Môn, Liên Giang và Thủ đô Đài Bắc; lưu ý, ngay cả Thủ đô Đài Bắc phồn hoa cũng nằm trong danh sách suy giảm này. Khi sự sinh sản ở mọi ngóc ngách của toàn quốc không bù đắp được cái chết, thì bốn thành phố/huyện đang tăng trưởng thực chất chỉ tạm thời đứng trên sự suy giảm của người khác.

Đây là lý do tại sao tổng dân số liên tục giảm 23 tháng, xuống còn 23.299.132 người. Đó là sự co lại đồng bộ của cả hòn đảo, mỗi thành phố/huyện đều đang thu nhỏ. Sự khác biệt chỉ là một số nơi tạm thời duy trì được nhờ di cư vào, còn một số nơi thậm chí không có được đệm này.

## Chân dung do dữ liệu vẽ ra

Quay trở lại chặng đường ban đầu. Từ khu Thân Nghĩa, Đài Bắc đến Cao Hùng, mật độ người giảm từ 8.975 xuống 59 người/km², giống như xuyên qua hai quốc gia. Bây giờ bạn biết, đó không chỉ là sự chênh lệch về mật độ. Trên con đường đó, quy mô dân số biến từ người khổng lồ thành hạt bụi, sự già hóa chuyển từ sự trẻ trung được hỗ trợ bởi Khu công nghệ cao sang ranh giới già hóa của huyện nông nghiệp; điều duy nhất không thay đổi là, bất kể bạn dừng lại ở thành phố/huyện nào, cái chết tại địa phương đã nhiều hơn sinh.

Đây chính là chân dung Đài Loan năm 2025: một khuôn mặt có sự phân hóa cao và đang cùng nhau già đi. Sự chênh lệch bên trong nó đáng kinh ngạc—chênh lệch mật độ 151 lần, chênh lệch quy mô 297 lần, chênh lệch mức độ già hóa gần một thế hệ; nhưng hoàn cảnh cơ bản mà nó đối mặt lại vô cùng đồng nhất: cả đảo đều sống không bằng cái chết, tổng dân số giảm liên tục 23 tháng, và trong bảy năm đã từ xã hội cao niên lao vào siêu cao niên. Dự báo của Ủy ban Phát triển Quốc gia cho biết, theo dự đoán trung bình, đến năm 2070, tổng dân số Đài Loan sẽ còn lại 14,97 triệu người, tỷ lệ trên 65 tuổi đạt 46,5%; và vào năm 2028, lợi thế dân số sẽ kết thúc. Bức chân dung này không tự cải thiện được. [^3]

Thừa nhận sự không đồng nhất bên trong Đài Loan là để nhìn rõ vấn đề thực sự của hòn đảo: một nơi có sự khác biệt lớn như vậy, phải dùng một bộ chính sách để chăm sóc cả bốn triệu người chen chúc trong lòng chảo và mười ba nghìn người sống trên các đảo xa, đồng thời đối mặt với Tân Trúc trẻ nhất và Gia Nghĩa già nhất. Nó phân hóa, nhưng nó phải hành động như một tổng thể; nó lão hóa, nhưng nó phải cùng nhau tìm cách giải quyết. Dữ liệu đã vẽ ra khuôn mặt này cho chúng ta, và cách phản ứng lại khuôn mặt này là vấn đề mà hòn đảo cần cùng trả lời.

## Đọc thêm

- [Thủ đô Đài Bắc](/vi/geography/taipei-city) — Thành phố đông đúc nhất toàn đảo (8.975 người/km²), và cũng là nơi già nhất trong Lục Đô (chỉ số lão hóa 202), là nhân vật chung của hai thái cực mật độ và già hóa trong bài viết này.
- [Cao Hùng](/vi/geography/taitung-county) — Thái cực vắng vẻ nhất toàn đảo (59 người/km²), hai đảo xa đã gánh chịu cái giá của cả hòn đảo.
- [Gia Nghĩa](/vi/geography/chiayi-county) — Chỉ số lão hóa cao nhất toàn đảo 291,69, mỗi đứa trẻ tương ứng gần ba người già, đại diện cho ranh giới già hóa của huyện nông nghiệp.
- [Huyện Tân Trúc](/vi/geography/hsinchu-county) — Tỷ lệ già hóa 15,08% thấp nhất toàn đảo, là khu vực kéo cấu trúc dân số về phía trẻ nhờ Khu công nghệ cao.
- [Khủng hoảng tỷ lệ sinh thấp của Đài Loan](/vi/society/taiwan-low-birth-rate-crisis) — Mặt sinh sản của bức chân dung này: trẻ sơ sinh dưới 110.000, mặt khác của sự sống không bằng cái chết trên toàn đảo.

## Nguồn hình ảnh

Bài viết sử dụng 3 hình ảnh, hình chính là ảnh vệ tinh thuộc phạm vi công cộng của NASA (được lưu vào `public/article-images/`), hai hình nhúng được cấp phép Creative Commons (Wikimedia Commons), đều có ghi rõ nguồn:

- [Ảnh vệ tinh đảo chính Đài Loan (NASA mosaic)](https://commons.wikimedia.org/wiki/File:Taiwan_Main_Island_Mosaic_NASA_2020.jpg) (hình chính) — NASA, Phạm vi công cộng.
- [Đường chân trời Thủ đô Đài Bắc](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg) (phần đông đúc nhất) — Ảnh: Heeheemalu, 2026, CC BY-SA 4.0.
- [Đường lớn Bách Lãng ở Cao Hùng](<https://commons.wikimedia.org/wiki/File:29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_(28896712393).jpg>) (phần vắng vẻ nhất) — Ảnh: Sinchen.Lin, 2016, CC BY 2.0.

## Tài liệu tham khảo

[^1]: Cục Hành chính dân sự Bộ Nội vụ, Dữ liệu thống kê dân số (Cuối năm 114 / 31-12-2025, số dân của các thành phố/huyện, diện tích đất đai, mật độ dân số, tỷ lệ dân số trên 65 tuổi, chỉ số lão hóa). Tổng dân số 22 thành phố/huyện là 23.299.132 và hoàn toàn khớp với tổng thống kê chính thức. [https://www.ris.gov.tw/app/portal/346]

[^2]: Thông tấn xã Trung ương / Bộ Nội vụ, 〈Đài Loan chính thức bước vào xã hội siêu cao niên〉, 09-01-2026. Báo cáo ghi nhận tổng dân số cuối năm 2025 là 23.299.132 người, tỷ lệ trên 65 tuổi là 20,06% (4,67 triệu người), Thủ đô Đài Bắc cao nhất với 24,18%, Tân Trúc thấp nhất với 15,08%, và trẻ sơ sinh năm 2025 là 107.812 người. [https://www.cna.com.tw/news/ahel/202601090098.aspx]

[^3]: Ủy ban Phát triển Quốc gia, 〈Dự báo dân số Trung Hoa Dân Quốc (2024–2070)〉, công bố ngày 17-10-2024. Theo dự đoán trung bình, Đài Loan bước vào xã hội siêu cao niên năm 2025, lợi thế dân số kết thúc năm 2028 (dân số trong độ tuổi lao động dưới 2/3 tổng dân số), và tổng dân số giảm xuống còn 14,97 triệu người vào năm 2070, tỷ lệ trên 65 tuổi đạt 46,5%. [https://www.ndc.gov.tw/nc_27_38548]

[^4]: Bộ Nội vụ, Cải cách ngũ đô năm 2010 (Huyện Đài Bắc nâng cấp thành Tân Bắc, sáp nhập các thành phố/huyện Đài Trung, Đài Nam, Cao Hùng, có hiệu lực từ 25-12-2010); Thông tấn xã Trung ương, 〈Huyện Đào Viên được cải cách thành thành phố trực thuộc tỉnh ngày 25 tháng 12〉, 15-12-2014. [https://www.cna.com.tw/news/firstnews/201412150027.aspx]

[^5]: Bộ Nội vụ, 〈Quốc gia chúng ta chính thức bước vào xã hội cao niên〉 (Tỷ lệ dân số trên 65 tuổi đạt 14,05%), năm 2018. [https://www.moi.gov.tw/News_Content.aspx?n=2&s=11663]
