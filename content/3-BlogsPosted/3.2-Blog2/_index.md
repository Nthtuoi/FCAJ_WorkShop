---
title: "Blog 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# An Introduction to Amazon Nova Forge — A Solution for Enterprises to Build Their Own Frontier Models

Hello everyone in the AWS Study Group VN community. While self-studying AWS services, I came across an AWS blog post about Amazon Nova Forge. The first question that crossed my mind was: how can a business get an AI model that "understands" its internal data without incurring the massive costs of building one from scratch? After digging into the details, I realized that Nova Forge aims to solve exactly that problem, so I wanted to share my understanding of it.

Currently, the most common way for businesses to "teach" AI to understand internal data is through fine-tuning—essentially feeding company data into the model so it can learn the information. While this sounds promising, the issue is that the more new data is injected, the greater the risk that the model will "forget" the foundational skills it already possesses, such as reasoning, natural language understanding, and logical analysis. This phenomenon is known as "catastrophic forgetting."

So, what about building a model from scratch? The costs run into the millions of dollars, requiring a team of experts and massive infrastructure—something not every business can manage. This is precisely the dilemma most enterprises face: the need for AI that deeply understands internal data, yet a lack of solutions that are both effective and cost-efficient. That is why Amazon Nova Forge was created.

Amazon Nova Forge is an AWS service that enables businesses to build their own frontier AI models, deeply trained on industry-specific data. Its key differentiator compared to traditional methods—such as superficial surface-level fine-tuning or costly development from scratch—is that it allows you to start from an existing Amazon Nova checkpoint (a model already pre-trained by AWS to a certain stage) and then continue training it using your own internal data.

Simply put: AWS has already handled the most difficult and costly aspects—you simply pick up where they left off and teach the model the specific details of your industry that it doesn't yet know.

Nova Forge offers three different starting points, depending on the amount of internal data you have:

- Pre-trained: The model possesses foundational knowledge—such as reading, writing, and reasoning—but lacks specialization in any specific field. This is suitable for companies with large volumes of internal data, as the model is at the stage where it is most 'hungry' for domain-specific knowledge.
- Mid-trained: The model is undergoing fine-tuning and is not yet fully finalized; it remains 'open' to absorbing further information. This is suitable for companies with a moderate amount of data.
- Post-trained: The model is fully developed and ready for deployment. This is suitable for companies that only wish to make minor adjustments to the model's behavior without needing to retrain it on in-depth, specialized knowledge.

A major risk when training AI on internal data is "catastrophic forgetting"—where newly ingested data overwrites the model's existing knowledge, causing it to gradually lose foundational skills such as reasoning and natural language understanding.
Nova Forge addresses this issue through data mixing: instead of training the model solely on the company's internal data, AWS allows you to blend it with Amazon Nova's standard data at an appropriate ratio.

Kết quả: model vừa học được kiến thức chuyên biệt của công ty, vừa giữ được nền tảng trí tuệ tổng quát mà nó đã có.
Một ví dụ thực tế mà mình nghĩ đến ngay là thương mại điện tử. Hình dung bạn vào website của một shop mỹ phẩm, chatbot hỏi bạn về tình trạng da - da dầu, hay bị mụn - rồi tự động gợi ý đúng sản phẩm phù hợp với bạn. Chatbot đó không chỉ 'tìm kiếm' mà thực sự hiểu dữ liệu sản phẩm, chính sách, và đặc thù khách hàng của shop đó - đó là thứ mà Nova Forge có thể giúp xây dựng.

Conclusion: Amazon Nova Forge enables businesses to build their own frontier models—trained extensively on data specific to their target industry—at a significantly lower cost than building them from scratch.

![imageBlog](/images/3-BlogsPosted/blog2.png)

Nguồn:https://aws.amazon.com/vi/blogs/aws/introducing-amazon-nova-forge-build-your-own-frontier-models-using-nova/