---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Kiến trúc hạ tầng mạng Amazon VPC.
* Cấu trúc định tuyến và các nhóm dịch vụ bảo mật mạng.
* Thực hành Lab và xử lý sự cố
### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Nghiên cứu lý thuyết Amazon Virtual Private Cloud (VPC)  <br>- Phân tích cấu trúc phân định địa chỉ IP bằng CIDR Block <br>- Tìm hiểu kiến trúc chia nhỏ mạng qua Public Subnet và Private Subnet.                                                                                              | 27/04/2026   | 27/04/2026      |
| 3   | - Nghiên cứu cơ chế định tuyến và bảo mật tầng mạng trong VPC <br>- Tìm hiểu chức năng của Internet Gateway (IGW), NAT Gateway, Route Tables, Security Groups (Stateful) và Network ACLs (Stateless).                                            | 28/04/2026   | 28/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   |- **Thực hành Lab VPC :** <br>&emsp; + Khởi tạo một VPC tùy chỉnh thủ công <br>&emsp; + Tạo lập các phân khu mạng Public Subnet và Private Subnet trên các Availability Zones (AZs) khác nhau để đảm bảo tính dự phòng. | 29/04/2026   | 29/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Tìm hiểu EC2 cơ bản: <br>&emsp; + Instance types <br>&emsp; + AMI <br>&emsp; + EBS <br>&emsp; + ... <br> - Các cách remote SSH vào EC2 <br> - Tìm hiểu Elastic IP   <br>                  | 30/04/2026   | 30/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - ****Thực hành Lab VPC:** <br>&emsp; + Khởi tạo và gắn kết Internet Gateway (IGW) vào Custom VPC <br>&emsp; + Cấu hình Custom Route Table để định tuyến traffic từ Public Subnet đi ra Internet qua IGW                                                                                          | 01/05/2026   | 01/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 2:

* Hiểu kiến trúc hạ tầng Amazon VPC và cơ chế phân bổ IP: 
  * CIDR Block: Thiết kế và phân bổ dải IP hợp lý, tránh trùng chấp với hệ thống local.
  * Subnetting: Phân chia mạng qua Public Subnet (kết nối Internet) và Private Subnet (cô lập bảo mật) trên nhiều Availability Zones (AZs) để dự phòng thảm họa.

* Nắm vững cấu trúc định tuyến và các nhóm dịch vụ bảo mật mạng: 
  * Routing: Hiểu rõ chức năng của Internet Gateway (IGW), NAT Gateway và cách cấu hình Route Tables để điều phối lưu lượng mạng.
  * Networking Security: Phân biệt rõ hai lớp bảo mật:
    * Security Groups: Tường lửa mức Instance (Stateful)
    * Network ACLs (NACLs): Tường lửa mức Subnet (Stateless).

* thực hành Lab và xử lý sự cố:

  * Triển khai: Khởi tạo thành công Custom VPC thủ công, liên kết IGW và cấu hình định tuyến cho Public Subnet ra Internet.
  * Xử lý sự cố: Có khả năng rà soát cấu hình, cô lập và sửa lỗi mất kết nối Internet hoặc cấu hình sai Route Table.
  * Tài liệu hóa: Tối ưu hóa kiến trúc và hoàn thiện sơ đồ luồng đi của network traffic.
  ![ảnh demo](/images/1-Worklog/Lab_VPC1.png)
  ![ảnh demo](/images/1-Worklog/lab_VPC2.png)
  ![ảnh demo](/images/1-Worklog/subnet1.png)
  ![ảnh demo](/images/1-Worklog/subnet2.png)
  ![ảnh demo](/images/1-Worklog/internet_gateway.png)
  ![ảnh demo](/images/1-Worklog/security_group1.png)
  ![ảnh demo](/images/1-Worklog/security_group2.png)