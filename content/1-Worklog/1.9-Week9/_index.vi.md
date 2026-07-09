---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---


### Mục tiêu tuần 9:

* Triển khai phát triển ứng dụng Frontend ReactJS bằng Vite và TailwindCSS.
* Tích hợp các dịch vụ AWS thông qua Amplify SDK, Axios (API Gateway, Cognito, S3).
* Đóng gói mã nguồn và triển khai lên môi trường Production sử dụng Amazon S3 và CloudFront CDN.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Khởi tạo dự án ReactJS bằng Vite. <br>- Cấu hình thư viện UI TailwindCSS. <br>- Thiết lập cấu trúc thư mục chuẩn (components/, services/, hooks/, context/). | 15/06/2026   | 15/06/2026      | React & Vite Docs |
| 3   | - Cài đặt, cấu hình thư viện **AWS Amplify SDK** kết nối đến Cognito User Pool và App Client. <br>- Viết logic Form Đăng ký/Đăng nhập/OTP. <br>- Thiết lập lớp bảo vệ **Protected Routes**. | 16/06/2026   | 16/06/2026      | AWS Amplify Docs |
| 4   | - Xây dựng Component kéo thả file (**Drag & Drop**), giới hạn đuôi1 .mp3, .wav. <br>- Dùng Axios lấy **S3 Presigned URL** từ API Gateway (POST /upload-url). <br>- Thực hiện lệnh PUT đẩy trực tiếp file lên S3 Audio Bucket. | 17/06/2026   | 17/06/2026      | AWS S3 Developer Guide |
| 5   | - Gọi API GET /jobs đổ dữ liệu vào bảng lịch sử; viết logic **Polling** (5-10s) cập nhật trạng thái file. <br>- Code trang hiển thị nội dung transcript, nút Copy và Download. <br>- Phối hợp với Backend làm **Integration Test**. | 18/06/2026   | 18/06/2026      | Nội bộ dự án |
| 6   | - Chạy lệnh npm run build biên dịch mã nguồn thành file tĩnh. <br>- Khởi tạo S3 Frontend Bucket, bật Static Website Hosting. <br>- Khởi tạo CloudFront Distribution, cấu hình **Origin Access Control (OAC)**. <br>- Cấu hình CloudFront Error Pages điều hướng lỗi 403/404 về /index.html. | 19/06/2026   | 19/06/2026      | AWS CloudFront Guide |

### Kết quả đạt được tuần 9:

* Triển khai phát triển ứng dụng Frontend ReactJS bằng Vite và TailwindCSS.

  * Khởi tạo thành công dự án ReactJS bằng Vite + TailwindCSS với cấu trúc thư mục chuẩn doanh nghiệp; thiết lập State Management quản lý chặt chẽ JWT Token và cơ chế Polling API.

  * Tích hợp thành công cấu hình bảo mật, xử lý trọn vẹn luồng Form Đăng ký/Đăng nhập, xác thực mã OTP qua Email và thiết lập lớp bảo vệ Protected Routes.
 
* Tích hợp các dịch vụ AWS thông qua Amplify SDK, Axios (API Gateway, Cognito, S3).

  * Xây dựng thành công Component kéo thả file (Drag & Drop); làm chủ kỹ năng truyền JWT Token qua Axios để lấy S3 Presigned URL từ API Gateway và thực hiện lệnh PUT đẩy trực tiếp file âm thanh lên S3 an toàn.
  * Cấu hình cơ chế tự động Polling (chu kỳ 5-10 giây) để cập nhật trạng thái File Processing, hiển thị kết quả biên dịch (Transcript) và phối hợp thực hiện Integration Test toàn luồng hệ thống.

![anh demo](/images/5-Workshop/5.3-DeployFrontend/deploy-11.png)
![anh demo](/images/5-Workshop/5.3-DeployFrontend/sp-1.png)
![anh demo](/images/5-Workshop/5.3-DeployFrontend/sp-2.png)
![anh demo](/images/5-Workshop/5.3-DeployFrontend/sp-3.png)