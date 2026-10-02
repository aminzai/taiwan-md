---
title: 'Đài Loan công nghệ kể chuyện: Con chip 100 điểm, microphone 60 điểm'
description: 'Đài Loan làm được con chip 100 điểm, nhưng quen dùng giọng báo cáo của nhà cung cấp để nói về nó. Cùng một con chip, Qualcomm kể thành truyền thuyết, MediaTek kể thành bảng thông số kỹ thuật; NVIDIA không tự làm con nào, nhưng lợi nhuận ròng lại gấp đôi công ty sản xuất. Khoảng cách 40 điểm này, thị trường đã tính toán kỹ, và hóa đơn in chữ trên tỷ suất lợi nhuận ròng.'
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
    'đường cong hình nụ cười',
    'ý nói thầm',
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
rationale:
  why_this_hook: '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。'
  whats_excluded: '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。'
  where_it_hedges: '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。'
  whos_pushing_back: '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'
sporeLinks: []
curation: incubating
translatedFrom: Technology/台灣科技說故事.md
sourceCommitSha: 18585807b
sourceContentHash: 'sha256:056a94a81916a22b'
sourceBodyHash: 'sha256:805b10284be61867'
translatedAt: 2026-10-03T01:02:12+08:00
---

# Đài Loan công nghệ kể chuyện: Con chip 100 điểm, microphone 60 điểm

![Toàn cảnh nhà máy Fab 14B của TSMC tại Đài Nam, với kiến trúc công nghiệp nhiều tầng kéo dài dưới bầu trời xanh, là hiện trường vật lý của công suất công nghệ tiên tiến](/article-images/technology/tsmc-fab-14b-2025.webp)
_Nhà máy Fab 14B của TSMC tại Đài Nam, tháng 5 năm 2025. Ảnh: 4300streetcar. [Giấy phép qua Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Tóm tắt 30 giây:** Tháng 6 năm 2024, Jensen Huang tại nhà vận động Đại học Đài Bắc đã kể chuyện con chip do TSMC làm thành một kỷ nguyên; cùng quý đó, hội thảo tài chính của TSMC vẫn chỉ là những con số, tỷ lệ sử dụng công suất, triển vọng bảo thủ. Năm tài chính NVIDIA 2026 doanh thu 215,9 tỷ đô la Mỹ, lợi nhuận ròng 120,1 tỷ đô la[^5][^6]; TSMC, công ty làm chip cho nó, năm 2025 doanh thu 122,4 tỷ đô la, lợi nhuận ròng 55,1 tỷ đô la[^5][^6]. Công ty kết nối câu chuyện, kiếm được gấp đôi người thực hiện. Bài viết này sẽ dịch ra những lời nói đằng sau câu chuyện.

Ngày 2 tháng 6 năm 2024, nhà vận động Đại học Đài Bắc. Jensen Huang lên sân khấu mặc chiếc áo da đen nổi tiếng, nói hai tiếng đồng hồ. Cảnh dưới sân khấu giống như một đêm nhạc hòa nhạc: trực tiếp, báo chí quốc tế, mọi người cầm điện thoại. Ông nói về Blackwell, nói về CUDA, kể những trang chiếu thành buổi khai mạc của một kỷ nguyên[^19].

Trên cùng một hòn đảo, lái xe về phía nam không đầy 100 km, ở Tân Trúc. Hội thảo tài chính của TSMC có một bức tranh khác: con số tài chính, tỷ lệ sử dụng công suất, tăng hàng quý, giảm hàng năm, triển vọng bảo thủ. Tất cả các chip tiên tiến nhất trên thế giới đều ở dây trên dây chuyền sản xuất, nhưng toàn bộ bài trình bày nghe như một bài giảng về kế toán.

Cùng một con chip, hai cách kể chuyện. Khoảng cách 40 điểm ở giữa, thị trường đã tính toán kỹ.

Sự khác biệt giữa hai cảnh này, người Đài Loan thực sự đã thấy từ nhỏ. Chúng tôi quen rồi: sản phẩm là chúng tôi làm, tiếng vỗ tay là của người khác. Tại các hội chợ triển lãm, các nhà cung cấp Đài Loan nói về chi phí, nói về tỷ lệ tốt, nói về thời gian giao hàng; các thương hiệu Mỹ nói về tương lai, nói về sứ mệnh, nói về thay đổi thế giới. Khoảng cách ở giữa, đó chính là 40 điểm đó. Khoảng cách 40 điểm này trông như thế nào, bài viết này sẽ dịch cho bạn.

## Cùng một con chip, hai cách kể chuyện

Tháng 10 năm 2024, hai buổi giới thiệu sản phẩm cách nhau chưa đầy hai tuần. MediaTek giới thiệu Dimensity 9400 tại Thâm Quyến, Qualcomm tổ chức Snapdragon Summit tại Maui, Hawaii[^9][^10].

[MediaTek](economy/mediatek/) là một trong những nhà cung cấp chip điện thoại di động lớn nhất toàn cầu tính theo số lượng xuất khẩu, chiếm 70% thị phần chip TV[^4b]. Số lượng xuất khẩu của Qualcomm thấp hơn nó, nhưng doanh thu và mức giảm giá thương hiệu lại cao hơn. Sự khác biệt ở đâu? Qualcomm bán cái tên "Snapdragon": được đặt tên từ năm 2006 đến nay, đã nuôi dưỡng gần hai mươi năm[^8], có mascot riêng, có hội nghị công nghệ hàng năm riêng. Tại các buổi giới thiệu sản phẩm điện thoại thế hệ cao nhất toàn cầu, câu nói "Powered by Snapdragon" còn nổi bật hơn cả logo của nhà sản xuất điện thoại.

MediaTek bán bảng thông số kỹ thuật. Buổi giới thiệu Dimensity 9400 chứa các tiến trình, IPC, đường cong hiệu suất năng lượng, tất cả các con số đều đứng vững, vòng đánh giá đặt cho nó cái tên "Vua hiệu suất năng lượng"[^9]. Nhưng người tiêu dùng chỉ biết Snapdragon.

MediaTek thực sự đã ngồi trên ngôi vị số một về số lượng xuất khẩu. Quý thứ ba năm 2020, số lượng xuất khẩu chip điện thoại di động của MediaTek lần đầu tiên vượt Qualcomm, chiếm khoảng 31% thị phần[^7]. Nhưng trong những năm khi số lượng xuất khẩu đứng đầu, nguồn doanh thu chính của MediaTek nằm ở điện thoại di động tầm trung và thấp, phân khúc cao cấp luôn bị Qualcomm khống chế. Cho đến cuối năm 2021 khi Dimensity 9000 ra đời, MediaTek mới lần đầu tiên đưa chip tiên tiến vào bảng so sánh các điện thoại Android cao cấp của mỗi hãng. Thông số kỹ thuật đã bắt kịp, nhưng buổi giới thiệu sản phẩm vẫn giống như báo cáo của nhà cung cấp với khách hàng.

MediaTek thực sự biết vấn đề này. Những năm gần đây nó bắt đầu học tập: chip tiên tiến có tên riêng, buổi giới thiệu sản phẩm có màn khai mạc, các hãng điện thoại hợp tác cũng sẵn sàng để "Dimensity" vào trong quảng cáo. Hướng đi là đúng, chỉ là bắt đầu muộn hơn mười mấy năm. Nuôi dưỡng thương hiệu là một cuộc chạy dài, người chạy sớm sẽ được lợi thế từng vòng.

> 💡 **Bạn có biết không**
> Snapdragon là cái tên tiếng Anh của cánh gà (snapdragon flower), là tên của một loài hoa; Dimensity là ngôi sao thứ ba của Bắc Đẩu[^8]. Một công ty lấy tên từ vườn hoa, một công ty lấy từ bầu trời sao, cả hai đều rất tốt. Sự khác biệt là: Qualcomm đã nuôi dưỡng bông hoa này thành một thương hiệu đi trên tấm thảm đỏ, còn ánh sáng của Dimensity hầu hết thời gian vẫn dừng trên bảng thông số kỹ thuật.

> 📝 **Ghi chú của người sắp xếp**
> Cuộc chiến thương hiệu trong ngành chip chỉ có một điểm: người tiêu dùng chi tiền chỉ nhận ra Snapdragon hay Dimensity, không ai hỏi TSMC đã sản xuất con chip nào. Qualcomm bắt đầu nuôi dưỡng thương hiệu từ năm 2006, MediaTek chỉ gắn cái tên "Dimensity" vào chip tiên tiến từ cuối năm 2019. Hai mươi năm lợi ích lũy kế từ lời kể chuyện, bất cứ bảng thông số kỹ thuật nào cũng không thể bắt kịp.

## Quietly Brilliant là cách chết của nó

Tiếp tục đào lại một trường hợp đau đớn hơn. Ngày 7 tháng 4 năm 2011, giá trị thị trường của HTC vượt Nokia, khoảng 33,8 tỷ đô la[^1]. Lúc đó HTC chiếm khoảng 20% thị trường điện thoại di động, ngang hàng với Samsung, Apple[^2].

Trong lựa chọn công nghệ, HTC hầu như luôn đúng: năm 2008 tạo ra chiếc điện thoại Android đầu tiên G1[^3]. Trong năm 2013, One sử dụng khung thân một mảnh từ hợp kim nhôm, con đường camera pixel lớn, dual lens, tất cả đều do nó đi tiên phong. Nhưng bạn còn nhớ slogan thương hiệu toàn cầu của nó không?

![Ảnh chi tiết cạnh khung thân HTC One M7, thiết kế một mảnh từ hợp kim nhôm, là tiêu chuẩn kỹ thuật của ngành vào lúc 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), năm 2013. Ảnh: Asmoth, CC BY-SA 4.0. [Giấy phép qua Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant." - Xuất sắc yên tĩnh.

Cùng thời kỳ đó, quảng cáo của Samsung "The Next Big Thing is already here" trực tiếp quay những fan Apple xếp hàng trước cửa hàng, kéo hình ảnh những người xếp hàng thành những kẻ ngờ nghệch[^18]. HTC coi khiêm tốn là đề xuất thương hiệu, Samsung coi Apple là nhân vật phản diện chính. Hơn hai năm sau đó, giá cổ phiếu HTC lao từ con số ngàn xuống hàng trăm[^2].

HTC thực sự đã có một cơ hội phục hưng. One (M7) năm 2013 có nhiều nơi dẫn đầu ngành: khung thân một mảnh từ hợp kim nhôm, camera pixel lớn UltraPixel, loa kép phía trước BoomSound. Năm đó nó chiếm mọi giải "điện thoại của năm" từ các tờ báo lớn, nhưng doanh số bị đánh bại rất nhiều bởi S4 của Samsung cùng thời. Buổi giới thiệu M7 nói về thông số kỹ thuật, Samsung nói về phong cách sống, Apple kể giải pháp nhận dạng vân tay thành thay đổi thế giới. Cùng một thế hệ điện thoại, ba cách kể chuyện, ba số phận.

Nhìn lại nguyên nhân thua của HTC, tất nhiên không chỉ là một câu slogan. Nhưng mất phần kể chuyện là hạt giống ngã đầu tiên: khi thị trường bắt đầu lựa chọn phe camps qua câu chuyện, phía không kể được câu chuyện sẽ bị cho vào rổ "sắp lỗi thời". Kỹ sư không tin cái này, cảm thấy sản phẩm sẽ nói. Sản phẩm quả thực sẽ nói, chỉ là hầu hết người tiêu dùng không hiểu, cũng không muốn nghe.

![Hình ảnh HTC Dream mở khiếp bàn phím trượt, chiếc G1 Android toàn cầu đầu tiên năm 2008](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), năm 2008. Ảnh: Marcus Sümnick, CC BY 3.0. [Giấy phép qua Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Ghi chú của người sắp xếp**
> Bản thân "Quietly Brilliant" đã là một bản dịch của lời nói thầm: một công ty chọn "sự yên tĩnh" làm lý do thương hiệu toàn cầu, tương đương với tự nguyện bàn giao quyền kể chuyện. Bảng thông số kỹ thuật sẽ bị quên lãng, câu chuyện sẽ được nhớ đến. HTC đã làm đúng mọi lựa chọn công nghệ, nhưng thua mọi lựa chọn kể chuyện.

## Đường cong hình nụ cười: Người Đài Loan 30 năm trước đã vẽ sẵn bản đồ tình huống của mình

Bi kịch của HTC không phải là một trường hợp cô lập, nó có bằng chứng hình ảnh.

Năm 1992, Stan Shih vẽ "đường cong hình nụ cười" trong cuốn sách "Tái tạo Acer": nghiên cứu và phát triển cùng với thương hiệu ở hai đầu, giá trị cao nhất, sản xuất ở giữa, giá trị thấp nhất[^4]. Người Đài Loan tự vẽ cái biểu đồ này, rồi ba mươi năm tiếp theo, đội quân chính của ngành công nghệ Đài Loan bị mắc kẹt tại điểm thấp nhất của đường cong: Foxconn lắp ráp iPhone cho Apple, tỷ lệ lợi nhuận gộp hàng năm chỉ có chữ số đơn[^11]. Apple lấy được phần lớn lợi nhuận của toàn bộ ngành công nghệ điện thoại, ước tính cao nhất của nghiên cứu thị trường vượt quá 80%[^11].

[TSMC](/vi/economy/tsmc/) là ngoại lệ đó. Nó dựa trên "không thiết kế sản phẩm riêng của mình" một điều cấm kỵ này, đã biến sản xuất hợp đồng thành một kinh doanh từng lấy được hai đầu: khách hàng không thể rời khỏi nó, nó cũng không cần phải cạnh tranh với khách hàng vì sự tôn sùng của người tiêu dùng. Nhưng kinh doanh này được xây dựng trên sự tin tưởng B2B, không cần phải kể chuyện với công chúng. Sự yên tĩnh của TSMC là chiến lược kinh doanh, tác dụng phụ là: nơi làm chip tốt nhất Đài Loan, chính xác là nơi không cần phải luyện tập kể chuyện.

Cũng không phải không ai quay sang phía bên phải. ASUS tạo ra thương hiệu phụ ROG (Cộng hòa của Gamers) vào năm 2006, biến những người chơi game thành một cộng đồng nhận dạng thương hiệu, mắt kẻ phản bội là một trong những nhãn hiệu nhận dạng phần cứng chơi game cao nhất trên thế giới[^15]. Nhưng ROG là thiểu số: hầu hết các công ty Đài Loan, kể cả logo trên mặt trước của sản phẩm cũng không dám phóng to.

Phía bên phải của đường cong, Đài Loan thực sự đã đứng lên rồi. Acer từng là một trong ba thương hiệu máy tính cá nhân lớn nhất toàn cầu, bốn chữ cái Acer (宏碁) đã dán trên khắp các cửa lên máy bay trên thế giới. Nhưng lợi nhuận từ máy tính cá nhân quá mỏng, mỏng đến độ giảm giá thương hiệu không đủ sức chống đỡ sự nặng nề ở phía bên phải. ROG chứng minh phía bên phải đứng được, chỉ là phải chọn đúng chiến trường.

Điều tàn nhẫn nhất của đường cong hình nụ cười, là nó là một câu hỏi lựa chọn không ai kiểm tra lại trong ba mươi năm. Ba mươi năm trước Đài Loan chọn đứng ở giữa, vì đó là câu trả lời hợp lý nhất lúc đó: không có vốn, không có thương hiệu, không có thị trường, sản xuất hợp đồng là con đường sống duy nhất. Điều thực sự nguy hiểm, là tiếp tục lấy câu trả lời hợp lý ba mươi năm trước, thành câu trả lời ngày hôm nay.

## Kinh tế học của việc khoe khoang

Con số là thành thực nhất. Năm tài chính NVIDIA 2026 (tháng 2 năm 2025 đến tháng 1 năm 2026) doanh thu 215,9 tỷ đô la Mỹ, lợi nhuận ròng 120,1 tỷ đô la[^5]. TSMC năm 2025 toàn năm doanh thu 122,4 tỷ đô la Mỹ, lợi nhuận ròng 55,1 tỷ đô la[^6]. Hầu như tất cả các chip của NVIDIA được giao cho TSMC sản xuất, nó tự bán hệ sinh thái CUDA, là "thời đại AI" này câu chuyện. Kết quả: công ty kết nối câu chuyện, doanh thu gấp 1,8 lần công ty thực hiện, lợi nhuận ròng gấp 2,2 lần.

Cùng một chuỗi cung ứng, đi lên phía người tiêu dùng, độ dốc còn dốc hơn:

| Vị trí chuỗi cung ứng    | Doanh thu 2025   | Lợi nhuận ròng | Tỷ suất lợi nhuận |
| ------------------------ | ---------------- | -------------- | ----------------- |
| Foxconn (lắp ráp iPhone) | 8,1 nghìn tỷ NT$ | 189,4 tỷ NT$   | 2,3%              |
| Apple (bán iPhone)       | 416,2 tỷ đô la   | 112 tỷ đô la   | 26,9%             |
| TSMC (sản xuất chip)     | 122,4 tỷ đô la   | 55,1 tỷ đô la  | 45,0%             |
| NVIDIA (kể chuyện)       | 215,9 tỷ đô la   | 120,1 tỷ đô la | 55,6%             |

_Dữ liệu: Foxconn và Apple là năm tài chính 2025, NVIDIA là FY2026 (đến tháng 1 năm 2026), TSMC là năm 2025, lấy từ báo cáo tài chính của mỗi công ty (được kiểm chứng chéo qua cột báo cáo tài chính Wikipedia)[^5][^6][^11]._

Sản xuất kiếm 2,3%, bán thương hiệu kiếm 26,9%, tự tay sản xuất công nghệ tiên tiến kiếm 45%, kể chuyện chip thành kỷ nguyên kiếm 55,6%. Định giá là chiết khấu của dòng tiền tương lai. Tương lai một nửa là kỹ thuật làm ra, một nửa là kể ra. Văn hóa mặc định của Silicon Valley là fake it till you make it (dùm cái trước, rồi nghĩ cách làm). Văn hóa mặc định của Đài Loan là "chưa làm được, không dám nói". Sự khác biệt giữa hai văn hóa không phải sự khác biệt đạo đức, là sự khác biệt tỷ suất chiết khấu: thị trường chiết khấu ít cho "câu chuyện có thể nói được", chiết khấu nhiều cho "thứ không thể nói được".

Cơ chế giảm giá thương hiệu cũng rất thẳng thắn: cùng một con chip được TSMC sản xuất, dán logo Snapdragon lên, nhà sản xuất điện thoại sẵn sàng trả thêm tiền đó chính là giảm giá. Giảm giá đến từ đâu? Từ cảnh trong buổi giới thiệu sản phẩm, từ Summit hàng năm định kỳ, từ kỳ vọng thói quen của nhà phát triển rằng "con chip Snapdragon tiếp theo chắc sẽ nhanh hơn". Những thứ này không đi vào bảng thông số kỹ thuật, nhưng chúng đi vào báo cáo tài chính.

Có người nói, lỗi ở thị trường, là Wall Street đang gây sốt. Nhưng trên cùng một thị trường, TSMC lại không bị chiết khấu: tỷ suất lợi nhuận ròng của TSMC 45%, cao hơn cả Apple. Thị trường thực sự rất sẵn sàng trả tiền cho khả năng của Đài Loan, điều kiện là khả năng đó phải được kể ra được. Khách hàng của TSMC đã kể cho nó: mỗi buổi giới thiệu sản phẩm Apple, mỗi buổi GTC của NVIDIA, đều là quảng cáo miễn phí cho TSMC.

Có người hỏi, nếu kể chuyện lớn, có phải là nói dối không? Câu trả lời của Jensen Huang được viết trong báo cáo tài chính: mỗi câu anh ấy nói, đằng sau đều có công suất, tỷ lệ tốt, lượng xuất khẩu hỗ trợ. Ranh giới giữa biết kể chuyện và khoe khoang, là sau khi kể xong có hay không có gì đó chứng minh. Đài Loan có, chỉ là quên nói thôi.

> ⚠️ **Góc nhìn gây tranh cãi**
> Một bên nói, lời kể chuyện 60 điểm của Đài Loan là đức hạnh: mạch máu kinh doanh sản xuất hợp đồng là sự tin tưởng, sự yên tĩnh là tài sản; nếu TSMC cứ tổ chức buổi giới thiệu sản phẩm suốt ngày, khách hàng sẽ ngủ không được. Bên khác nói, giảm giá từ lời kể chuyện sẽ truyền dẫn một cách có hệ thống: các công ty Đài Loan bị định giá thấp, lương theo đó bị định giá thấp, những người tài năng sẽ đi đến các công ty biết kể chuyện, thế hệ tiếp theo sản phẩm từ đó sẽ kể chuyện còn không được. Bạn tin phía nào, sẽ sống trong vòng lặp đó. Hiện tại cả hai lập luận vẫn còn sống, cũng chưa có bên nào thắng.

## Đài Loan không phải không biết kể chuyện

Những người kể chuyện giỏi, Đài Loan thực sự đều có.

Morris Chang năm 2021 gọi TSMC là "Núi thần hộ nước"[^12]. Bốn chữ, để toàn bộ Đài Loan sẵn sàng nhường đất, nước, điện cho ngành công nghiệp chip. Đây là một cái tên ở mức cao nhất trong lịch sử tiếp thị: từ nay mỗi tin tức thiếu nước thiếu điện, tự động trở thành quảng cáo công ích "Núi thần cần bạn". Cuối năm 2024, Morris Chang hơn chín mươi tuổi xuất bản tập II tự truyện, bán thành sách bán chạy nhất[^13b].

Sự kiện tự truyện bán thành sách bán chạy nhất, chính nó giải thích được vấn đề: một doanh nhân hơn chín mươi tuổi, viết cả đời của mình thành hai tập sách, người Đài Loan xếp hàng mua. Người Đài Loan yêu nghe chuyện, cũng yêu mua chuyện, chỉ là khi tới lúc mình lên sân khấu kể thôi, lời nói lại ngắn.

Nhóm người Đài Loan biết kể chuyện này, lý lịch có điểm chung: Morris Chang làm việc tại Texas Instruments hai mươi lăm năm, Jensen Huang khởi nghiệp ở Silicon Valley ba mươi năm, Lisa Su học tập tại MIT đến bằng tiến sĩ. Không ai trong số họ luyện tập được kỹ năng này ở Đài Loan. Đất Đài Loan trồng được những người như vậy, nhưng nơi làm việc của Đài Loan không dạy cái này. Trường học dạy vẽ mạch điện đúng, không dạy kể mạch điện thành kỷ nguyên.

Nên câu hỏi không bao giờ ở khả năng. Vấn đề là cấu trúc ngành công nghiệp Đài Loan đã gửi những người biết kể chuyện sang nước ngoài, hoặc gửi vào phòng họp của sản xuất hợp đồng. Để mở khóa điều này, chỉ dựa vào các bộ phận tiếp thị của vài công ty không đủ, phải từ quản trị công ty, cấu trúc lương, tất cả cho đến giáo dục trường học.

![Ảnh Morris Chang dưới vai trò lãnh đạo đại diện tham dự hội nghị trực tuyến Lãnh đạo Kinh tế APEC năm 2021, ảnh chính thức của tổng thống phủ](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang tham dự Hội nghị Lãnh đạo Kinh tế APEC năm 2021. Ảnh: Wang Yu Ching / Tổng thống Phủ, CC BY 2.0. [Giấy phép qua Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Stan Shih vẽ đường cong hình nụ cười, cũng là trong việc bán khái niệm: một khái niệm để triết lý quản lý doanh nghiệp của ông được toàn bộ các trường kinh doanh trên thế giới trích dẫn.

Jensen Huang sinh ra tại Đài Nam, chín tuổi đi Mỹ[^13]. Lisa Su sinh ra tại Đài Nam, ba tuổi đi Mỹ[^14]. Hai người khoẻ nhất kể chuyện bán dẫn trên thế giới, đều là hạt giống Đài Loan, đất Mỹ.

![Ảnh Jensen Huang đang giảng dạy khóa học CS 153 tại Đại học Stanford, mặc áo da đen nổi tiếng, hai tay ra hiệu minh họa](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang bài giảng tại Đại học Stanford CS 153, tháng 4 năm 2026. Ảnh: Anderseidesvik, CC BY-SA 4.0. [Giấy phép qua Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Trong công ty khởi nghiệp Đài Loan cũng có những người biết kể chuyện. Gogoro thành lập năm 2011, năm 2015 tại CES kể trạm trao đổi pin thành "mạng lưới năng lượng", nói mình là công ty năng lượng, nhân tiện bán xe máy. Câu chuyện hay đến độ năm 2022 cho phép nó qua SPAC lên sàn chứng khoán Nasdaq, năm 2024 cả Castrol của BP còn đầu tư năm mươi triệu đô la[^16]. Gogoro cho đến nay vẫn còn tìm vòng lặp kinh doanh, nhưng ví dụ của nó nói rõ: biết kể chuyện, ít nhất cũng được tấm vé để được thị trường kiểm tra. Không biết kể, cả cửa cũng không vào được.

Quy luật rõ ràng: Đài Loan không thiếu tài năng kể chuyện, thiếu môi trường cho phép kích to câu chuyện. Gene sản xuất hợp đồng dạy là "khách hàng là nhân vật chính", môi trường kể chuyện dạy là "tôi có thể là nhân vật chính".

> 📝 **Ghi chú của người sắp xếp**
> Nơi đáng để chơi với bốn chữ "Núi thần hộ nước" nhất: khi Morris Chang nói nó, nó là kể cho xã hội Đài Loan một câu chuyện cần được hỗ trợ: cần điện, cần nước, cần đất, cần nhân tài. Kể chuyện không phải là sự tự mãn, là cơ sở hạ tầng chính sách công nghiệp. Người Đài Loan nghe hiểu bốn chữ này, có nghĩa là năng lực kể chuyện của Đài Loan không bị hỏng, chỉ là hiếm khi sử dụng ra ngoài.

## Bảng so sánh ý nói thầm

Cùng một sự kiện kỹ thuật, hai cách nói. Dịch ý nói đằng sau lời nói ra, sự khác biệt tự thấy.

| Người nói                            | Lời nói bề ngoài                                                                                      | Ý nói thầm dịch ra                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hội thảo tài chính TSMC              | "Tỷ lệ sử dụng công suất tiếp tục hồi phục, chúng tôi duy trì tự tin trong tăng trưởng dài hạn."      | Chỉ có tôi làm được chip tiên tiến nhất thế giới, nhưng nói thẳng như vậy là không giống kỹ sư lắm.                                                          |
| Báo cáo kỹ sư Đài Loan               | "Công nghệ này vẫn có một chút không gian để tối ưu hóa."                                             | Chúng tôi đã làm được số một thế giới, nhưng trước tiên hạ giá 20%, tránh bị tấn công.                                                                       |
| Pitch trang đầu khởi nghiệp Mỹ       | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."            | Hiện tại công ty chỉ có ba kỹ sư và một slide PowerPoint, nhưng ước mơ vô giá, vui lòng cho tiền.                                                            |
| Pitch trang đầu khởi nghiệp Đài Loan | "Thành viên đội ngũ tốt nghiệp từ NTU/NCTU/NTHU, từng làm việc tại MediaTek 8 năm, 12 bằng sáng chế." | Chúng tôi không biết nói tầm nhìn, trước tiên dùng bằng cấp học vấn như áo chống đạn.                                                                        |
| Jensen Huang                         | "The more you buy, the more you save."                                                                | Chiếc card này mắt đắt, nhưng nếu không mua, chi phí điện và xếp hàng tính toán sẽ ăn hơn.                                                                   |
| Hội thảo Snapdragon của Qualcomm     | "The era of on-device AI begins now."                                                                 | Chạy điểm chờ iPhone ra rồi nói, trước tiên cho bạn cảm giác bạn đang chứng kiến kỷ nguyên.                                                                  |
| Quảng cáo HTC 2010                   | "Quietly Brilliant"                                                                                   | Chúng tôi rất xuất sắc, nhưng xin lỗi không dám nói to.                                                                                                      |
| Quảng cáo Samsung 2011               | "The Next Big Thing is already here."                                                                 | Những người xếp hàng trước cửa hàng Apple trông thực sự ngu dốt, đến mua của tôi.                                                                            |
| Elon Musk                            | "We will make life multiplanetary."                                                                   | Tên lửa hiện tại thỉnh thoảng nổ, nhưng câu chuyện phải cất cánh trước.                                                                                      |
| Morris Chang 2021                    | "Bán dẫn là Núi thần hộ nước của Đài Loan."                                                           | Bốn chữ, để toàn bộ Đài Loan nhường đất, nhường nước, nhường điện cho chip. Người Đài Loan biết kể chuyện một câu, bằng một cả năm slide hội thảo tài chính. |

_Trong bảng, các hàng TSMC, kỹ sư Đài Loan, hai hàng khởi nghiệp, và Qualcomm là tổng quát hóa ý nói của những phát biểu điển hình, không phải trích dẫn chính xác từng chữ; năm hàng Jensen Huang, HTC, Samsung, Musk, Morris Chang là slogan công khai thực tế hoặc phát biểu[^17][^18][^12]._

Sau khi dịch bạn sẽ thấy rõ, sự khác biệt giữa kể chuyện giỏi và kể chuyện tệ, hầu hết thời gian chỉ là hai cách sắp xếp từ của cùng một sự kiện.

Bảng này không phải để chế nhạo ai. Sự khiêm tốn trong kỹ thuật rất hữu ích: nó để hợp tác đi đúng đắn, để kiểm soát chất lượng không dám nới lỏng. Nhưng khiêm tốn một khi bước ra khỏi phòng họp, lại trở thành phiếu chiết khấu. Đài Loan cần học, là giữ khiêm tốn trong phòng thí nghiệm, đưa tự tin lên sân khấu.

## Quay lại nhà vận động Đại học Đài Bắc

Mỗi slide Jensen Huang nói tối hôm đó, hiện trường vật lý đều ở Tân Trúc, Đài Trung, Đài Nam trong những phòng sạch. Câu chuyện kể xong, toàn thế giới mua. Người trong phòng sạch tiếp tục ca trực, hội thảo tài chính tiếp tục bảo thủ.

Công nghệ 100 điểm không tự động trở thành kể chuyện 100 điểm. Những điểm 40 kia cần có ai đó lên sân khấu, mặc áo da thành chiếc áo giáp, kể chip thành kỷ nguyên.

Núi thần hộ nước tiếp theo của Đài Loan, có thể không phải con chip mới nào, là câu chuyện mới nào.

> ✦ Qualcomm nuôi dưỡng một con SoC thành một thương hiệu đi trên tấm thảm đỏ, Jensen Huang kể con chip do TSMC sản xuất thành kỷ nguyên, Morris Chang dùng bốn chữ để cho toàn bộ Đài Loan nhường đất cho bán dẫn. Đài Loan công nghệ có 100 điểm, thiếu người sẵn sàng lên sân khấu, kể nó thành 100 điểm.

---

**Đọc thêm**:

- [Ngành công nghiệp bán dẫn: Từ chuyển giao công nghệ RCA đến GaN và đóng gói lượng tử - cách mạng vật liệu 50 năm](/vi/technology/taiwan-semiconductor-industry/) — Lời kể chuyện công nghệ hoàn chỉnh của Núi thần hộ nước, cũng như chiếc dây buộc "NVIDIA độc quyền hóa công suất CoWoS"
- [Đài Loan Doanh nghiệp: TSMC](/vi/economy/tsmc/) — Công ty này đã viết sự kín đáo vào mô hình kinh doanh, cơ cấu quản trị và tài chính
- [Đài Loan Doanh nghiệp: MediaTek](/vi/economy/mediatek/) — Nhà cung cấp chip điện thoại di động lớn nhất toàn cầu, tại sao lời kể chuyện vẫn đang theo đuổi
- [Đài Loan Doanh nghiệp: HTC](/vi/economy/htc-android-pioneer-vr-transformation/) — Lịch sử doanh nghiệp hoàn chỉnh của cái chết "Quietly Brilliant"
- [Jensen Huang](/vi/people/jensen-huang/) — Sinh ra tại Đài Nam, lớn lên tại Mỹ, người kể chuyện chip tốt nhất trên thế giới
- [NVIDIA tại Đài Loan](/vi/technology/nvidia-in-taiwan/) — Mối quan hệ giữa cái áo da đó và chuỗi cung ứng Đài Loan
- [Computex: Ba triển lãm máy tính quốc tế lớn, còn lại cái duy nhất lớn trên Đài Bắc](/vi/technology/computex/) — Mỗi tháng 5, những tập đoàn AI toàn cầu luân phiên lên sân khấu Đài Bắc dùng cùng một bộ kịch bản kể chuyện

## Nguồn hình ảnh

Bài viết này sử dụng 5 hình ảnh có giấy phép CC, được lưu trữ tại `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Ảnh: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Ảnh: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Ảnh: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Ảnh: Wang Yu Ching / Tổng thống Phủ, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Ảnh: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Tài liệu tham khảo

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — Ngày 7 tháng 4 năm 2011 giá trị thị trường của HTC khoảng 33,8 tỷ đô la, vượt Nokia

[^2]: [Wikipedia — HTC](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Năm 2011 thị phần điện thoại di động khoảng 20%, giá trị thị trường vượt quá một triệu tỷ NT$, giá cổ phiếu từng đứng trên một ngàn NT$

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — Năm 2008 chiếc điện thoại Android toàn cầu đầu tiên

[^4]: [Wikipedia — Đường cong hình nụ cười](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Stan Shih đề xuất trong cuốn sách "Tái tạo Acer" năm 1992

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Nhà cung cấp SoC điện thoại di động lớn nhất toàn cầu tính theo số lượng xuất khẩu; thị phần chip TV khoảng 70%

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Bản tin chính thức của NVIDIA; doanh thu FY2026 215,9 tỷ đô la Mỹ, lợi nhuận ròng 120,1 tỷ đô la (kiểm chứng chéo cột báo cáo tài chính Wikipedia: https://en.wikipedia.org/wiki/Nvidia)

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Trang nhà đầu tư chính thức của TSMC; toàn năm 2025 doanh thu 122,42 tỷ đô la Mỹ, lợi nhuận ròng 55,13 tỷ đô la (kiểm chứng chéo cột báo cáo tài chính Wikipedia: https://en.wikipedia.org/wiki/TSMC)

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Quý thứ ba năm 2020 số lượng xuất khẩu chip điện thoại di động của MediaTek lần đầu tiên vượt Qualcomm, thị phần khoảng 31%

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Nền tảng SoC Snapdragon công bố tháng 11 năm 2006; nguồn gốc tên thương hiệu từ tên hoa cánh gà, Dimensity lấy từ ngôi sao thứ ba của Bắc Đẩu (hai cách đặt tên là dữ liệu công khai của thương hiệu, chờ bổ sung liên kết nguồn chính thức)

[^9]: [MediaTek — Thông cáo báo chí Dimensity 9400](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 công bố tháng 10 năm 2024; vòng đánh giá phổ biến vì hiệu suất năng lượng xuất sắc (mô tả tổng quát). Xem [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200) để biết thông tin về thiết bị sử dụng đầu tiên

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 được tổ chức tại đảo Maui, Hawaii, công bố Snapdragon 8 Elite (URL bản tin chính thức đã hết hạn, lấy nguồn thứ cấp từ Wikipedia)

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) ／ [Wikipedia — Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Doanh thu năm tài chính 2025 của Foxconn 8.103 triệu tỷ NT$, lợi nhuận ròng 189,35 tỷ NT$ (tỷ suất lợi nhuận khoảng 2,3%); Doanh thu FY2025 của Apple 416,2 tỷ đô la, lợi nhuận ròng 112 tỷ đô la (tỷ suất lợi nhuận khoảng 26,9%). Tỷ lệ lợi nhuận iPhone của Apple giai đoạn cao điểm vượt quá 80%: ước tính hàng năm của Counterpoint (chờ bổ sung liên kết nguồn)

[^12]: [Wikipedia — Núi thần hộ nước](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Biệt danh của TSMC (Silicon Shield); "Bán dẫn là Núi thần hộ nước của Đài Loan" là phát biểu công khai của Morris Chang năm 2021 (chờ bổ sung liên kết nguồn báo chí)

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Sinh năm 1963 tại Đài Nam, năm 1972 (lúc 9 tuổi) di cư đến Mỹ

[^13b]: Tập II tự truyện của Morris Chang công bố tháng 11 năm 2024, doanh số ở mức sách bán chạy nhất của năm đó (chờ bổ sung liên kết nguồn)

[^14]: [Wikipedia — Lisa Su](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Sinh năm 1969 tại Đài Nam, ba tuổi di cư cùng gia đình sang Mỹ

[^15]: [Wikipedia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Năm 2006 tạo lập thương hiệu phụ "Cộng hòa của Gamers" (ROG)

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Thành lập năm 2011; năm 2015 công bố Gogoro Smartscooter và Mạng lưới năng lượng tại CES; năm 2022 sát nhập với SPAC Poema Global lên sàn chứng khoán Nasdaq; năm 2024 BP's Castrol tuyên bố đầu tư tối đa năm mươi triệu đô la

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — "The more you buy, the more you save" của Jensen Huang từ video chính thức sự kiện này

[^18]: "Quietly Brilliant" là slogan thương hiệu toàn cầu của HTC từ năm 2009, "The Next Big Thing is Already Here" là slogan quảng cáo Galaxy của Samsung năm 2011, "We will make life multiplanetary" là tuyên bố sứ mệnh của SpaceX (cả ba là các văn bản kinh doanh công khai)

[^19]: [NVIDIA at Computex 2024 — Video bài giảng chính thức](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Bài giảng chính thức của Jensen Huang tại Computex ngày 2 tháng 6 năm 2024 tại nhà vận động Đại học Đài Bắc
