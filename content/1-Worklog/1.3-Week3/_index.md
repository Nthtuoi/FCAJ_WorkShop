---
title: "Week 3 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives:

* Understand the Amazon EC2 cloud computing service and its configuration mechanism.

* Practice application creation and deployment (Hands-on Labs).

* Gain exposure to the cloud programming environment and command-line skills.

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Research the Amazon Elastic Compute Cloud (EC2) cloud computing service; <br> - Learn about server families (Instance Types), operating system packaging mechanisms (Amazon Machine Image - AMI), and security management via Key Pairs.                                                                                                   | 04/05/2026 | 04/05/2026      |
| 3   | -**EC2 LAB Practice (Part 1):**<br>&emsp; + Launch an EC2 virtual server using Linux/Windows operating system placed in the Public Subnet of a Custom VPC<br>&emsp; + demo image showing how to open SSH (22) and RDP (3389) ports                                              | 05/05/2026 | 05/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | -**EC2 Lab Practice (Part 2):**<br>&emsp; + Accessing EC2 Instance<br>&emsp; + Installing and configuring a Web Server service (Nginx or Apache)<br>&emsp; + Demo image of opening HTTP port (80). | 06/05/2026 | 06/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Learn about AWS Cloud9 services. <br>- Create a cloud-based integrated development environment (Cloud IDE).<br>- Configure Cloud9 to connect with EC2 resources.                            | 07/05/2026 | 07/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Use the AWS Cloud9 terminal to execute basic automation scripts. - Practice file management and server performance testing (CPU/RAM) through the Cloud9 command-line interface.                                                                                    | 08/05/2026 | 08/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 3 Achievements:

* Understanding Amazon EC2 cloud computing services and configuration mechanisms:

* Instance Configuration: Master the criteria for selecting cost-effective server families (CPU, RAM, Storage) for each application load.

* AMI & Key Pairs: Understand the operating system packaging mechanism via Amazon Machine Image (AMI) and how to manage access security using key pairs.

* Hands-on Labs: Practice creating and deploying applications.

* Launching & Connecting: Successfully create an EC2 server (Linux/Windows) in the Public Subnet of a Custom VPC. Establish a stable remote connection via Terminal (SSH - port 22) or Remote Desktop (RDP - port 3389).

* Web Server: Successfully install and configure the Web Server service (Nginx/Apache) and open the correct HTTP port (80) on the Security Group to test successful public access via the Public IP.

* Access to cloud programming environments and command-line skills:

* AWS Cloud9: Setting up a centralized coding workspace directly in the browser using the built-in AWS CLI; identifying and analyzing the root causes of Cloud9 access issues to resolve resource linking problems.

* CLI & Terminal: Using the command line to execute basic automation scripts, manage files, and check server system performance (CPU/RAM).

![ảnh demo](/images/1-Worklog/Launch_microsoft1.png)
![ảnh demo](/images/1-Worklog/Launch_microsoft2.png)
![ảnh demo](/images/1-Worklog/custom_IAM.png)
![ảnh demo](/images/1-Worklog/s3_bucket.png)
* Create S3 bucket
![ảnh demo](/images/1-Worklog/s3_1.png)
* Complete the data upload.

![ảnh demo](/images/1-Worklog/s3_2.png)
*Enable static website functionality.

![ảnh demo](/images/1-Worklog/s3_3.png)
* Configure public access block

![ảnh demo](/images/1-Worklog/s3_4.png)
* Check the website

![ảnh demo](/images/1-Worklog/s3_5.png)
* Access with distribution domain name
