---
title: "Week 6 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
### Week 6 Objectives:

Amazon RDS Relational Database & Amazon Route 53 Domain Management
* Understand the architecture of Amazon RDS relational database management.

* Deploy, secure, and link databases (Hands-on RDS Labs).

* Understand the Amazon Route 53 domain management service.
### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Research Amazon Relational Database Service (RDS) - Learn about automation features: Automated Backups, Multi-AZ Deployments (High Availability), and Read Replicas (Extended Capabilities).                                                                                                   | 25/05/2026 | 25/05/2026      |
| 3   | -**RDS Lab Practice (Part 1):**<br>&emsp; + Create a DB Subnet Group including the Private Subnets of the Custom VPC<br>&emsp; + Initialize a Database Instance using the MySQL Engine on Amazon RDS located entirely within an isolated network subnet (Private Subnet).                                              | 26/05/2026  | 26/05/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 4   | -**RDS Lab Practice (Part 2):**<br>&emsp; + Demo image of RDS accepting a single inbound connection (port 3306) from the EC2 server's Security Group (Web Tier)<br>&emsp; + Write code/configure the connection from the Web application on EC2 to the RDS Endpoint. | 27/05/2026 | 27/05/2026     | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Research Amazon Route 53 domain name management service. <br> - Learn about routing policies (Simple, Weighted, Latency, Failover) and a hybrid DNS setup solution for connecting a VPC internal network. <br>                           | 28/05/20265 | 28/05/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Lab Practice Route 53:** <br>&emsp; + Create a Private Hosted Zone associated with a Custom VPC<br>&emsp; + Initialize DNS records (A Record, CNAME Record) pointing to the EC2 server or Elastic Load Balancer.                                                                                    | 29/05/2026   | 29/05/2026        | <https://cloudjourney.awsstudygroup.com/> |


### Week 6 Achievements:

* Understand the Amazon RDS relational database management architecture.

  * Automated administration: Master the data layer separation architecture and automation features that reduce administrative workload (Automated Backups, Multi-AZ Deployments for high availability, and Read Replicas for extended read capabilities).

  * Data layer security: Understand how to design DB Subnet Groups entirely within isolated network subdivisions (Private Subnets) to completely isolate the database from the internet.

* Database deployment, security, and linking (Hands-on RDS Labs).

  * Database initialization: Successfully initialize a highly secure database instance (MySQL engine) with no public IP address in a Custom VPC's private subnet.

  * 2-Tier architecture: Excellently configure the RDS Security Group to accept only inbound connections (port 3306) from the EC2 Web Tier Security Group. Successfully connected and executed data queries/writes from an EC2 web application to an RDS endpoint.

* Understanding Amazon Route 53 domain name management service.

  * Routing Policy: Understand how to configure Route 53 to convert friendly domain names into cloud resource IPs; understand Routing Policies (Simple, Weighted, Latency, Failover) and the Hybrid DNS solution.

  * Internal Resolution: Successfully created a Private Hosted Zone associated with a Custom VPC and initialized DNS records (A Record, CNAME Record). Internal resources within the VPC network can now interact smoothly with each other through a custom domain name.
![ảnh demo](/images/1-Worklog/rds1.png)
![ảnh demo](/images/1-Worklog/rds2.png)
* Tạo RDS Sercurity group
![ảnh demo](/images/1-Worklog/rds3.png)
* Tạo DB subnet group
![ảnh demo](/images/1-Worklog/rds4.png)
* Tạo EC2 Instance