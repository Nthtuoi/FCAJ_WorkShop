---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Building Protein Research Copilot and Amazon Bedrock AgentCore

Building a Protein Research Copilot with Amazon Bedrock AgentCore
Hello, AWS Study Group VN! While exploring AI Agents on AWS, I came across a fascinating use case: building a Protein Research Copilot using Amazon Bedrock AgentCore. This AI system assists protein researchers in searching for homologous peptides and analyzing biological data using nothing but natural language.</br>

Previously, to identify proteins or peptides with similar structures, researchers had to:
* Manually search through large datasets
* Run sequence comparison algorithms
* Analyze results themselves using biological expertise

This process was time-consuming, error-prone, and difficult to scale as data volumes grew.

With Protein Research Copilot, AWS combines AI Agents, Vector Search, and Foundation Models to automate the entire research workflow: </br>

**Natural Language Query Parsing**

“Find 10 peptides similar to dengue virus peptide LPAIVREAI”
and convert it into a structured query.

**Vector Similarity Search**

Protein sequences are converted into embeddings using a specialized model (ESM-C 300M), followed by a search for similar peptides in a vector database.

**AI-powered Summarization**

After retrieving results, the AI ​​automatically summarizes them and provides scientific insights to the researcher.</br>
The system utilizes key AWS services:
* Amazon Bedrock AgentCore — Runtime for deploying and scaling AI agents
* Amazon Bedrock — Runs LLMs for reasoning and summarization
* Amazon SageMaker — Deploys protein embedding models
* Amazon Aurora PostgreSQL + pgvector — Stores embeddings for semantic search

The most notable point:

Instead of the AI ​​“memorizing” the entire protein dataset, the system employs Retrieval-Augmented Generation (RAG) to:

1. Retrieve the relevant data
2. Provide context to the LLM
3. Deliver more accurate answers and reduce hallucinations

This helps shorten the research process from hours to just a few minutes.

Conclusion:</br>
Protein Research Copilot demonstrates that AI agents are not limited to chatbots but can also be applied to specialized fields such as biomedicine, pharmaceuticals, and scientific research. It serves as an excellent example of how AWS combines Agentic AI, vector databases, and LLMs to build practical AI systems at production scale.
![imageBlog](/images/3-BlogsPosted/blog.png)

</br>
Nguồn tham khảo: https://aws.amazon.com/vi/blogs/machine-learning/build-a-protein-research-copilot-with-amazon-bedrock-agentcore/