---
title: 'Vương quốc Hải tặc: Kỹ thuật đảo ngược mô phỏng thời gian, được viết vào gen niềm tin của TSMC'
description: 'Từ những năm 1970 đến 1990, Đài Loan từng bị truyền thông quốc tế gọi là "Vương quốc Hải tặc". Bài viết này truy tìm sự hưng suy của ngành công nghiệp hàng nhái, cuộc khủng hoảng 6/12 và Điều khoản Đặc biệt 301 đã buộc hệ thống phải chuyển đổi, đồng thời giải thích tại sao mô hình niềm tin "không cạnh tranh với khách hàng" của TSMC lại là sự đảo ngược lịch sử này.'
date: 2026-08-18
category: 'History'
tags:
  [
    'Bản quyền',
    'Hàng nhái',
    'TSMC',
    'Đặc biệt 301',
    'Luật bản quyền',
    'Trương Trung Mưu',
  ]
subcategory: '經濟發展史'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-18
lastHumanReview: true
researchReport: 'reports/research/2026-08/pirate-kingdom-tsmc-trust.md'
readingTime: 12
rationale:
  why_this_hook: '「海盜王國」的國際汙名與台積電信任經濟形成強反差，影片引發的懷舊共鳴可轉化為制度史知識增量'
  whats_excluded: '排除未經正式新聞證實的坊間細節（麥當樂判決最終結果未下筆），排除中國大陸觀點來源'
  where_it_hedges: '「六成仿冒品出自台灣」為 1986 年美聯社轉述美國 ITC 單方估計，文中已標明來源'
  whos_pushing_back: '部分民眾對盜版年代帶有懷舊情感，可能質疑仿冒與台積電成功直接掛鉤的因果敘事'
curation: 'incubating'
translatedFrom: 'History/台灣盜版史.md'
sourceCommitSha: '373a07d35'
sourceContentHash: 'sha256:b8045765d1db3274'
sourceBodyHash: 'sha256:a195178fa37b285e'
translatedAt: '2026-09-16T11:57:32+08:00'
---

> **Tóm tắt trong 30 giây:** Từ những năm 1970 đến 1990, Đài Loan bị _Newsweek_ gọi là "Vương quốc Hải tặc" do nạn hàng nhái và lậu bản quy mô lớn. ITC của Mỹ ước tính 60% hàng nhái toàn cầu trong thời kỳ đó có nguồn gốc từ Đài Loan, và năm 1989, nước này đã được đưa vào danh sách quan sát ưu tiên Đặc biệt 301 của Mỹ [^4][^5]. Bài viết này xem xét ba thời điểm chuyển đổi: sự sửa đổi Luật Bản quyền năm 1992 kết thúc cuộc chiến truyện tranh lậu; việc ngành điện tử chuyển từ làm hàng nhái Apple sang OEM cho máy tương thích IBM trong những năm 1980; và cách TSMC định nghĩa lại sản xuất Đài Loan bằng mô hình niềm tin "không cạnh tranh với khách hàng" vào năm 1987. Vương quốc Hải tặc không biến mất, nó được tái cấu trúc bởi hệ thống và mô hình kinh doanh để trở thành Vương quốc Bán dẫn [^9][^13].

# Vương quốc Hải tặc: Kỹ thuật đảo ngược mô phỏng thời gian, được viết vào gen niềm tin của TSMC

Tháng 12 năm 1984, _Newsweek_ và _Asia Magazine_ cùng đặt cho Đài Loan một biệt danh: "Bến đỗ hải tặc" [^1]. Ba tháng trước đó, _Life Magazine_ mới đăng một bài báo bìa gọi hàng nhái là "ngành công nghiệp mới nổi của Đài Loan" [^1]. Du khách nước ngoài sau khi xuống máy bay thường đổ về đường Tôn Trung Bắc Lộ, chi khoảng 25 đô la Mỹ để mua một chiếc đồng hồ Rolex giả. Các cửa sổ hiệu sách trưng bày cuốn _Encyclopedia Britannica_ phiên bản giản thể bị sao chép. Ở các tiệm cam ven ngõ, truyện tranh lậu giá 10 đồng được chất trong giỏ nhựa cho trẻ em sau giờ học lựa chọn [^2]. Cùng thời kỳ đó, một "McDonald's" gần ga Đài Bắc với biển hiệu giống Kim tự tháp vàng đã hoạt động sáu năm, sớm hơn McDonald's chính thức sáu năm tại Đài Loan. Trong vụ kiện nhãn hiệu sơ thẩm, McDonald's chính hãng thậm chí từng thua kiện, và lý do chính thức của cơ quan đăng ký nhãn hiệu lại cho rằng nhãn hiệu chính hãng có "nguy cơ lừa dối công chúng hoặc khiến công chúng hiểu lầm" [^3]. Hàng nhái ở Đài Loan những năm 1980 không chỉ là kinh tế ngầm, mà còn là một hoạt động công khai ngang nhiên: biển hiệu dám xuất hiện sớm hơn hàng thật, và các vụ kiện cũng được tiến hành trước. Trong thời đại đó, hầu như không ai cảm thấy điều này có gì sai, bởi ranh giới giữa "hàng nhái" và "bắt chước" chỉ được vạch ra sau khi Mỹ đưa Điều khoản 301 lên bàn đàm phán.

Sự sao chép còn lan sang giới giải trí. "Tiểu Hổ Đội," nổi tiếng khắp hai bờ eo biển vào cuối những năm 1980, đã bắt chước phong cách thần tượng Nhật Bản là "Shonen Dai" cả về cấu trúc nhóm lẫn phong cách biểu diễn. Ý tưởng của bộ ba "Ngũ Bảo Hoàng Kim" trong chương trình đoạt giải vàng _Hoàng Kim Đôi Bạn_ được lấy từ một chương trình của đài TBS Nhật Bản. Nhân vật mang tính biểu tượng "Bà lão Dương" của Dương Phàm lại dựa trên nhân vật hài kịch nổi tiếng Jimura Ken của Nhật Bản. Những chương trình và nhóm này không phải là bản sao được cấp phép chính thức, mà là sản phẩm do các nhà sản xuất địa phương học hỏi từng chi tiết từ tín hiệu truyền hình Nhật Bản. Đó là cách ngành giải trí Đài Loan tồn tại trong thời đại không có phí bản quyền và không có sự giám sát của hãng gốc.

> Tháng 3 năm 1986, _The New York Times_ trích lời một nhà ngoại giao phương Tây: "Cho đến vài năm trước, Đài Loan vẫn là thủ đô hàng nhái và lậu bản không tranh cãi trên thế giới." [^2]

📝 Ghi chú của người biên tập: Vị thế toàn cầu của ngành bán dẫn Đài Loan và thời kỳ hàng nhái mà cả thế giới đã chê bai không phải là một vết đứt gãy, mà là cùng một nhóm người.

![Các biển hiệu và tiểu thương ở chợ đêm Hoa Tây phố: "Chợ rắn" những năm 1980 là nơi tập trung để du khách nước ngoài mua đồng hồ và hàng điện tử nhái (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC0)](https://upload.wikimedia.org/wikipedia/commons/e/e0/Huaxi_Street_Night_Market.jpg)

## Ai đã gọi Đài Loan là Vương quốc Hải tặc?

"Vương quốc Hải tặc" không phải là một ẩn dụ, mà là một ghi chép ngoại giao có nguồn gốc. Từ năm 1989, Văn phòng Đại diện Thương mại Mỹ công bố danh sách quan sát "Đặc biệt 301" hàng năm; Đài Loan đã lọt vào danh sách "Quốc gia được ưu tiên quan sát" ngay trong năm đầu tiên và tiếp tục ra vào danh sách trong gần hai mươi năm cho đến tháng 1 năm 2009 [^4]. Để hiểu trọng lượng của biệt danh này, cần đặt nó vào bối cảnh thời gian: Đài Loan giữa những năm 1980 đã tăng trưởng kim ngạch xuất khẩu từ mức một tỷ đô la vào những năm 1970 lên 38.8 tỷ đô la vào năm 1986, trở thành một trong những nền kinh tế có tốc độ tăng trưởng xuất khẩu nhanh nhất thế giới lúc bấy giờ. Trong số hàng hóa xuất khẩu có cả hàng chính hãng và hàng nhái, đây chính là lý do khiến Washington và các chủ doanh nghiệp cùng lo lắng [^11]. Báo cáo gỡ bỏ đã ghi nhận Đài Loan là "thăng hoa từ bến đỗ của những kẻ lậu bản thành thánh địa nghiên cứu và phát triển sáng tạo". Tài liệu đó cũng ghi lại sự ra đời và cái chết của Vương quốc Hải tặc [^4].

Thực tế giữa những năm 1980 còn khó coi hơn cả danh sách. Tháng 3 năm 1986, phóng viên _The New York Times_ John Burns đã khảo sát thực địa tại Đài Bắc: một chiếc Rolex nhái ở chợ đêm Hoa Tây chỉ bán với giá 10 đô la Mỹ, trong khi giá niêm yết của hàng thật Tiffany dành cho người Hoa cùng thời là 8.850 đô la Mỹ. Phần mềm WordStar lậu được bán với giá 5 đô la. Thương hiệu "Yeal" làm nhái ổ khóa Yale, chỉ khác một chữ cái đã dám lên kệ [^2]. Báo cáo của hãng Reuters vào tháng 9 cùng năm còn trực tiếp hơn, trích dẫn ước tính của Ủy ban Thương mại Quốc tế (ITC) Mỹ: đầu những năm 1980, có tới sáu phần mười hàng nhái lưu hành trên thế giới là từ Đài Loan [^5]. Lời tuyên bố công khai của chính quyền Reagan lúc đó là ngành công nghiệp Mỹ bị thiệt hại 20 tỷ đô la mỗi năm do hàng nhái. _Business Weekly_ năm 1986 còn tính toán nặng hơn, cho rằng hàng nhái đã gây thiệt hại 750.000 cơ hội việc làm cho Mỹ [^6].

```tw-stat
# Các số liệu quan trọng của Vương quốc Hải tặc Đài Loan #
1989|Điểm bắt đầu danh sách|Đài Loan lần đầu được đưa vào Danh sách Quan sát Ưu tiên Đặc biệt 301 của Mỹ
2009|Gỡ bỏ|Đài Loan chính thức được gỡ khỏi Danh sách Quan sát Đặc biệt 301
60%|Tỷ lệ hàng nhái|Ước tính đầu những năm 1980, sáu phần mười hàng nhái toàn cầu có nguồn gốc từ Đài Loan (ITC)
750.000|Số việc làm bị thiệt hại|*Business Weekly* cho rằng hàng nhái đã gây thiệt hại số lượng việc làm này cho Mỹ
Nguồn: Ủy ban Thương mại Quốc tế (ITC) / Văn phòng Đại diện Thương mại Mỹ / *Business Weekly*, 1986-2009
```

📝 Ghi chú của người biên tập: Một nền kinh tế xuất khẩu hàng chục tỷ đô la, sáu phần mười hàng nhái toàn cầu đến từ nhà máy của nó—đây không phải là trộm cắp vặt, mà là dây chuyền sản xuất cấp quốc gia.

## Truyện tranh: Từ chế độ kiểm duyệt đến cuộc chiến 6/12

Sự bùng nổ truyện tranh lậu bắt nguồn một cách đáng ngạc nhiên từ chính sự kiểm soát của chính phủ. Trong những năm 1960, chính phủ thực hiện hệ thống kiểm duyệt truyện tranh nghiêm ngặt; các nhà sáng tạo trong nước nhiều lần bị bác bỏ khi nộp hồ sơ, khiến thị trường truyện tranh nội địa suy thoái. Tuy nhiên, truyện tranh Nhật Bản lậu lại chiếm lĩnh thị trường với giá cực thấp mà không cần trả tiền bản quyền, nhờ hối lộ quan chức kiểm duyệt để nhận được giấy phép xuất bản hợp pháp do chính phủ cấp [^7]. Nói cách khác, trong thời kỳ truyện tranh lậu hoành hành nhất, những kẻ buôn lậu lại nắm giữ các tài liệu chứng minh do chính phủ ban hành [^7].

Cấu trúc "hàng nhái hợp pháp" này đã tạo ra một thế hệ độc đáo của độc giả truyện tranh Đài Loan. Trẻ em ở các tiệm cam ven ngõ và hiệu sách xung quanh trường học có thể mua được một cuốn truyện tranh Nhật Bản với giá 10 hoặc 20 Đài tệ: không có trang bản quyền, chất lượng dịch thuật khác nhau, thậm chí tên nhân vật cũng có thể thay đổi giữa các nhà xuất bản, nhưng giá chỉ bằng một phần mười tạp chí chính hãng. Truyện tranh không còn là thú vui của tầng lớp trung lưu mà trở thành sinh hoạt thường ngày của dân chúng. Chính phủ vừa dùng hệ thống kiểm duyệt để giết chết con đường mưu sinh của người sáng tạo trong nước, vừa bảo chứng cho những kẻ buôn lậu bằng giấy phép xuất bản; ngành công nghiệp truyện tranh nội địa đã hoàn toàn mất đi không gian cạnh tranh dưới sự kẹp chặt kép này.

Vào ngày 15 tháng 7 năm 1987, khi chế độ mở cửa được thực hiện, hệ thống kiểm duyệt bỗng nhiên trở nên vô hiệu, và truyện tranh lậu bước vào thời kỳ Chiến quốc. Nhiều nhà xuất bản như Đông Lập, Đại Nhiên, Tiển Đoan cùng dịch một tác phẩm nổi tiếng; _Dragon Ball_ và _Haikyuu!!_ được các nhà xuất bản khác nhau dịch, khiến độc giả muốn mua cùng một cuốn truyện có thể nhận được bốn phiên bản dịch [^8]. Đỉnh cao của thời kỳ Chiến quốc, số lượng phát hành của _Shonen Kaiho_ đạt 230.000 bản, con số này còn cao hơn tổng lượng phát hành của nhiều tạp chí chính hãng cùng thời [^8].

Vào ngày 12 tháng 6 năm 1992, Luật Bản quyền sửa đổi có hiệu lực; các sản phẩm tái bản dịch từ nước ngoài được in trước đó vẫn được bán trong khoảng thời gian đệm hai năm. Nghĩa là sau ngày 12 tháng 6 năm 1994, tất cả truyện tranh dịch lậu phải ngừng lưu hành. Người hâm mộ truyện tranh gọi ngày này là "Giới hạn 6/12"; cảnh các hiệu sách thanh lý hàng tồn kho trước giới hạn đã trở thành ký ức tập thể của thế hệ người Đài Loan đó [^9]. Trong hai tháng cuối cùng trước giới hạn, các hiệu sách và tiệm cho thuê truyện trên toàn đảo chất đống hàng hóa trước cửa, dán nhãn "Thanh lý toàn bộ". Nhiều học sinh trong thời gian đó đã mang về một túi đầy truyện lậu với số tiền vốn chỉ đủ mua một cuốn—đó là lễ cáo biệt của truyện tranh lậu ở Đài Loan, và cũng là màn khai mạc của kỷ nguyên chính hãng.

Sự chuyển đổi sau giới hạn không diễn ra trong một đêm. Giá niêm yết của truyện tranh được cấp phép chính hãng cao gấp nhiều lần hàng nhái; các nhà xuất bản buộc phải học quy trình biên tập, tiêu chuẩn dịch giả và phân chia bản quyền của Nhật Bản. Những người thợ dịch trước đây chuyển sang làm quản lý bản quyền và biên tập viên. Phía độc giả cũng thích nghi: từ "có thể mua ở bất cứ đâu" thành "chỉ một nhà xuất bản mới có bản chính hãng", việc săn lùng các tập truyện đơn lẻ chính hãng, ủng hộ nhà xuất bản đã trở thành sinh hoạt thường ngày của người hâm mộ truyện tranh cuối những năm 1990. Giới hạn đã buộc một sự chuyển đổi mang tính cấu trúc: vào tháng 1 năm 1992, Đông Lập ký hợp đồng _Akira_ với Shogakukan, trở thành tác phẩm truyện tranh Đài Loan đầu tiên được ký kết chính thức với nhà xuất bản Nhật Bản; những kẻ buôn lậu lần lượt chuyển mình thành đại lý chính hãng [^8].

```tw-timeline
# Bốn mươi năm của Truyện tranh Lậu: Từ Hàng nhái hợp pháp đến Đại lý Chính hãng #
1960s|Thời kỳ kiểm duyệt|Truyện tranh nội địa suy thoái, truyện tranh Nhật Bản lậu được lưu hành với giấy phép chính phủ giá rẻ
1987|Chiến quốc sau mở cửa|Hệ thống kiểm duyệt thất bại, nhiều nhà xuất bản cùng dịch một tác phẩm
1992.1|Ký kết chính hãng|Đông Lập ký hợp đồng *Akira* với Shogakukan, đại lý chính hãng đầu tiên
1992.6|Sửa đổi Luật Bản quyền|Luật Bản quyền sửa đổi có hiệu lực, tác phẩm nước ngoài lần đầu được bảo hộ
1994.6.12|Giới hạn 6/12|Ngày bán cuối cùng của sản phẩm tái bản dịch lậu, sự kết thúc của thời đại hàng nhái
2009|Gỡ bỏ quốc tế|Đài Loan tự gỡ khỏi Danh sách Quan sát Đặc biệt 301 của Mỹ
Nguồn: Điều 112 Luật Bản quyền Trung Hoa Dân Quốc / *Industrial Times*, 1992-2009
```

![Cửa hàng cho thuê truyện tranh Shilin được thành lập năm 1986, vẫn đang hoạt động—trong những năm 1980 đến 90, các tiệm cho thuê là đầu mối lưu thông truyện tranh lậu (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC BY-SA 3.0)](https://upload.wikimedia.org/wikipedia/commons/f/f1/Ikkoku-kan_Comic_Bookshop_Shilin_Branch_20101209.jpg)

## Ngành điện tử: Kỹ thuật đảo ngược mổ xẻ sự ra đời của Apple

Khoản vốn ban đầu của ngành điện tử Đài Loan cũng đến từ việc tháo dỡ. Năm 1981, Acer (tên lúc đó là Multitech) đã tung ra máy tính giảng dạy "Tiểu Giáo Sư Số Một" với giá 70 đô la Mỹ; năm sau, họ tung ra "Tiểu Giáo Sư Số Hai" với giá 7.950 Đài tệ, và cái sau gần như là bản sao của Apple II [^10]. Báo cáo của _The Christian Science Monitor_ năm 1984 viết rằng các cửa hàng máy tính ở khu Tôn Trung Bắc Lộ có thể tạo ra một chiếc máy tính nhái Apple trong hai giờ với giá 350 đô la Mỹ, chỉ bằng khoảng một nửa giá gốc [^11]. Cùng thời điểm đó, Shen Tong Computer tung ra "Tiểu Thần Thông," và Jing Ji Electronics tung ra máy tương thích Famicom "Tiểu Thiên Tài" chưa được Nintendo cấp phép; các loại hàng nhái đã mở rộng từ máy tính sang máy chơi game [^10].

![Biển hiệu chợ đêm khu đi bộ Ximending: Các cửa hàng điện tử và quầy quần áo ở Ximending từng là nơi tập trung chính của hàng nhái và phần mềm lậu trong thời kỳ Vương quốc Hải tặc (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC BY 3.0)](https://upload.wikimedia.org/wikipedia/commons/2/23/Ximending_Main_Alley_at_Night.jpg)

Năm 1983, Apple Computer đã chính thức kiện các nhà sản xuất Đài Loan vi phạm bản quyền. Máy tính Tiểu Giáo Sư Số Hai của Acer bị hải quan Mỹ giữ lại; Apple cáo buộc nội dung hướng dẫn sử dụng được dịch từ tài liệu Apple II, và cuối cùng Acer bị yêu cầu bồi thường 20 đô la Mỹ cho mỗi chiếc máy [^10]. Vụ kiện này đã tạo ra hai kết quả. Thứ nhất, khả năng tháo dỡ, làm nhái và thay đổi nhanh chóng mà các nhà sản xuất Đài Loan rèn luyện được thông qua kỹ thuật đảo ngược đã được chuyển hướng sang OEM/ODM cho máy tương thích kiến trúc mở của IBM. Trong đầu những năm 1980, IBM đã tiếp xúc với 11 nhà sản xuất Đài Loan; trong đó, 7 công ty đã ký thỏa thuận ngừng sản xuất hàng nhái và xin lỗi công khai, sau đó chuyển sang gia công được cấp phép [^11]. Thứ hai, Trương Trung Mưu (Jensen Huang) vì thương hiệu Multitech thường xuyên gặp tranh chấp nhãn hiệu ở nước ngoài, đã đau đớn đổi tên thành Acer vào năm 1987 với giá 2 triệu đô la Mỹ, thay thế giá trị thương hiệu tích lũy nhiều năm [^10].

Cụm điện tử tại Khu công nghệ cao Hsinchu được hình thành trong giai đoạn chuyển tiếp "từ hàng nhái sang gia công" này. Các kỹ sư Đài Loan thời kỳ hàng nhái đã học cách đọc mạch, thay đổi thiết kế và đáp ứng tiến độ; những năng lực này đã có lối thoát hợp pháp sau kiến trúc mở của IBM, trực tiếp đặt nền móng cho vương quốc OEM/ODM điện tử Đài Loan sau này [^11].

Điều đáng nói là sự chuyển đổi này không phải là một sự thức tỉnh đạo đức độc đáo của Đài Loan, mà là kết quả cấu trúc ngành do kiến trúc mở của IBM mang lại. Sau khi thông số kỹ thuật phần cứng của PC IBM được công bố, thị trường máy tương thích không cần phá mã mẫu, mà chỉ cần lắp ráp và tinh chỉnh nhanh hơn, rẻ hơn so với hãng gốc—đây chính là năng lực mà các nhà sản xuất Đài Loan đã rèn luyện trong chiến hào hàng nhái suốt hai mươi năm. Từ "sao chép bản thảo" đến "đáp ứng tiến độ gia công," kỹ năng là một bộ kỹ năng giống nhau, sự khác biệt chỉ nằm ở điều khoản cấp phép trong hợp đồng. Chuỗi năng lực này được mở rộng đến OEM máy tính xách tay, OEM bo mạch chủ, và cuối cùng tìm thấy nơi xuất khẩu cao cấp nhất trong phòng sạch sản xuất chip. Hệ thống EMS và ODM điện tử Đài Loan đã đạt vị trí số một toàn cầu trong ba mươi năm tiếp theo; từ cuối những năm 1990, hơn bảy phần mười máy tính xách tay được xuất ra toàn cầu đều do chuỗi cung ứng Đài Loan thiết kế hoặc lắp ráp. Trí nhớ cơ bắp về việc tạo mẫu nhanh, thay đổi nhanh và sản xuất hàng loạt nhanh chóng được rèn luyện trong thời kỳ hàng nhái chính là nền tảng của tỷ lệ bảy mươi phần trăm đó [^11].

![Các khu thương mại điện tử Quang Hoa ở Đài Bắc và các khu chợ bên cạnh cầu cũ: Trong những năm 1960 đến 90, phố máy tính quanh trung tâm thương mại Quang Hoa là cái nôi văn hóa linh kiện và lắp ráp điện tử của Đài Loan, cũng là bối cảnh cốt lõi của việc lưu thông máy tính nhái (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC BY-SA 3.0)](https://upload.wikimedia.org/wikipedia/commons/f/fe/Guang_Hua_Digital_Plaza_and_Mitsubishi_Delica_4WD_20080203.jpg)

## Điều khoản Đặc biệt 301: Mùa sửa luật dưới lưỡi dao thuế quan Mỹ

Hóa đơn thiệt hại mà hàng nhái gây ra cho Mỹ cuối cùng đã trở thành vũ khí ngoại giao và thương mại. Trong những năm 1980, Mỹ nhiều lần đe dọa áp dụng trả đũa thương mại đối với Đài Loan. Năm 1984, chính phủ Đài Loan bắt đầu cấm xuất khẩu hàng nhái và thành lập các nhóm dự án; năm 1983, Luật Nhãn hiệu được sửa đổi, và phần mềm máy tính được đưa vào sự bảo hộ của Luật Bản quyền [^11][^12]. Về mặt thực thi pháp luật cũng có áp lực: số vụ truy tố hình sự tăng từ 344 vụ vào năm 1983 lên 629 vụ vào năm 1985; hải quan đã công khai nghiền nát các máy tính nhái bị thu giữ thành tin tức hàng năm [^2][^5]. Sau khi Đài Loan lần đầu tiên được đưa vào danh sách Đặc biệt 301 vào năm 1989, chính phủ tiếp tục "cắt gọt" Luật Sáng chế, Luật Nhãn hiệu và Luật Bản quyền; năng lực điều tra và mức án pháp lý đều tăng lên [^4][^12]. Việc sửa đổi lớn về Luật Bản quyền năm 1992 là đòn chí mạng: xóa bỏ giới hạn pháp lý của "quyền dịch", xác định rõ ràng chương trình máy tính là tác phẩm, và trao cho tác phẩm nước ngoài địa vị được bảo hộ lần đầu tiên ở Đài Loan, trực tiếp chấm dứt khu vực xám "hợp pháp" trong việc in lại sách và phần mềm nước ngoài [^9]. Sau khi sửa luật, Bộ Kinh tế cũng thành lập Hội đồng điều phối sở hữu trí tuệ để giám sát việc thực thi; các Viện kiểm sát địa phương được bố trí công tố viên chuyên trách để truy quét từ người bán hàng rong ở chợ đêm đến nhà in và nhà nhập khẩu.

Bóng ma của Đặc biệt 301 không chỉ nằm trên các điều khoản pháp lý, mà còn trong ngành công nghiệp hàng ngày. Sau khi xuất khẩu hàng nhái bị cấm rõ ràng, các tiểu thương ở chợ đêm Hoa Tây và Ximending đã mất nguồn thu nhập chính. Ngành may mặc buộc phải rút khỏi dây chuyền may nhái Adidas, Nike để chuyển sang OEM hợp pháp—cùng máy may, cùng công nhân, chỉ là nhãn mác được thêu trên vải thay đổi từ Abiba thành nhãn hiệu được cấp phép quốc tế. "Công viên giải trí Thế giới Cổ tích" khai trương ở Tân Trúc năm 1984 đã mô phỏng khu Disney, và tại Hoa Liên Mỹ Lân (Hualien Meilun), từng dựng một biểu tượng Mickey Mouse khổng lồ chưa được cấp phép; những cảnh quan này dần biến mất hoặc được cải tạo sau khi các quy định về sở hữu trí tuệ siết chặt, trở thành một trang kỷ niệm đáng xấu hổ trong lịch sử du lịch địa phương [^12]. Biển hiệu của Vương quốc Hải tặc là từng mảnh bị pháp luật tháo dỡ.

Sự trớ trêu của logic sửa luật này là: sự rút lui của Vương quốc Hải tặc không phải là sự thức tỉnh đạo đức tự phát của xã hội Đài Loan, mà là sự chuyển giao hệ thống dưới lưỡi dao trả đũa thương mại. Một think tank Đài Loan, _Observer_, đã thẳng thắn trong bài tổng kết rằng Đài Loan chỉ dần xây dựng nên một hệ thống pháp lý sở hữu trí tuệ hiện đại thông qua quá trình đáp ứng yêu cầu về sở hữu trí tuệ của Mỹ [^12]. Cho đến khi được gỡ bỏ vào năm 2009, hệ thống do áp lực bên ngoài này đã hoàn thành hai mươi năm [^4].

```tw-versus
# Giữa những năm 1980: Tiêu chuẩn kép pháp lý của Vương quốc Hải tặc #
Đồng hồ Tiffany chính hãng|8.850 đô la Mỹ|Giá bán tại Đài Bắc được trích dẫn bởi *The New York Times* năm 1986
Đồng hồ Rolex nhái|10 đô la Mỹ|Tỷ giá thị trường chợ đêm Hoa Tây cùng thời
Phần mềm và máy tính chính hãng|Giá thị trường|Hoàn thành trong hai giờ tại các cửa hàng máy tính Tôn Trung Bắc Lộ
Phần mềm WordStar lậu|5 đô la Mỹ|Gấp hàng trăm lần chênh lệch với giá thật
Nguồn: *The New York Times* / *Los Angeles Times*, 1986
```

## Sự đảo ngược của niềm tin: Tại sao TSMC phải đối lập với hàng nhái

Vào năm 1987, năm trước khi Luật Bản quyền được sửa đổi và cùng năm mở cửa, Trương Trung Mưu (Jensen Huang) đã thành lập TSMC. Mô hình kinh doanh của TSMC là một nghịch lý được thiết kế: chỉ làm gia công wafer, không sở hữu thương hiệu sản phẩm, tuyệt đối không cạnh tranh với khách hàng. TSMC chính thức ghi vào triết lý kinh doanh rằng "chúng tôi luôn định vị khách hàng là đối tác và tuyệt đối không cạnh tranh với khách hàng," đồng thời liệt kê "trung thực và chính trực" là giá trị cốt lõi cơ bản và quan trọng nhất [^13]. Chủ tịch hiện tại Ngụy Triết Gia (Wei Zhejia) đã tóm tắt một cách thẳng thắn hơn: "Bước đầu tiên để nhận được sự tin tưởng của khách hàng là không cạnh tranh với họ." [^14]

Mô hình này có thể thành công vì bản chất đơn đặt hàng gia công wafer bán dẫn là giao dịch dựa trên lòng tin. Các công ty thiết kế giao các sơ đồ mạch chưa được sản xuất, nếu bị rò rỉ sẽ hủy hoại toàn bộ năng lực cạnh tranh, cho một nhà máy gia công. Nếu nhà máy gia công có tiền sử làm nhái, hoặc có khả năng tự mình ra sản phẩm, sẽ không ai đặt hàng. Trong một quốc gia vừa bị _Newsweek_ gọi là "bến đỗ hải tặc," Trương Trung Mưu đã xây dựng một mô hình kinh doanh cần được bảo chứng bằng uy tín cấp quốc gia—niềm tin của TSMC chính là sự phủ định trực tiếp đối với hình ảnh Vương quốc Hải tặc [^1].

Đặt dòng thời gian về năm 1987, canh bạc này còn lớn hơn nhiều so với khi nhìn lại ngày nay. Xu hướng bán dẫn quốc tế chủ đạo lúc đó là mô hình sản xuất tích hợp (IDM) của Intel và Texas Instruments—tự thiết kế, tự sản xuất, tự bán sản phẩm. Không ai tin rằng một công ty chỉ sản xuất mà không thiết kế có thể tồn tại. Intel đã từ chối đầu tư vào TSMC; các đối tác châu Âu và Nhật Bản cũng lần lượt rút lui. Trương Trung Mưu đã bảo đảm cho mô hình kinh doanh chưa được kiểm chứng này bằng uy tín cá nhân trong điều kiện gần như không có đồng minh [^15]. Điều kiện kỹ thuật để mô hình gia công tồn tại là rào cản vốn của sản xuất wafer quá cao đến mức các công ty thiết kế không thể tự xây nhà máy—nhưng điều kiện kinh doanh chỉ có một từ: niềm tin.

Lợi ích của lòng tin được nhân lên theo cấp số nhân trong ba mươi năm tiếp theo. Vì không cạnh tranh với khách hàng, TSMC đồng thời trở thành nhà cung cấp cho các công ty cạnh tranh lẫn nhau như Intel, Qualcomm, Nvidia và Apple; mỗi bên đều giao những yêu cầu quy trình mật nhất vào phòng sạch của Trương Trung Mưu. Nếu TSMC tự ra sản phẩm, toàn bộ mạng lưới khách hàng này sẽ sụp đổ trong một quý. TSMC đã biến "niềm tin" thành hào kinh tế, khiến đối thủ cạnh tranh ngay cả khi bắt kịp về công nghệ cũng không thể cướp đi khách hàng, vì rủi ro chuyển nhà của khách hàng không chỉ là chi phí mà còn là nguy cơ rò rỉ bí mật [^14][^15]. Năm 2021, khi phỏng vấn Trương Trung Mưu, ông đã trả lời câu hỏi về yếu tố quan trọng nhất giúp TSMC thành công bằng một từ tiếng Anh: "trust" [^15]. Trong bản đánh giá chiến lược phát triển công ty viết tay năm 1998, trong hơn mười lựa chọn, lựa chọn duy nhất là "không làm" chính là áp dụng chiến lược giá thấp—vì giá thấp sẽ thu hút những khách hàng chỉ quan tâm đến giá cả và ăn mòn lòng tin [^15].

```tw-figure
# trust #
Yếu tố đơn lẻ quan trọng nhất giúp TSMC thành công
——Trương Trung Mưu, phỏng vấn với Tạ Kim Hà năm 2021
Nguồn: Newtalk News, 2021
```

![Mặt tiền khu nhà máy của TSMC: Năm 1987, Trương Trung Mưu thành lập TSMC, mô hình gia công wafer thuần túy được xây dựng trên lòng tin "không cạnh tranh với khách hàng," hoàn toàn tách biệt khỏi hình ảnh Vương quốc Hải tặc (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC BY 4.0)](https://upload.wikimedia.org/wikipedia/commons/3/3a/TSMC_Fab_6_front_May_2025.jpg)

![Bộ vi xử lý Intel Pentium trên wafer: Mô hình niềm tin của TSMC đưa thiết kế chip mật nhất của khách hàng vào phòng sạch; mỗi con chip trên một tấm silicon là bằng chứng vật chất của giao dịch dựa trên lòng tin (Ảnh do tác giả Wikimedia Commons cung cấp, giấy phép CC BY 2.0)](https://upload.wikimedia.org/wikipedia/commons/6/65/Wafer_with_Pentium_chips.jpg)

📝 Ghi chú của người biên tập: McDonald's và McDonald's, Tiểu Giáo Sư và Apple II, Chợ rắn và TSMC—trên cùng một hòn đảo, "sao chép" đã được rèn thành "niềm tin" trong bốn mươi năm.

## Dư âm: Vương quốc Hải tặc để lại gì cho ngày nay?

Báo cáo gỡ bỏ của Văn phòng Đại diện Thương mại Mỹ năm 2009 định nghĩa Đài Loan là "thánh địa nghiên cứu và phát triển sáng tạo" [^4]. Nhìn lại, di sản mà thời kỳ Vương quốc Hải tặc để lại là hai mặt. Mặt tích cực là năng lực kỹ thuật được mài giũa qua quá trình đảo ngược—tháo dỡ, làm nhái, thay đổi, đáp ứng tiến độ; những năng lực này đã tìm thấy lối thoát hợp pháp trong kỷ nguyên kiến trúc mở của IBM và gia công wafer, nuôi dưỡng một chuỗi ngành hoàn chỉnh từ gia công đến bán dẫn [^10][^11]. Dữ liệu ngày nay thể hiện rõ quy mô của sự đảo ngược: TSMC là một công ty chiếm hơn một nửa doanh thu gia công wafer toàn cầu, đồng thời nắm giữ phần lớn thị phần trong các quy trình tiên tiến; giá trị vốn hóa của nó từng đạt gần ba phần của tổng giá trị thị trường chứng khoán Đài Loan. Hòn đảo này, ba mươi năm trước bị chê là quốc gia hàng nhái, giờ đây các công ty thiết kế chip trên toàn thế giới tranh nhau giao bản vẽ mật nhất cho nó [^13][^14]. Mặt tiêu cực là gánh nặng niềm tin: các vụ kiện nhãn hiệu (vụ kiện McDonald's kéo dài nhiều năm mới có phán quyết), tranh chấp thương hiệu (Multitech buộc phải đổi tên) và hình ảnh quốc tế đã khiến các doanh nghiệp Đài Loan phải trả chi phí uy tín trong thị trường nước ngoài thêm hàng thập kỷ [^3][^10].

Điều đáng chú ý là hành trình từ hàng nhái đến niềm tin này không phải là một trường hợp đơn lẻ của Đài Loan. Vào thế kỷ 19, Mỹ bị người châu Âu gọi là quốc gia vi phạm bản quyền lớn nhất; Đức trong giai đoạn công nghiệp hóa ban đầu đã sản xuất hàng loạt máy móc nhái Anh và bị chính phủ Anh yêu cầu dán nhãn "Made in Germany" để phân biệt; Nhật Bản cũng trải qua giai đoạn nhái và bắt chước dày đặc trong thời kỳ kinh tế tăng trưởng sau chiến tranh [^6]. Kịch bản chung của các quốc gia là: hàng nhái là lối tắt của quá trình đuổi kịp, nhưng chỉ khi hệ thống đóng lại lối tắt đó và mở ra con đường hiện thực hóa năng lực thực sự thì ngành công nghiệp mới có thể nâng cấp. Điểm đặc biệt của Đài Loan là việc đóng và mở đường gần như diễn ra đồng thời—việc sửa đổi Luật Bản quyền năm 1992 đã buộc hàng nhái phải chuyển sang chính hãng, còn TSMC được thành lập vào năm 1987 đã định nghĩa lại uy tín sản xuất Đài Loan bằng "niềm tin"; trong năm mà một con đường đóng lại, con đường khác đang được lát ở phòng sạch Hsinchu [^9][^13].

Vương quốc Hải tặc không biến mất, nó được tái cấu trúc bởi hệ thống và mô hình kinh doanh để trở thành Vương quốc Bán dẫn. Và mỗi khi ngày nay có người chỉ trích một quốc gia là quốc gia hàng nhái mới, câu trả lời của lịch sử thường là cùng một câu: họ vẫn đang ở trong thời kỳ Vương quốc Hải tặc.

**Đọc thêm**: Nếu quan tâm đến bối cảnh tài liệu của giới hạn 6/12, có thể đọc phân tích từng từ Điều 112 trong _Giải thích Luật Bản quyền_ của Chương Trung Tín (Zhang Zhongxin), và luận án tiến sĩ năm 2015 về ngành truyện tranh Đài Loan của Lý Lệnh Nghi [^9].

## Tài liệu tham khảo

[^1]: [Taiwan Tries to Get Its Computer Pirates Off High-Tech Seas](https://www.csmonitor.com/1984/1206/120632.html) — Báo cáo ngày 6 tháng 12 năm 1984 của _The Christian Science Monitor_, ghi lại thực tế máy tính nhái Apple và hành động truy quét của chính phủ.

[^2]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — Báo cáo ngày 30 tháng 3 năm 1986 của _The New York Times_, mô tả giá Rolex nhái ở chợ rắn, ổ khóa Yeal và số vụ kiện.

[^3]: [Bản tin Đài Ích: Tài liệu tranh chấp nhãn hiệu](https://www.taie.com.tw/data/magazine/1730856057OGWXL.pdf) — Bản tin Hiệp hội Nhãn hiệu Đài Loan ghi lại các vụ kiện nhãn hiệu McDonald's và McDonald's, trong đó McDonald's từng thua sơ thẩm.

[^4]: [Đài Loan là Vương quốc Hải tặc?](https://www.chinatimes.com/newspapers/20131229000166-260209) — Chuyên mục của Vu Quốc Khâm trên _Industrial Times_, tổng hợp hồ sơ ra vào danh sách Đặc biệt 301 và đánh giá của Mỹ năm 2009.

[^5]: ['Knockoff' King Taiwan Tries to Mend Its Ways](https://www.latimes.com/archives/la-xpm-1986-09-02-fi-13692-story.html) — Báo cáo ngày 2 tháng 9 năm 1986 của hãng Reuters tại _Los Angeles Times_, trích dẫn tỷ lệ hàng nhái 60% của ITC và ý kiến của Lý Đại Kim.

[^6]: [From the Counterfeiting Capital of the World](https://scholarship.law.vanderbilt.edu/cgi/viewcontent.cgi?article=1488&context=vjtl) — Bài luận học thuật trên Vanderbilt Law Review, hồi tưởng về ngành công nghiệp hàng nhái Đài Loan và áp lực sở hữu trí tuệ của Mỹ.

[^7]: [Thời kỳ lậu bản Đài - Hồng Kông](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Tổng quan Wikipedia về hệ thống kiểm duyệt truyện tranh Nhật Bản ở Đài Loan và Hồng Kông từ những năm 1960 đến 1990 và vấn đề giấy phép xuất bản.

[^8]: [Shonen Kaiho và Chiến quốc hàng nhái](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Wikipedia ghi lại làn sóng dịch thuật sau khi mở cửa, số lượng phát hành 230.000 cuốn của _Shonen Kaiho_ và việc Đông Lập ký hợp đồng với _Akira_.

[^9]: [Giới hạn 6/12](https://zh.wikipedia.org/zh-hant/%E5%85%AD%E4%B8%80%E4%BA%8C%E5%A4%A7%E9%99%90) — Wikipedia mô tả chi tiết về sửa đổi Luật Bản quyền năm 1992, khoảng thời gian đệm Điều 112 và giới hạn vào ngày 12 tháng 6 năm 1994.

[^10]: [Bảo tàng Khoa học Công nghệ: Tổ tiên máy tính Đài Loan](https://scitechvista.nat.gov.tw/Article/c000008/detail?ID=e5ccc61e-3d6d-44a8-97ca-6bb19a390f51) — Vườn khoa học của Viện Khoa học Tự nhiên trích _Khoa học Phát triển_ số 474, ghi lại dòng sản phẩm Tiểu Giáo Sư và vụ kiện Apple bồi thường.

[^11]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — Báo cáo của _The New York Times_ đồng thời ghi lại việc hải quan giữ hàng năm 1984, IBM ký thỏa thuận xin lỗi và tiến trình sửa luật (tham khảo thêm bối cảnh trả đũa 301 tại [^4]).

[^12]: [Từ Vương quốc Hải tặc đến Thiên đường lừa đảo](http://old.observer-taipei.com/www.observer-taipei.com/article7f6f.html?id=1105) — _Observer_ số 33 hồi tưởng về sự hình thành hệ thống pháp lý sở hữu trí tuệ Đài Loan dưới Điều khoản Đặc biệt 301.

[^13]: [Giá trị cốt lõi doanh nghiệp và triết lý kinh doanh](https://www.tsmc.com/chinese/aboutTSMC/values) — Trang web chính thức của TSMC, đăng tải giá trị cốt lõi "trung thực và chính trực" và triết lý kinh doanh "tuyệt đối không cạnh tranh với khách hàng".

[^14]: [Ngụy Triết Gia: Không cạnh tranh với khách hàng là bước đầu tiên để có được lòng tin](https://www.cna.com.tw/news/afe/202402290371.aspx) — Phỏng vấn Ngụy Triết Gia trên thông tấn xã Trung ương ngày 29 tháng 2 năm 2024 về mô hình niềm tin của TSMC.

[^15]: [Tạ Kim Hà hỏi Trương Trung Mưu: Yếu tố quan trọng nhất giúp TSMC thành công](https://newtalk.tw/news/view/2021-11-02/660071) — Báo cáo ngày 2 tháng 11 năm 2021 của Newtalk News, Trương Trung Mưu trả lời "trust" và không áp dụng chiến lược giá thấp.
