---
title: "Worklog Tuần 10"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu tuần 10:

* Kiểm thử toàn diện hệ thống (End-to-End Testing) và Kiểm thử chấp nhận người dùng (UAT).

* Sửa lỗi hệ thống (Bug Fixing) và tối ưu hóa hiệu năng ứng dụng (Performance Tuning).

* Thiết lập hệ thống giám sát và lưu vết nhật ký (Monitoring & Logging) trên AWS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Phối hợp nhóm thực hiện Kiểm thử toàn luồng (End-to-End Testing) từ lúc User Đăng ký -> Upload Audio -> Xem kết quả Transcribe. <br> - Ghi nhận các bug phát sinh.                                                                                             | 22/06/2026    | 22/06/2026      |
| 3   |  - Tập trung fix lỗi CORS trên API Gateway/S3. <br> - Xử lý các tình huống biên (Edge Cases): File âm thanh quá lớn gây Timeout, Token Cognito hết hạn giữa chừng khi Polling.                                           | 23/06/2026    | 23/06/2026       |  |
| 4   |  - Tối ưu hóa Frontend: Chạy Lazy Loading cho các component nặng, tối ưu dung lượng file build nhằm giảm thời gian tải trang ban đầu (First Contentful Paint) qua CloudFront.  | 24/06/2026    | 24/06/2026       |  |
| 5   |  - Nghiên cứu dịch vụ Amazon CloudWatch. <br> - Thiết lập Dashboard giám sát số lượng Request vào API Gateway, tỷ lệ lỗi 4XX/5XX, và lượng Logs từ các dịch vụ AWS sử dụng.                  | 25/06/2026    | 25/06/2026      |  |
| 6   |  - Mời một số người dùng bên ngoài chạy thử hệ thống (User Acceptance Testing - UAT). <br> - Thu thập phản hồi về trải nghiệm UI/UX và độ chính xác của tính năng xử lý âm thanh.                                                                                         | 26/06/2026    | 26/06/2026       | |


### Kết quả đạt được tuần 10:

* Kiểm thử toàn diện hệ thống (End-to-End Testing) và Kiểm thử chấp nhận người dùng (UAT).
  * Hoàn thành 100% kịch bản kiểm thử End-to-End; cô lập và xử lý triệt để các lỗi nghiêm trọng về CORS và lỗi Timeout khi xử lý file âm thanh dung lượng lớn.
  * Hệ thống tự động refresh token Cognito mượt mà, không làm gián đoạn luồng Polling API của người dùng.
  * 

* Thiết lập hệ thống giám sát và lưu vết nhật ký (Monitoring & Logging) trên AWS.
  * Thiết lập thành công bảng điều khiển CloudWatch Dashboard, cho phép theo dõi trực quan theo thời gian thực trạng thái sức khỏe của API Gateway, S3, và kiểm soát lưu lượng hệ thống.

  
