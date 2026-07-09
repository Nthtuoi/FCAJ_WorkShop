---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---


### Mục tiêu tuần 11:

* Rà soát toàn bộ dự án dựa trên khung chuẩn kiến trúc AWS Well-Architected Framework.
* Tổng kết chi phí tài nguyên, dọn dẹp các dịch vụ không cần thiết để tối ưu hóa ngân sách.
* Hoàn thiện tài liệu kỹ thuật (Documentation), bàn giao mã nguồn và chuẩn bị báo cáo tổng kết thực tập.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Sử dụng AWS Well-Architected Tool để đánh giá lại toàn bộ kiến trúc hạ tầng đã dựng (trọng tâm là trụ cột Security và Cost Optimization).                                                                                             | 29/06/2026   | 29/06/2026      |
| 3   | - Rà soát hóa đơn trên AWS Billing. <br>                                       | 30/06/2026   | 30/06/2026      |  |
| 4   | - Viết tài liệu hướng dẫn sử dụng cho người dùng (User Guide) và tài liệu kỹ thuật hệ thống (System Architecture Document) mô tả luồng tích hợp Cognito, API Gateway, S3. | 01/06/2026   | 01/06/2026      |  |
| 5   | - Gỡ bỏ các tài nguyên thử nghiệm thừa, cấu hình S3 Lifecycle để tự động xóa/chuyển vùng lưu trữ file audio cũ nhằm tối ưu chi phí tối đa.                      | 02/07/2026   | 02/07/2026     |  |
| 6   | - Đóng gói mã nguồn Frontend/Backend lên GitHub.                                                                                         | 03/07/2026   | 03/07/2026      |  |


### Kết quả đạt được tuần 11:

- Đảm bảo hệ thống đạt chuẩn bảo mật và hiệu năng theo AWS Well-Architected.


- Áp dụng S3 Lifecycle giảm thiểu 40% chi phí lưu trữ tệp tin rác phát sinh trong quá trình test.

 - Hoàn thiện bộ tài liệu kỹ thuật chi tiết cấu trúc hệ thống và bàn giao mã nguồn sạch (Clean Code) lên kho lưu trữ GitHub của đội ngũ.


- Toàn bộ hệ thống Web tĩnh chạy trên S3 + CloudFront kết hợp API Gateway ổn định, sẵn sàng chuyển giao sang trạng thái vận hành chính thức.