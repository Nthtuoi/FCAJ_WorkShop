---
title: "Week 4 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---


### Week 4 Objectives:

Secure Applications with IAM Roles & Administering via AWS CLI
* Understand secure permission mechanisms for cloud applications.

* Master the skills of deploying IAM Roles and configuring AWS CLI (Hands-on Labs).

* Interact across services and consolidate system architectures.

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | Research on secure application permission mechanisms<br> - Analysis of security risks when using hard-coded Access Keys<br> - Exploration of solutions using IAM Roles assigned to services (EC2 Instance Profile).                                                                                                  | 11/05/2026  | 11/05/2026       |
| 3   | - **Practice:** + Initialize an IAM Role with Read-Only permissions + Attach this IAM Role to the EC2 server using the Modify IAM Role feature on the AWS Console.                                              | 12/05/2026  | 12/05/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Learn and install the AWS Command Line Interface (AWS CLI) tool on the EC2 operating system environment (Ubuntu/Windows). - Learn the basic command syntax for controlling resources (aws s3, aws ec2). | 13/05/2026 | 13/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | **Practice:** <br>&emsp; + Use AWS CLI commands on EC2 to list and retrieve resources from other AWS services (such as Amazon S3)<br>&emsp; + Verify that the IAM Role has automatically granted permission for the CLI command to execute successfully.                            | 14/05/2026 | 14/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Conduct a comprehensive review and evaluation of all knowledge and practical products from January (including: IAM, VPC, EC2, Cloud9, AWS CLI); Summarize knowledge and write a report.                                                                                    | 15/05/2026 | 15/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 4 Achievements:

* Understanding secure authorization mechanisms for cloud applications:

  * Identity Security: Clearly identify the serious risks of using hard-coded Access Keys; understand the automatic rotation mechanism of temporary credentials for IAM Roles through EC2 Instance Profiles.

  * Secure Authorization: Master the solution of assigning permissions to services instead of users, enabling EC2 to interact with other AWS resources without storing confidential login credentials on the server.

  * ...

* Deploying IAM Roles and configuring AWS CLI (Hands-on Labs):

  * IAM Role Configuration: Successfully initialize the IAM Role (Read-Only permissions) and directly assign it to the EC2 server (Modify IAM Role) on the AWS Console.

  * AWS CLI Installation: Successfully deploy and install the latest version of AWS CLI on EC2's operating system (Ubuntu/Windows) and verify its stable operation via the Terminal.

* Cross-service interaction and system architecture integration:

  * Advanced CLI execution: Proficiently use command syntax (AWS S3, AWS EC2) to successfully enumerate and retrieve resources from Amazon S3 using the secure identification mechanism of the IAM Role.

  * Integration & Evaluation: Complete a review of all core knowledge areas (IAM, VPC, EC2, Cloud9, AWS CLI) and finalize the progress report.

![ảnh demo](/images/1-Worklog/4_1.png)
![ảnh demo](/images/1-Worklog/4_2.png)