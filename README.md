## 🍔 24-1_DSL_Modeling_NLP2_진실의_입
##### NLP 3조 - 10기: 박성원 11기: 김민석 김현진 윤정수 황채민
## 💡 주제
* 음식점 긍부정 리뷰 요약 및 카테고리 세분화
* 카카오 리뷰 데이터를 활용하여 fine tuning한 KoELECTRA 모델로 네이버 음식점 리뷰의 긍부정을 분석하였습니다.
이후 GPT API를 이용해 각 긍정 부정 리뷰를 4-5줄로 요약하였고, 각 결과물을 담은 로컬 웹사이트를 간단하게 제작해 보았습니다.
식당의 긍부정 리뷰, 특히 소비자가 부정적으로 평가하는 부분이 무엇인지 알고 싶을 때 이를 가시적으로 파악하는 데에 도움이 되셨으면 좋겠습니다! 
---
# Overview

## 1. Pipeline
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/c498282e-1dbd-411a-bcd6-9f44c222928b)

## 2. Motivation
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/2fb04be8-5de7-4714-bff8-ac3e9818f709)
긍정적인 부분에 초점이 맞춰져 있는 음식점 리뷰들 ... -> 부정적인 리뷰도 비중있게 다루는 식당 리뷰 사이트를 만들어보자!
## 3. Dataset
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/aca15096-6e81-4366-ba02-a0c163f51c99)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/89ef8be3-73f4-4e78-8f0c-298db39da925)

## 4. Sentimental Analysis
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/c33696fe-dd6b-47f8-914f-9858c456c331)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/e4dc4b68-1e44-478a-8f35-904def989a2b)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/55ca418b-6eff-4389-9827-25342dc01e97)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/2420e3c9-5673-4b20-a3ce-091379c0404c)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/59d30b9a-07f7-4096-929d-4a602b907151)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/f6f72302-4173-4b4b-b410-c6b296b9d50d)

### 5. Category Classification & Text Summarization
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/1919ec21-3088-4240-b4a4-d6a225387425)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/aa783c25-bdc6-439f-aad9-03b7ad20669c)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/617ee8cb-fa84-4770-b160-22848e2d9504)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/3198fcf4-0f2f-4da8-bb75-35afb44fe69a)

![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/e0eec9d8-1af8-4c40-987e-d8bf4c09f556)

### 6. Results
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/8fd4abe9-3026-4bb5-b744-4609bb9c5277)
저희가 소비자에게 제공하고자 했던 서비스를 간단하게나마 구현하여 프로젝트의 의도를 시각적으로 간결하게 파악할 수 있도록 하였습니다. 
백엔드와 프론트엔드를 연결하는 등의 기술력이 부족하여 로컬 사이트에서 직접 데이터를 삽입하여 구현하였고, app.py 파일 실행을 통해 사이트를 직접 경험해보실 수 있습니다. 

### 7. Limitation
![image](https://github.com/Chaemin-Hwang/24-1_DSL_Modeling_NLP2_Restaurant_Review_Sentiment_Analysis/assets/147033744/2aedd3ba-558e-49c4-8fac-bce96566a205)





