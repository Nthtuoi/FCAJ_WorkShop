---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AWS Audio To Text 
## Speech-to-Text Conversion System on AWS

### 1. Project Overview

The AWS Audio To Text project is a serverless system built on AWS that allows users to upload audio or video files (such as MP3, MP4, WAV, or M4A) and automatically convert spoken content into text.

Users access the website via Amazon CloudFront, authenticate using Amazon Cognito, and upload files to Amazon S3 using presigned URLs. Once uploaded, files are automatically processed through an S3 event trigger, SQS, Lambda, and Amazon Transcribe. The resulting transcripts are stored in an S3 output bucket, job statuses are recorded in DynamoDB, and email notifications are sent via Amazon SNS.

In this workshop, the team will present the entire system-building process, covering architectural design, AWS service deployment, Lambda coding, React frontend integration, pipeline testing, and website deployment to CloudFront. AWS Audio To Text – An audio-to-text conversion system on AWS.

### 2. Objectives

The primary objective of the project is to build an automated audio-to-text conversion system on the AWS platform.

Specific objectives include:
- Build a serverless system: Utilize Lambda, S3, SQS, API Gateway, and DynamoDB to minimize server management.
- Support audio/video file uploads: Allow users to upload MP3, MP4, WAV, and M4A files.
- Convert audio to text: Use Amazon Transcribe to generate transcripts.
- Manage users: Use Amazon Cognito for user registration, login, and authentication.
- Store conversion history: Save metadata, job status, and transcript paths in DynamoDB.
- Send notifications: Use Amazon SNS to send email notifications upon job completion.
- Deploy the website online: Host the React frontend using an S3 bucket and CloudFront.
- Monitor and debug: Use CloudWatch Logs to track Lambda activity.
### 3. Problem to Solve

*Current Issue* </br>
After online meetings, classes, or interviews, users often have to listen to entire audio or video files to take notes on key points. This process is time-consuming, prone to information loss, and difficult to manage when dealing with multiple files. Furthermore, audio/video files are often large; uploading them via a traditional backend can overload the system. Since converting audio to text is also time-consuming, there is a need for an automated, asynchronous, and user-secure processing system.

*Solution* </br>
The AWS Audio-to-Text system utilizes a serverless architecture on AWS to automatically convert audio into text. Users log in via Amazon Cognito and upload files directly to Amazon S3 using presigned URLs. Upon upload, an S3 Event sends a message to Amazon SQS, triggering AWS Lambda to call Amazon Transcribe for the audio-to-text conversion. The output is stored in an S3 Output Bucket, while processing status and history are saved in DynamoDB; additionally, Amazon SNS sends an email notification upon completion. The website is deployed using an S3 Frontend Bucket and CloudFront, enabling users to easily access the site, view transcripts, download results, and manage their file history.

### 4. Solution Architecture
The system is designed based on a serverless model, comprising the following key layers: frontend, authentication, API, processing, storage, database, notification, and monitoring.
![anhsodo](/images/2-Proposal/anhsodo1.jpg)
*AWS Services Used*
- *Amazon CloudFront*: Distributes the React website via HTTPS.
- *Amazon S3*: Stores React frontend build files, user-uploaded audio/video files, and `transcript.json`/`transcript.txt` files (across 3 buckets).
- *Amazon Cognito*: Manages registration, login, and JWT token issuance.
- *Amazon API Gateway*: Provides APIs for the frontend to communicate with the backend.
- *AWS Lambda*: Handles serverless backend logic (5 functions).
- *Amazon SQS*: Queues audio files for asynchronous processing.
- *Amazon Transcribe*: Converts audio to text.
- *Amazon DynamoDB*: Stores job details, processing status, and file history.
- *Amazon SNS*: Sends email notifications upon completion of processing.
- *Amazon CloudWatch*: Stores logs and supports Lambda debugging.
*Component Design*
- *Web Interface*: The React application is built and hosted in an Amazon S3 frontend bucket, then distributed via Amazon CloudFront to allow user access to the system over HTTPS.
- *User Management*: Amazon Cognito handles registration and login, issuing JWT tokens to authenticate users during API calls.
- *API Gateway*: Amazon API Gateway receives requests from the frontend, validates Cognito tokens, and routes requests to the appropriate Lambda functions.
- *File Upload*: The `lambda-upload-url` function generates a presigned URL allowing users to upload audio/video files directly to the Amazon S3 audio bucket, while simultaneously creating a job record in DynamoDB.
- *Input File Storage*: The Amazon S3 audio bucket stores user-uploaded MP3, MP4, WAV, or M4A files.
- *Processing Queue*: Amazon SQS receives events from the S3 audio bucket following file uploads, enabling asynchronous processing and preventing system overload.
- *Transcription processing*: The `lambda-processor` reads messages from SQS and invokes Amazon Transcribe to convert audio content into text.
- *Result storage*: The Amazon S3 Output Bucket stores transcription results, including the `transcript.json` file generated by Transcribe and a `transcript.txt` file reformatted for readability.
- *Result handling*: The `lambda-result-handler` reads the `transcript.json` file, generates the `transcript.txt` file, updates the job status in DynamoDB, and sends a notification via SNS.
- *State management*: Amazon DynamoDB stores job details, processing status, `user_id`, file name, creation timestamp, and the transcription file path.
- *Result retrieval*: The `lambda-get-job` function retrieves the job status from DynamoDB and the `transcript.txt` content from the S3 Output Bucket, returning the result to the web interface.
- *Transcription history*: The `lambda-list-jobs` function retrieves the list of uploaded and transcribed files for the currently logged-in user.
- *Notifications*: Amazon SNS sends email notifications once the audio-to-text transcription process is complete.
- *System monitoring*: Amazon CloudWatch logs Lambda function activity to facilitate auditing, debugging, and system monitoring.
### 5. Implementation Schedule
- Day 1: Analyze requirements, define core functions, and create architecture and workflow diagrams
- Day 2: Create S3 buckets, Cognito User Pool, and App Client; configure user login
- Day 3: Set up DynamoDB, SQS, and API Gateway; configure IAM roles and policies for Lambda
- Day 4: Develop Lambda functions: `lambda-upload-url`, `lambda-processor`, and `lambda-result-handler`
- Day 5: Develop Lambda functions: `lambda-get-job` and `lambda-list-jobs`; integrate API Gateway with Cognito Authorizer
- Day 6: Develop React frontend; integrate Cognito; implement file upload, transcript display, and download button
- Day 7: Perform end-to-end testing; configure SNS email notifications; deploy frontend to S3 + CloudFront; verify CloudWatch Logs

### 6. Budget Estimate  
You can view the costs on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=cf2cfdc1015110291d128e4a975ec054236c00df)  

*Infrastructure Costs*  
- *Amazon CloudFront*: $0.12/month (1 GB data transfer out to the internet, 1,000 HTTPS requests/month).
- *Amazon S3*: $0.03/month (1 GB S3 Standard, 500 PUT/COPY/POST/LIST requests, 1,000 GET/SELECT/other requests).
- *Amazon Cognito*: $0.00/month (10 monthly active users).
- *Amazon API Gateway*: $0.00/month (HTTP API: 0.001 million requests/month, equivalent to 1,000 requests; average size of 34 KB/request).
- *AWS Lambda*: $0.00/month (1,000 requests/month, x86 architecture, Buffered invoke mode, 512 MB ephemeral storage).
- *Amazon SQS*: $0.00/month (0.001 million Standard Queue requests/month, equivalent to 1,000 requests).
- *Amazon Transcribe*: $0.60/month (100 minutes of batch processing using standard Amazon Transcribe).
- *Amazon DynamoDB*: $0.03/month (Standard table class, 0.1 GB storage, 1 KB average item size).
- *Amazon SNS*: $0.00/month (1,000 requests/month, 1,000 EMAIL/EMAIL-JSON notifications).
- *Amazon CloudWatch*: $0.07/month (0.1 GB Standard Logs ingested).

*Total*: $0.85/month, $10.20/12 months.

### 7. Risk Assessment

*Risk Matrix*
- IAM Error: High impact, medium probability. Lambda may be unable to access S3, DynamoDB, Transcribe, or SNS.
- CORS Error: Medium impact, high probability. The frontend may fail to call the API or upload files to S3.
- S3 Event/SQS Failure: High impact, medium probability. Files are uploaded successfully but fail to enter the processing pipeline.
- Transcribe error: High impact, medium probability. Incorrect file formats, poor audio quality, or incorrect language codes can prevent the system from generating transcripts.
- AWS budget overrun: Medium impact, low probability. Costs may increase if testing numerous large files or running multiple Transcribe jobs.
- Cognito error: Medium impact, medium probability. Users may be unable to log in, or the API may return authentication errors.

*Mitigation Strategies*
- IAM: Assign appropriate permissions to each Lambda function and check for errors via CloudWatch Logs.
- CORS: Configure CORS for API Gateway, the S3 Audio Bucket, and the S3 Output Bucket.
- S3 Event/SQS: Verify Event Notifications, SQS policies, and Lambda triggers.
- Transcribe: Restrict input to MP3, MP4, WAV, and M4A formats; test using short, clear audio files.
- Costs: Use small test files, set up AWS Budget Alerts, and delete unnecessary resources after the demo.
- Cognito: Verify the User Pool ID, App Client ID, JWT Authorizer, and Authorization header.

*Contingency Plan*
- If the automated pipeline fails, the team will manually check each step—from S3, SQS, Lambda, and Transcribe to DynamoDB.
- If the trigger fails to activate, the Lambda function can be tested using a sample event. If a frontend error occurs after deployment, the team will revert to running the application locally to verify the API first, then rebuild and redeploy to S3/CloudFront.
- If costs rise, the team will pause the trigger, delete test files, and review the billing details.