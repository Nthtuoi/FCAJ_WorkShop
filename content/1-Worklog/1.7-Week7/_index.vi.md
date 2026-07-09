---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
Hệ thống Tự động mở rộng quy mô & Giám sát CloudWatch
* Hiểu nguyên lý thiết kế hệ thống có tính sẵn sàng cao (High Availability).
* Thiết lập hạ tầng tự động mở rộng (Hands-on ASG Labs).
* Hiểu về giám sát và kích hoạt phản ứng tự động (CloudWatch & Stress Test).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Nghiên cứu lý thuyết về thiết kế hệ thống có khả năng tự phục hồi và mở rộng (Scalability & High Availability)<br> - Tìm hiểu cách thức vận hành của Amazon EC2 Auto Scaling, Launch Templates và các chính sách tăng/giảm máy chủ (Scaling Policies).                                                                                              | 01/06/2026   | 01/06/2026      |
| 3   | - **Thực hành Lab Auto Scaling (Phần 1):** <br>&emsp; +  Tạo một Launch Template chứa cấu hình chuẩn của máy chủ Web (AMI, Instance Type, Security Group, User Data script)<br>&emsp; + Thiết lập một Auto Scaling Group (ASG) liên kết với nhiều Subnets khác nhau trên đa vùng khả dụng (Multi-AZ).                                             | 02/06/2026  | 02/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Nghiên cứu dịch vụ giám sát hệ thống Amazon CloudWatch<br> -  Tìm hiểu các khái niệm CloudWatch Metrics (Chỉ số), Logs (Nhật ký hệ thống), Alarms (Cảnh báo) và Dashboards (Bảng điều khiển trực quan). | 03/06/2026   | 03/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   |  - **Thực hành tích hợp hệ thống:** <br>&emsp; +  Cấu hình một CloudWatch Alarm theo dõi chỉ số sử dụng CPU (CPU Utilization) của Auto Scaling Group<br>&emsp; Thiết lập điều kiện: Nếu CPU > 70% trong vòng 3 phút, phát tín hiệu kích hoạt ASG tự động bổ sung thêm 1 máy chủ EC2 mới.                  | 04/06/2026   |   04/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Thực hành:** <br>&emsp; + Thực hiện bài Test tải giả lập (Stress Test) bằng cách chạy script vắt kiệt tài nguyên CPU trên máy chủ EC2 hiện tại<br>&emsp;+ Quan sát biểu đồ CloudWatch Dashboard và theo dõi hành vi phản ứng của hệ thống.                                                                                        | 05/06/2026   | 05/06/2026     | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 7:


* Hiểu nguyên lý thiết kế hệ thống có tính sẵn sàng cao (High Availability).

  * Scalability: Nắm vững nguyên lý "Bung - Co" (Scale-out / Scale-in) tự động của hạ tầng Cloud dựa theo nhu cầu sử dụng thực tế để tối ưu hóa hiệu suất và chi phí.

  * Auto Scaling & Cấu hình: Hiểu rõ cơ chế vận hành của Amazon EC2 Auto Scaling, cách hoạt động của Launch Templates và các chiến lược tăng/giảm máy chủ (Scaling Policies).

* Thiết lập hạ tầng tự động mở rộng (Hands-on ASG Labs).

  * Khởi tạo bộ khung: Khởi tạo thành công bộ khung Auto Scaling Group (ASG) với đầy đủ cấu hình số lượng máy chủ mong muốn (Desired), tối thiểu (Min) và tối đa (Max).

  * Thiết lập Launch Template: Tạo lập thành công Launch Template chuẩn hóa (AMI, Instance Type, Security Group, User Data script) liên kết với đa vùng khả dụng (Multi-AZ) để đảm bảo tính tự phục hồi khi có sự cố.

* Hiểu về giám sát và kích hoạt phản ứng tự động (CloudWatch & Stress Test).
* Giám sát hệ thống: Nắm chắc cách thiết lập các điểm kiểm soát hiệu năng phần cứng và lưu vết log hoạt động của ứng dụng qua CloudWatch Metrics, Logs, Alarms và Dashboards.


