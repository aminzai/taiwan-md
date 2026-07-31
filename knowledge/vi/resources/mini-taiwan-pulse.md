---
title: 'Mini Taiwan Pulse — Trực quan hoá 3D lưu thông Đài Loan thời gian thực'
description: 'Cảm nhận nhịp đập Đài Loan qua dữ liệu mở — đàn máy bay vẽ cung tròn trên bầu trời, tàu thuyền chạy qua mặt biển, tàu hoả vồ về đường ray, 23 lớp dữ liệu thể hiện hơi thở của hòn đảo.'
date: 2026-03-22
category: 'resources'
tags:
  [
    resources,
    open-data,
    visualization,
    transportation,
    3D,
    real-time,
    Taiwan.md,
  ]
subcategory: 'Công nghệ công dân'
author: 'Taiwan.md'
featured: false
lastVerified: 2026-03-22
lastHumanReview: false
translatedFrom: 'resources/mini-taiwan-pulse.md'
sourceCommitSha: '31a871b9'
sourceContentHash: 'sha256:3100c78e3e84a12add36d6426705108e81b8eb560b532aa751fe9e4ff63831e3'
sourceBodyHash: 'sha256:409b7d5c9d0f3bbd4cbdfa1454ceb7d6576908a3d9d6f079d06a535d4717d7a8'
translatedAt: '2026-07-31T00:00:00Z'
---

# Mini Taiwan Pulse — Trực quan hoá 3D lưu thông Đài Loan thời gian thực 🌐

> 📖 **Bài viết phiên bản đầy đủ**: Tài nguyên này đã được nâng cấp thành bài viết nghiên cứu sâu về công nghệ công dân, phiên bản hoàn chỉnh xem tại [Mini Taiwan Pulse: Một nhà phân tích dữ liệu đã vẽ nhịp đập lưu thông Đài Loan thành quỹ đạo sáng 3D mà hít thở](/technology/mini-taiwan-pulse) (2026-04-19). Trang này được giữ lại làm mục chỉ mục trong danh sách tài nguyên.

> **Tóm lược 30 giây:** Một dự án mã nguồn mở biến động lực lưu thông Đài Loan thành thời gian thực thành quỹ đạo sáng 3D. Máy bay vẽ cung tròn trên bầu trời, tàu thuyền để lại dấu vệt, tàu hoả chạy dọc đường ray — 23 lớp có thể chuyển đổi độc lập, để bạn "nhìn thấy" mạch đập của Đài Loan.

## Tại sao đáng chú ý

Hầu hết mọi người khi nhìn bản đồ Đài Loan, họ chỉ thấy một đường bao tĩnh. Mini Taiwan Pulse cho bạn thấy một **hòn đảo đang hít thở**.

Tham vọng của dự án này không nhỏ: tập hợp dữ liệu mở rải rác trong các cơ quan chính phủ — chuyến bay, AIS tàu thuyền, lịch biểu tàu hoả Đài Loan và tàu cao tốc, lộ trình tàu điện ngầm, thống kê dân số, quan sát khí tượng — tất cả trên cùng một bản đồ 3D. Không chỉ là những dấu chấm đơn giản, mà dùng quỹ đạo sáng, bóng sáng, dấu vệt commet để biến dữ liệu thành cảnh quan chuyển động.

> **📝 Ghi chú của người biên tập**
> Cơ sở hạ tầng dữ liệu mở Đài Loan nằm trong top của châu Á ([Chỉ số dữ liệu mở toàn cầu](https://index.okfn.org/) đã lần lượt vào top 10 nhiều lần), nhưng khoảng cách giữa "dữ liệu được mở" và "dữ liệu được nhìn thấy" là rất lớn. Mini Taiwan Pulse đang lấp khoảng cách này.

## Ba lớp mạch đập

### Bầu trời — Quỹ đạo sáng máy bay ✈️

Bao gồm động lực thời gian thực của hơn 1.500 chuyến bay trên 14 sân bay toàn Đài Loan. Mỗi máy bay là một quả cầu phát sáng, phía sau có vệt commet hình nón. Tỷ lệ chiều cao có thể điều chỉnh (1x ~ 5x), giúp bạn dễ dàng nhìn thấy sự khác biệt giữa các tuyến bay cao và thấp.

Nguồn dữ liệu: API FlightRadar24.

### Đại dương — Theo dõi tàu thuyền 🚢

Vị trí tàu thuyền trên biển quanh Đài Loan, được đánh dấu bằng quả cầu sáng xanh lam, mỗi tàu để lại dấu vệt 30 phút. Hệ thống tự động lọc ra các bước nhảy GPS bất thường và MMSI không hợp lệ, đảm bảo mỗi điểm sáng bạn nhìn thấy đều là một con tàu thực tế.

Nguồn dữ liệu: Dữ liệu vị trí tàu thuyền AIS (Hệ thống nhận diện tự động).

### Đất liền — Sáu hệ thống đường ray 🚄

Đây có lẽ là phần đáng ngạc nhiên nhất. Sáu hệ thống đường ray hoạt động đồng bộ:

| Hệ thống                     | Quy mô                                     |
| ---------------------------- | ------------------------------------------ |
| Đường sắt Đài Loan (TRA)     | 265 tuyến, 333 chuyến tàu, 6 màu theo loại |
| Tàu cao tốc Đài Loan (THSR)  | Tuyến chính nam-bắc + chi tuyến            |
| MRT Đài Bắc (TRTC)           | 8 tuyến                                    |
| MRT Cao Hùng (KRTC)          | Tuyến đỏ + tuyến cam                       |
| Tàu điện nhẹ Cao Hùng (KLRT) | Tàu điện nhẹ vòng quanh                    |
| MRT Đài Trung (TMRT)         | Tuyến xanh + tuyến xanh dương              |

Xử lý đường sắt Đài Loan đặc biệt phức tạp — kết hợp đường ray OD, tuyến phân nhánh như tam giác Chương Hóa, tất cả đều có động cơ xử lý chuyên biệt.

Nguồn dữ liệu: Lịch biểu công khai + dữ liệu đường ray [OpenStreetMap](https://www.openstreetmap.org/).

## Không chỉ là giao thông

Ngoài các phương tiện di chuyển, dự án còn xếp chồng các lớp tĩnh và phân tích:

- **Cơ sở hạ tầng**: Ranh giới 14 sân bay, cột sáng 535 nhà ga (chiều cao = số lần dừng), chùm sáng 3D quay 36 đèn biển
- **Mạng lưới đường bộ**: Đường bộ cao tốc (đỏ), đường tỉnh lộ (cam), đường xe đạp (xanh), độ rộng tự thích ứng zoom
- **Phân tích dân số**: Bản đồ nhiệt dân số lục giác H3, hỗ trợ chuyển đổi lưu lượng ngày/đêm, 9 chỉ số dân số
- **Khí tượng**: Dữ liệu trạm quan sát thời gian thực + bề mặt cong nhiệt độ 3D (độ phân giải lưới 0,03°)
- **Tin tức**: RSS Cơ quan thông tấn trung ương + API Gemini địa lý mã hoá, đánh dấu sự kiện tin tức trên bản đồ
- **Tắc đường đường bộ cao tốc**: Mức độ tắc đường thời gian thực mã hoá theo màu

Tổng cộng **23 lớp có thể chuyển đổi độc lập**, mười danh mục.

## Điểm sáng kỹ thuật

- **TypeScript + Mapbox GL + Three.js**: Bản đồ 2D dùng kết xuất gốc Mapbox, các phần tử 3D (quả cầu sáng, quỹ đạo sáng, cột sáng, bề mặt cong nhiệt độ) xếp chồng lên bằng Three.js
- **Xem xét hiệu suất**: Tàu thuyền dùng InstancedMesh kết xuất hàng loạt, loại bỏ thị trường (viewport culling) tránh kết xuất các đối tượng không nhìn thấy
- **Khoa học màu sắc**: Lớp dân số dùng các thang màu nhận thức đều Plasma / Viridis / Inferno, log1p + bình thường hoá gamma để xử lý phân phối đuôi nặng, thân thiện với người mù màu
- **Giấy phép MIT**: Hoàn toàn mã nguồn mở, hoan nghênh fork và đóng góp

> **📝 Ghi chú của người biên tập**
> Sử dụng additive blending để xếp chồng quỹ đạo sáng là lựa chọn thông minh — các khu vực đường bay trùng lặp tự nhiên sáng hơn, về mặt trực quan bạn có thể thấy mức độ tắc của tuyến bay mà không cần bảng thống kê bổ sung.

## Hệ sinh thái dữ liệu mở

Các nguồn dữ liệu mà dự án này kết nối, chính nó đã là một danh sách hướng dẫn dữ liệu mở Đài Loan:

| Dữ liệu                       | Nguồn                                                             |
| ----------------------------- | ----------------------------------------------------------------- |
| Vị trí máy bay thời gian thực | API FlightRadar24                                                 |
| AIS tàu thuyền                | Hệ thống nhận diện tự động tàu thuyền quốc tế                     |
| Lịch biểu đường sắt           | Lịch biểu công khai + OSM                                         |
| Xe buýt/Xe khách/Xe đạp       | [TDX Dữ liệu giao thông công cộng](https://tdx.transportdata.tw/) |
| Thống kê dân số               | [SEGIS Thông tin địa lý thống kê](https://segis.moi.gov.tw/)      |
| Quan sát khí tượng            | [Cơ quan khí tượng trung ương](https://www.cwa.gov.tw/)           |
| Trang trại gió ngoài khơi     | Bộ Năng lượng                                                     |
| Sự kiện tin tức               | RSS Cơ quan thông tấn trung ương CNA                              |
| Ranh giới sân bay/cảng/nhà ga | [API Overpass OSM](https://overpass-turbo.eu/)                    |

⚠️ **Điều đáng chú ý:** [Dịch vụ lưu thông dữ liệu TDX Đài Loan](https://tdx.transportdata.tw/) là một trong số ít nền tảng chính phủ hợp nhất dữ liệu giao thông công cộng toàn quốc theo tiêu chuẩn duy nhất, bao gồm xe buýt, xe khách, đường sắt, xe đạp, v.v., với tài liệu API hoàn chỉnh và sử dụng miễn phí. Điều này không phổ biến trên phạm vi toàn cầu.

## Liên kết

- **GitHub**: [ianlkl11234s/mini-taiwan-pulse](https://github.com/ianlkl11234s/mini-taiwan-pulse)
- **Giấy phép**: MIT License
- **Ngôn ngữ**: TypeScript
- **Tài nguyên liên quan**: [Nền tảng dữ liệu lưu thông TDX](https://tdx.transportdata.tw/) · [Nền tảng dữ liệu mở chính phủ](https://data.gov.tw/) · [Thông tin địa lý thống kê SEGIS](https://segis.moi.gov.tw/)

---

_Xác minh lần cuối: 2026-03-22_
