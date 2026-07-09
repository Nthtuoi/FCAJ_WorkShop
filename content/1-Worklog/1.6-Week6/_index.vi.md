---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
### Mục tiêu tuần 6:
Cơ sở dữ liệu quan hệ Amazon RDS & Quản lý tên miền Amazon Route 53
* Hiểu kiến trúc quản lý cơ sở dữ liệu quan hệ Amazon RDS.
* Triển khai, bảo mật và liên kết Database (Hands-on RDS Labs).
* Hiểu về dịch vụ quản lý hệ thống tên miền Amazon Route 53

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Nghiên cứu dịch vụ quản lý cơ sở dữ liệu quan hệ Amazon Relational Database Service (RDS)<br>- Tìm hiểu các tính năng tự động hóa: Automated Backups, Multi-AZ Deployments (Tính sẵn sàng cao) và Read Replicas (Mở rộng khả năng. đọc).                                                                                          | 25/05/2026   | 25/05/2026      |
| 3   |  -**Thực hành Lab RDS (Phần 1):**<br>&emsp; + Tạo lập một DB Subnet Group bao gồm các Private Subnets của Custom VPC<br>&emsp; + Tiến hành khởi tạo một Database Instance sử dụng Engine MySQL trên Amazon RDS nằm hoàn toàn trong phân khu mạng cô lập (Private Subnet).                                            | 26/05/2026    | 26/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | -**Thực hành Lab RDS (Phần 2):**<br>&emsp; + ảnh demo của RDS chấp nhận kết nối inbound (cổng 3306) duy nhất từ Security Group của máy chủ EC2 (Web Tier)<br>&emsp; + Thực hiện viết code/cấu hình kết nối từ ứng dụng Web trên EC2 tới Endpoint của RDS.    | 27/05/2026   | 27/05/2026     | <https://cloudjourney.awsstudygroup.com/> |
| 5   | -Nghiên cứu dịch vụ quản lý hệ thống tên miền Amazon Route 53 <br> - Tìm hiểu các chính sách định tuyến (Routing Policies: Simple, Weighted, Latency, Failover) và giải pháp thiết lập DNS Hybrid kết nối mạng nội bộ VPC.  <br>                  | 28/05/2026   | 28/05/2026     | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Thực hành Lab Route 53:** <br>&emsp; + Tạo một Private Hosted Zone gắn với Custom VPC<br>&emsp; + Khởi tạo các bản ghi DNS (A Record, CNAME Record) trỏ về máy chủ EC2 hoặc Elastic Load Balancer.                                                                                        | 29/05/2026   | 29/05/2026        | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 6:

* Hiểu kiến trúc quản lý cơ sở dữ liệu quan hệ Amazon RDS.

  * Quản trị tự động: Nắm vững kiến trúc tách biệt tầng dữ liệu và các tính năng tự động hóa giúp giảm tải công việc quản trị (Automated Backups, Multi-AZ Deployments cho tính sẵn sàng cao, và Read Replicas để mở rộng khả năng đọc).

  * Bảo mật tầng dữ liệu: Hiểu cách thiết kế DB Subnet Group nằm hoàn toàn trong phân khu mạng cô lập (Private Subnets) để cách ly hoàn toàn Database với Internet.

* Triển khai, bảo mật và liên kết Database (Hands-on RDS Labs).
  * Khởi tạo Database: Khởi tạo thành công Database Instance (Engine MySQL) bảo mật cao, không có IP Public trong Private Subnet của Custom VPC.

  * Kiến trúc 2 tầng (2-Tier): Cấu hình xuất sắc Security Group của RDS để chỉ chấp nhận kết nối inbound (cổng 3306) duy nhất từ Security Group của EC2 Web Tier. Kết nối và thực thi truy vấn/ghi dữ liệu thành công từ ứng dụng Web trên EC2 tới Endpoint của RDS.

* Hiểu về dịch vụ quản lý hệ thống tên miền Amazon Route 53
  * Chính sách định tuyến: Hiểu cách cấu hình Route 53 để chuyển đổi tên miền thân thiện (Domain Name) thành IP tài nguyên đám mây; nắm rõ các Routing Policies (Simple, Weighted, Latency, Failover) và giải pháp DNS Hybrid.
  
  * Phân giải nội bộ: Tạo lập thành công Private Hosted Zone gắn với Custom VPC và khởi tạo các bản ghi DNS (A Record, CNAME Record). Các tài nguyên nội bộ trong mạng VPC đã có thể tương tác mượt mà với nhau thông qua domain name tự định nghĩa.

![ảnh demo](/images/1-Worklog/rds1.png)
![ảnh demo](/images/1-Worklog/rds2.png)
* Tạo RDS Sercurity group
![ảnh demo](/images/1-Worklog/rds3.png)
* Tạo DB subnet group
![ảnh demo](/images/1-Worklog/rds4.png)
* Tạo EC2 Instance