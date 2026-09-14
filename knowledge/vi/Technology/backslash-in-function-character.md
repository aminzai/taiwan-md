---
title: "Dấu gạch chéo ngược trong chữ 'Công': Hai lớp thuế mặc định mà kỹ sư Đài Loan trả mỗi ngày"
description: "Trên Windows 11 với ngôn ngữ zh-TW, kịch bản trạng thái dịch ném toàn bộ hơn bốn nghìn đường dẫn quét được vào thư mục gốc, Technology trở thành không, trong khi CI của Linux cùng tuần lại xanh. Kịch bản dùng dấu gạch chéo xuôi để tách tên phân loại, ổ đĩa dùng dấu gạch chéo ngược, không tách được. Một lớp cũ hơn chôn vùi trong ký tự: byte thứ hai của 'Công' trong Big5 chính là dấu gạch chéo ngược ASCII, cộng đồng phát triển gọi đó là 'Hứa Công Gài'. Dù đường dẫn viết thế nào, ký tự chứa những dấu hiệu gì, giá trị mặc định đều không tính đến máy này. quotePath của Git là một đường khác, nguyên nhân khác biệt."
date: 2026-08-13
category: 'Technology'
tags: ['Mã nguồn mở', 'Windows', 'Big5', 'UTF-8', 'Mã hóa ký tự', 'Trung thể']
subcategory: 'Chữ viết và công cụ'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-13
lastHumanReview: false
translatedFrom: 'Technology/功字裡的那根反斜線.md'
sourceCommitSha: '5dcaeea42'
sourceContentHash: 'sha256:5f01e7a8c9e76d21'
translatedAt: '2026-09-13T21:41:59.562907+00:00'
---

> **Tóm tắt 30 giây:** Tôi chạy kịch bản trạng thái dịch, màn hình hiển thị 4546, tất cả đều ở `root`. Trên GitHub, CI Linux báo xanh. Sau đó mới nhận ra hai vấn đề. Dấu gạch chéo ngược trong đường dẫn Windows, kịch bản dùng dấu gạch chéo xuôi không tách được. Phần sau của mã Big5 cho chữ "Công" (功) chính là ký tự ASCII `\`. Hai vấn đề cơ chế khác nhau, nhưng thường cùng xuất hiện trên một máy Windows tiếng Trung thể.

Tôi duy trì kịch bản trạng thái dịch cho Taiwan.md trên Windows 11 ngôn ngữ zh-TW. Đêm đó chạy như thường lệ `i18n-status.py`, chờ terminal in ra con số. Console là cp950. Không có dòng đỏ nào trong đầu ra.

Màn hình dừng ở 4546. Tất cả nằm trong một phân loại tên `root`. Technology là 0.

Cùng tuần đẩy lên GitHub, CI trên Linux báo xanh.

Biến kịch bản tên `zh_articles`, quét các đường dẫn dưới `knowledge` trừ thư mục tiếng Anh, about và thư mục gạch dưới, tiếng Nhật, tiếng Hàn, tiếng Ả Rập cũng được tính vào. Đêm đó nó thậm chí không tách được tên phân loại, hơn bốn nghìn đường dẫn bị nhét vào cùng một ô. Không có ngoại lệ, không có cảnh báo. Thống kê trông như cả trang web hỏng, không thiếu một tệp nào.[^8]

Đường dẫn trên ổ cứng là `knowledge\Technology\một-bài-viết.md`, các thư mục cách nhau bằng dấu gạch chéo ngược. Kịch bản dùng `split('/')` để lấy tên phân loại. Trên Linux dòng này chạy được vì đường dẫn vốn dùng dấu gạch chéo xuôi. Trên Windows nó không tách được dấu gạch chéo ngược, toàn bộ đường dẫn trả về nguyên vẹn, bài viết bị ném vào `root` mặc định.[^1]

Sau khi đổi để `pathlib` xử lý thư mục, Technology có 59 bài, khớp với nội dung thư mục. Giữa hai chỉ cách nhau một giả định: máy của bạn dùng loại gạch chéo nào để tách thư mục.

> **📝 Ghi chú người bảo tàng:** Cú pháp kịch bản không sai, CI cũng thực sự chạy thử. Nứt nẻ ở giữa "máy tác giả thực sự ngồi" và "máy công cụ tưởng bạn ngồi". Khe hở này không thuộc bất kỳ giai đoạn nào, nên không ai chịu trách nhiệm theo dõi.

## Đường gạch ngang trong chữ «Công»

Đường dẫn là lớp thứ nhất. Lớp thứ hai cũ hơn nhiều, chôn sâu trong chữ.

Big5 được định案 năm 1984, một chữ Hán hai byte. Nếu byte thứ hai rơi vào khoảng `0x40` đến `0x7E`, sẽ trùng lặp với các ký hiệu ASCII thường dùng: `[`, `]`, `{`, `}`, `\`, `|`. Nguyên phó giáo sư khoa Quản trị thông tin Đại học Kỹ thuật Triều Dương Hồng Triều Quý (nghỉ hưu tháng 8 năm 2023) từng viết trên trang giảng dạy: 「Do 40-7E là phạm vi mã ASCII của các ký tự thường dùng, nên đôi khi gây phiền toái cho lập trình viên.」[^2]

Mã của chữ «Công» là `A5 5C`. Byte sau đó `0x5C`, trong ASCII chính là dấu gạch ngạch `\`. Một chương trình quét chuỗi theo từng byte, coi `\` làm ký tự thoát hoặc dấu phân cách, khi quét đến nửa sau của «Công», sẽ tưởng rằng mình gặp phải đường dẫn. Tên tệp có «Công», đường dẫn có «Công», đều có thể bị vấp ở chỗ này.

Cộng đồng lập trình Đài Loan và Hồng Kông gọi nó là «Hứa Công Cái»: «Hứa» là `B3 5C`, «Công» là `A5 5C`, «Cái» là `BB 5C`, ba chữ thường dùng viết liền nhau như tên người.[^5] Hồng Triều Quý còn liệt kê «Gia Dã Trình Trận Công», byte thứ hai lần lượt trùng với `[`, `]`, `{`, `}`, `\`, và viết công cụ quét `b5tm`.[^2] Một bug được đặt tên người, thường là vì nó xuất hiện đủ thường xuyên, khiến một thế hệ phải có cách chỉ trỏ vào nó để nói.

Năm 2015, tác giả blog «Dark Thread» chuyển sang Visual Studio 2015. Các file `.cs` cũ vẫn lưu dưới BIG5. Sau khi trình biên dịch chuyển sang Roslyn, các «Hứa Công Cái» trong file biến thành lỗi biên dịch.

Hai ngày sau đồng nghiệp nói với anh ấy, họ chuyển cũng bị kẹt rất lâu, cuối cùng lội qua bài viết quay về bài của anh ấy. Có người dùng có hàng ngàn file, chuyển một còn dính một đống, «chỉ tốt nói Goodbye với VS2015». Sau đó anh ấy viết một công cụ nhỏ chuyển hàng loạt sang UTF-8, vì lưu thủ công từng cái không xong.[^7]

Đây không cùng một chuyện với `split('/')` ở trên. Một là công cụ hiện đại giả định đường dẫn trông như thế nào. Một là bốn mươi năm trước chọn hai byte, rồi để ký hiệu sinh sống trong thân xác chữ. Cơ chế khác nhau, hóa đơn却 thường cùng đến trên một máy cp950. Về phía nhập liệu làm sao đưa chữ vào máy, xem [[東亞文字輸入法]]. Ở đây nói đến sau khi chữ đã nằm trên ổ cứng, chuỗi công cụ còn nhận ra nó hay không.

## Giá trị mặc định không nhánh riêng cho máy này

Git bật mặc định `core.quotePath`. Tên tệp có byte lớn hơn `0x80`, `git status` sẽ in ra dạng bát phân như `\344\270\255`. Tên tệp tiếng Trung vẫn còn đó, chỉ là bạn hàng ngày không hiểu kho chứa của mình đang nói gì.[^3] Nó thoát (escape) các byte cao của UTF-8. `0x5C` của Big5 là một vấn đề khác. Trông đều như dấu gạch chéo ngược, nhưng nguyên nhân khác nhau.

Python 3 trên Windows nếu `open()` không viết `encoding='utf-8'`, có thể kế thừa locale hệ thống. Cùng một tệp UTF-8, Linux đọc được, máy này dùng cp950 giải mã, dấu câu hay bopomofo liền hỏng.[^4] Tôi tự trả giá một lần: dùng `Get-Content | Set-Content` của PowerShell 5.1 chuyển tệp UTF-8, dấu gạch ngang dài trong diff biến thành `??`. Đó cũng là thuế mặc định, không phải chủ đề thứ hai.

Khi thông báo trạng thái mang emoji, bảng điều khiển (console) cp950 này sập ngay. Bộ ký tự không có những ký hiệu đó, Python in không ra, ngoại lệ ném lên tầng trên cùng. CI Linux không bắt được chuyện này, vì nó không chạy trên máy này.

Đường dẫn ví dụ `$HOME/project/src` trong Git, Python, CI, không có nhánh riêng cho Windows zh-TW.

Hồng Triều Quý năm 2015 nhận phỏng vấn iThome, nói về định dạng tệp chính phủ nên dùng gì, có thể sống bao lâu. Báo dẫn ý ông: nếu chính phủ chỉ dùng sản phẩm Microsoft mở tệp dữ liệu, tức là tin rằng tuổi thọ Microsoft sẽ dài hơn Trung Hoa Dân Quốc.[^6] Câu nói đó nói về định dạng tệp và thời hạn bảo lưu. Dữ liệu gắn vào bộ công cụ mặc định nào, kéo dài thời gian, thành vấn đề ai còn đọc được. Hợp tác mã nguồn mở gắn vào môi trường mặc định của một loại máy nào đó. Kéo co giữa công nghệ công dân và định dạng tệp chính phủ, xem [[開源社群與g0v]]. Văn hóa các nhà phát triển Đài Loan lâu nay hấp thụ sự chênh lệch này, xem [[台灣開源精神]]。

Dấu phân cách đường dẫn, mã hóa terminal, `$HOME` trong ví dụ CI, không có nhánh phụ mở cho máy này. Ngày 4546 đường dẫn bị phân loại sai, không một dòng code nào báo lỗi. Thống kê trông bình thường, cho đến khi bạn ngồi trước máy này.

## Mở rộng đọc

- [Tinh thần mã nguồn mở Đài Loan](/vi/technology/taiwan-open-source-spirit)：Văn hóa và bối cảnh các nhà phát triển Đài Loan tham gia mã nguồn mở。
- [Phương pháp nhập văn bản Đông Á](/vi/technology/east-asian-input-methods)：Chữ được gõ vào máy tính như thế nào, từ bảng mã đến bàn phím。
- [Cộng đồng mã nguồn mở và g0v](/vi/technology/open-source-and-g0v)：Hợp tác giữa dữ liệu mở và định dạng chính phủ。

## Tài liệu tham khảo

[^1]: [Microsoft Learn: Định dạng đường dẫn tệp trên hệ thống Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — Tài liệu .NET giải thích đường dẫn DOS truyền thống dùng dấu gạch chéo ngược làm phân cách thư mục, dấu gạch chéo xuôi sẽ được chuyển thành dấu gạch chéo ngược.

[^2]: [Hồng Triều Quý: Các vấn đề mã Big-5 có thể gặp khi lập trình](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Trang hướng dẫn liệt kê các chữ thường dùng có byte thứ hai rơi vào khoảng nguy hiểm ASCII (giá, dã, trình, trận, công), và giới thiệu công cụ quét b5tm. Cuối trang không ghi chức danh. Năm 2015 iThome gọi là phó giáo sư. Trang chủ bản thân ghi năm 1997–2023 công tác tại Khoa Quản trị Thông tin Triều Dương, nghỉ hưu tháng 8/2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Tài liệu chính thức giải thích mặc định hiển thị đường dẫn có byte > 0x80 dưới dạng chuỗi thoát bát phân.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Mô tả hàm chỉ ra khi không chỉ định encoding, có thể dùng locale hệ thống làm mã hóa mặc định.

[^5]: [Wikipedia: Mã Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Ghi rõ 'công' 0xA55C, 'hứa' 0xB35C, 'cái' 0xBB5C, và giải thích vấn đề này được gọi đùa là Hứa Công Cái.

[^6]: [iThome: Phỏng vấn Hồng Triều Quý](https://www.ithome.com.tw/news/93606) — Phỏng vấn 2015, bài viết xưng phó giáo sư Khoa Quản trị Thông tin Trường Đại học Kỹ nghệ Triều Dương. Trang gốc thường lỗi 403, câu về 'tuổi thọ Microsoft' chỉ lấy từ bản tóm tắt kết quả tìm kiếm, không coi là trích dẫn nguyên văn.

[^7]: [Dark Thread: Quyển Khiên Tiềm Ẩn – Giải quyết vấn đề tương thích BIG5 tệp chương trình VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Bản ghi 2015 khi Visual Studio 2015 biên dịch mã nguồn BIG5, Hứa Công Cái gây lỗi biên dịch. Bài viết có câu 'chỉ còn đường nói Goodbye với VS2015'.

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Hợp nhất 26/07/2026. Trước sửa trên Windows categories chỉ còn root: 4546, sau sửa Technology zh: 59. Cùng loại bỏ emoji làm sập bảng điều khiển cp950.
