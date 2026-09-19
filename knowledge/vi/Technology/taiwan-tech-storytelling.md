---
title: 'Khoa học công nghệ Đài Loan kể chuyện: Chip đạt 100 điểm, micro chỉ được 60 điểm'
description: 'Đài Loan làm ra những con chip tuyệt vời nhưng lại quen dùng giọng điệu của bản thuyết trình nhà cung cấp để nói về chúng. Cùng một con chip, Qualcomm tô vẽ thành thần thoại, MediaTek mô tả bằng bảng thông số; NVIDIA không tự tay làm bất cứ thứ gì, nhưng lợi nhuận ròng lại gấp đôi bên gia công. Khoảng cách 40 điểm này thị trường đã tính toán từ lâu, và hóa đơn đó được in trên tỷ suất lợi nhuận ròng.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'công nghệ',
    'kể chuyện',
    'thương hiệu',
    'bán dẫn',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'đường cong nụ cười',
    'ẩn ý',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-15
lastHumanReview: false
difficulty: 'beginner'
readingTime: 16
image: '/article-images/technology/tsmc-fab-14b-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg'
rationale: "{'why_this_hook': '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。', 'whats_excluded': '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。', 'where_it_hedges': '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。', 'whos_pushing_back': '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'}"
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '6d762f5ac'
sourceContentHash: 'sha256:7e79f4d7834c55c1'
sourceBodyHash: 'sha256:e24305e511c42507'
translatedAt: '2026-09-14T00:53:30+08:00'
---

# Khoa học công nghệ Đài Loan kể chuyện: Chip đạt 100 điểm, micro chỉ được 60 điểm

![Hình ảnh nhà máy Fab 14B của TSMC tại Khu khoa học Tainan, nhiều tòa nhà công nghiệp trải dài dưới bầu trời xanh, là hiện trường vật lý của năng lực sản xuất tiên tiến](/article-images/technology/tsmc-fab-14b-2025.webp)
_Nhà máy Fab 14B của TSMC ở Tainan, tháng 5 năm 2025. Ảnh: 4300streetcar. Giấy phép qua Wikimedia Commons._

> **Tóm tắt 30 giây:** Tháng 6 năm 2024, Jensen Huang đã biến con chip của TSMC thành một kỷ nguyên tại Nhà thi đấu Đại học Đài Loan; trong cùng quý đó, buổi báo cáo tài chính của TSMC lại chỉ là những con số tài chính, tỷ lệ sử dụng công suất và triển vọng thận trọng. NVIDIA đạt doanh thu 215,9 tỷ USD và lợi nhuận ròng 120,1 tỷ USD cho năm tài khóa 2026; TSMC, bên gia công chip cho họ, có doanh thu 122,4 tỷ USD và lợi nhuận ròng 55,1 tỷ USD trong năm 2025[^5][^6]. Công ty kể chuyện kiếm được gấp đôi người trực tiếp làm ra sản phẩm. Bài viết này muốn lật mở những lời nói đằng sau câu chữ.

Ngày 2 tháng 6 năm 2024, tại Nhà thi đấu Đại học Đài Loan. Jensen Huang mặc chiếc áo da đen bước lên sân khấu và thuyết trình suốt hai giờ. Khán giả đông như một buổi hòa nhạc: truyền hình trực tiếp, báo chí nước ngoài, biển người giơ điện thoại. Ông nói về Blackwell, nói về CUDA, biến từng trang slide thành màn khai mạc của một kỷ nguyên[^19].

Trên cùng một hòn đảo, cách đó chưa đầy trăm km về phía Nam là Hsinchu. Buổi báo cáo tài chính của TSMC lại mang một phong cách khác: những con số tài chính, tỷ lệ sử dụng công suất, tăng giảm hàng quý, và khoảng triển vọng thận trọng. Những con chip tiên tiến nhất thế giới đều nằm trên dây chuyền sản xuất đó, nhưng toàn bộ buổi thuyết trình nghe giống như một tiết học kế toán.

Cùng một con chip, hai cách kể chuyện. 40 điểm chênh lệch kia thị trường đã tính sổ từ lâu.

Sự khác biệt giữa hai bối cảnh này thực ra người Đài Loan nhìn thấy từ nhỏ đến lớn. Chúng ta quen với: sản phẩm là do chúng ta làm, còn tràng pháo tay là của người khác. Tại các triển lãm, gian hàng của các nhà cung cấp Đài Loan nói về chi phí, tỷ lệ tốt và thời hạn giao hàng; sân khấu của các thương hiệu Mỹ lại nói về tương lai, sứ mệnh và sự thay đổi thế giới. Khoảng cách giữa hai bên chính là 40 điểm đó. Bài viết này sẽ lật mở cho bạn xem 40 điểm đó trông như thế nào.

## Cùng một con chip, hai cách kể chuyện

Tháng 10 năm 2024, hai buổi ra mắt diễn ra chưa đầy hai tuần sau nhau. MediaTek giới thiệu Dimensity 9400 tại Thâm Quyến, còn Qualcomm tổ chức Snapdragon Summit tại đảo Maui, Hawaii[^9][^10].

[MediaTek](/vi/economy/mediatek/) là một trong những nhà cung cấp chip điện thoại lớn nhất thế giới tính theo sản lượng xuất xưởng, chiếm bảy phần mười thị trường chip TV[^4b]. Về sản lượng xuất xưởng, Qualcomm vượt trội hơn MediaTek, nhưng về doanh thu và lợi thế thương hiệu thì lại thắng. Khác biệt ở đâu? Qualcomm bán cái tên "Snapdragon": được đặt từ năm 2006 đến nay đã gần hai mươi năm[^8], có linh vật riêng, lễ hội công nghệ hàng năm của mình. Cụm từ "Powered by Snapdragon" tại các buổi ra mắt điện thoại cao cấp toàn cầu còn nổi bật hơn cả thương hiệu của nhà sản xuất điện thoại.

MediaTek bán bảng thông số kỹ thuật. Buổi giới thiệu Dimensity 9400 tập trung vào quy trình, IPC và đường cong hiệu năng; tất cả các con số đều vững chắc, được giới đánh giá phong tặng danh xưng "Vua Hiệu Năng"[^9]. Nhưng người tiêu dùng chỉ quen biết Snapdragon.

Ngai vàng sản lượng xuất xưởng, MediaTek thực ra đã từng ngồi qua. Trong quý 3 năm 2020, sản lượng chip điện thoại của MediaTek lần đầu tiên vượt qua Qualcomm, chiếm khoảng ba mươi mốt phần trăm[^7]. Nhưng trong những năm dẫn đầu về sản lượng đó, nguồn thu chính của MediaTek đến từ các dòng máy tầm trung và thấp; đỉnh cao của dòng flagship luôn là Qualcomm. Cho đến khi Dimensity 9000 ra mắt cuối năm 2021, MediaTek mới lần đầu tiên đưa chip flagship vào bảng so sánh của các điện thoại Android cao cấp. Thông số đã đuổi kịp, nhưng buổi giới thiệu vẫn giống như một bài thuyết trình của nhà cung cấp với khách hàng.

MediaTek thực sự biết vấn đề này. Những năm gần đây họ bắt đầu học hỏi: chip flagship cần có tên riêng, và buổi ra mắt cần có màn trình diễn mở màn; các hãng điện thoại hợp tác cũng sẵn lòng đưa "Dimensity" vào khẩu hiệu quảng cáo. Hướng đi là đúng, chỉ là khởi hành muộn hơn mười mấy năm. Việc xây dựng thương hiệu là một cuộc chạy marathon, người bắt đầu sớm mỗi vòng đều đang hưởng lợi kép.

> 💡 **Bạn có biết không**
> Snapdragon là tên tiếng Anh của hoa kim ngân (snapdragon flower); Dimensity là ngôi sao thứ ba trong chòm sao Bắc Đẩu[^8]. Một bên đặt tên theo loài hoa, một bên đặt tên theo bản đồ sao, đều rất hay. Khác biệt là: Qualcomm đã nuôi dưỡng bông hoa này thành một thương hiệu đi thảm đỏ, còn ánh sáng của ngôi sao Dimensity phần lớn vẫn dừng lại trên bảng thông số kỹ thuật.

> 📝 **Ghi chú biên tập viên**
> Cuộc chiến thương hiệu trong ngành chip vô cùng tàn nhẫn: khi người tiêu dùng chi tiền thì họ nhận ra Snapdragon hay Dimensity, chứ không ai hỏi TSMC đã gia công con nào. Qualcomm bắt đầu xây dựng thương hiệu từ năm 2006, còn MediaTek mới gắn dòng "Dimensity" vào flagship cuối năm 2019. Lợi suất kể chuyện hai mươi năm không gì theo kịp được một bảng thông số kỹ thuật.

## Sự lấp lánh thầm lặng đã chết như thế nào

Quay lại một trường hợp đau đớn hơn nữa. Ngày 7 tháng 4 năm 2011, giá trị của HTC vượt qua Nokia, khoảng 33,8 tỷ USD[^1]. Khi đó, HTC chiếm khoảng hai mươi phần trăm thị trường điện thoại, cùng với Samsung và Apple là bộ ba lớn[^2].

Về lựa chọn công nghệ, HTC gần như làm đúng tất cả: ra mắt chiếc điện thoại Android đầu tiên G1 vào năm 2008[^3]. Dòng One năm 2013 với thân máy hợp kim nhôm nguyên khối, camera độ phân giải lớn và hai ống kính, đều là những thứ họ đi trước. Nhưng bạn còn nhớ khẩu hiệu thương hiệu toàn cầu của họ không?

![Ảnh chụp cận cảnh bên hông HTC One M7, thiết kế nguyên khối bằng hợp kim nhôm, là tiêu chuẩn công nghệ trong ngành khi ra mắt năm 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), năm 2013. Ảnh: Asmoth, CC BY-SA 4.0. Giấy phép qua Wikimedia Commons._

"Quietly Brilliant." Sự xuất sắc thầm lặng.

Cùng thời điểm đó, quảng cáo của Samsung "The Next Big Thing is already here" (Điều vĩ đại tiếp theo đã ở đây) trực tiếp chụp cảnh người hâm mộ Apple xếp hàng trước cửa hàng, biến những người đang xếp hàng thành kẻ ngốc[^18]. HTC coi sự khiêm tốn là tuyên ngôn thương hiệu, còn Samsung lại xem Apple là nhân vật phản diện. Hơn hai năm sau, giá cổ phiếu của HTC từ trên nghìn đồng lao dốc xuống trăm đồng[^2].

HTC thực ra đã có một cơ hội lật ngược tình thế. Nhiều điểm vượt trội của One (M7) năm 2013: thân máy hợp kim nhôm nguyên khối, camera UltraPixel độ phân giải lớn, loa kép BoomSound phía trước. Năm đó họ giành được danh hiệu "Điện thoại của năm" từ các phương tiện truyền thông lớn, nhưng doanh số lại kém xa Samsung S4 cùng thời. Buổi ra mắt M7 nói về thông số kỹ thuật, Samsung nói về lối sống, còn Apple biến tính năng nhận diện vân tay thành sự thay đổi thế giới. Cùng một dòng điện thoại, ba cách kể chuyện, ba số phận khác nhau.

Nhìn lại nguyên nhân thất bại của HTC, tất nhiên không chỉ là một khẩu hiệu. Nhưng việc đánh mất câu chuyện là quân cờ đầu tiên bị đổ: khi thị trường bắt đầu lựa chọn phe bằng câu chuyện, bên nào không kể được chuyện thì bị đưa vào giỏ "sắp lỗi thời". Các kỹ sư không tin điều này, họ nghĩ sản phẩm sẽ tự lên tiếng. Sản phẩm quả thực có thể lên tiếng, nhưng đa số người tiêu dùng không nghe hiểu và cũng không muốn nghe.

![Ảnh HTC Dream mở bàn phím trượt, chiếc điện thoại Android đầu tiên trên thế giới G1](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), năm 2008. Ảnh: Marcus Sümnick, CC BY 3.0. Giấy phép qua Wikimedia Commons._

> 📝 **Ghi chú biên tập viên**
> "Quietly Brilliant" tự nó đã là một bản dịch ẩn ý: việc một công ty chọn "khiêm tốn" làm tuyên ngôn thương hiệu toàn cầu, đồng nghĩa với việc chủ động giao quyền kể chuyện. Bảng thông số kỹ thuật sẽ bị lãng quên, còn câu chuyện thì được ghi nhớ. HTC đã làm đúng mọi lựa chọn về kỹ thuật, nhưng lại thua trong mọi lựa chọn về tự sự.

## Đường cong nụ cười: Người Đài Loan vẽ ra tình thế của mình 30 năm trước

Bi kịch của HTC không phải là trường hợp đơn lẻ, nó có bằng chứng.

Năm 1992, Thi Trân Vinh (施振榮) đã vẽ ra "Đường cong Nụ cười" trong cuốn _Tái tạo Acer_: Nghiên cứu và phát triển và thương hiệu ở hai đầu, giá trị cao nhất; sản xuất ở giữa, giá trị thấp nhất[^4]. Người Đài Loan tự vẽ bức tranh này, và suốt ba mươi năm tiếp theo, đội ngũ công nghệ Đài Loan đã bị mắc kẹt ở điểm thấp nhất của đường cong: Foxconn lắp ráp iPhone cho Apple, tỷ suất lợi nhuận gộp thường chỉ là một chữ số. Apple lấy đi phần lớn lợi nhuận của ngành điện thoại, ước tính nghiên cứu thị trường chiếm hơn tám mươi phần trăm[^11].

[TSMC](/vi/economy/tsmc/) là ngoại lệ. Họ dựa trên quy tắc "không tự thiết kế sản phẩm" để biến việc gia công thành một nghề kinh doanh nắm giữ cả hai đầu: khách hàng không thể rời xa họ, nhưng họ cũng không cần tranh giành sự sùng bái của người tiêu dùng với khách hàng. Nhưng ngành này được xây dựng trên lòng tin B2B, không cần kể chuyện cho đại chúng. Sự khiêm tốn của TSMC là chiến lược kinh doanh, tác dụng phụ là: nơi Đài Loan giỏi nhất về chip lại chính là nơi không cần luyện tập kể chuyện nhất.

Cũng không phải không có ai vươn lên phía bên phải. Wistek (華碩) thành lập thương hiệu phụ ROG (Republic of Gamers - Quốc gia Game thủ) vào năm 2006, tạo ra một cộng đồng người chơi game nhận diện thương hiệu, và là một trong những dấu hiệu được công nhận về phần cứng eSports trên toàn cầu[^15]. Nhưng ROG chỉ là thiểu số: logo của đa số các công ty Đài Loan thậm chí còn không dám phóng to ở mặt trước sản phẩm.

Ở phía bên phải của đường cong, Đài Loan thực sự đã đứng lên. Acer từng là một trong ba thương hiệu PC hàng đầu thế giới, năm chữ cái này từng được dán trên cổng lên máy bay tại khắp nơi trên thế giới. Nhưng lợi nhuận của ngành PC quá mỏng, mỏng đến mức không đủ sức gánh trọng lượng ở phía bên phải. ROG đã chứng minh rằng có thể đứng vững ở phía bên phải, nhưng cần chọn đúng chiến trường.

Điểm tàn nhẫn nhất của Đường cong Nụ cười là nó là một câu hỏi trắc nghiệm mà ba mươi năm qua chưa ai xem xét lại. Ba mươi năm trước Đài Loan chọn đứng ở giữa, bởi vì đó là câu trả lời hợp lý nhất lúc bấy giờ: không có vốn, không có thương hiệu, không có thị trường, gia công là con đường sống duy nhất. Điều thực sự nguy hiểm là tiếp tục coi câu trả lời hợp lý của ba mươi năm trước là câu trả lời cho ngày hôm nay.

## Kinh tế học của việc khoe mẽ

Con số là thành thật nhất. NVIDIA đạt doanh thu 215,9 tỷ USD và lợi nhuận ròng 120,1 tỷ USD cho năm tài khóa 2026 (từ tháng 2 năm 2025 đến tháng 1 năm 2026)[^5]. TSMC có doanh thu toàn năm 2025 là 122,4 tỷ USD và lợi nhuận ròng 55,1 tỷ USD[^6]. Hầu hết chip của NVIDIA đều được giao cho TSMC sản xuất; họ bán hệ sinh thái CUDA, bán câu chuyện về "kỷ nguyên AI". Kết quả: công ty kể chuyện có doanh thu gấp 1,8 lần công ty trực tiếp làm ra sản phẩm, và lợi nhuận ròng gấp 2,2 lần.

Trên cùng một chuỗi cung ứng, khi đi lên đến đầu người tiêu dùng, độ dốc càng lớn:

| Vị trí trong Chuỗi Cung Ứng | Doanh thu năm 2025  | Lợi nhuận ròng  | Tỷ suất lợi nhuận ròng |
| :-------------------------- | :------------------ | :-------------- | :--------------------- |
| Foxconn (lắp ráp iPhone)    | 8,1 nghìn tỷ Đài tệ | 189,4 tỷ Đài tệ | 2.3%                   |
| Apple (bán iPhone)          | 416,2 tỷ USD        | 112 tỷ USD      | 26.9%                  |
| TSMC (sản xuất chip)        | 122,4 tỷ USD        | 55,1 tỷ USD     | 45.0%                  |
| NVIDIA (kể chuyện)          | 215,9 tỷ USD        | 120,1 tỷ USD    | 55.6%                  |

_Dữ liệu: Foxconn và Apple cho năm tài khóa 2025; NVIDIA cho FY2026 (tính đến tháng 1 năm 2026); TSMC cho năm 2025, lấy từ báo cáo tài chính của các công ty (đã đối chiếu chéo với cột báo cáo tài chính trên Wikipedia)[^5][^6][^11]._

Người lắp ráp kiếm được 2.3%, người bán thương hiệu kiếm được 26.9%, người làm sản xuất tiên tiến kiếm được 45%, còn người biến chip thành kỷ nguyên kiếm được 55.6%. Định giá là sự chiết khấu dòng tiền tương lai. Một nửa tương lai do kỹ thuật tạo ra, một nửa do câu chuyện kể ra. Văn hóa mặc định của Thung lũng Silicon là "giả vờ cho đến khi làm được" (fake it till you make it). Văn hóa mặc định của Đài Loan là "chưa làm được nên không dám nói". Khoảng cách giữa hai nền văn hóa này không phải là khoảng cách đạo đức, mà là khoảng cách tỷ suất chiết khấu: thị trường ít giảm giá đối với "câu chuyện có thể kể", nhưng lại giảm nhiều đối với "năng lực không thể kể".

Cơ chế lợi thế thương hiệu cũng rất trực diện: cùng một con chip do TSMC gia công, số tiền mà nhà sản xuất điện thoại sẵn lòng trả thêm khi dán nhãn Snapdragon chính là phần lợi thế. Lợi thế này đến từ đâu? Từ sự hoành tráng của buổi ra mắt, từ các Summit cố định hàng năm, từ kỳ vọng mang tính thói quen của giới lập trình viên rằng "Snapdragon tiếp theo chắc chắn sẽ nhanh hơn". Những thứ này không có trong bảng thông số kỹ thuật, nhưng chúng có trong báo cáo tài chính.

Có người nói đây là lỗi của thị trường, là sự thao túng của Phố Wall. Nhưng cùng một thị trường, TSMC lại không bị giảm giá: tỷ suất lợi nhuận ròng của TSMC là 45%, cao hơn Apple một bậc. Thị trường thực ra rất sẵn lòng trả tiền cho năng lực của Đài Loan, với điều kiện năng lực đó phải được kể ra. Khách hàng của TSMC đã nói hộ họ: mỗi buổi ra mắt của Apple, mỗi sự kiện GTC của NVIDIA đều là quảng cáo miễn phí cho TSMC.

Có người hỏi, việc tô vẽ câu chuyện lớn có trở thành lừa đảo không? Câu trả lời của Jensen Huang nằm trong báo cáo tài chính: mọi lời ông nói đều được hỗ trợ bởi năng lực sản xuất, tỷ lệ tốt và sản lượng xuất xưởng. Ranh giới giữa kể chuyện và khoe mẽ là sau khi kể xong liệu có thứ gì giữ vững nó hay không. Đài Loan có thứ đó, chỉ là thường quên nói ra.

> ⚠️ **Quan điểm gây tranh cãi**
> Một phe cho rằng, sự tự sự 60 điểm của Đài Loan là một đức tính: mạch sống của ngành gia công là lòng tin, khiêm tốn là tài sản; nếu TSMC ngày nào cũng tổ chức buổi thuyết trình thì khách hàng sẽ không ngủ được. Phe còn lại nói rằng việc định giá thấp về mặt tự sự sẽ lan truyền có hệ thống: các công ty Đài Loan bị đánh giá thấp, mức lương cũng bị đánh giá thấp, nhân tài chảy vào các doanh nghiệp biết kể chuyện, và thế hệ sản phẩm tiếp theo càng khó kể chuyện hơn. Bạn tin phe nào thì sẽ sống trong vòng lặp đó. Hai quan điểm này hiện vẫn tồn tại và chưa có bên nào chiến thắng.

## Đài Loan không phải là không biết kể chuyện

Người kể chuyện giỏi, Đài Loan thực sự có.

Morris Chang (張忠謀) đã gọi TSMC là "Núi thần hộ quốc" vào năm 2021[^12]. Bốn chữ này khiến toàn bộ người dân Đài Loan sẵn lòng nhường đường, nhường nước, nhường điện cho ngành bán dẫn. Đây là một cái tên đỉnh cao trong lịch sử tiếp thị: từ đó trở đi, mỗi tin tức về thiếu nước hay mất điện đều tự động biến thành quảng cáo nhân đạo "Núi thần cần bạn". Cuối năm 2024, Morris Chang xuất bản tập hai cuốn tự truyện của mình và nó lại bán chạy[^13b].

Việc cuốn tự truyện bán chạy đã nói lên vấn đề: một doanh nhân gần chín mươi tuổi viết cả cuộc đời mình thành hai cuốn sách, người Đài Loan xếp hàng mua. Người Đài Loan thích nghe chuyện, cũng thích mua câu chuyện, nhưng khi đến lượt mình đứng trên sân khấu, lời lại ngắn ngủi.

Nhóm người Đài Loan biết kể chuyện này có một điểm chung trong hồ sơ: Morris Chang đã làm việc tại Texas Instruments hai mươi lăm năm; Jensen Huang khởi nghiệp ở Thung lũng Silicon ba mươi năm; Su Zifan (蘇姿丰) học tiến sĩ tại MIT. Không ai trong số họ được rèn luyện kỹ năng này tại Đài Loan. Đất đai của Đài Loan có thể nuôi dưỡng những người như vậy, nhưng môi trường làm việc của Đài Loan lại không dạy điều đó. Trường học dạy vẽ đúng mạch điện, chứ không dạy cách biến mạch điện thành một kỷ nguyên.

Vì vậy, vấn đề chưa bao giờ là tài năng. Vấn đề là cấu trúc công nghiệp của Đài Loan đã đưa những người biết kể chuyện ra nước ngoài, hoặc nhốt họ vào phòng họp gia công. Để gỡ nút thắt này, chỉ dựa vào bộ phận tiếp thị của vài công ty là không đủ, mà phải cải cách từ quản trị doanh nghiệp, cơ cấu lương thưởng cho đến giáo dục trường học.

![Ảnh Jensen Huang tham dự Hội nghị Lãnh đạo Kinh tế APEC năm 2021 với tư cách đại diện lãnh đạo, ảnh chính thức của Phủ Tổng thống](/article-images/technology/morris-chang-apec-2021.webp)
_Jensen Huang tham dự Hội nghị Lãnh đạo Kinh tế APEC năm 2021. Ảnh: Wang Yu Ching / Phủ Tổng thống, CC BY 2.0. Giấy phép qua Wikimedia Commons._

Thi Trân Vinh vẽ Đường cong Nụ cười cũng là đang bán một khái niệm: một khái niệm đã khiến triết lý quản lý doanh nghiệp của ông được các trường kinh doanh trên toàn thế giới trích dẫn.

Jensen Huang sinh ra ở Tainan, đi Mỹ năm 9 tuổi[^13]. Su Zifan sinh ra ở Tainan, đi Mỹ năm 3 tuổi[^14]. Hai người giỏi kể chuyện về bán dẫn nhất thế giới đều mang gốc Đài Loan và máu Mỹ.

![Ảnh Jensen Huang thuyết trình trong khóa học CS 153 tại Đại học Stanford, mặc chiếc áo da đen đặc trưng, hai tay ra hiệu giải thích](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang thuyết trình trong khóa học CS 153 tại Đại học Stanford, tháng 4 năm 2026. Ảnh: Anderseidesvik, CC BY-SA 4.0. Giấy phép qua Wikimedia Commons._

Trong các startup của Đài Loan cũng có người biết kể chuyện. Gogoro thành lập vào năm 2011, và vào năm 2015 đã biến trạm đổi pin tại CES thành "mạng lưới năng lượng", tự nhận là công ty năng lượng và tiện thể bán xe máy. Câu chuyện này được lan truyền đến năm 2022 khi họ niêm yết trên Nasdaq thông qua SPAC, và năm 2024 Castrol thuộc BP cũng đầu tư 50 triệu USD[^16]. Gogoro cho đến nay vẫn đang tìm kiếm vòng khép kín về kinh doanh, nhưng ví dụ của nó cho thấy: biết kể chuyện thì ít nhất có được tấm vé để thị trường kiểm chứng. Người không biết kể thì ngay cả cánh cổng cũng không vào được.

Quy luật rất rõ ràng: Đài Loan không thiếu tài năng kể chuyện, mà thiếu môi trường cho phép câu chuyện được kể lớn. Ngành gen gia công dạy "khách hàng là nhân vật chính", còn môi trường kể chuyện dạy "tôi có thể là nhân vật chính".

> 📝 **Ghi chú biên tập viên**
> Điểm đáng thú vị nhất của bốn chữ "Núi thần hộ quốc" là: khi Morris Chang nói về nó, ông đang nói với xã hội Đài Loan một câu chuyện cần được ủng hộ: cần điện, cần nước, cần đất, cần nhân tài. Kể chuyện không phải là sự phù phiếm, mà là cơ sở hạ tầng chính sách công nghiệp. Người Đài Loan hiểu bốn chữ này, đại diện cho năng lực tự sự của người Đài Loan chưa xấu đi, chỉ là ít khi được sử dụng ra bên ngoài.

## Bảng đối chiếu bản dịch ẩn ý

Cùng một sự thật kỹ thuật, hai cách nói. Hãy lật mở những lời đằng sau câu chữ và tự mình so sánh.

| Người nói                                 | Lời nói bề mặt                                                                                                                                                                                                     | Bản dịch ẩn ý                                                                                                                                                                           |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Báo cáo tài chính TSMC                    | "Tỷ lệ sử dụng công suất tiếp tục tăng, chúng tôi tự tin vào sự tăng trưởng dài hạn."                                                                                                                              | Con chip tiên tiến nhất thế giới chỉ có mình tôi làm được, nhưng nói ra câu này thì không giống kỹ sư.                                                                                  |
| Bài thuyết trình của kỹ sư Đài Loan       | "Công nghệ này vẫn còn một số không gian để tối ưu hóa."                                                                                                                                                           | Chúng ta đã đạt hạng nhất thế giới rồi, nên giảm giá 20% trước để tránh bị vả mặt.                                                                                                      |
| Trang đầu tiên pitch của startup Mỹ       | "We are building the world's first AI-native platform to reinvent a $5 trillion industry." (Chúng tôi đang xây dựng nền tảng bản địa AI đầu tiên trên thế giới để tái tạo một ngành công nghiệp 5 nghìn tỷ đô la.) | Hiện tại công ty chỉ có ba kỹ sư và một bài PPT, nhưng giấc mơ vô giá, xin hãy cho tiền trước.                                                                                          |
| Trang đầu tiên pitch của startup Đài Loan | "Nhóm thành viên tốt nghiệp từ Đại học Quốc gia Đài Loan/Đại học Khoa học và Công nghệ Đài Loan, đã làm việc tại MediaTek tám năm, sở hữu 12 bằng sáng chế."                                                       | Chúng tôi không biết nói về tầm nhìn, nên dùng bằng cấp và kinh nghiệm như áo giáp chống đạn.                                                                                           |
| Jensen Huang                              | "The more you buy, the more you save." (Bạn mua càng nhiều, bạn tiết kiệm càng nhiều.)                                                                                                                             | Chiếc thẻ này rất đắt, nhưng nếu bạn không mua, hóa đơn điện và năng lực tính toán sẽ ăn hết.                                                                                           |
| Snapdragon Summit của Qualcomm            | "The era of on-device AI begins now." (Kỷ nguyên AI trên thiết bị bắt đầu từ bây giờ.)                                                                                                                             | Cứ đợi iPhone ra rồi nói tiếp, trước đã làm cho bạn cảm thấy mình đang chứng kiến một kỷ nguyên.                                                                                        |
| Quảng cáo HTC 2010                        | "Quietly Brilliant" (Xuất sắc thầm lặng)                                                                                                                                                                           | Chúng tôi rất brilliant, nhưng xin lỗi, không dám nói to.                                                                                                                               |
| Quảng cáo Samsung 2011                    | "The Next Big Thing is already here." (Điều vĩ đại tiếp theo đã ở đây.)                                                                                                                                            | Những người xếp hàng trước cửa hàng Apple trông thật ngốc nghếch, hãy đến mua của tôi đi.                                                                                               |
| Elon Musk                                 | "We will make life multiplanetary." (Chúng ta sẽ làm cho sự sống đa hành tinh.)                                                                                                                                    | Tên lửa đôi khi bị nổ, nhưng câu chuyện phải cất cánh trước đã.                                                                                                                         |
| Morris Chang 2021                         | "Bán dẫn là Núi thần hộ quốc của Đài Loan."                                                                                                                                                                        | Bốn chữ này khiến toàn bộ người Đài Loan nhường đường, nhường nước, nhường điện cho bán dẫn. Một câu nói của người Đài Loan biết kể chuyện có giá trị hơn cả một năm báo cáo tài chính. |

_Các dấu ngoặc kép trong bảng là sự khái quát hóa các lời nói điển hình, không phải trích dẫn từng chữ; các cột Jensen Huang, HTC, Samsung, Musk, Morris Chang là các khẩu hiệu hoặc phát biểu công khai thực tế[^17][^18][^12]._

Sau khi dịch, bạn sẽ thấy sự khác biệt giữa việc kể chuyện tốt và kể chuyện dở thường chỉ nằm ở hai thứ tự từ của cùng một sự thật.

Bảng này không nhằm mục đích chế giễu ai. Sự khiêm tốn rất hữu ích trong kỹ thuật: nó giúp hợp tác tiếp diễn, giúp bộ phận quản lý chất lượng không dám nới lỏng tiêu chuẩn. Nhưng khi sự khiêm tốn bước ra khỏi phòng họp, nó trở thành một phiếu giảm giá. Điều Đài Loan cần học là giữ sự khiêm tốn trong phòng thí nghiệm và mang sự tự tin lên sân khấu.

## Trở lại Nhà thi đấu Đại học Đài Loan

Mỗi trang slide mà Jensen Huang trình bày đêm đó đều được sản xuất tại các phòng sạch ở Hsinchu, Taichung và Tainan. Sau khi câu chuyện kết thúc, cả thế giới đã thanh toán. Những người trong phòng sạch tiếp tục làm việc theo ca, buổi báo cáo tài chính vẫn thận trọng.

Công nghệ 100 điểm sẽ không tự động trở thành sự tự sự 100 điểm. 40 điểm đó cần có ai đó bước lên sân khấu, mặc chiếc áo da thành chiến bào, và biến con chip thành một kỷ nguyên.

Núi thần hộ quốc tiếp theo của Đài Loan, có thể không phải là một con chip mới nào, mà là một câu chuyện mới nào.

> ✦ Qualcomm đã nuôi dưỡng một SoC trở thành thương hiệu đi thảm đỏ; Jensen Huang đã biến chip do TSMC làm ra thành một kỷ nguyên; Morris Chang dùng bốn chữ để khiến toàn bộ Đài Loan nhường đường cho bán dẫn. Công nghệ Đài Loan có những thứ đạt 100 điểm, nhưng thiếu người sẵn lòng lên sân khấu và kể nó như một sự hoàn hảo.

---

**Đọc thêm**:

- [Ngành công nghiệp bán dẫn: Cuộc cách mạng vật liệu 50 năm từ RCA sang Nitride Gallium và đóng gói lượng tử](/vi/technology/taiwan-semiconductor-industry) — Câu chuyện kỹ thuật trọn vẹn của Núi thần hộ quốc, và sự ràng buộc "NVIDIA chiếm dụng năng lực CoWoS"
- [Công ty Đài Loan: TSMC](/vi/economy/tsmc) — Quản trị và cấu trúc tài chính của công ty này đã viết sự khiêm tốn vào mô hình kinh doanh.
- [Công ty Đài Loan: MediaTek](/vi/economy/mediatek) — Nhà sản xuất chip điện thoại có sản lượng xuất xưởng lớn nhất thế giới, tại sao câu chuyện vẫn đang đuổi kịp
- [Công ty Đài Loan: Wistek (華碩)](/vi/economy/htc-android-pioneer-vr-transformation) — Toàn bộ lịch sử doanh nghiệp về sự chết chóc của "Quietly Brilliant"
- [Jensen Huang](/vi/people/jensen-huang) — Sinh ra ở Tainan, lớn lên ở Mỹ, người kể chuyện chip giỏi nhất thế giới
- [NVIDIA tại Đài Loan](/vi/technology/nvidia-in-taiwan) — Mối quan hệ giữa chiếc áo da và chuỗi cung ứng Đài Loan
- [Computex: Ba triển lãm máy tính quốc tế thu được hai, cái còn lại tồn tại ở Đài Bắc](/vi/technology/computex) — Hàng năm vào tháng 5, các gã khổng lồ AI toàn cầu lần lượt kể chuyện bằng cùng một bộ lời lẽ tại Đài Bắc.

## Nguồn hình ảnh

Bài viết này sử dụng 5 hình ảnh được cấp phép CC, lưu trữ trong `public/article-images/technology/`:

- [TSMC Fab 14B Tháng 5 năm 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Ảnh: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Ảnh: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream mở](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Ảnh: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang tại APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Ảnh: Wang Yu Ching / Phủ Tổng thống, CC BY 2.0, Wikimedia Commons
- [Jensen Huang tại Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Ảnh: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Tài liệu tham khảo

[^1]: [The Free Library — Vốn hóa thị trường HTC vượt qua Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — Ngày 7 tháng 4 năm 2011, vốn hóa của HTC khoảng 33,8 tỷ USD, vượt qua Nokia.

[^2]: [Wikipedia — Wistek (華碩)](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Thị phần điện thoại vào năm 2011 khoảng 20%, giá trị thị trường vượt nghìn tỷ Đài tệ, giá cổ phiếu từng đạt trên nghìn đồng.

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — Chiếc điện thoại Android đầu tiên trên thế giới vào năm 2008.

[^4]: [Wikipedia — Đường cong Nụ cười](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Đề xuất bởi Thi Trân Vinh vào năm 1992 trong cuốn _Tái tạo Acer_.

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Một trong những nhà cung cấp SoC điện thoại lớn nhất thế giới tính theo sản lượng; chiếm khoảng bảy phần mười thị trường chip TV.

[^5]: [Nvidia — Báo cáo tài chính Quý 4 và Năm Tài khóa 2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Thông cáo báo chí chính thức của NVIDIA; Doanh thu FY2026 là 215,9 tỷ USD, lợi nhuận ròng 120,1 tỷ USD (đã đối chiếu chéo với cột báo cáo tài chính trên Wikipedia: https://en.wikipedia.org/wiki/Nvidia）).

[^6]: [TSMC — Kết quả Quý 4 năm 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Trang nhà đầu tư chính thức của TSMC; Doanh thu toàn năm 2025 là 122,4 tỷ USD, lợi nhuận ròng 55,1 tỷ USD (đã đối chiếu chéo với cột báo cáo tài chính trên Wikipedia: https://en.wikipedia.org/wiki/TSMC）).

[^7]: [Counterpoint — MediaTek trở thành nhà cung cấp chipset điện thoại lớn nhất trong Quý 3 năm 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Sản lượng chip điện thoại của MediaTek lần đầu tiên vượt qua Qualcomm trong quý 3 năm 2020, chiếm khoảng 31%.

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Nền tảng SoC Snapdragon được công bố vào tháng 11 năm 2006; tên thương hiệu lấy từ hoa kim ngân và ngôi sao thứ ba trong chòm sao Bắc Đẩu (hai cách đặt tên là tài liệu công khai của thương hiệu, đang chờ liên kết nguồn chính thức).

[^9]: [MediaTek — Thông cáo báo chí Dimensity 9400](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 được ra mắt vào tháng 10 năm 2024; giới đánh giá phổ biến khen ngợi hiệu năng năng lượng (mô tả tổng hợp). Các mẫu điện thoại đầu tiên sử dụng xem tại [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200).

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 được tổ chức tại Maui, Hawaii; công bố Snapdragon 8 Elite (URL thông cáo báo chí chính thức đã hết hạn, dựa trên Wikipedia cũ).

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — / [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Doanh thu năm tài khóa 2025 của Foxconn là 8,103 nghìn tỷ Đài tệ, lợi nhuận ròng 189,35 tỷ Đài tệ (tỷ suất lợi nhuận ròng khoảng 2.3%); Doanh thu FY2025 của Apple là 416,2 tỷ USD, lợi nhuận ròng 112 tỷ USD (tỷ suất lợi nhuận ròng khoảng 26.9%). Giai đoạn đỉnh cao lợi nhuận điện thoại của Apple chiếm hơn tám mươi phần trăm: ước tính hàng năm của Counterpoint (đang chờ liên kết nguồn)

[^12]: [Wikipedia — Núi thần hộ quốc](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Tên gọi khác của TSMC (Shield Silicon); "Bán dẫn là Núi thần hộ quốc của Đài Loan" là phát biểu công khai của Morris Chang năm 2021 (đang chờ liên kết nguồn báo chí).

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Sinh ra ở Tainan vào năm 1963, di cư sang Mỹ năm 1972 (khi 9 tuổi).

[^13b]: Tập hai cuốn tự truyện của Morris Chang được xuất bản vào tháng 11 năm 2024 và bán chạy như sách bán chạy trong năm (đang chờ liên kết nguồn).

[^14]: [Wikipedia — Su Zifan (蘇姿丰)](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Sinh ra ở Tainan vào năm 1969, di cư sang Mỹ cùng gia đình khi 3 tuổi.

[^15]: [Wikipedia — Wistek (華碩)](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Thành lập thương hiệu phụ "Republic of Gamers" (ROG) vào năm 2006.

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Thành lập vào năm 2011; ra mắt Gogoro Smartscooter và mạng lưới năng lượng tại CES năm 2015; niêm yết trên Nasdaq thông qua SPAC với Poema Global vào năm 2022; Castrol thuộc BP tuyên bố đầu tư tối đa 50 triệu USD vào năm 2024.

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — "The more you buy, the more you save" của Jensen Huang được trích từ video chính thức tại sự kiện này.

[^18]: "Quietly Brilliant" là khẩu hiệu thương hiệu toàn cầu của HTC từ năm 2009; "The Next Big Thing is Already Here" là khẩu hiệu quảng cáo Galaxy của Samsung năm 2011; "We will make life multiplanetary" là tuyên bố sứ mệnh của SpaceX (cả ba đều là văn bản thương mại công khai).

[^19]: [NVIDIA tại Computex 2024 — Video diễn thuyết chủ đề chính thức](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Bài diễn thuyết chủ đề chính của Jensen Huang tại Nhà thi đấu Đại học Đài Loan ngày 2 tháng 6 năm 2024.
