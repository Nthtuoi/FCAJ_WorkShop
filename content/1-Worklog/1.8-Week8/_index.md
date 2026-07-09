---
title: "Week 8 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:

Implementing the Audio-To-Text project:
* System analysis, survey, and Cloud infrastructure architecture design.

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Team meeting to analyze system use cases in detail: Registration/login, presigned URL generation mechanism for direct file uploads, Amazon Transcribe processing lifecycle, and automated notification process.<br>- Dissecting the "Data Contract" (API Contract) – standardizing the input/output JSON structure between the frontend and backend.                                                                                                   | 08/06/2026 | 08/06/2026      |
| 3   | - Design wireframe interfaces for the following screens: Login/Register screen, main dashboard (containing the file drag-and-drop area), real-time file processing status, and history page.<br>- Design data flow diagrams.                                              | 09/06/2026 | 09/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Sketch out the cloud infrastructure architecture diagram for the entire project. |10/06/2026  | 10/06/2026       | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Risk Assessment & Planning Report Packaging.                            | 11/06/2026 | 11/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Write a summary report of the Plan phase.                                                                                   |12/06/2026 | 12/06/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 8 Achievements:

* System analysis, survey, and Cloud infrastructure architecture design.

  * Successfully designed a Cloud infrastructure architecture diagram strictly adhering to AWS Well-Architected standards: Security pillar (Cognito Authorizer, S3 OAC) and Performance Efficiency (load reduction using SQS, optimization using CloudFront).

  * Identifyed and developed fallback plans for major technical risks such as CORS errors, Presigned URL expiration errors, and Timeout errors when processing large files.

  * Developed a sophisticated business process analysis: Login (Cognito), Presigned URL generation, Amazon Transcribe lifecycle, and automated notification system.
  ![anh minh hoa phan tich du an](/images/1-Worklog/phantichvakhaosat.png)
* Project analysis

![anh minh hoa luong hoat dong](/images/1-Worklog/workflow.png)
* Workflow

![anh minh hoa dich vu can dung](/images/1-Worklog/dichvu.png)
* Services in the project

![anh minh hoa so do aws Architecture](/images/1-Worklog/sodo.png)
*AWS Architecture Diagram