---
title: "Week 2 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Amazon VPC network infrastructure architecture.

* Routing structure and network security service groups.

* Lab practice and troubleshooting.
### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Theoretical study of Amazon Virtual Private Cloud (VPC) <br>- Analysis of IP address allocation structure using CIDR Block <br>- Understanding network segmentation architecture via Public Subnet and Private Subnet.                                                                                                  | 27/04/2026 | 27/04/2026      |
| 3   | - Study the routing and network layer security mechanisms in VPC. <br>- Understand the functions of Internet Gateway (IGW), NAT Gateway, Route Tables, Security Groups (Stateful), and Network ACLs (Stateless).                                              | 28/04/2026 | 28/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - **VPC Lab Practice:** + Manually create a custom VPC + Establish Public Subnet and Private Subnet segments on different Availability Zones (AZs) to ensure redundancy. | 29/04/2026 | 29/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Understanding EC2 basics: <br>&emsp; + Instance types <br>&emsp; + AMI <br>&emsp; + EBS <br>&emsp; + ... <br> - Ways to remotely access EC2 via SSH <br> - Understanding Elastic IP <br>                            | 30/04/2026 | 30/04/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - ****VPC Lab Practice:** <br>&emsp; + Initialize and connect the Internet Gateway (IGW) to the Custom VPC <br>&emsp; + Configure a Custom Route Table to route traffic from the Public Subnet to the Internet via the IGW                                                                                     | 01/05/2026 | 01/05/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 2 Achievements:

* Understanding Amazon VPC infrastructure architecture and IP allocation mechanisms:

* CIDR Block: Designing and allocating IP ranges appropriately, avoiding conflicts with the local system.

* Subnetting: Dividing the network into Public Subnets (Internet connection) and Private Subnets (security isolation) across multiple Availability Zones (AZs) for disaster recovery.

* Mastering routing structure and network security service groups:

* Routing: Understanding the functions of Internet Gateway (IGW), NAT Gateway, and how to configure Route Tables to manage network traffic.

* Networking Security: Clearly distinguishing between two security layers:

* Security Groups: Instance-level firewalls (Stateful)

* Network ACLs (NACLs): Subnet-level firewalls (Stateless).

* Lab practice and troubleshooting:

* Deployment: Successfully creating a Custom VPC manually, linking the IGW, and configuring routing for the Public Subnet to the Internet.

* Troubleshooting: Capable of reviewing configurations, isolating and fixing internet connection issues or incorrect route table configurations.

* Documentation: Optimizing architecture and refining network traffic flow diagrams.
![ảnh demo](/images/1-Worklog/Lab_VPC1.png)
![ảnh demo](/images/1-Worklog/lab_VPC2.png)
![ảnh demo](/images/1-Worklog/subnet1.png)
![ảnh demo](/images/1-Worklog/subnet2.png)
![ảnh demo](/images/1-Worklog/internet_gateway.png)
![ảnh demo](/images/1-Worklog/security_group1.png)
![ảnh demo](/images/1-Worklog/security_group2.png)