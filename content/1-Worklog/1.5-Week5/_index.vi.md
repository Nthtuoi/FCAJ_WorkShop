---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---


### Mục tiêu tuần 5:
Dịch vụ lưu trữ Amazon S3 & Triển khai nhanh với Amazon Lightsail
* Hiểu bản chất dịch vụ lưu trữ đối tượng Amazon S3.
* Thực hành cấu hình S3 và xử lý lỗi phân quyền (Hands-on S3 Labs).
* Tiếp cận giải pháp triển khai nhanh Amazon Lightsail.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Nghiên cứu dịch vụ lưu trữ đối tượng Amazon Simple Storage Service (S3)<br>- Tìm hiểu các khái niệm Buckets, Objects, S3 Storage Classes và tính năng Static Website Hosting trên.S3.                                                                                             | 18/05/2026   | 18/05/2026      |
| 3   | - **Thực hành LAB S3 (Phần 1):** <br>&emsp;+  Khởi tạo một S3 Bucket công khai<br>&emsp;+ Tải lên (Upload) các mã nguồn của một trang web tĩnh (gồm các file .html, .css, .js)<br>&emsp;+ Kích hoạt tính năng Static Website Hosting                                            | 19/05/2026   | 19/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - **Thực hành LAB S3 (Phần 2):** <br>&emsp;+  Cấu hình S3 Block Public Access <br>&emsp;+ Viết và áp dụng một đoạn mã cấu hình S3 Bucket Policy (định dạng JSON) nhằm cấp quyền đọc công khai (s3:GetObject) cho mọi người dùng Internet. | 20/05/2026   | 20/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Nghiên cứu dịch vụ Amazon Lightsail<br>- Tìm hiểu giải pháp triển khai ứng dụng trọn gói (VPS tích hợp sẵn bản quyền, database, network) với chi phí cố định<br>- Phân biệt phạm vi sử dụng giữa Lightsail và Amazon EC2.                  | 21/05/2026   | 21/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Thực hành Lightsail:** <br>&emsp; +  Tạo mới một WordPress Instance trên nền tảng Amazon Lightsail<br>&emsp; + Thiết lập Static IP và cấu hình tường lửa (Firewall) ngay trên giao diện rút gọn của Lightsail.                                                                                        | 22/05/2026   | 22/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 5:

* Hiểu bản chất dịch vụ lưu trữ đối tượng Amazon S3: 
  * Lưu trữ dữ liệu: Nắm vững nguyên lý lưu trữ dữ liệu phi cấu trúc thông qua các khái niệm Buckets, Objects và phương pháp tối ưu chi phí theo vòng đời dữ liệu (Lifecycle Policy/Storage Classes).
  * Static Website: Hiểu cơ chế hoạt động của tính năng Static Website Hosting để biến một S3 Bucket thành không gian lưu trữ và chạy trực tiếp website tĩnh trên Internet.
  * ...

* Thực hành cấu hình S3 và xử lý lỗi phân quyền (Hands-on S3 Labs):
  * Triển khai Web tĩnh: Tải lên thành công mã nguồn (.html, .css, .js) và kích hoạt Endpoint URL cho website tĩnh. Nhận diện và cô lập lỗi 403 Forbidden khi hệ thống chưa được mở quyền.
  * Cấu hình Bảo mật: Làm chủ kỹ năng quản lý truy cập bằng cách cấu hình S3 Block Public Access kết hợp viết mã JSON cho S3 Bucket Policy (s3:GetObject), giúp xử lý triệt để lỗi phân quyền và đưa website vận hành public mượt mà.
  * ...

* Tiếp cận giải pháp triển khai nhanh Amazon Lightsail:
  * Tối ưu giải pháp: Phân biệt rõ phạm vi sử dụng giữa Lightsail (chi phí cố định, trọn gói) và EC2 (linh hoạt, tùy biến cao); hiểu phương án tối ưu chi phí và đẩy nhanh tốc độ đưa sản phẩm ra thị trường (Time-to-market) cho các dự án nhỏ.
  *Thực hành WordPress: Khởi tạo thành công một WordPress Instance tích hợp sẵn database trên đám mây; thiết lập thành thạo Static IP và cấu hình tường lửa (Firewall) ngay trên giao diện rút gọn của Lightsail.
* ...


