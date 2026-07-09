---
title: "Week 7 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

CloudWatch Automated Scaling & Monitoring System
* Understand the principles of designing high-availability systems.

* Set up automated scaling infrastructure (Hands-on ASG Labs).

* Understand automated monitoring and response activation (CloudWatch & Stress Test).

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Theoretical research on the design of self-healing and scalable systems (Scalability & High Availability)<br> - Understanding how Amazon EC2 Auto Scaling, Launch Templates, and server scaling policies work.                                                                                                   | 01/06/2026 | 01/06/2026      |
| 3   | - **Auto Scaling Lab Practice (Part 1):** <br>&emsp; + Create a Launch Template containing standard Web server configuration (AMI, Instance Type, Security Group, User Data script)<br>&emsp; + Set up an Auto Scaling Group (ASG) linked to multiple different Subnets across multiple availability zones (Multi-AZ).                                              | 02/06/2026  | 02/06/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Research the Amazon CloudWatch system monitoring service - Learn about the concepts of CloudWatch Metrics, Logs, Alarms, and Dashboards. | 03/06/2026  | 03/06/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - **System Integration Practice:** <br>&emsp; + Configure a CloudWatch Alarm to monitor CPU usage of the Auto Scaling Group<br>&emsp; Set the condition: If CPU > 70% within 3 minutes, trigger ASG to automatically add a new EC2 server.                           | 04/06/2026  | 04/06/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Practice:** <br>&emsp; + Perform a simulated load test (Stress Test) by running a script that exhausts CPU resources on the current EC2 server.<br>&emsp; + Observe the CloudWatch Dashboard graph and monitor the system's response behavior.                                                                                     | 05/06/2026 | 05/06/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 7 Achievements:

* Understand the principles of high-availability system design.

  * Scalability: Master the principles of automatic scale-out/scale-in of cloud infrastructure based on actual usage needs to optimize performance and costs.

  * Auto Scaling & Configuration: Understand the operating mechanism of Amazon EC2 Auto Scaling, how Launch Templates work, and strategies for scaling up/down servers.

* Set up hands-on ASG Labs for automated scaling.

  * Framework creation: Successfully create an Auto Scaling Group (ASG) framework with full configuration of the desired number of servers (Desired), minimum (Min), and maximum (Max).

  * Launch Template Setup: Successfully create a standardized Launch Template (AMI, Instance Type, Security Group, User Data script) linked to multi-AZ (Multi-Availability Zone) to ensure self-recovery in case of failure.

* Understanding Monitoring and Activating Automated Responses (CloudWatch & Stress Test).

* System Monitoring: Master how to set up hardware performance control points and log application activity via CloudWatch Metrics, Logs, Alarms, and Dashboards.