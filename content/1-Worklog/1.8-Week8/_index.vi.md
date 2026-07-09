---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:
Triển khai dự án Audio To Text
* Phân tích, khảo sát hệ thống và Thiết kế kiến trúc hạ tầng Cloud.


### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Họp nhóm phân tích chi tiết các ca sử dụng (Use Cases) của hệ thống: Đăng ký/đăng nhập, cơ chế sinh Presigned URL để upload file trực tiếp, vòng đời xử lý của Amazon Transcribe, và quy trình gửi thông báo tự động.<br>- Bóc tách "Hợp đồng dữ liệu" (API Contract) – thống nhất cấu trúc JSON đầu vào/đầu ra giữa Frontend và Backend.                                                                                              | 08/06/2026   | 08/06/2026           |
| 3   | -Thiết kế giao diện khung (Wireframe) cho các màn hình: Màn hình Login/Register, Dashboard chính (chứa khu vực kéo thả file), Trạng thái xử lý file theo thời gian thực, và Trang lịch sử (History).<br>- Thiết kế sơ đồ luồng dữ liệu.                                           | 09/06/2026   | 09/06/2026       |  |
| 4   | -  Phác thảo sơ đồ kiến trúc hạ tầng Cloud cho toàn bộ dự án. | 10/06/2026    | 10/06/2026       |  |
| 5   | - Đánh giá rủi ro (Risk Assessment) & Đóng gói báo cáo kế hoạch.                        | 11/06/2026    | 11/06/2026       | > |
| 6   | - Viết báo cáo tổng kết giai đoạn Kế hoạch .                                                                                        | 12/06/2026    | 12/06/2026       |  |


### Kết quả đạt được tuần 8:

* Phân tích, khảo sát hệ thống và Thiết kế kiến trúc hạ tầng Cloud.
  * Thiết kế thành công sơ đồ kiến trúc hạ tầng Cloud áp dụng nghiêm ngặt các tiêu chuẩn AWS Well-Architected: Trụ cột Security (Cognito Authorizer, S3 OAC) và Performance Efficiency (giảm tải bằng SQS, tối ưu bằng CloudFront).
  * Nhận diện và xây dựng giải pháp dự phòng (Fallback plans) cho các rủi ro kỹ thuật lớn như lỗi CORS, lỗi quá hạn Presigned URL và lỗi Timeout khi xử lý file dung lượng lớn.
  * tư duy bóc tách luồng nghiệp vụ phức tạp: Đăng nhập (Cognito), sinh Presigned URL, vòng đời Amazon Transcribe và hệ thống gửi thông báo tự động.

![anh minh hoa phan tich du an](/images/1-Worklog/phantichvakhaosat.png)
* Phân tích dự án

![anh minh hoa luong hoat dong](/images/1-Worklog/workflow.png)
* Luồng hoạt động

![anh minh hoa dich vu can dung](/images/1-Worklog/dichvu.png)
* Các dịch vụ trong dự án

![anh minh hoa so do aws Architecture](/images/1-Worklog/sodo.png)
* Sơ đồ AWS Architecture