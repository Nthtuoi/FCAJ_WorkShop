---
title: "Week 10 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:

* End-to-End Testing and User Acceptance Testing (UAT).

* Bug fixing and application performance tuning.

* Setting up monitoring and logging systems on AWS.

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Collaborate with the team to conduct End-to-End testing, covering the flow from User Registration to Audio Upload and viewing Transcription results. <br> - Log any bugs encountered.                                                                                                   |22/06/2026 | 22/06/2026      |
| 3   | - Focused on fixing CORS issues on API Gateway/S3. <br> - Handled edge cases: audio files that are too large causing timeouts, and Cognito tokens expiring during polling.                                              | 23/06/2026 | 23/06/2026      |  |
| 4   | - Frontend Optimization: Implement lazy loading for heavy components and optimize build file sizes to reduce initial page load time (First Contentful Paint) via CloudFront. | 24/06/2026 | 24/06/2026      |  |
| 5   | - Research the Amazon CloudWatch service. <br> - Set up a dashboard to monitor the number of API Gateway requests, 4XX/5XX error rates, and log volumes from the AWS services being used.                          | 25/06/2026 | 25/06/2026      |  |
| 6   | - Invite select external users to test the system (User Acceptance Testing - UAT). <br> - Gather feedback on the UI/UX experience and the accuracy of the audio processing features.                                                                                    | 26/06/2026 | 26/06/2026      |  |


### Week 10 Achievements:

* End-to-End Testing and User Acceptance Testing (UAT).
  * Completed 100% of End-to-End test scenarios; isolated and fully resolved critical CORS errors and timeout issues encountered when processing large audio files.
  * Implemented seamless automatic Cognito token refreshing that does not disrupt the user's API polling flow.
  * 

* Setup of monitoring and logging systems on AWS.
  * Successfully configured CloudWatch Dashboards, enabling real-time visual monitoring of API Gateway and S3 health status as well as system traffic management.