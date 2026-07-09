---
title: "Worklog Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Hiểu dịch vụ điện toán đám mây Amazon EC2 và cơ chế cấu hình.
* Thực hành khởi tạo và triển khai ứng dụng (Hands-on Labs).
* Tiếp cận môi trường lập trình đám mây và kỹ năng dòng lệnh

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Nghiên cứu dịch vụ điện toán đám mây Amazon Elastic Compute Cloud (EC2); <br> -  Tìm hiểu các họ máy chủ (Instance Types), cơ chế đóng gói hệ điều hành (Amazon Machine Image - AMI) và quản lý bảo mật qua Key Pairs.                                                                                             | 04/05/2026   | 04/05/2026      |<https://cloudjourney.awsstudygroup.com/> |
| 3   | -**Thực hành LAB EC2 (Phần 1):**<br>&emsp; + Khởi tạo (Launch) một máy chủ ảo EC2 sử dụng hệ điều hành Linux/Windows đặt trong Public Subnet của Custom VPC<br>&emsp; + ảnh demo cho phép mở cổng SSH (22) và RDP (3389)                                            | 05/05/2026   | 05/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | -**Thực hành Lab EC2 (Phần 2):**<br>&emsp; + Truy cập vào EC2 Instance<br>&emsp; + Cài đặt và cấu hình một dịch vụ Web Server (Nginx hoặc Apache) <br>&emsp; +ảnh demo mở cổng HTTP (80).  | 06/05/2026   | 06/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   |- Tìm hiểu dịch vụ AWS Cloud9 <br>- Khởi tạo một môi trường phát triển tích hợp (Cloud IDE) dựa trên nền tảng đám mây<br>- Cấu hình liên kết Cloud9 với tài nguyên EC2.                  | 07/05/2026   | 07/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | -Sử dụng terminal của AWS Cloud9 để thực thi các script tự động hóa cơ bản<br>- Thực hành quản lý tệp tin và kiểm tra hiệu năng (CPU/RAM) của máy chủ thông qua giao diện dòng lệnh của Cloud9.                                                                                        | 08/05/2026   | 08/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 3:

* Hiểu dịch vụ điện toán đám mây Amazon EC2 và cơ chế cấu hình: 
  * Instance Cấu hình: Nắm vững tiêu chí lựa chọn họ máy chủ (Instance Types) tối ưu chi phí (CPU, RAM, Storage) theo từng loại tải ứng dụng.
  * AMI & Key Pairs: Hiểu rõ cơ chế đóng gói hệ điều hành qua Amazon Machine Image (AMI) và cách quản lý bảo mật truy cập bằng cặp khóa (Key Pairs).

* Thực hành khởi tạo và triển khai ứng dụng (Hands-on Labs)
  * Khởi chạy & Kết nối: Khởi tạo thành công máy chủ EC2 (Linux/Windows) trong Public Subnet của Custom VPC. Kết nối từ xa ổn định qua Terminal (SSH - cổng 22) hoặc Remote Desktop (RDP - cổng 3389).
  * Web Server: Cài đặt, cấu hình thành công dịch vụ Web Server (Nginx/Apache) và mở đúng cổng HTTP (80) trên Security Group để kiểm tra truy cập public qua IP Public thành công.

* Tiếp cận môi trường lập trình đám mây và kỹ năng dòng lệnh:
  * AWS Cloud9: Thiết lập không gian làm việc code tập trung trực tiếp trên trình duyệt tích hợp sẵn AWS CLI; nhận diện và phân tích được nguyên nhân sự cố khi gặp tình huống không truy cập được Cloud9 để xử lý liên kết tài nguyên.
  * CLI & Terminal: Sử dụng dòng lệnh để thực thi script tự động hóa cơ bản, quản lý tệp tin và kiểm tra hiệu năng hệ thống (CPU/RAM) của máy chủ.

![ảnh demo](/images/1-Worklog/Launch_microsoft1.png)
![ảnh demo](/images/1-Worklog/Launch_microsoft2.png)
![ảnh demo](/images/1-Worklog/custom_IAM.png)
![ảnh demo](/images/1-Worklog/s3_bucket.png)
* Create S3 bucket
![ảnh demo](/images/1-Worklog/s3_1.png)
* Thực thiện tải dữ liệu lên

![ảnh demo](/images/1-Worklog/s3_2.png)
* Bật tính năng static website

![ảnh demo](/images/1-Worklog/s3_3.png)
* Cấu hình block public access

![ảnh demo](/images/1-Worklog/s3_4.png)
* Kiểm tra website

![ảnh demo](/images/1-Worklog/s3_5.png)
* Truy cập với distribution domain name
