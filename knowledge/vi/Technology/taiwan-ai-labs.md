---
title: 'Phòng thí nghiệm Trí tuệ Nhân tạo Đài Loan (Taiwan AI Labs)'
description: 'Tổ chức nghiên cứu AI phi lợi nhuận do "cha đẻ PTT" Đốc Dĩnh Cầm (Ethan Tu) sáng lập vào tháng 3 năm 2017. Các mô hình mã nguồn mở: TAIDE (mô hình ngôn ngữ lớn tiếng Trung phồn thể), TAME, FedGPT, với hơn 60 tỷ token ngữ liệu tiếng Trung phồn thể. Chuyên về y tế thông minh và phòng chống chiến tranh nhận thức. Ứng dụng khoảng cách xã hội COVID (công nghệ Bluetooth phi tập trung).'
date: 2026-03-19
author: 'idlccp02'
category: 'Technology'
subcategory: '人工智慧'
tags:
  [
    'Trí tuệ nhân tạo',
    'Y tế thông minh',
    'Đốc Dĩnh Cầm',
    'Đổi mới công nghệ',
    'Phòng chống chiến tranh thông tin',
    'TAIDE',
    'PTT',
  ]
readingTime: 8
lastVerified: 2026-05-07
lastHumanReview: true
featured: true
translatedFrom: 'Technology/台灣人工智慧實驗室.md'
sourceCommitSha: 'c8e5ac9ea'
sourceContentHash: 'sha256:905a736099878754'
sourceBodyHash: 'sha256:f134440a7453a1a5'
translatedAt: '2026-07-18T18:59:52+08:00'
---

# Phòng thí nghiệm Trí tuệ Nhân tạo Đài Loan (Taiwan AI Labs)

> **Tổng quan 30 giây:** Phòng thí nghiệm Trí tuệ Nhân tạo Đài Loan do "cha đẻ PTT" Đốc Dĩnh Cầm (Ethan Tu) sáng lập vào tháng 3 năm 2017, là tổ chức nghiên cứu AI phi lợi nhuận đầu tiên ở châu Á. [^1] Tiểu sử Đốc Dĩnh Cầm: Năm 1995, khi đang là sinh viên năm thứ hai đại học, ông đã tạo ra PTT trong ký túc xá bằng máy tính 486; năm 2006 gia nhập Microsoft; năm 2012 gia nhập bộ phận AI của Microsoft (xem P0⚠️ về sự khác biệt trong mô tả chức danh khu vực châu Á-Thái Bình Dương). [^2] Các mô hình ngôn ngữ mã nguồn mở: **TAIDE** (mô hình ngôn ngữ lớn tiếng Trung phồn thể), **TAME**, **FedGPT** cấp độ liên minh, với kho ngữ liệu vượt quá 60 tỷ token tiếng Trung phồn thể. [^3] Các lĩnh vực cốt lõi: Y tế thông minh, phòng chống chiến tranh nhận thức, Ứng dụng khoảng cách xã hội COVID-19 (Bluetooth phi tập trung). [^4]

---

## Bối cảnh thành lập và triết lý cốt lõi

Taiwan AI Labs được Đốc Dĩnh Cầm (Ethan Tu) thành lập vào tháng 3 năm 2017. [^1] Vào thời điểm đó, sự phát triển AI toàn cầu chủ yếu do các gã khổng lồ công nghệ đa quốc gia lớn dẫn dắt. Đốc Dĩnh Cầm nhận thấy những lợi thế độc đáo của Đài Loan trong phần cứng bán dẫn, nhân tài phần mềm và cơ sở dữ liệu Bảo hiểm Y tế Toàn dân, nên quyết định trở về Đài Loan để sáng lập phòng thí nghiệm.

Chức danh của Đốc Dĩnh Cầm: Trong thông cáo báo chí của TSMC và một số phương tiện truyền thông được ghi nhận là "Giám đốc Nghiên cứu Khu vực châu Á-Thái Bình Dương trước đây của bộ phận AI Microsoft", nhưng Wikipedia ghi là "Bộ phận AI của Microsoft". Chức danh chính xác có sự khác biệt (xem P0⚠️), khuyến nghị tham khảo LinkedIn chính thức hoặc thông báo trên trang web Taiwan AI Labs. [^2]

Triết lý cốt lõi: "Công nghệ vì điều tốt (Tech for Good)" và "Tinh thần mã nguồn mở" — không lấy lợi ích thương mại làm mục tiêu duy nhất, mà tập trung vào các điểm đau xã hội, chia sẻ kết quả nghiên cứu với giới doanh nghiệp, chính phủ và học thuật thông qua mã nguồn mở hoặc hợp tác.

---

## Ba lĩnh vực nghiên cứu cốt lõi

### Y tế thông minh (Smart Healthcare)

Sử dụng dữ liệu Bảo hiểm Y tế Toàn dân và dữ liệu lâm sàng của Đài Loan để phát triển các ứng dụng AI trong y tế — như nhận diện hình ảnh y tế (u não, tổn thương phổi), phân tích trình tự gen AI, v.v.

Để giải quyết vấn đề quyền riêng tư của dữ liệu y tế, phòng thí nghiệm áp dụng "Học liên bang (Federated Learning)": Mô hình AI được huấn luyện cục bộ trên máy chủ của từng bệnh viện, chỉ trả về các tham số mô hình, dữ liệu bệnh nhân gốc không bao giờ rời khỏi bệnh viện, phá vỡ các "hòn đảo dữ liệu" giữa các tổ chức y tế.

### Thành phố thông minh và Giao diện Người-Máy

Bao gồm hệ thống kiểm tra bằng drone, phân tích giao thông thông minh, và AI giọng nói/văn học "Yating (雅婷)" — có thể thực hiện nhận diện giọng nói tiếng Trung địa phương chính xác (bao gồm tiếng Trung Đài Loan và sự pha trộn Trung-Anh), đồng thời có khả năng sáng tác âm nhạc.

### Phòng chống Chiến tranh Thông tin và Chiến tranh Nhận thức

Đài Loan được coi là một trong những khu vực chịu tấn công bởi tin giả nghiêm trọng nhất thế giới. Dự án "Infodemic" sử dụng AI để phân tích các hành vi phối hợp bất chính (Coordinated Inauthentic Behavior) trên mạng xã hội, định kỳ công bố báo cáo quan sát môi trường thông tin.

---

## Các mô hình ngôn ngữ mã nguồn mở: TAIDE, TAME, FedGPT

Taiwan AI Labs đã tung ra ba mô hình mã nguồn mở liên quan đến tiếng Trung phồn thể [^3]: **TAIDE** (Trustworthy AI Dialogue Engine) là mô hình ngôn ngữ lớn tiếng Trung phồn thể, với kho ngữ liệu huấn luyện vượt quá 60 tỷ token tiếng Trung phồn thể; **TAME** là một mô hình mã nguồn mở khác, mục đích sử dụng chi tiết xem tài liệu chính thức; **FedGPT** là mô hình ngôn ngữ cấp độ học liên bang, nhấn mạnh vào kiến trúc quyền riêng tư dữ liệu. Ba mô hình này cùng giải quyết vấn đề: tỷ lệ ngữ liệu tiếng Trung phồn thể trong dữ liệu huấn luyện AI toàn cầu rất thấp, khó tránh khỏi thế giới quan mặc định của tiếng Trung giản thể — một tình thế cố kết cấu.

---

## Thực hành phòng chống dịch COVID-19

Trong giai đoạn dịch bệnh bắt đầu từ năm 2020, Taiwan AI Labs hợp tác với chính phủ để ra mắt "Ứng dụng Khoảng cách Xã hội Đài Loan": Sử dụng công nghệ Bluetooth phi tập trung, không thu thập vị trí GPS cá nhân, hỗ trợ điều tra dịch tễ trong khi đảm bảo quyền riêng tư, trở thành hình mẫu quốc tế về phòng chống dịch bằng công nghệ [^4]. Sản phẩm này cũng là ví dụ cụ thể về việc chuyển đổi đường lối nghiên cứu "Học liên bang" và "Ưu tiên quyền riêng tư" từ lý thuyết sang triển khai công cộng quy mô lớn.

---

## Tài liệu tham khảo thêm

- [Miin (迷音): Đốc Dĩnh Cầm dạy AI bắt tài khoản dẫn hướng, bản thân lại bị kiện vì ăn cắp tin](/technology/迷音Miin) — Sản phẩm chủ lực của phòng thí nghiệm hướng tới công chúng, dùng AI để bắt các tài khoản thao tác phối hợp, cuối năm 2025 rơi vào vụ kiện về bản quyền do báo chí tổng hợp.
- [Phát triển Trí tuệ Nhân tạo và Chiến lược Tương lai của Đài Loan: Từ Giải Nobel Đôi năm 2024 đến Chợ Đêm Ninh Hạ](/technology/台灣人工智慧發展與未來策略) — Đặt Taiwan AI Labs vào bàn cờ tổng thể của "lực bá quyền phần cứng + Giải Nobel Đôi năm 2024", nhìn khoảng cách giữa TAIDE và nghiên cứu nền tảng AI toàn cầu.
- [Tại sao Đài Loan cần Kho tri thức riêng](/about/為什麼台灣需要自己的知識庫) — Mặt khác của việc xây dựng năng lực AI từ dân gian: khoảng trống ngữ liệu cho mô hình, và việc từ chối trả lời các chủ đề liên quan đến Đài Loan của AI thực tế có thể đo lường được.
- [Trang web chính thức Taiwan AI Labs](https://ailabs.tw/)
- [Đốc Dĩnh Cầm — Wikipedia](https://zh.wikipedia.org/zh-tw/杜奕瑾)
- [BNext: Đốc Dĩnh Cầm trở về Đài Loan sáng lập AI Lab](https://www.bnext.com.tw/article/44267/founder-of-ptt-ethan-tu-back-to-taiwan-to-establish-an-ai-lab)
- [Trung tâm Nghiên cứu Môi trường Thông tin IORG Đài Loan](https://iorg.tw/)

---

## Tài liệu tham khảo

[^1]: [Taiwan AI Labs: Về chúng tôi](https://ailabs.tw/zh/關於我們/) — Xác nhận Đốc Dĩnh Cầm sáng lập vào tháng 3 năm 2017, định vị là tổ chức nghiên cứu AI phi lợi nhuận đầu tiên ở châu Á.

[^2]: [Wikipedia: Đốc Dĩnh Cầm](https://zh.wikipedia.org/zh-tw/杜奕瑾) — Xác nhận năm 1995, sinh viên năm thứ hai đại học trong ký túc xá tạo ra PTT bằng máy tính 486; năm 2006 gia nhập Microsoft; năm 2012 gia nhập bộ phận AI của Microsoft (chức danh chính xác "Giám đốc Nghiên cứu Khu vực châu Á-Thái Bình Dương" có sự khác biệt, xem P0⚠️).

[^3]: [Verse: Phỏng vấn Đốc Dĩnh Cầm (TAIDE/TAME/FedGPT)](https://www.verse.com.tw/article/my-way-ethan-tu) — Xác nhận tên các mô hình mã nguồn mở TAIDE/TAME/FedGPT; kho ngữ liệu TAIDE vượt quá 60 tỷ token tiếng Trung phồn thể.

[^4]: [Cục Quản lý Dịch bệnh, Bộ Y tế và Phúc lợi: Giải thích Ứng dụng Khoảng cách Xã hội Đài Loan](https://www.cdc.gov.tw/) — Xác nhận Ứng dụng Khoảng cách Xã hội COVID-19 sử dụng công nghệ Bluetooth phi tập trung, không thu thập vị trí GPS.

[^5]: [BNext: Đốc Dĩnh Cầm trở về Đài Loan sáng lập AI Lab](https://www.bnext.com.tw/article/44267/founder-of-ptt-ethan-tu-back-to-taiwan-to-establish-an-ai-lab) — Bài báo về bối cảnh và động lực Đốc Dĩnh Cầm trở về Đài Loan sáng lập Taiwan AI Labs.

---

_Bài viết này do cộng tác viên cộng đồng @idlccp02 biên soạn, cập nhật bổ sung kết quả kiểm chứng sự kiện P0 vào ngày 2026-05-07 (TAIDE/TAME/FedGPT/60 tỷ token; hedge về chức danh Microsoft của Đốc Dĩnh Cầm)._
