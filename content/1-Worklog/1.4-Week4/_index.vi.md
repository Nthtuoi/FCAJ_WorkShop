---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:
Bảo mật ứng dụng với IAM Role & Quản trị qua AWS CLI
* Hiểu cơ chế cấp quyền an toàn cho ứng dụng đám mây.
* Thành thạo kỹ năng triển khai IAM Role và cấu hình AWS CLI (Hands-on Labs).
* Tương tác dịch vụ chéo và tổng hợp kiến trúc hệ thống

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | Nghiên cứu cơ chế cấp quyền an toàn cho ứng dụng (Application Permissions)<br> - Phân tích rủi ro bảo mật khi sử dụng hard-coded Access Keys<br> - Tìm hiểu giải pháp sử dụng IAM Role gán cho dịch vụ (EC2 Instance Profile).                                                                                             | 11/05/2026   | 11/05/2026      |
| 3   | - **Thực hành:**<br>&emsp; + Khởi tạo một IAM Role có quyền Read-Only <br>&emsp; + Tiến hành gán (Attach) IAM Role này vào máy chủ EC2 thông qua tính năng Modify IAM Role trên AWS Console.                                           | 12/05/2026   | 12/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Tìm hiểu và cài đặt công cụ AWS Command Line Interface (AWS CLI) trên môi trường hệ điều hành của EC2 (Ubuntu/Windows)<br>- Tìm hiểu các cú pháp lệnh cơ bản điều khiển tài nguyên (aws s3, aws ec2). | 13/05/2026   | 13/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | **Thực hành:** <br>&emsp; + Sử dụng các câu lệnh AWS CLI trên EC2 phát lệnh liệt kê, truy xuất tài nguyên từ dịch vụ AWS khác (như Amazon S3)<br>&emsp; + Kiểm chứng việc IAM Role đã tự động cấp quyền cho lệnh CLI thực thi thành công.                  | 14/05/2026   | 14/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Tiến hành rà soát, đánh giá toàn bộ kiến thức và sản phẩm thực hành của Tháng 1 (bao gồm: IAM, VPC, EC2, Cloud9, AWS CLI); Tổng hợp kiến thức viết báo cáo.                                                                                         | 15/05/2026   | 15/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Kết quả đạt được tuần 4:

* Hiểu cơ chế cấp quyền an toàn cho ứng dụng đám mây: 
  * Bảo mật Định danh: Nhận diện rõ rủi ro nghiêm trọng của việc dùng mã cứng (hard-coded) Access Keys; hiểu rõ cơ chế tự động xoay vòng mã xác thực tạm thời (Temporary Credentials) của IAM Role thông qua EC2 Instance Profile.
  * Ủy quyền An toàn: Nắm vững giải pháp gán quyền cho dịch vụ thay vì cho người dùng, giúp EC2 tương tác với các tài nguyên AWS khác mà không cần lưu trữ thông tin đăng nhập mật bên trong máy chủ.
 * ..

* Triển khai IAM Role và cấu hình AWS CLI (Hands-on Labs):
  * Cấu hình IAM Role: Khởi tạo thành công IAM Role (quyền Read-Only) và gán trực tiếp vào máy chủ EC2 (Modify IAM Role) trên AWS Console.
  * Cài đặt AWS CLI: Triển khai cài đặt thành công phiên bản AWS CLI mới nhất trên hệ điều hành của EC2 (Ubuntu/Windows) và kiểm tra trạng thái hoạt động ổn định qua Terminal.

* Tương tác dịch vụ chéo và tổng hợp kiến trúc hệ thống:

  * Thực thi CLI Nâng cao: Sử dụng thành thạo các cú pháp lệnh (aws s3, aws ec2) để liệt kê, truy xuất tài nguyên từ Amazon S3 thành công nhờ vào cơ chế định danh an toàn của IAM Role.
  * Tổng hợp & Đánh giá: Hoàn thành rà soát toàn bộ kiến thức cốt lõi (IAM, VPC, EC2, Cloud9, AWS CLI) và hoàn thiện Báo cáo tiến độ.

![ảnh demo](/images/1-Worklog/4_1.png)
![ảnh demo](/images/1-Worklog/4_2.png)
