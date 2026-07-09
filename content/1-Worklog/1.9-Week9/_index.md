---
title: "Week 9 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

* Develop a ReactJS frontend application using Vite and TailwindCSS.

* Integrate AWS services via Amplify SDK and Axios (API Gateway, Cognito, S3).

* Package source code and deploy to a production environment using Amazon S3 and CloudFront CDN.

### Tasks to be carried out this week:
| Day | Task                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 2   | - Initialize the ReactJS project using Vite. <br>- Configure the TailwindCSS UI library. <br>- Set up the standard directory structure (components/, services/, hooks/, context/).                                                                                                   | 15/06/2026 | 15/06/2026      | React & Vite Docs |
| 3   |- Install and configure the **AWS Amplify SDK** library to connect to the Cognito User Pool and App Client. <br>- Write the logic for the Registration/Login/OTP forms. <br>- Set up the **Protected Routes** protection layer.                                              | 16/06/2026 | 16/06/2026      |  AWS Amplify Docs |
| 4   | - Build a drag-and-drop component, limiting file extensions to .mp3 and .wav. <br>- Use Axios to retrieve the **S3 Presigned URL** from the API Gateway (POST /upload-url). <br>- Execute the PUT command to directly upload the file to the S3 Audio Bucket. | 17/06/2026 | 17/06/2026      | AWS S3 Developer Guide |
| 5   |- Call the GET API /jobs to populate the history table with data; write **Polling** logic (5-10 seconds) to update the file status. <br>- Code the page to display the transcript content, Copy and Download buttons. <br>- Collaborate with the Backend to perform **Integration Tests**.                           | 18/06/2026 | 18/06/2026      | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - Run the `npm run build` command to compile the source code into a static file. <br>- Initialize the S3 Frontend Bucket and enable Static Website Hosting. <br>- Initialize CloudFront Distribution and configure **Origin Access Control (OAC)**. <br>- Configure CloudFront Error Pages to redirect 403/404 errors to /index.html.                                                                                     | 19/06/2026 | 19/06/2026      | <https://cloudjourney.awsstudygroup.com/> |


### Week 9 Achievements:

* Implemented a ReactJS frontend application using Vite and TailwindCSS.

* Successfully initialized a ReactJS project using Vite and TailwindCSS with a standard enterprise directory structure; established State Management to tightly manage JWT tokens and a Polling API mechanism.

* Successfully integrated security configurations, fully handled the Registration/Login form flow, verified OTP codes via email, and set up Protected Routes protection.

* Integrated AWS services via Amplify SDK and Axios (API Gateway, Cognito, S3).

* Successfully built a drag-and-drop file component; mastered the skill of passing JWT tokens via Axios to obtain S3 presigned URLs from the API Gateway and execute a PUT command to securely push audio files directly to S3.

* Configure an automatic polling mechanism (5-10 second cycle) to update the file processing status, display compilation results (transcript), and coordinate the execution of system-wide integration tests.

*Image illustrating the Cognito-integrated login and OTP authentication interface:*

> ![Cognito Authentication Interface](/images/5-Workshop/giao-dien-auth-cognito.png)
> *Image illustrating the drag-and-drop file dashboard and processing history management list:*

> ![Dashboard and Data Polling Interface](/images/5-Workshop/giao-dien-dashboard-history.png)