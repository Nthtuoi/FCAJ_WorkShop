---
title: "Worklog Tuần 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---
### Mục tiêu tuần 1:

* Kết nối, làm quen với các thành viên trong First Cloud AI Journey.
* Hiểu dịch vụ AWS cơ bản, cách dùng console & CLI.
* Tìm hiểu về quản trị tài khoản, Kiểm soát chi phí & AWS IAM

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Làm quen với các thành viên FCAJ <br> - Đọc và lưu ý các nội quy, quy định tại đơn vị thực tập                                                                                             | 20/04/2026   | 20/04/2026     |
| 3   | - Tìm hiểu AWS và các loại dịch vụ <br>&emsp; + Compute <br>&emsp; + Storage <br>&emsp; + Networking <br>&emsp; + Database <br>&emsp; + ... <br>                                            | 21/04/2026   | 21/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Tạo AWS Free Tier account <br> - Tìm hiểu AWS Console & AWS CLI <br> - **Thực hành:** <br>&emsp; + Thiết lập bảo mật đa lớp (Multi-Factor Authentication - MFA) cho tài khoản Root; <br> &emsp; + Cài AWS CLI & cấu hình <br> &emsp; + Cách sử dụng AWS CLI | 22/04/2026   | 22/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Tìm hiểu cơ chế vận hành của bộ phận AWS Support; Phân biệt các gói Support Plans (Basic, Developer, Business, Enterprise); Thực hành quy trình tạo ticket hỗ trợ kỹ thuật trên AWS Console.                  | 23/04/2026   | 23/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Nghiên cứu lý thuyết AWS Identity and Access Management (IAM); Phân tích các khái niệm cốt lõi: IAM Users, Groups, Roles và Policies (JSON format); Tìm hiểu nguyên lý đặc quyền tối thiểu (Principle of Least Privilege). <br> - **Thực hành AWS IAM Lab:** <br>&emsp; + Khởi tạo IAM Group (Dev/Admin), tạo IAM User, đính kèm các IAM Managed Policies <br>&emsp; + Thực hiện kiểm tra, phân tích quyền truy cập (Access Advisor) để xác minh tính chính xác của Policy<br>&emsp; + Gắn EBS volume                                                                                         | 24/04/2026   | 24/04/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 1 

* Hiểu AWS là gì và nắm được các nhóm dịch vụ cơ bản: 
  * Compute
  * Storage
  * Networking 
  * Database
  * ...

* Đã tạo và cấu hình AWS Free Tier account thành công.

* Làm quen với AWS Management Console và biết cách tìm, truy cập, sử dụng dịch vụ từ giao diện web.

* Cài đặt và cấu hình AWS CLI trên máy tính bao gồm:
  * Access Key
  * Secret Key
  * Region mặc định
  * ...

* Khởi tạo và Bảo mật Tài khoản Nền tảng AWS

  * Khởi tạo thành công tài khoản AWS Free Tier và làm quen với AWS Console/CLI
  * Hoàn thành thiết lập bảo mật đa lớp (MFA) cho tài khoản Root, đảm bảo an toàn tuyệt đối cho hệ thống.
  * ...

* Nghiên cứu Lý thuyết AWS IAM
  * Nắm vững cấu trúc JSON của Policy và phân biệt rõ các khái niệm Core (Users, Groups, Roles)
  * Hiểu nguyên lý "Đặc quyền tối thiểu" (Least Privilege) để ứng dụng vào bảo mật đám mây
* Triển khai thành công Lab tạo User, Group (Dev/Admin) và đính kèm Policy


