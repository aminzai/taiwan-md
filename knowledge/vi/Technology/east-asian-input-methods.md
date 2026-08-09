---
title: 'Cuộc xung đột nền tảng trên bàn phím: sự tiến hóa trăm năm của phương pháp nhập văn bản Đông Á'
description: 'Khi toàn bộ bàn phím thế giới đều giống hệt nhau, những nền văn minh khác nhau làm cách nào để nhét chữ viết của mình vào 26 chữ cái Tiếng Anh? Từ chữ Zhuyin của Đài Loan đến bố cục Dubeol của Hàn Quốc, phương pháp nhập văn bản là một cuộc chiến bảo vệ văn hóa im lặng'
translatedFrom: 'Technology/東亞文字輸入法.md'
sourceCommitSha: '24efd20f3'
sourceContentHash: 'sha256:d8c6f0fd322ce1e4'
sourceBodyHash: 'sha256:c009ff8e72f638e1'
translatedAt: '2026-08-09T11:16:34+08:00'
date: 2026-03-19
category: 'Technology'
tags:
  [
    'phương pháp nhập',
    'công nghệ',
    'văn hóa',
    'chữ Zhuyin',
    'Cangjie',
    'bàn phím',
    'số hóa',
    'Đông Á',
    'chữ viết',
  ]
subcategory: 'Chữ viết và công cụ'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-03-19
lastHumanReview: false
readingTime: 15
---

# Cuộc xung đột nền tảng trên bàn phím: sự tiến hóa trăm năm của phương pháp nhập văn bản Đông Á

## 30 giây tổng quan

Toàn bộ bàn phím máy tính trên thế giới đều có bố cục QWERTY — một kiểu bố trí được thiết kế cho máy đánh chữ Tiếng Anh vào những năm 1870. Nhưng Đông Á có hơn 2 tỷ người sử dụng các hệ thống chữ viết (chữ Hán, hiragana, Hangul, chữ Thái, chữ Myanmar) mà chúng không phải là chữ cái phiên âm chút nào. Họ phải làm sao? Câu trả lời là: mỗi nền văn minh đã tự phát minh ra lớp dịch của riêng mình — phương pháp nhập văn bản. Những phương pháp nhập này không chỉ là công cụ kỹ thuật mà còn là chiến trường của sự nhận dạng văn hóa. Đài Loan dùng chữ Zhuyin, Trung Quốc dùng Pinyin, Nhật Bản dùng chữ Rômani, Hàn Quốc trực tiếp tách các chữ cái, mỗi lựa chọn đều phản ánh những triết học khác nhau của một nền văn minh khi đối mặt với số hóa.

---

## Bản chất của vấn đề: 26 chữ cái vs hàng chục ngàn chữ

Người dùng tiếng Anh không bao giờ cần đến "phương pháp nhập" — bàn phím có 26 chữ cái, bạn gõ gì thì ra cái đó. Nhưng chữ Hán có hơn 50.000 chữ, và những chữ thường dùng cũng có 3.000-5.000 chữ. Bạn không thể làm một cái bàn phím có 5.000 phím.

Điều này có nghĩa là nền văn minh Đông Á phải giải quyết một vấn đề cơ bản: **làm sao để dùng một số lượng phím hạn chế để biểu đạt chữ viết vô hạn?**

Mỗi nền văn minh đã đưa ra những câu trả lời hoàn toàn khác nhau, và những câu trả lời này phản ánh sâu sắc về cấu trúc ngôn ngữ, hệ thống giáo dục, thậm chí cả những lựa chọn chính trị của họ.

---

## 🇹🇼 Đài Loan: Chữ Zhuyin（tìm chữ bằng "âm thanh"）

### Nguồn gốc lịch sử của chữ Zhuyin

Phương pháp nhập chữ Zhuyin là phương pháp chủ yếu ở Đài Loan, sử dụng 37 ký hiệu chữ Zhuyin （ㄅㄆㄇㄈ⋯) để đánh dấu phát âm. Bạn muốn gõ "Đài Loan", chỉ cần nhấn `ㄊㄞˊ ㄨㄢ`, hệ thống hiển thị các chữ cùng âm để bạn chọn.

Bản thân chữ Zhuyin được sinh ra năm 1913 tại "Hội thống nhất đọc âm", bởi các học giả như Chương Thái Liêm và những người khác tạo ra từ việc đơn giản hóa các phần của chữ Hán cổ. Đó là một hệ thống **hoàn toàn độc lập với chữ cái Latin để đánh dấu phát âm**, điểm này rất quan trọng.

### Tại sao Đài Loan lại bám chắc chữ Zhuyin?

Đài Loan bám chắc chữ Zhuyin, đằng sau có bốn tầng lý do tương hỗ nhau. Hệ thống giáo dục là cơ bản: những tuần đầu tiên của lớp một tiểu học dành riêng để dạy chữ Zhuyin, đây là công cụ nhận diện chữ sâu nhất của mỗi người Đài Loan, chi phí để thay đổi quá lớn. Nhận dạng văn hóa là động lực: chữ Zhuyin là hệ thống đánh dấu riêng có của thế giới Hán tự chính thống, không sử dụng chữ cái Latin, được coi là sự kế tục của truyền thống văn hóa Hoa Hoa. Từ góc độ kỹ thuật, chữ Zhuyin có thể đánh dấu chính xác bốn thanh của tiếng Quốc ngữ （thậm chí cả thanh nhẹ), điều mà Pinyin khó có thể thực hiện được hoàn toàn. Cuối cùng, bàn phím Đài Loan ở mỗi chữ cái Tiếng Anh đều có ký hiệu chữ Zhuyin tương ứng, tạo thành đánh dấu kép, khiến hệ thống này cũng được gắn chặt vào tầng phần cứng.

### Những hạn chế của chữ Zhuyin

Vấn đề lớn nhất của chữ Zhuyin là **quá nhiều chữ đồng âm**. Tiếng Quốc ngữ chỉ có khoảng 1.300 âm tiết khác nhau, nhưng phải tương ứng với hàng chục ngàn chữ Hán. Gõ "ㄕˋ" có thể xuất hiện "是、事、式、室、市、試、視、適、勢、世⋯⋯" hàng chục chữ. Người dùng phải chọn từ danh sách ứng cử, và điều này làm chậm tốc độ nhập văn bản.

Gần đây, các phương pháp nhập chữ Zhuyin thông minh (như New Phonetic Input Method của Microsoft, RIME) đã nâng cao độ chính xác đáng kể thông qua dự đoán bối cảnh AI, nhưng vấn đề cơ bản của việc chọn chữ vẫn tồn tại.

### Cangjie: Một con đường khác

Năm 1976, người được gọi là "cha đẻ máy tính tiếng Hoa"，**Chu Pang Phục**，đã phát minh ra **phương pháp nhập Cangjie**, một phương pháp hoàn toàn không dựa vào phát âm mà **dựa vào việc tách rời hình dạng chữ**. Mỗi chữ Hán được tách thành 1-5 "chân chữ", tương ứng với 25 phím trên bàn phím (từ A đến Y，bỏ qua phím Z[^2]).

Ví dụ "明" = 日 + 月 = `A` + `B`.

Ưu điểm của Cangjie là **một chữ một mã**, không cần chọn chữ. Những người dùng Cangjie thành thạo có thể có tốc độ vượt quá chữ Zhuyin. Chu Pang Phục sau đó tuyên bố từ bỏ quyền sở hữu trí tuệ của Cangjie, làm cho nó trở thành tiền thân của phần mềm nguồn mở theo phương pháp nhập văn bản Hán, sớm hơn phong trào phần mềm mã nguồn mở hai mươi năm[^1].

Cangjie rất phổ biến ở Hồng Kông （hơn nửa người dùng máy tính), nhưng ở Đài Loan luôn là một tập hợp nhỏ, lý do chính là đường cong học tập dốc.

### Phương pháp nhập hàng-cột (Hangjie)

**Phương pháp nhập hàng-cột** được Liêu Minh Đức phát minh ra là một lựa chọn địa phương khác của Đài Loan, dựa trên phím số để tách rời hình dạng chữ，triết học thiết kế là "không cần phải ghi nhớ quá nhiều chân chữ". Nó đại diện cho sự đổi mới liên tục của Đài Loan trong lĩnh vực phương pháp nhập văn bản.

---

## 🇨🇳 Trung Quốc: Pinyin tiếng Hoa (dùng chữ cái Latin để ghép tiếng Hoa)

### Lựa chọn Pinyin

Phương pháp nhập chữ chính để ở đại lục Trung Quốc là **phương pháp nhập Pinyin tiếng Hoa**, trực tiếp dùng 26 chữ cái Tiếng Anh để ghép âm thanh của chữ Hán. Gõ "台灣" là nhập vào `taiwan`, hệ thống chuyển đổi thành chữ Trung Quốc đơn giản hóa.

Lựa chọn này có bối cảnh lịch sử sâu sắc:

1. **1958 năm công bố kế hoạch Pinyin tiếng Hoa**: thay thế chữ Zhuyin ở Trung Quốc trước đó （Trung Quốc gọi là "Ký hiệu chữ Zhuyin") và Pinyin Wade-Giles
2. **Cải cách chữ đơn giản hóa**: bắt đầu từ năm 1956, thúc đẩy chữ đơn giản hóa, tạo thành bổ sung với nhập văn bản Pinyin — học Pinyin → dùng Pinyin để gõ → gõ ra chữ đơn giản hóa
3. **Xem xét quốc tế hóa**: Pinyin sử dụng chữ cái Latin, tiện lợi cho người nước ngoài học tiếng Hoa, cũng tiện lợi cho những người sử dụng tiếng Hoa nhập văn bản trên bất kỳ bàn phím tiêu chuẩn nào

### Pinyin vs Zhuyin: một phân khúc văn hóa mà bạn có thể không chú ý

Về mặt bề ngoài, chữ Zhuyin và Pinyin đều là "dùng phát âm để tìm chữ". Nhưng những khác biệt sâu sắc là khổng lồ:

|                              | Zhuyin Đài Loan                       | Pinyin Trung Quốc                   |
| ---------------------------- | ------------------------------------- | ----------------------------------- |
| Hệ thống ký hiệu             | Ký hiệu độc lập (ㄅㄆㄇ)              | Chữ cái Latin (bpmf)                |
| Nguồn gốc văn hóa            | Bắt nguồn từ các phần chữ Hán         | Bắt nguồn từ phong trào La Tinh hóa |
| Điều kiên tiên quyết học tập | Không cần học tiếng Anh trước         | Cần phải biết chữ cái Tiếng Anh     |
| Yêu cầu bàn phím             | Cần bàn phím được đánh dấu chữ Zhuyin | Bất kỳ bàn phím Tiếng Anh nào       |
| Mối quan hệ với chữ viết     | "Mô tả phát âm"                       | "Dịch thành chữ cái Latin"          |

Khác biệt này không chỉ là kỹ thuật mà còn phản ánh những chia rẽ cơ bản giữa hai bờ về "tiếng Hoa phải kết nối với quốc tế như thế nào". Đài Loan chọn lựa để giữ lại một hệ thống ký hiệu độc lập với phương Tây, Trung Quốc chọn lựa để quy phục tới La Tinh hóa.

### Năm nét chữ: "Cangjie" của Trung Quốc

Điều đáng lưu ý là Trung Quốc cũng có phương pháp nhập hình dạng chữ, đại diện là **Năm nét chữ** （Vương Yông Dân, 1983 năm). Logic của nó giống như Cangjie, tách chữ Hán thành các nét tương ứng với bàn phím. Năm nét chữ cực kỳ phổ biến ở văn phòng Trung Quốc những năm 1990, nhưng khi phương pháp nhập Pinyin trở nên thông minh hơn và điện thoại thông minh phổ biến, tỷ lệ sử dụng giảm xuống rất nhanh. Ngày nay, hơn 95% người dùng ở Trung Quốc sử dụng Pinyin.

---

## 🇯🇵 Nhật Bản: Chữ Rômani→Hiragana→Kanji quá ba giai đoạn biến thân

### Thách thức độc đáo của nhập tiếng Nhật

Tiếng Nhật là một trong những hệ thống chữ viết phức tạp nhất trên thế giới, sử dụng đồng thời ba bộ chữ:

- **Hiragana** (ひらがな): 46 ký hiệu âm tiết cơ bản
- **Katakana** (カタカナ): 46 ký hiệu, chủ yếu dùng cho từ vay mượn nước ngoài
- **Kanji** (漢字): thường dùng khoảng 2.000-3.000 chữ

Cách tiêu chuẩn của phương pháp nhập tiếng Nhật là "**nhập chữ Rômani**" (ローマ字入力):

1. Gõ chữ cái Tiếng Anh → tự động chuyển đổi thành hiragana: `ka` → `か`、`n` → `ん`
2. Tiếp tục gõ, hệ thống kết hợp thành từ: `kanji` → `かんじ`
3. Nhấn phím cách để chuyển đổi thành kanji: `かんじ` → `漢字`

Đây là một quá trình **chuyển đổi ba tầng**: chữ cái Tiếng Anh→Hiragana→Kanji, mỗi tầng đều cần phán đoán của người dùng.

### Tại sao Nhật Bản lại dùng chữ Rômani thay vì nhập hiragana trực tiếp?

Nhật Bản có **nhập hiragana trực tiếp** (かな入力) lựa chọn, mỗi phím trên bàn phím tương ứng với một hiragana. Nhưng điều này cần ghi nhớ hơn 50 vị trí phím, hơn nữa hệ thống giáo dục Nhật Bản đã dạy chữ Rômani trong giáo dục tiếng Anh, vì vậy hầu hết mọi người cảm thấy sử dụng chữ cái Tiếng Anh tiện lợi hơn.

Bây giờ, đa số người dùng Nhật Bản sử dụng nhập chữ Rômani (tỷ lệ ước tính khoảng 80-90%, các con số cụ thể thay đổi tùy theo phương pháp điều tra[^6]), chỉ có một số ít những người già hơn hoặc những chuyên viên đánh máy sử dụng nhập hiragana trực tiếp.

### Hàm ý văn hóa của nhập tiếng Nhật

Chuyển đổi kanji của tiếng Nhật có một hiệu ứng văn hóa thú vị: những thanh niên bắt đầu **quên cách viết tay chữ kanji**. Vì phương pháp nhập sẽ tự động hiển thị chữ kanji chính xác, người dùng chỉ cần biết "làm sao để phát âm" là được, không cần ghi nhớ "cách viết". Hiện tượng này ở Nhật Bản có một thuật ngữ chuyên biệt: "**quên chữ kanji**" （忘記漢字）.

---

## 🇰🇷 Hàn Quốc: Hai bàn phím (thiết kế bàn phím được yêu thích nhất)

### Thiên tài của Hangul: chữ cái có thể tương ứng trực tiếp với phím

Chữ Hangul (한글) là một hệ thống chữ cái được Vua Thế Tông lệnh tạo ra năm 1443, cũng là một trong rất ít những chữ viết "có người phát minh rõ ràng" trên thế giới. Nó được tạo thành từ 14 phụ âm (ㄱㄴㄷㄹ⋯) và 10 nguyên âm (ㅏㅓㅗㅜ⋯), những chữ cái này kết hợp thành các ô âm tiết.

Tổng cộng phụ âm + nguyên âm của Hangul chỉ có 24 chữ cái cơ bản, đúng hạp có thể để vào 26 phím của bàn phím QWERTY!

### Dubeol (두벌식): tay trái phụ âm、tay phải nguyên âm

Phương pháp nhập tiêu chuẩn của Hàn Quốc **Dubeol** (hai bàn phím) được thiết kế cực kỳ trực giác:

- **Tay trái** chịu trách nhiệm nhấn phụ âm: ㄱ(r) ㄴ(s) ㄷ(e) ㄹ(f) ㅁ(a)⋯
- **Tay phải** chịu trách nhiệm nhấn nguyên âm: ㅏ(k) ㅓ(j) ㅗ(h) ㅜ(n) ㅡ(m)⋯

Khi gõ, hai tay lần lượt, tiết tấu cảm giác cực tốt, và **không cần chọn chữ**, gõ gì thì ra cái đó.

Đây là **cái duy nhất trong tất cả các phương pháp nhập Đông Á không cần danh sách ứng cử chữ**. Ô âm tiết Hangul được kết hợp ngay lập tức: nhấn `ㅎ` + `ㅏ` + `ㄴ` = 한, nhấn `ㄱ` + `ㅡ` + `ㄹ` = 글. Toàn bộ quá trình không có độ trễ, không chọn chữ.

### Tại sao phương pháp nhập chữ Hangul lại được yêu thích nhất?

Vì bản thân Hangul được thiết kế cho "tốt viết". Triết học thiết kế của Vua Thế Tông là "kẻ thông minh không đủ một buổi sáng để hiểu được, kẻ ngu cả mười ngày cũng có thể học được"[^3] (聰明人一個早上學會，笨人十天也能學會). 600 năm sau, hệ thống thiết kế này vẫn hoàn toàn phù hợp hoàn hảo thời đại số hóa: 24 chữ cái chính xác để vào bàn phím, phụ âm nguyên âm chia cho tay trái-phải, không cần chuyển đổi, không cần chọn chữ.

---

## 🇹🇭 Thái Lan: Kedmanee (bố cục được kế tục từ thời đại máy đánh chữ)

### Thách thức của chữ Thái: 44 phụ âm + ký hiệu thanh điệu

Chữ Thái có 44 ký hiệu phụ âm、15 ký hiệu nguyên âm (có thể kết hợp thành 28 dạng nguyên âm khác nhau)、4 ký hiệu thanh điệu, cộng lại vượt quá 60 ký tự, vượt quá nhiều phím trên bàn phím tiêu chuẩn.

Giải pháp là **bố cục Kedmanee** (เกษมณี), được Suwanprasert Ketmanee thiết kế cho máy đánh chữ Thái trong những năm 1920-1930[^4] (Wikipedia ghi lại bố cục này được định hình vào khoảng năm 1932). Nó đặt những ký tự thường dùng nhất ở các vị trí không cần Shift，những ký tự ít dùng đặt ở tầng Shift.

### Tính chất đặc biệt của nhập chữ Thái

Chữ Thái là **chữ cái biểu thanh**, nhưng quy tắc viết của nó cực kỳ phức tạp: nguyên âm có thể xuất hiện ở trước phụ âm、sau phụ âm、trên phụ âm、dưới phụ âm. Ví dụ เ (e) viết ở phía trước phụ âm, nhưng khi phát âm lại ở phía sau. Điều này có nghĩa là thứ tự gõ và thứ tự đọc không nhất thiết phải giống nhau, người dùng cần thích nghi với một số tình huống "gõ nguyên âm trước rồi gõ phụ âm".

Nhập chữ Thái không cần chọn chữ (tương tự như Hangul), nhưng cần ghi nhớ hai tầng (bình thường + Shift) của vị trí phím.

---

## 🇲🇲 Myanmar: Cuộc chiến Unicode

### Zawgyi vs Myanmar Unicode: một cuộc nội chiến số hóa

Câu chuyện phương pháp nhập chữ Myanmar là câu chuyện đầy kịch tính nhất ở Đông Á. Chữ Myanmar có 33 phụ âm và quy tắc kết hợp phức tạp, nhưng vấn đề thật sự không nằm ở phương pháp nhập chữ, mà ở **mã hóa chữ**.

Vào những năm 2000, kỹ sư Myanmar Zaw Htut đã phát triển **chữ Zawgyi**, nó không tuân thủ tiêu chuẩn Unicode, nhưng vì hữu ích nên nhanh chóng phổ biến. Vào những năm 2010, khoảng 90% điện thoại thông minh Myanmar sử dụng Zawgyi.

Vấn đề là: Zawgyi và Unicode không tương thích. Đoạn văn bản giống nhau trong hai hệ thống hiển thị hoàn toàn khác nhau, gây ra nhiều nhầm lẫn trong giao tiếp.

Năm 2019, chính phủ Myanmar chính thức tuyên bố chuyển đổi hoàn toàn sang **Myanmar Unicode**[^5]. Facebook cũng cùng năm đó buộc chuyển đổi những người dùng Myanmar từ Zawgyi sang Unicode. Quá trình chuyển đổi này ảnh hưởng đến hơn 20 triệu người dùng, quy mô tương đương như một quốc gia thực hiện dọn dẹp lại cơ sở hạ tầng số hóa của họ.

---

## So sánh: Triết học bàn phím của sáu nền văn minh

| Nền văn minh  | Phương pháp nhập chính | Nguyên lý                   | Cần chọn chữ?            | Định vị văn hóa           |
| ------------- | ---------------------- | --------------------------- | ------------------------ | ------------------------- |
| 🇹🇼 Đài Loan   | Zhuyin                 | Ký hiệu độc lập đánh dấu âm | ✅ Rất nhiều chữ đồng âm | Tính độc lập văn hóa      |
| 🇨🇳 Trung Quốc | Pinyin tiếng Hoa       | Chữ cái Latin ghép âm thanh | ✅ Rất nhiều chữ đồng âm | Kết nối quốc tế hóa       |
| 🇯🇵 Nhật Bản   | Chữ Rômani             | Latin→Hiragana→Kanji        | ✅ Chuyển đổi kanji      | Chuyển đổi đa tầng        |
| 🇰🇷 Hàn Quốc   | Dubeol                 | Chữ cái tương ứng trực tiếp | ❌ Kết hợp ngay lập tức  | Thích ứng hoàn hảo        |
| 🇹🇭 Thái Lan   | Kedmanee               | Ký tự tương ứng trực tiếp   | ❌ Xuất ra trực tiếp     | Di sản máy đánh chữ       |
| 🇲🇲 Myanmar    | Myanmar Unicode        | Kết hợp ký tự               | ❌ Xuất ra trực tiếp     | Cuộc chiến tiêu chuẩn hóa |

---

## Thời đại điện thoại thông minh: chiến trường mới

Điện thoại thông minh đã thay đổi hoàn toàn hệ sinh thái phương pháp nhập. Bàn phím Zhuyin của Đài Loan (lưới 9 ô hoặc toàn bàn phím) vẫn là chủ yếu trên điện thoại, nhưng tỷ lệ sử dụng nhập viết tay và nhập bằng giọng nói tăng nhanh chóng. Trung Quốc đi theo hướng AI: Sogou Pinyin、Baidu Input Method trở thành chủ yếu，"nhập trượt" nâng cao hiệu quả Pinyin đáng kể. Nhật Bản phát triển ra **phương pháp nhập Flick** (フリック入力), dùng ngón tay trượt trên lưới 9 ô để chọn hướng hiragana, hoàn toàn không cần chữ cái Tiếng Anh. Hàn Quốc có **phương pháp nhập Qianzí** (천지인, Cheonjiin), dùng ㅣ ㆍ ㅡ (Thiên địa nhân) ba nét cơ bản để kết hợp tất cả chữ Hangul, cực kỳ phù hợp với màn hình nhỏ.

Thời đại điện thoại thông minh khiến một hiện tượng thú vị trở nên rõ ràng hơn: **thế hệ trẻ đang mất khả năng viết tay**. Điều này đặc biệt nặng nề trong khu vực văn hóa chữ Hán: khi phương pháp nhập giúp bạn ghi nhớ tất cả chữ Hán, tay của bạn quên mất.

---

## Thời đại AI: sự chết của phương pháp nhập?

Khi công nghệ nhận diện giọng nói và kỹ thuật AI hội thoại tiến bộ, một câu hỏi căn bản nổi lên: **chúng ta còn cần phương pháp nhập không?** Nhập bằng giọng nói đã thay thế được gõ trong nhiều tình huống，tỷ lệ sử dụng tin nhắn giọng nói của WeChat ở Trung Quốc đặc biệt cao. Dự đoán AI khiến phương pháp nhập càng trở nên "thông minh", gõ vài chữ thì có thể dự đoán cả câu. Tiến bộ công nghệ nhận diện viết tay cũng khiến "viết chữ bằng ngón tay trên màn hình" trở nên khả thi.

Nhưng phương pháp nhập sẽ không biến mất. Vì nó không chỉ là công cụ — nó là **phương tiện truyền tải ký ức văn hóa**. Những tuần mười tiếp theo khi trẻ em Đài Loan học chữ Zhuyin, cái khoảnh khắc người Nhật bản chuyển đổi chữ Rômani thành chữ kanji trên bàn phím, tiết tấu của phụ âm tay trái nguyên âm tay phải của người Hàn Quốc, đều là cuộc hội thoại thân mật giữa mỗi nền văn minh với chữ viết của mình trong thời đại số hóa.

---

## Đọc thêm

- Ngành công nghiệp bán dẫn (半導體產業) — ngành công nghiệp sản xuất chip phía sau bàn phím

## Tài liệu tham khảo

[^1]: [Giải mã thế thân của bàn phím (dưới): Cangjie với lịch sử văn hóa nhập tiếng Zhuyin](https://www.thenewslens.com/article/12229) — Mạng thời báo Nhân dân, lịch sử và bối cảnh văn hóa của phương pháp nhập Cangjie

[^2]: [Chu Pang Phục và phương pháp nhập Cangjie](https://zh.wikipedia.org/zh-hant/%E6%9C%B1%E9%82%A6%E5%BE%A9) — Wikipedia; mô tả thiết kế của Cangjie sử dụng 25 phím (từ A đến Y)

[^3]: [Hướng dẫn bố cục bàn phím tiếng Hàn](https://www.90daykorean.com/korean-keyboard/) — Ngôn ngữ Hàn 90 ngày; mô tả cấu hình bàn phím Dubeol tiếng Hàn

[^4]: [Bố cục bàn phím Kedmanee tiếng Thái](https://en.wikipedia.org/wiki/Thai_Kedmanee_keyboard_layout) — Wikipedia; thông tin về người thiết kế Suwanprasert Ketmanee và thời đại

[^5]: [Quá trình di cư từ Zawgyi sang Unicode của Myanmar](https://en.wikipedia.org/wiki/Zawgyi_font) — Wikipedia; quy trình chuyển đổi từ Zawgyi sang Unicode ở Myanmar

[^6]: [Nhập tiếng Nhật - nhập chữ Rômani](https://www.youtube.com/watch?v=_HXOVMobmAA) — Hướng dẫn YouTube; tình trạng sử dụng nhập chữ Rômani hiện tại ở Nhật Bản
