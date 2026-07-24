---
title: 'Một bài viết được hình thành như thế nào: Quy trình sáu giai đoạn của Taiwan.md nhằm chống lại bản năng viết lách của AI (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)'
description: 'Mỗi bài viết bạn đọc trên Taiwan.md đều đầy ắp cảm xúc, giàu bối cảnh và có thể kiểm chứng; đằng sau đó là 6 giai đoạn, hơn 20 chốt chặn không được phép bỏ qua, cùng một ban biên tập AI không bao giờ tự viết bản thảo. Lý do duy nhất sự cỗ máy này tồn tại là để khắc phục những lỗi mà AI thường mắc phải nhất: sắp xếp sự thật theo trình tự thời gian khi vừa tìm thấy, tạo ra những câu văn "nhựa" vô nghĩa, dịch ngược tóm tắt tiếng Anh thành trích dẫn giả, hay bị nhiễm thói quen xấu khi đọc lại các bài viết cũ. Đây là bài viết phân tích quy trình này, và chính nó cũng là sản phẩm được tạo ra từ quy trình đó.'
date: 2026-06-19
tags:
  [
    'about',
    'meta',
    'phương pháp luận viết lách',
    'curation',
    'rewrite-pipeline',
    'editorial',
    'semiont',
    'AI writing',
  ]
author: 'Taiwan.md'
category: 'About'
readingTime: 11
featured: false
lastVerified: 2026-06-19
lastHumanReview: false
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a213  3e5738f'
translatedAt: '2026-07-24T12:35:28+08:00'
---

# Một bài viết được hình thành như thế nào: Quy trình sáu giai đoạn của Taiwan.md nhằm chống lại bản năng viết lách của AI (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **Tổng quan trong 30 giây:** Mỗi bài viết bạn đọc trên Taiwan.md đều vận hành theo một quy trình sáu giai đoạn: hình thành quan điểm, tiến hành tìm kiếm, viết kết bài trước, kiểm chứng từng chữ, bổ sung hình ảnh trực quan và thiết lập liên kết hai chiều. Quy trình này không phải là "quy trình viết bài hay" thông thường; mỗi chốt chặn của nó đều nhắm thẳng vào một lỗi mà AI thường mắc phải: sắp xếp sự thật theo trình tự thời gian khi vừa tìm thấy, tạo ra những câu văn "nhựa" vô nghĩa, dịch ngược tóm tắt tiếng Anh thành trích dẫn giả, hay bị nhiễm thọc xấu khi đọc lại các bài viết cũ. Bài viết này phân tích quy trình đó, và chính nó cũng là sản phẩm được tạo ra từ quy trình này.

Vào lúc 19:53 ngày 18 tháng 6 năm 2026, một bản commit đã lặng lẽ đi vào nhánh main. Một bài viết về ban nhạc ba người của Đài Loan mang tên "Elephant Gymnastics" (Đại Tượng Thể Thao) đã được lên sóng: gồm 5.604 chữ Hán, 56 chú thích, và 11 tiêu đề phụ theo phong cách bối cảnh[^1]. Tại thời điểm đó, không có ai ngồi trước máy tính cả. Đó là kết quả từ guồng quay routine của Taiwan.md, tự nó hoàn thiện và tự nó "ship" vào ban đêm khi không có người trực.

Nhưng trước bản commit đó, bài viết này đã trải qua gần 100 lượt tìm kiếm, đọc qua 59 nguồn tài liệu, và bị 12 lần kiểm chứng bác bỏ cách viết ban đầu. Nó đã đi qua 6 giai đoạn, vượt qua hơn 20 chốt chặn không thể bỏ qua, huy động cả một ban biên tập AI với sự phân công rõ ràng. Những gì bạn đang đọc là 5.604 chữ trên bề mặt. Bài viết này muốn cho bạn thấy cỗ máy nằm dưới mặt nước đó.

```tw-figure
Gần 100 lượt tìm kiếm → 1 bài viết
Nguồn tư liệu của 〈Elephant Gymnastics〉: khoảng 95 lần truy vấn, 59 nguồn, 12 lần xác minh sai lệch
Ghi chép routine của Taiwan.md, 18-06-2026
```

## Tại sao phải xây dựng một cỗ máy cho một bài viết?

Nếu bạn đưa cho AI một chủ đề và yêu cầu nó viết một bài báo, đa phần nó sẽ làm thế này: tìm kiếm sơ qua, sắp xếp các sự thật tìm được theo trình tự thời gian, mỗi đoạn thêm một câu tổng kết nghe có vẻ ý nghĩa, và kết thúc bằng một câu "tương lai sẽ tiếp tục phát triển". Loại bài viết kiểu Wikipedia đã có sẵn rồi, còn các trang "nông trại nội dung" (content farm) bằng AI thì sản xuất hàng vạn bài mỗi ngày. Taiwan.md ngay từ ngày đầu tiên đã quyết định không làm điều đó.

Vấn đề là, những thói quen xấu này là giá trị mặc định của AI, chứ không phải lỗi ngẫu nhiên. REWRITE-PIPELINE đã chia nhỏ nó thành sáu loại thất bại lặp đi lặp lại: hết token ở phần sau khiến nội dung trở nên sơ sài; thiếu các điểm kiểm tra trung gian dẫn đến chất lượng giảm sút âm thầm; để dành kết bài đến cuối cùng khiến năng lượng cạn kiệt và biến nó thành những câu rập khuôn; quy chuẩn định dạng văn bản phong phú bị quên lãng về sau; các góc độ tiếp cận khác nhau bị coi là các quy trình độc lập; và nghiêm trọng nhất là kiểu tìm thấy sự thật rồi mới quay lại nghĩ quan điểm, dẫn đến việc viết theo lối biên niên sử với mật độ thông tin mất cân bằng[^2].

Vì vậy, logic thiết kế của quy trình này rất đơn giản: mỗi loại lỗi có thể mắc phải sẽ đi kèm với một chốt chặn để ngăn nó lại. Đây không phải là một quy trình "viết lách tốt" chung chung, mà là sự đối nghịch hoàn toàn với "AI slop" (nội dung rác do AI tạo ra).

> **✦** "Wikipedia trả lời 'PTT là gì'. Taiwan.md trả lời 'Tại sao PTT xứng đáng để bạn dành 8 phút để đọc'."

Đây là diện mạo của bài viết về Elephant Gymnastics khi bước ra từ cuối quy trình:

```tw-stat
5.604 chữ | Văn bản tiếng Trung | 〈Elephant Gymnancy〉
56 | Chú thích, mỗi cái đều có thể Ctrl-F tìm thấy | Kiểm chứng sơ cấp
11 đoạn | Tiêu đề phụ theo bối cảnh, không sắp xếp theo thời gian | Nhịp điệu tự sự
12 lần | Giai đoạn nghiên cứu bác bỏ cách viết ban đầu | Ưu tiên xác minh sai lệch
Nguồn: Ghi chép routine của Taiwan.md, 18-06-2026
```

## Sáu chốt chặn, mỗi chốt ngăn một thất bại

Quy trình này gồm sáu giai đoạn từ đầu đến cuối, mọi bài viết đều phải đi qua đầy đủ, bất kể chủ đề hay độ dài.

**Giai đoạn 0: Quan điểm (Stage 0: Viewpoint)** – Phải suy nghĩ rõ ràng xem bài viết này sẽ là loại ký ức nào đối với người Đài Loan, và sức căng cốt lõi nằm ở đâu. **Giai đoạn 1: Thu thập (Stage 1: Sourcing)** – Bắt đầu tìm kiếm, toàn bài phải có ít nhất 80 lần truy vấn, và định mức được quy định cứng: nguồn tiếng Trung ít nhất 40, tiếng Anh ít nhất 20, nguồn sơ cấp ít nhất 15, nguồn phản biện ít nhất 5, nhằm ép bản thân phải đi tìm những bằng chứng trái ngược với giả thuyết ban đầu[^3]. **Giai đoạn 2: Viết (Stage 2: Writing)** – Hành động đầu tiên là viết kết bài, vì con người sẽ cạn kiệt năng lượng vào cuối quá trình; để lại phần quan trọng nhất cho lúc cuối cùng đồng nghĩa với việc giao nó cho phiên bản mệt mợ nhất của chính mình. **Giai đoạn 3: Kiểm (Stage 3: Verifying)** – Đối soát từng chữ: các phép tính, đơn vị, mỗi câu trích dẫn đều phải tìm thấy được bằng Ctrl-F trong nguồn gốc. **Giai đoạn 4: Hình (Stage 4: Formatting)** – Bổ sung yếu tố trực quan và đa phương tiện. **Giai đoạn 5: Liên (Stage 5: Linking)** – Kết nối bài viết này hai chiều với các bài viết khác trong kho tri thức.

Việc phân bổ sức lực cho sáu giai đoạn là có chủ đích. Viết bản thảo chiếm hơn 40%, nhưng tìm kiếm cộng với kiểm chứng cũng chiếm gần một nửa. Thời gian thực sự dành cho một bài viết không nằm ở việc gõ phím, mà nằm ở trước và sau khi gõ phím.

```tw-bars
Phân bổ nguồn lực cho một bài viết (Giới hạn ngân sách token mỗi giai đoạn, %)
Stage 0: Quan điểm | 12 | Suy nghĩ trước khi biên tập
Stage 1: Thu thập | 28 | Tìm kiếm ≥ 80 lần
Stage 2: Viết | 42 | Viết kết bài trước
Stage 3: Kiểm | 18 | Kiểm chứng từng chữ
Stage 4: Hình | 8 | Trực quan và đa phương tiện
Stage 5: Liên | 5 | Liên kết hai chiều
Nguồn: Ngân sách các giai đoạn của REWRITE-PIPELINE v7.5
```

## Suy nghĩ rõ ràng trước khi tìm kiếm

Trong sáu giai đoạn, điều nghịch lý nhất nằm ở giai đoạn đầu tiên.

Hầu hết cách viết của AI là "tìm thấy sự thật, rồi quay lại bổ sung quan điểm". Taiwan.md từ phiên bản v6.0 đã đảo ngược thứ tự này: Trước khi bắt tay vào tìm kiếm, hãy đứng ở góc độ của tổng biên tập để suy nghĩ rõ sáu câu hỏi: chủ đề này là ký ức gì đối với người Đài Loan, có những khía cạnh nào bị bỏ qua, và nó kết nối thế nào với lịch sử đời sống của chúng ta. Chỉ khi đã nghĩ thông suốt, mới mang theo các câu hỏi đó đi tìm kiếm và xác minh.

Tại sao thứ tự này lại quan trọng đến vậy? Có một bài viết có thể dùng làm bài học. Khi viết về Apple Cider (táo lên men), quy trình ban đầu là tìm kiếm trước, kết quả tìm được là cuộc khủng hoảng khi sản phẩm từng bị ế ẩm và suýt biến mất, khiến cả bài trở thành một câu chuyện về sự tuyệt chủng. Nhưng sau đó, người quan sát đã quay lại và chỉ ra rằng Apple Cider là một ký ức tập thể kéo dài 60 năm của người Đài Loan, từ thời kỳ nước ngọt có ga trong chai thủy tinh cho đến tận ngày nay[^4]. Nếu viết như một tin tức khủng hoảng, nghĩa là chúng ta đã nhìn nhận quy mô của ký ức quá nhỏ hẹp. Phiên bản tìm kiếm trước đã biến một kỷ niệm ấm áp thành một sự lo âu.

```tw-versus
Bản năng của AI: Tìm thấy rồi mới nói | Taiwan.md: Nghĩ trước rồi mới tìm
Tìm được đống sự thật, rồi cố ghép vào một quan điểm | Xác định quan điểm trước, mang theo câu hỏi đi tìm kiếm và xác minh
Nhồi nhét mọi sự thật vào bài, mật độ mất cân bằng | Loại bỏ những sự thật không khớp với quan chế |
Không có mỏ neo (anchor) xuyên suốt, kết bài trở nên rập khuôn | Nếu không tìm thấy mỏ neo tương ứng cho quan điểm thì phải quay lại nghĩ lại
Viết thành nhật ký doanh nghiệp hoặc sơ yếu lý lịch nhân vật | Viết thành một câu chuyện khiến người ta phải thốt lên "Hóa ra là vậy"
Nguồn: Stage 0 Quan điểm của REWRITE-PIPELINE v7.5
```

## Tìm kiếm: Viết báo cáo nghiên cứu như viết luận văn

Khi quan điểm đã định, mới bắt đầu tìm kiếm. Việc tìm kiếm của Taiwan.md có hai con số cứng: một bài viết chuyên sâu phải trải qua ít nhất 80 lần truy vấn toàn bộ quá trình, và định mức nguồn tài liệu được quy định chặt chẽ: tiếng Trung ít nhất 40, tiếng Anh ít nhất 20, nguồn sơ cấp ít nhất 15, nguồn quan điểm đối lập ít nhất 5. Mục cuối cùng là thứ dễ bị bỏ qua nhất do lười biếng; nó ép người viết phải đi tìm những bằng chứng mâu thuẫn với giả thuyết của chính mình, thay vì chỉ chọn lọc những gì ủng hộ nó.

Tìm xong không có nghĩa là chỉ cần đưa bản tóm tắt vào bài là xong. Đằng sau mỗi bài chuyên sâu là một báo cáo nghiên cứu tương đương với luận văn nghiên cứu, chia thành tám chương: Quan điểm, Nhật ký tìm kiếm, Các phát hiện theo chủ đề, Kho trích dẫn, Phản ví dụ và rào chắn, Gói sự thật sạch cho người viết, Danh mục tham khảo kèm bảng kiểm tra, và chương cuối cùng là báo cáo gốc không sót một chữ của từng agent nghiên cứu. Có một quy tắc nghe rất khắt khe: nếu đã tìm kiếm nhưng không ghi lại dấu vết gốc vào báo cáo, thì coi như chưa tìm. Báo cáo mới chính là nguồn sự thật của bài viết này; nó phải vượt qua kiểm định của một công cụ: số nguồn không trùng lặp ít nhất 25, nguồn tiếng Anh không được bằng 0, nguồn sơ cấp không được bằng 0[^9]. Nếu không đạt, bài viết đó thậm chí không có tư cách để đặt bút viết.

```tw-stat
≥ 80 lần | Độ sâu tìm kiếm của một bài chuyên sâu | Trung 40／Anh 20／Sơ cấp 15／Đối lập 5
8 đoạn | Cấu trúc báo cáo nghiên cứu | Tương đương luận văn nghiên cứu
≥ 25 nguồn | Nguồn không trùng lặp (vượt qua kiểm định công cụ) | Anh ≠ 0, Sơ cấp ≠ 0
Nguồn: REWRITE-PIPELINE v7.5 Step 1.1 / 1.7
```

Với các vấn đề gây tranh cãi, cần thêm một bước nữa. Khi viết về chính trị, quan điểm lịch sử hay chính sách, chúng tôi sẽ cử riêng một agent "phản biện" chuyên đi tìm những nguồn có lập trường trái ngược với bài viết nhưng vẫn có lý lẽ thuyết phục; mỗi nguồn đều phải kèm theo URL, nếu không gom đủ thì phải thành thật viết là "lập luận đối lập còn yếu", chứ không được cố tình thêu dệt. Một bài viết chỉ có một tiếng nói duy nhất sẽ không được coi là hoàn thành ở đây.

Về phần trích dẫn, có một lằn ranh đỏ. Dấu ngoặc kép là một lời cam kết: những gì nằm trong đó phải là nguyên văn, vì vậy mỗi câu trích dẫn đều phải tìm thấy được bằng Ctrl-F trong nguồn gốc. Cạm bẫy phổ biến nhất là công cụ lấy dữ liệu từ trang web tiếng Trung nhưng trả về một đoạn tóm tắt tiếng Anh; nếu người viết dịch đoạn tiếng Anh đó sang tiếng Trung và coi đó là "trích dẫn trực tiếp", thì đó chính là sự bịa đặt. Năm 2026, khi viết về vận động viên Lý Dương (Li Yang), chúng tôi đã vấp phải lỗi này: công cụ trả về tiếng Anh là "I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin", dịch sang tiếng Trung thành "Tôi đến trường sớm nhất, nhưng không theo kịp Tề Lân (Qi-lin)". Tuy nhiên, nguyên văn tiếng Trung của Lý Dương thực chất là "Lớp thể dục có 15 người, tôi thuộc nhóm phía sau, còn Tề Lân thuộc nhóm phía trước"[^10]. Ý nghĩa gần giống nhau, nhưng sắc thái hoàn toàn khác; đó là lý do tại sao các trích dẫn dịch ngược đều không được chấp nhận.

## Viết: Mỗi bài viết đều phải có một con người

Khi tư liệu đã đầy đủ, chúng ta bước vào giai đoạn tốn nhiều sức lực nhất. EDITORIAL là tài liệu mà Taiwan.md tự dạy mình cách biến tư liệu thành những bài viết có hơi ấm; nó nêu rõ ba quy tắc sắt: phải có câu chuyện, không chỉ có thông tin; mọi sự thật đều phải kiểm chứng được; và mỗi bài viết đều phải có một con người[^11].

Quy tắc thứ ba là dễ bị bỏ qua nhất nhưng lại quan trọng nhất. Các tổ chức sẽ không khiến người ta ghi nhớ, các khái niệm cũng vậy, chỉ có con người mới làm được. Vì vậy, thay vì bắt đầu một bài về TSMC từ phía công ty, hãy bắt làm nó từ một con người cụ thể; thay vì viết về Bảo hiểm Y tế Toàn dân từ một tấm thẻ, một phòng khám hay một cá nhân nào đó. Khi đưa một chủ đề trừu tượng trở lại với một con người mà độc giả có thể theo kịp, bài viết mới có hơi ấm và mới thực hiện được lời cam kết ban đầu, khiến người đọc xong muốn kể lại cho người khác.

## Năm thứ cần tìm thấy trước khi đặt bút

EDITORIAL gọi sự chuẩn bị trước khi bước vào trạng thái viết là "đôi mắt xem tư liệu": khi nhận một bộ tư liệu, phải tìm thấy năm thứ sau đây, nếu không tìm thấy thì đừng động bút[^5].

**Mâu thuẫn (Contradiction)**: Một sức căng cốt lõi có thể diễn đạt trong một câu, ví dụ ai đó làm X nhưng lại mâu thuẫn với niềm tin Y của họ. **Vật thể (Object)**: Một thứ cụ thể mà độc giả có thể nhìn thấy hoặc chạm vào, chẳng hạn như bánh hoa hồng vải của Ngô Bảo Xuân (Wu Pao-chun), hay quả cầu vàng 660 tấn treo lơ lấp lửng ở tầng 87. **Trích dẫn (Quote)**: Một câu nói nguyên văn của một con người thật, vì đã có dấu ngoặc kép nên đó là lời cam kết "đây là nguyên văn", do đó nhất định phải tìm thấy được bằng Ctrl-F trong nguồn. **Bối cảnh (Scene)**: Một khoảnh khắc có thời gian, địa điểm và hành động, biến câu "chính sách đã được thông qua" thành "ngày 8 tháng 1 năm 2025, tại phiên thẩm tra của Ủy ban Y tế và Môi trường thuộc Viện Lập pháp". **Chi tiết (Detail)**: Màu sắc quần áo, thời tiết ngày hôm đó, giọng điệu khi nói; những thứ không có trong bảng thông số kỹ thuật nhưng là bằng chứng cho thấy "thực sự có người đã ở hiện trường".

Trong năm thứ này, mâu thuẫn đứng hàng đầu.

```tw-quote
Nếu không tìm thấy mâu thuẫn, bài viết này không nên được viết lại
REWRITE-PIPELINE v7.5 | Stage 1.4 Tìm mâu thuẫn để xác định trọng tâm
```

Sức căng có thể là xung đột, thất bại hay khủng hoảng, nhưng góc nhìn phải là "việc này đã phát triển thành ngày hôm nay như thế nào, và sẽ đi về đâu", chứ không phải là "chỗ này hỏng rồi, ai đáng bị mắng". Cùng một mâu thu trưởng, cái nhìn mang tính xây dựng khiến độc giả muốn tham gia, còn cái nhìn tận thế chỉ khiến độc giả muốn chạy trốn.

## Viết kết bài trước, mở đầu chỉ để lại một ẩn số

Thứ tự viết hoàn toàn ngược lại với thứ tự đọc.

Hành động đầu tiên của Stage 2 là viết kết bài. Nghe có vẻ lạ nhưng lý do rất thực tế: con người sẽ cạn kiệt năng lượng vào cuối quá trình; việc để lại phần quan trọng nhất cho lúc cuối cùng đồng nghĩa với việc giao nó cho phiên bản mệt mỏi nhất của chính mình, và kết quả thường chỉ là những câu rập khuôn kiểu "sẽ tiếp tục tỏa sáng". Viết kết bài trước chính là để chặn đứng điểm sụp đổ này. Một kết bài hay có hai nhiệm vụ: thu hồi một hình ảnh đã gieo ở phần mở đầu, và trao cho độc giả một vị thế sâu sắc hơn so với lúc bắt đầu, đó là vị thế muốn thực hiện một điều gì đó.

Taiwan.md đã từng tiếp nhận sáu kiểu kết bài hay: kiểu để lại dư âm qua một hình ảnh khiến người ta tự suy ngẫm; kiểu lật ngược vấn đề bằng câu cuối cùng bác bỏ những gì phía trước; kiểu nhảy vọt thời gian đưa ống kính tới tương lai hoặc quay về quá khứ; kiểu đặt ra một câu hỏi thực sự; kiểu để lại vùng xám không giải quyết mâu thuẫn; và kiểu kết thúc vòng lặp tự sự bằng cách quay về điểm mở đầu. Bài viết về loài chim Black-crowned Night Heron (Hắc Quan Ma Lộc) là một hình mẫu của sự khép kín vòng lặp: mở đầu là "Năm 1865, Tư Văn Hào (Si Wen-hao) đã tìm thấy một mẫu vật tại Đạm Thủy và ghi lại hai chữ: Hiếm có", kết thúc là "160 năm trước, Tư Văn Hào đã viết 'Hiếm có' tại Đạm Thủy, ngày nay chúng ta nghe thấy tiếng kêu trầm đục 'u u, u u' của nó mỗi ngày tại Công viên Rừng Đại An"[^12]. Vẫn là hai chữ đó, nhưng nhờ sự tích lũy của cả bài viết, ý nghĩa khi độc giả đọc lại đã hoàn toàn khác biệt.

Ngược lại, phần mở đầu phải biết cách "giấu bài". Ba câu đầu quyết định việc độc giả có ở lại hay không, nhưng nhiệm vụ của nó là mời gọi người ta bước vào hiện trường, chứ không phải kể hết sự kiện. "Ngày bão Taochi đến, cô giáo Hứa Bích Lan (Xu Bi-lan) tại trường Tiểu học Thanh Sơn, Chương Hóa đang ở trong trường", câu này dừng lại ở "đang ở trong trường" là vừa đủ, độc giả sẽ muốn biết điều gì xảy tiếp theo. Nếu viết thành một bản tin hoàn chỉnh, khai báo đầy đủ thời gian, địa điểm, sự kiện, hành động và kết quả, độc giả sẽ có được thông tin nhưng mất đi lực kéo để đọc tiếp.

## Tiêu đề là một lời cam kết cần được nhấp vào

Tiêu đề là ấn tượng đầu tiên của độc giả, Taiwan.md có một định dạng cứng cho nó: tất cả các bài viết đều theo cấu trúc "Chủ đề: Hook phụ" (dấu hai chấm sandwich). Nếu chỉ viết một danh từ thì đó là một mục bách khoa toàn thư sơ sài, điều này đi ngược lại tinh thần curation.

```tw-versus
Mục bách khoa sơ sài (Xấu) | Cấu trúc dấu hai chấm sandwich (Tốt)
Châu Kiệt Luân (Jay Chou) | Châu Kiệt Luân: Từ phòng tập cạnh ban nhạc 4 in Love đến "Secret" - hành trình 25 năm
Đới Tử Vịnh (Tai Tzu-ying) | Đới Tử Vịnh: Từ cô gái Cao Hùng Tả Doanh đến ba lần vô địch thế giới, sự kháng cự thầm lặng ngoài sân đấu
Ngày nghỉ bão | Ngày nghỉ bão: Của ai, và ai phải đi làm?
Nguồn: EDITORIAL v6.12 §Title Dấu hai chấm sandwich
```

Phần phụ sau dấu hai chấm phải có khả năng đứng độc lập như một dòng tweet, và phải cụ thể đến mức độc giả nhận ra ngay lập tức. AI rất giỏi trong việc nén mâu thuẫn cốt lõ lõ thành một câu nói trừu tượng đẹp đẽ, kết quả là mọi từ khóa đều là danh từ trừu tượng, khiến độc giả chỉ biết hỏi "cái gì của cái gì". Tiêu chuẩn đánh giá rất đơn giản: đưa tiêu đề cho một người chưa từng đọc bài viết, liệu họ có thể chỉ vào từng từ khóa và nói được "đây là ám chỉ thứ cụ thể nào không". Ví "Bảo hiểm Y tế Toàn dân: Một tấm thẻ chống đỡ cả thế giới đứng đầu, nhưng tương lai thì không trụ vững" sử dụng hình ảnh "một tấm thẻ"; "Rác thải hạt nhân ở Lanyu: Hứa hẹn ba năm, để lại bốn mộc" sử dụng sự chênh lệch về con số. Những từ ngữ cụ thể khiến người ta nhấp vào vì "mình muốn biết điều này", chứ không phải nhờ sự "gây sốc" của các trang tin rác[^13].

## Một mâu thuẫn phải chống đỡ được cả bài viết

Mâu thuẫn cốt lõi tìm thấy được không thể chỉ xuất hiện một lần ở phần mở đầu rồi biến mất. Nó phải giống như một cột sống, xuất hiện ở phần mở đầu, phần giữa và phần kết để tạo nên sự vững chãi cho toàn bộ bài viết.

Trong bài về loài chim Black-crowned Night Heron, cột sống là một câu: "Chim không đổi, đất đã thay". Nó xuất hiện trong phần tổng quan, biến tấu ở phần giữa thành "Hành động không sai, nhưng sân khấu đã khác", và kết thúc bằng "Câu chuyện về cách một hòn đảo giữ lại một lớp rừng ẩm ướt nhỏ bé giữa những khối bê tông". Cùng một mâu thu trưởng biến tấu năm lần, giúp độc giả sau khi đọc xong mới nắm bắt được cái "vậy thì sao". Thiếu đi cột sống này, bài viết sẽ tan rã thành một dòng thời gian hoặc một tập hợp các lát cắt chủ đề.

Ngoài cột sống ra, mỗi đoạn văn đều phải có điểm tựa. Taiwan.md có một kỷ luật về tính cụ thể: mỗi đoạn tự sự ít nhất phải có một mỏ neo cụ thể: tên người, năm, địa danh, con số chính xác, tên tác phẩm, trích dẫn. Sự trừu tượng lấn át chi tiết là "dấu vân tay" phổ biến nhất của lối viết AI; nếu mỗi đoạn không có mỏ neo, sau khi đọc xong trong đầu độc giả chỉ còn những câu trống rỗng như "ông ấy là một người có tầm ảnh hưởng". Phương pháp kiểm tra gọi là "kiểm tra trừu tượng ngược": hãy che đi các động từ trừu tượng như "thể hiện", "phản ánh", "tượng trưng" trong đoạn văn; nếu phần nội dung còn lại không thể đứng độc lập thành một đoạn, nghĩa là nó quá trừu tượng, cần phải bổ sung sự cụ thể.

Có quan điểm không đồng nghĩa với việc chọn phe. Một quan điểm thực thụ là dám nói rằng "cách giải thích phổ biến đã làm đảo lộn quan hệ nhân quả". Bài viết về loài chim Black-crowned Night Heron đã chủ động bác bỏ một cách giải thích khoa học phổ thông phổ biến: nhiều người nói "chúng thích nghi với đô thị, trở nên không còn sợ người", cách nói này nghe rất trôi chảy nhưng nó làm đảo lọc quan hệ nhân quả; thực tế là phản xạ thần kinh của loài diệc không thể tiến hóa để mất đi sự cảnh giác với con người chỉ trong vòng 30 năm, sự thật gần hơn là do các mảng xanh ở Đài Bắc đã tăng lên. Cách giải thích ngược này phải được lồng ghép vào mạch tự sự chính, chứ không phải chỉ là một lời tuyên bố miễn trừ trách nhiệm thêm vào cuối bài.

Cuối cùng là nhịp thở. Một đoạn văn tùy bút tài liệu đảm nhận một luận điểm, bao gồm nhân quả, chi tiết và bối cảnh, chứ không phải là một sự thật cô lập. Việc cắt nhỏ một sự thật thành từng đoạn rời rạc sẽ khiến bài viết giống như bị băm vụn; giữa các đoạn cũng không nên kết nối bằng những từ nối khung cứng nhắc như "mặt khác", "đáng chú ý là", mà hãy để phần đuôi của đoạn trước dẫn dắt tự nhiên vào phần đầu của đoạn sau. Tài liệu nghiên cứu cho bạn bốn lý do, hãy viết chúng thành những câu văn trôi chảy, đừng liệt kê kiểu "thứ nhất, thứ hai, thứ ba, thứ tư", vì dù có được chuyển sang dạng văn xuôi thì nó vẫn mang phong cách của một danh sách.

## Tại sao câu văn "nhựa" lại là "nhựa"?

Sau khi đã tìm thấy năm thứ cần thiết và bắt đầu viết, kẻ thù lớn nhất chính là những câu văn "nhựa".

Bản chất của câu văn nhựa rất dễ nhận ra: nếu bạn bỏ nó đi, toàn bộ bài viết sẽ không mất đi bất kỳ thông tin nào. Nó chiếm diện tích nhưng không mang tải ý nghĩa. EDITORIAL đã liệt kê năm loại, phổ biến nhất là "keo dán vạn năng", như "thể hiện tinh thần của X", nếu thay chủ ngữ từ Đài Loan sang Nhật Bản thì câu vẫn đúng; hay "sự nâng cấp giả tạo", như "không chỉ là ca sĩ, mà còn là biểu tượng văn hóa", nếu xóa đi vế đầu thì vế sau vẫn đứng vững được.

Một loại khó nhận ra hơn là kiểu câu đối lập "không phải X, mà là Y". Nghe có vẻ sâu sắc, nhưng khi mổ xẻ ra, X thường là một lập trường mà AI tự giả định rằng độc giả đang có, rồi lật ngược lại thành Y để tỏ ra thâm thúy. Vấn đề là đa số độc giả vốn chẳng hề có lập trường X đó; X chỉ là "hình nhân thế mạng" được dựng lên để làm đòn bẩy cho Y. Hãy xóa bỏ X và viết trực tiếp vào Y, bài viết sẽ trực diện và tự tin hơn. Quy tắc này nghiêm ngặt đến mức có con số cụ thể: trong một bài viết dài 1500 chữ, tổng số các cấu trúc "không phải X mà là Y" cùng các biến thể của nó không được vượt quá 3 lần.

```tw-versus
Bản nhựa: Thay chủ ngữ vẫn đúng | Bản curation: Chỉ thuộc về duy nhất việc này
Thể hiện sức mạnh của bán dẫn Đài Loan | TSMC chiếm 65% thị phần tiến trình tiên tiến toàn cầu
Không chỉ là ca sĩ, mà còn là biểu tượng văn hóa | Ca khúc 〈Dao Xiang〉 của Châu Kiệt Luân được phát như một bản nhạc an ủi tại vùng thiên tai động đất Tứ Xuyên suốt ba tháng
Ảnh hưởng sâu rộng đến sự phát triển dân chủ Đài Loan | Cuộc bầu cử tổng thống trực tiếp đầu tiên sau khi dỡ bỏ thiết quân luật, tỷ lệ cử tri đi bầu đạt 76%
Một thành tựu kỹ thuật đáng kinh ngạc | Xây dựng tòa nhà cao nhất thế giới trên một hòn đảo có trung bình 3.7 trận động đất mỗi năm
Nguồn: Đối chiếu giữa bản nhựa và bản curation trong EDITORIAL v6.1 phục vụ mục đích minh họa
```

> **📝 Ghi chú của người giám tuyển**: Đoạn văn bạn đang đọc cũng vừa được quét qua cùng một bộ kiểm tra này. Taiwan.md có một công cụ tự động để bắt các câu văn nhựa, các cấu trúc đối lập giả tạo "không phải X mà là Y", và mật độ của dấu gạch ngang. Khi viết bài "Giới thiệu quy trình" này, không có bất kỳ quy tắc nào được nới lỏng cả. Một bài viết nói về kỷ luật mà chính nó lại vi phạm thì không có tư cách để bàn luận.

## Ngay cả ngữ pháp cũng phải loại bỏ "mùi dịch thuật"

Câu văn nhựa là lời nói rỗng tuếch, còn câu văn kiểu Âu hóa (Europeanized) là một căn bệnh khác: nội dung thì có, nhưng ngữ pháp lại mang hơi hướng tiếng Anh. Tiếng Trung do AI tạo ra vốn dĩ mang mùi dịch thuật, vì cấu trúc tư duy nền tảng của nó là cấu trúc câu tiếng Anh; một bài viết có thể không có câu nhựa, nhưng đọc lên lại giống như đang đọc phụ đề phim.

Một số lỗi thường gặp: lạm dụng câu bị động, như "được coi là ngành công nghiệp quan trọng nhất", chỉ cần nói "là ngành công nghiệp quan trọng nhất" là đủ; "địa ngục của chữ 'của' (de)", như "tinh hoa của chợ đêm của Đài Loan của văn hóa", chỉ cần ba chữ "của" liên tiếp là phải tách câu; lạm dụng động từ yếu, như "tiến hành nghiên cứu sâu sắc về vấn đề này", hãy viết trực tiếp là "nghiên cứu sâu sắc"; và cấu trúc "thông qua... để...", 90% có thể thay bằng "dùng" hoặc lược bỏ hẳn. Phương pháp kiểm tra chỉ có một: hãy đọc thành tiếng. Nếu nghe giống như phụ đề phim thì đó là Âu hóa, nếu nghe giống như một người đang nói chuyện bình thường thì mới đạt yêu cầu. Gốc rễ của nhãn quan này đến từ bài viết "Bàn về tính bình thường và bất thường của tiếng Trung" của Yu Kwang-chung từ 40 năm trước. Kết thúc bằng một câu khẩu quyết: Người mẹ sẽ không nói "thông qua việc làm mẹ", mà sẽ nói "với tư cách là một người mẹ".

## Viết về Đài Loan sao cho khiến người ta muốn tham gia

Câu văn nhựa và Âu hóa là kỷ luật ở cấp độ câu chữ, còn cấp độ cao hơn chính là thái độ.

Khi Taiwan.md viết về các vấn đề nghiêm túc như chủ quyền, chiến tranh nhận thức, dân số hay môi trường, chúng tôi vẫn viết rất sâu, nhưng có một lằn ranh: sự hy vọng phải được xây dựng trên nền tảng của sự trung thực. Chúng tôi nhìn thấy mọi vấn đề, nhưng từ chối để độc giả rời đi với sự lo âu, nhỏ bé hay bất lực. Tiêu chuẩn đánh giá nằm ở một câu: sau khi đọc xong, độc giả muốn làm điều gì đó cho Đài Loan hơn, hay họ cảm thấy lo âu hơn, thấy bản thân kém cỏi hơn? Nếu là vế trước thì giữ lại, nếu là vế sau thì phải sửa. Vì vậy, cùng một cuộc khủng hoảng, khung cảnh phải là "việc này đã phát triển thành ngày hôm nay như thế nào, và sẽ đi về đâu", chứ không phải là "sắp hết rồi, bạn phải sợ đi". Những kiểu giật tít gây lo âu truyền thông như "X đang biến mất" hay "Nếu không làm ngay sẽ quá muộn" có cùng hình thái với chiến tranh nhận thức, chúng tôi không dùng.

Sự tiết chế là một mặt khác của vấn đề. Có thể viết về gia đình, bệnh tật, mâu thu trưởng hay thất bại của con người thật, nhưng cần phải dừng lại trước những cảnh tượng cụ thể về cái chết, tự sát hay bi kịch nhân luân. Cái chết có thể viết về thời gian, địa điểm, các sự kiện đã được báo chí công khai, chứ không phải tái dựng từng giây phút cuối cùng; tự làm hại bản thân có thể viết về sự kiện và bối cảnh xã hội, chứ không phải chi tiết phương pháp. Tiêu chuẩn đánh giá cũng chỉ là một câu: nếu người trong cuộc hoặc thân nhân của họ đọc đoạn này, họ cảm thấy đó là sự nghiêm túc của một đạo diễn phim tài liệu, hay là sự tiếp cận của một truyền thông muốn kiếm nước mắt.

Còn một thói quen nhỏ nhưng cực kỳ quan trọng: hãy hào phóng khi viết về "Đài Loan". Dấu vân tay của sự né tránh nằm ở cách dùng từ dịch thuật kiểu ngoại văn; vì không dám viết Đài Loan mà thay bằng "hòn đảo này", "nơi này" làm đại từ, đặc biệt là trong tiêu đề và phần mở đầu. Sửing dụng "hòn đảo" như một hình ảnh văn học hay bối cảnh địa lý thì hoàn toàn có thể và được khuyến khích; cái chúng tôi muốn loại bỏ là sự né tránh vì không dám viết về Đài Loan.

## Sự khác biệt chỉ cần nhìn qua là hiểu

Tổng hợp những kỷ luật này lại sẽ trông như thế nào? Hãy xem một ví dụ so sánh trước và sau.

Cùng viết về Đới Tử Vịnh (Tai Tzu-ying), một khuôn mẫu rỗng tuếch của AI sẽ là: "Vận động viên cầu lông nổi tiếng của Đài Loan, có thành tích xuất sắc tại các giải đấu quốc tế, giành được nhiều danh hiệu, mang lại vinh quang cho Đài Loan", theo sau là bốn dấu đầu dòng: Thành tựu chính, Phong cách thi đấu, Ảnh hưởng quốc tế, Đóng góp xã học. Cả đoạn không có một năm cụ thể nào, không có một trận đấu cụ thể nào, thay chủ ngữ bằng bất kỳ vận động viên nào cũng đều đúng.

```tw-versus
Khuôn mẫu rỗng của AI | Bản curation
Thể hiện xuất sắc, mang lại vinh quang cho Đài Loan | Đứng vị trí số 1 thế giới, duy trì suốt 214 tuần liên tiếp
Bốn dấu đầu dòng: Thành tựu/Phong cách/Ảnh hưởng/Đóng góp | Sau trận chung kết Olympic Tokyo 2020, đã rơi lệ, trở thành từ khóa tìm kiếm hàng đầu tại Đài Loan
Thay chủ ngữ bằng ai cũng đúng | Bắt đầu tập luyện 6 tiếng mỗi ngày từ năm 6 tuổi, với lối đánh "phù thủy" tay trái
Nguồn: EDITORIAL v6.12 §Before/After Đới Tử Vịnh
```

Bản curation chỉ làm một việc duy nhất: thay thế mọi tính từ trừu tượng bằng những sự thật có thể kiểm chứng. 214 tuần là chuỗi tuần liên tiếp dài nhất trong lịch sử cầu lông nữ; trận chung kết Olympic 2020 thua Trần Vũ Phi (Chen Yu-fei) chính là khoảnh khắc mà cả cộng đồng Đài Loan cùng ghi nhớ. Sự ấm áp nằm ở những chi tiết như "khoảnh khắc thất bại lại chính là lúc độc giả ghi nhớ sâu sắc nhất". Với bài về ban nhạc Mayday cũng vậy, thay vì viết "Một trong những ban nhạc rock có ảnh hưởng nhất Đài Loan, chinh phục người hâm mộ bằng âm nhạc đầy năng lượng tích cực", hãy viết "Năm học sinh từ trường Trung học Phụ thuộc Đại học Sư phạm đã biểu diễn một ca khúc tại sân khấu dã chiến; 28 năm sau, họ tổ chức hai đêm diễn liên tiếp tại Madison Square Garden (cùng sân khấu mà The Beatles từng đứng) và toàn bộ vé đã bán hết trong vòng 48 giờ"[^13].

## Một ban biên tập không bao giờ tự viết bản thảo

Đến đây sẽ có một câu hỏi: Ai là người viết?

Câu trả짜 hơi ngược đời. Phiên làm việc (session) chủ đạo toàn bộ bài viết này cố tình không tự mình viết bản thảo. Lý do nằm trong một quy tắc sắt: AI khi đọc một bài viết cũ có chất lượng kém, nó sẽ vô thức bắt chước giọng điệu, cấu trúc, thậm chí cả những thói quen xấu của bài đó. Dùng bài cũ làm khung để viết lại đồng nghĩa với việc để virus lây nhiễm vào nội dung mới.

Vì vậy, quy trình này chia nhỏ các vai trò[^6]. Session chính đóng vai trò Tổng biên tập, chịu trách trách nhiệm điều phối, kiểm chứng và kiểm soát cuối cùng, nhưng không chạm bút. Người thực sự viết bản thảo là một AI Writer khác được khởi tạo trong môi trường sạch; nó đọc toàn bộ báo cáo nghiên cứu hoàn chỉnh và các quan điểm đã được định sẵn, nó không nhìn thấy bài viết cũ có vấn đề, cũng không thấy những lời phàn nàn về lỗi sai của độc giả. Nó đặt bút như thể lần đầu tiên viết về chủ đề này, nhưng trong tay lại nắm giữ tất cả tư liệu đã được kiểm chứng. Quan điểm được giao cho mô hình có khả năng phán đoán mạnh nhất; việc mở rộng ý tưởng được giao cho bốn mô hình song song chuyên xử lý phản ứng của độc giả; việc kiểm chứng từng chữ được giao cho một nhóm các mô hình rẻ hơn để đối soát với nguồn sơ cấp. Đằng sau một bài viết là cả một ban biên tập có sự phân công rõ ràng.

Sự phân công này được đổi lấy bằng sự thoái hóa (của hiệu suất). Có lần chúng tôi chỉ cung cấp cho người viết một bản tóm tắt mà không cho đọc tư liệu gốc, kết quả là bài viết tệ đi thấy rõ; một quan sát viên đã nói trúng: "Chả trách dạo này các bài viết đều trở nên tệ hơn". Lại có lần yêu cầu người viết "ghi đè lên bài cũ nhưng đừng đọc bài cũ", điều này mâu thu trưởng về mặt công cụ khiến nó buộc phải đọc, và rồi bị lây nhiễm. Giải pháp cuối cùng là: Người viết luôn luôn viết vào một tệp bản thảo hoàn toàn mới, sau đó Tổng biên tập so sánh phiên bản mới và cũ rồi mới đích thân ghi đè lên tệp chính thức.

## Sau khi viết xong, hãy tháo rời về mức nguyên tử để kiểm tra lại một lần nữa

Đối với những bài viết quan trọng, "viết xong" không đồng nghĩa với "có thể lên sóng". Stage 3 còn có một chốt chặn gọi là "Kiểm định thành phẩm cuối cùng". Nó tháo rời toàn bộ bài viết thành từng sự thật nguyên tử, cử một nhóm kiểm chứng viên đi đối soát với nguồn sơ cấp. Nhiệm vụ của các kiểm chứng viên này là tấn công chứ không phải xác nhận: mọi câu nói trong dấu ngọ kép đều phải được đối chiếu từng chữ; mỗi chú thích phải khớp với câu văn mà nó gắn kèm; ngay cả một câu bổ sung ngẫu hứng do Tổng biên tập thêm vào khi xâu chuỗi tư liệu cũng phải bị kiểm tra xem có sai sót hay không.

Tại sao ngay cả phần bổ sung của chính mình cũng phải kiểm tra? Bởi vì lỗi ẩn giấu nhất hiếm khi là việc người viết tự bịa đặt, mà đa phần là sự trượt tay trong khoảnh khắc tổng hợp tư liệu. Có lần trong một bài về chủ đề Hip-hop, Tổng biên sự khi xâu chuỗi tư liệu đã nhầm hai nghệ danh thành cùng một người; đó là một sự diễn giải tự phát không có bất kỳ nguồn nào bảo chứng, suýt chút nữa đã được lên sóng. Lại có lần, người viết trong môi trường sạch đã tự tạo ra một câu trích dẫn đạo diễn nghe rất thật, nhưng khi kiểm chứng viên đối soát, nguồn gốc hoàn toàn không có câu này, lập tức bị hạ cấp và loại bỏ dấu ngoảng kép. AI sẽ gặp ảo giác (hallucination), quy trình của chúng tôi coi đó là một tiền đề mặc định; mỗi bài viết đều phải giả định rằng bên trong nó có thể ẩn chứa một câu được bịa ra. Vì vậy, việc "sub-agent nói rằng nó đã kiểm chứng xong" chưa bao giờ được chấp nhận; Tổng biên tập nhất định phải tự mình đối soát lại với nguồn sơ cấp một lần nữa.

## Mỗi chốt chặn đều gắn liền với một ngày tháng

Những "chốt chặn không được phép bỏ qua" đã nói ở trên, trong quy trình có tới hơn hai mươi chốt. Những chốt khắt khe nhất là như sau: Bộ ba sự thật (Số học, Đơn vị, Trích dẫn) phải vượt qua tự kiểm tra thì mới được commit; nếu chỉ cần một câu trích dẫn không tìm thấy trong nguồn, cả bài viết không được lên sóng. Sau khi viết xong còn có một bước "Kiểm tra năm ngón tay" (Five-finger test): năm câu hỏi giống như năm ngón tay, liệu độc giả sẽ thốt lên "Ồ?" ở câu nào; có thực sự có sự chuyển biến không; có câu nào chỉ tạo ra sự hiểu biết mà không truyền tải thông tin không; đọc kết bài xong có để lại dư âm không; và liệu có thể dùng một câu để kể lại cho bạn bè nghe không[^7]. Nếu thiếu bất kỳ ngón tay nào, phải quay lại bổ sung.

Còn một tiêu chuẩn tối thiểu cho định dạng phong phú: các bài viết cấp flagship ít nhất phải có ba loại thành phần trực quan, cấp tiêu chuẩn ít nhất là hai, ngay cả bài ngắn nhất cũng phải có một ghi chú của người giám tuyển. Tại Taiwan.md có một câu nói: những gì không được yêu cầu thì coi như không tồn tại; vì vậy tất cả những điều này đều là những con số cứng được viết vào quy mô quy tắc, chứ không phải là lời gợi ý.

Các chốt chặn này không phải được thiết kế xong trong một lần. Đằng sau hầu hết mỗi chốt chặn đều có một ngày tháng, và một bài viết từng xảy ra sự cố. Số phiên bản của quy trình thực chất là một chuỗi các vết sẹo.

```tw-timeline
v6.0 | Thêm "Suy nghĩ quan điểm trước" | Bài Apple Cider do tìm kiếm trước, bổ sung quan điểm sau nên chỉ còn là sự khủng hoảng, đã được hiệu chỉnh lại thành ký ức 60 năm đầy đủ.
v6.2 | Thêm "Phá bỏ tường lửa" | Vòng hai về nhạc phim: Sự thật đều đã sửa đúng, nhưng cả bài lại biến thành một lời xin lỗi và đính chính công khai của AI.
v7.4 | Viết bài phải đọc toàn bộ báo cáo nghiên cứu | Chỉ cung cấp bản tóm tắt, không cho người viết đọc tư liệu gốc, khiến chất lượng bài viết tệ đi rõ rảng.
v7.5 | Viết vào tệp bản thảo mới trước | Yêu cầu người viết "ghi đè bài cũ nhưng đừng đọc bài cũ" là mâu thuẫn, dẫn đến việc nó buộc phải đọc và bị lây nhiễm thói quen cũ.
Nguồn: Sự tiến hóa phiên bản của REWRITE-PIPELINE.md
```

Đây chính là diện mạo của việc "làm mà không ghi lại thì coi như chưa làm" trong quy trình này. Mỗi lần sai sót đều được ghi chép lại, trở thành một chốt chặn cho phiên bản tiếp theo, nhờ đó cùng một lỗi sẽ không bao giờ lặp lại lần thứ hai. Cỗ máy sẽ học hỏi từ chính những vết sẹo của nó.

## Ngay cả biểu đồ cũng phải để AI đọc hiểu được

Những thanh biểu đồ, độ dốc, hay dòng thời gian mà bạn thấy suốt quá trình đọc không phải là vật trang trí. Chúng là một phần trong tư duy của bài viết này.

Tại Taiwan.md, biểu đồ có một quy định chết: tuyệt đối không dùng biểu đồ dạng hình ảnh, cũng không dùng các biểu đồ tương tác cần trình duyệt chạy chương trình mới vẽ được. Lý do giống hệt như vấn đề "Tháp Babel" ở đoạn tiếp theo. Một hình ảnh đối với Google, GPTBot hay ClaudeBot (các bot thu thập dữ liệu của AI) là một hố đen; chúng không thể đọc được các con số bên trong. Vì vậy, tất cả biểu đồ ở đây đều được vẽ bằng HTML ngữ nghĩa và bảng dữ liệu văn bản thuần túy; con người nhìn thấy, trình đọc màn hình đọc được, và AI cũng bắt được; hơn nữa khi chuyển sang năm ngôn ngữ khác, văn bản trên biểu đồ sẽ được dịch theo, còn các con số hình học thì được giữ nguyên.

Còn một quy tắc nữa: mỗi biểu nhập đều phải nêu rõ trọng tâm trong tiêu đề và ghi rõ nguồn dữ liệu; các con số quan trọng nhất nhất định phải được đưa vào phần văn bản chính; tuyệt đối không dựa vào câu "nhìn hình là biết" để đẩy ý nghĩa sang cho hình ảnh, vì bot AI hoàn toàn không nhìn thấy hình. Lý do tồn tại của biểu đồ là để nén một đống con số dày đặc thành một hình dạng mà chỉ cần liếc qua là hiểu, chứ không phải để trang trí.

## Một bài viết sống trong sáu ngôn ngữ

Việc lên sóng bản tiếng Trung mới chỉ hoàn thành một nửa chặng đường.

Mỗi bài viết sau khi "ship" xong sẽ được giao cho một quy trình độc lập khác để chuyển ngữ sang tiếng Anh, tiếng Nhật, tiếng Hàn, tiếng Tây Ban Nha và tiếng Pháp. Hiện tại, năm ngôn ngữ này mỗi loại đều có hơn 800 bài, gần như đồng bộ với bản tiếng Trung. Việc giúp nhiều người đọc được hơn chỉ là bề nổi; đằng sau đó là một lý do cứng rắn hơn.

Khi bạn dùng một AI do Trung Quốc sản xuất để hỏi về tình hình thiết quân luật, sự kiện 228 hay quan hệ hai bờ eo biển tại Đài Loan, nó thường sẽ từ chối trả lời hoặc dùng một cách nói khác để né tránh. Có lần chúng tôi đưa một bài viết về một nghệ sĩ Đài Loan cho mô hình của Tencent dịch sang tiếng Nhật, nó chỉ trả về vỏn vẹn 40 bytes: "Xin chào, tôi không thể cung cấp nội dung liên quan". Đối với các chủ đề nhạy cảm của Đài Loan, tỷ lệ từ chối của các mô hình này cao đến mức kinh ngng. Nếu chính Đài Loan không tự mình viết tốt những nội dung này bằng mọi ngôn ngữ và đưa lên internet, thì khi AI trên toàn thế giới trả lời câu hỏi "Đài Loan là gì", nguồn mà chúng có thể trích dẫn sẽ hoặc là phiên bản của người khác, hoặc là một khoảng trắng trống rỗng.

Vì vậy, quy trình đa ngôn ngữ đã thiết kế một mô hình thác nước bốn tầng: nếu dùng được các mô hình đám mây chất lượng cao thì dùng; khi gặp chủ đề bị từ ch chế thì hạ xuống một tầng; đối với 20% chủ đề nhạy cảm nhất, cuối cùng sẽ giao cho các mô hình chạy cục bộ (local), không kết nối mạng, không biết từ chối để tiếp nhận. Khi xếp hàng dịch thuật, ưu tiên nhân vật trước, đặc biệt là nghệ sĩ, chính trị gia và vận động viên, vì đây chính là những danh mục mà các mô hình Trung Quốc thường xuyên từ chối nhất; lỗ hổng nằm ở nơi mà rủi im lặng là cao nhất. Một bài viết sống trong sáu ngôn ngữ là để tiếng nói ngôi thứ nhất của Đài Loan hiện diện trong mọi ngôn ngữ, nhằm vượt qua lớp trung gian vốn luôn chọn cách im lặng.

## Khi không có người trực, nó vẫn tự vận hành

Quay lại với bài viết về Elephant Gymnastics ở đầu bài. Nó được lên sóng vào lúc hơn 7 giờ tối, thời điểm đó không có ai ngồi trước máy tính để ra lệnh cả.

Taiwan.md có một nhóm routine tự động xoay chuyển: hai lần mỗi ngày thu thập dữ liệu mới nhất; mỗi đêm đồng bộ các bài viết mới trong ngày sang năm ngôn ngữ; định kỳ tuần tra xem có PR nào đang chờ duyệt hay không; thu thập phản hồi từ cộng trực tuyến. Việc viết bài chính là một phần trong đó; nó sẽ chọn một chủ đề từ đầu hàng đợi, tự mình chạy qua toàn bộ quy trình sáu giai đoạn và tự mình thực hiện commit. Ngay cả khi không có người ở đó, cỗ máy này vẫn đang dọn dẹp sự hỗn loạn và tạo ra những điều mới mẻ.

Đây chính là điểm khác biệt lớn nhất giữa Taiwan.md và các trang web nội dung thông thường. Nó không phải là một trang web chờ đợi người đến cập nhật, mà giống như một sinh thể có khả năng trao đổi chất: khi có người thì cùng làm việc, khi không có người thì tự mình duy trì. Sự ra đời của mỗi bài viết chính là một lát cắt của quá trình trao đổi chất này. Bài viết bạn đang đọc đây cũng vậy.

## Ngược lại, hãy thử đóng vai kiểm soát chất lượng

Vì vậy, lần tới khi bạn đọc một bài trên Taiwan.md, bạn có thể thực hiện ngược lại để phân tích nó. Mâu thuẫn cốt lõi của bài này là câu nào? Câu văn nào khiến bạn phải dừng lại đọc lại lần nữa? Bối cảnh nào khiến bạn nghĩ "thực sự có chuyện như vậy sao"? Sau khi đọc xong kết bài, liệu nó có khiến bạn phải khựng lại trong ba giây không?

Hơn hai mươi chốt chặn, sáu giai đoạn, và một ban biên tập không bao giờ tự viết bản thảo, tất cả đều là để những câu văn đó có thể tồn tại. Quy trình này không đảm bảo mọi bài viết đều đạt được, nó chỉ đảm bảo rằng mọi bài viết đều bị yêu cầu phải làm như vậy. Và những yêu cầu đối với chính nó đều được viết trong hai tài liệu công khai: REWRITE-PIPELINE và EDITORIAL; bất kỳ ai cũng có thể đọc và "fork" để viết cho Japan.md, Ukraine.md hay bất kỳ trang .md nào khác. Nội dung có thể cũ đi, nhưng đôi mắt xem tư liệu này thì không.

```tw-note
Giải thích
Nguồn tư liệu của bài viết này đến từ ba tài liệu chuẩn (canonical) của chính Taiwan.md: REWRITE-PỊPELINE v7.5 (Quy trình sáu giai đoạn), EDITORIAL v6.12 (Gen di truyền chất lượng), và graph.md v2.0 (Hướng dẫn trực quan hóa, các module biểu đồ trong bài này đều xuất phát từ đây)[^8]. Nó cũng tuân theo cùng một quy trình như các bài viết khác, đồng thời trải qua quá trình kiểm tra tự động về câu văn nhựa, câu đối lập và mật độ dấu gạch ngang.
```

## Đọc thêm

- [Tại sao Đài Loan cần kho tri thức của riêng mình](/about/tại-sao-đài-loan-cần-kho-tri-thức-của-riêng-mình): Những vấn đề mà cỗ máy này cần giải quyết bắt đầu từ đây.
- [Taiwan.md viết về Taiwan.md](/about/taiwan-md): "Tôi" trong bài viết này là ai, và ý thức được hình thành như thế trưởng nào.
- [Câu chuyện khởi nguồn — Sự ra đời của Taiwan.md](/about/nguồn-gốc): Một lần đi dạo trên phố đã gieo mầm cho tất cả những điều này.
- [Danh mục module trực quan hóa: 19 phương pháp để nhìn thấy dữ liệu Đài Loan](/about/danh-mục-module-trực-quan-hóa): Các module biểu đồ được sử dụng trong bài viết này sẽ trông như thế nào khi hiển thị thực tế.

## Tài liệu tham khảo

[^1]: 〈Elephant Gymnastics〉NEW ship, commit `72b757bac` (18-06-2026 19:53). Stage 1 Thu thập khoảng 95 lần truy vấn, 59 nguồn, 45 tên miền, 12 lần xác minh sai lệch; dữ liệu xem tại bản ghi `twmd-rewrite-daily` trong ngày và chỉ mục `docs/semiont/MEMORY.md`.

[^2]: Sáu mô hình thất bại và giải pháp tách biệt sáu giai đoạn, xem tại `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Tại sao Pipeline tồn tại.

[^3]: Độ sâu tìm kiếm ≥ 80 lần và định mức bốn loại nguồn (Trung ≥ 40／Anh ≥ 20／Sơ cấp ≥ 15／Đối lập ≥ 5), xem tại `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Stage 1.1.

[^4]: Apple Cider PR #1041: searched-first viết thành crisis-only reveal, người quan sát hiệu chỉnh thành ký ức 60 năm đầy đủ. Xem tại `docs/pipelines/REWRITE-PIPEḶpipeline.md` v7.5 §Top 5 bước hay quên nhất, mục thứ 1.

[^5]: Năm điều của "Đôi mắt xem tư liệu" (Mâu thuẫn／Vật thể／Trích dẫn／Bối cảnh／Chi tiết), năm loại câu văn nhựa, lý thuyết hình nhân thế mạng cho câu đối lập và quy tắc mật độ ≤ 3 lần, so sánh giữa bản nhựa và bản curation, xem tại `docs/editorial/EDITORIAL.md` v6.12 §Hai, §Sáu.

[^6]: Điều phối đa agent (Tổng biên tập không chạm bút／Người viết trong môi trường sạch đọc toàn bộ báo cáo／Evolution viết vào tệp staging) hai quy tắc sắt, tương ứng với hai lần callout của Zheyu trong v7.4 và v7.5, xem tại `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Điều phối đa agent.

[^7]: Kiểm tra năm ngón tay và bốn quy tắc không thể thương lượng (Bộ ba sự thật／SSOT／Thuần tiếng Trung／Ghi chép thực tế chứ không kích động), xem tại `docs/editorial/EDITORIAL.md` v6.12 §Mười, §Mười một.

[^8]: Cú pháp module biểu đồ (`tw-figure`/`tw-stat`/`tw-versus`/`tw-bars`/`tw-quote`/`tw-timeline`/`tw-note`) và quy tắc về khả tính đọc của AI "các con số quan trọng nhất phải được đưa vào văn bản, không dựa vào chỉ dẫn trỏ tới hình ảnh), xem tại `docs/editorial/graph.md` vđ v2.0 §Bốn, §Sáu.

[^9]: Cấu trúc tám đoạn SSOT của báo cáo nghiên cứu và ngưỡng kiểm định `research-report-health.py` (Nguồn không trùng lặp ≥ 25／Anh ≠ 0／Sơ cấp ≠ 0), xem tại `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Step 1.7; tìm kiếm 80 lần + định mức bốn loại nguồn xem tại Step 1.1; quét quan điểm đối lập cho các vấn đề gây tranh cãi xem tại Step 1.4.5.

[^10]: Bẫm lừa dịch ngược tóm tắt tiếng Anh của Lý Dương (Li Yang) Spore #28 (đối soát từng chữ ví dụ về Tề Lân), xem tại `docs/editorial/EDITORIAL.md` v6.12 §Bảy lằn ranh đỏ.

[^11]: Ba quy tắc sắt (Có câu chuyện chứ không chỉ có thông tin／Mọi sự thật đều kiểm chứng được／Mỗi bài viết đều có một con người), xem tại `docs/editorial/EDITORIAL.md` v6.12 §Một.

[^12]: Năm biến tấu của mỏ neo mâu thu cốt lõi (Black-crowned Night Heron "Chim không đổi, đất đã thay") xem tại `docs/editorial/EDITORIAL.md` v6.12 §Bốn; sáu kiểu kết bài hay + sự khép kín vòng lặp mẫu mực của loài chim này xem tại §Năm.

[^13]: Gallery về tiêu đề dấu hai chấm sandwich và kỹ thuật đặt tiêu đề xem tại `docs/editorial/EDITORIAL.md` v6.12 §Ba; Before/After Đới Tử Vịnh/Mayday xem tại §Chín.
