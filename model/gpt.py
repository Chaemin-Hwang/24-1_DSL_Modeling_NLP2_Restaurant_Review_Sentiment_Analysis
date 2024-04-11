#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openai
import time

def split_reviews(reviews):
    # 입력된 리뷰들을 하나의 문자열로 결합
    combined_review = ' '.join(reviews)

    # 결과를 저장할 리스트
    splitted_reviews = []

    # 1024자 단위로 문자열을 나누어 리스트에 저장
    while len(combined_review) > 0:
        splitted_reviews.append(combined_review[:1024])
        combined_review = combined_review[1024:]

    return splitted_reviews

def summarize_negative_reviews(api_key, model, review_content):

    openai.api_key = api_key
    
    # 고정된 질문 설정
    query_instructions = [
        '음식점 리뷰를 요약해줘. 요약할 때 다음의 지시를 따라줘.',
        '1. 반복적으로 나타나는 "부정적인" 감정을 집중적으로 요약할 것.',
        '2. 최대한 간결하게 3~5 문장 정도로 요약할 것.',
        '3. 문장에 (1), (2)와 같이 번호를 붙여서 정리할 것. 예를 들어 (1)직원이 불친절함 (2)맛이 없음 등과 같은 형식이 되게끔 하기.',
        '4. 자연스러운 문장이 되도록 유의할 것.'
    ]
    
    # 리뷰 내용과 질문 설정을 포함한 쿼리 생성
    query = str([query_instructions, "{", review_content, "}"])
    
    # 시스템 메시지 설정
    messages = [
        {"role": "system", "content": "너는 음식점 리뷰 문장을 요약해주는 일을 하게 될 거야. 인종 차별적이거나 혐오적인 내용은 제외해. 네가 요약할 리뷰는 '{}'에 감싸져 있어."},
        {"role": "user", "content": query}
    ]
    
    # ChatGPT API 호출
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    
    # 요약된 리뷰 내용 추출
    summary = response['choices'][0]['message']['content']
    return summary


def summarize_positive_reviews(api_key, model, review_contents):

    openai.api_key = api_key
    
    # 고정된 질문 설정
    query_instructions = [
        '음식점 리뷰를 요약해줘. 요약할 때 다음의 지시를 따라줘.',
        '1. 반복적으로 나타나는 "긍정적인" 감정을 집중적으로 요약할 것.',
        '2. 최대한 간결하게 3~5 문장 정도로 요약할 것.',
        '3. 문장에 (1), (2)와 같이 번호를 붙여서 정리할 것. 예를 들어 (1)직원이 친절함 (2)맛이 좋음 등과 같은 형식이 되게끔 하기.',
        '4. 자연스러운 문장이 되도록 유의할 것.'
    ]
    
    # 리뷰 내용과 질문 설정을 포함한 쿼리 생성
    query = str([query_instructions, "{", review_contents, "}"])
    
    # 시스템 메시지 설정
    messages = [
        {"role": "system", "content": "너는 음식점 리뷰 문장을 요약해주는 일을 하게 될 거야. 인종 차별적이거나 혐오적인 내용은 제외해. 네가 요약할 리뷰는 '{}'에 감싸져 있어."},
        {"role": "user", "content": query}
    ]
    
    # ChatGPT API 호출
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    
    # 요약된 리뷰 내용 추출
    summary = response['choices'][0]['message']['content']
    return summary

def extract_and_evaluate_reviews(api_key, model, review_data_list):

    openai.api_key = api_key
    
    # 고정된 쿼리 설명
    query_instructions = [
        '다음 50개의 음식점 리뷰에서 맛, 서비스, 가격에 관련된 표현을 추출해줘. 서비스에는 청결과 직원의 친절도가 포함돼.',
        '그리고 각각의 표현들의 긍정/부정 여부를 판별해줘.',
        '맛, 서비스, 가격과 관련 없는 문장이면 그냥 pass해.',
        '예시는 다음과 같아. "값은 싼데 맛없어요. 음식에서 머리카락 나왔어요" 라는 문장이 있을 때',
        '맛에 대한 표현은 "맛없어요"이고 이건 부정이므로 맛에 대한 부정 표현의 수가 +1 되는 거야. 서비스에 대한 표현은 "음식에서 머리카락 나왔어요"라는 부분이고\
         마찬가지로 서비스에 대한 부정표현 +1이 돼.',
        '반면 가격에 대한 부분은 "값은 싼데"이고 가격이 싸면 좋은 거니까 가격에 대한 긍정 표현의 갯수가 +1이 돼.',
        '최종적으로 맛에 대한 긍/부정 표현 각각의 개수, 서비스에 대한 긍/부정 표현 각각의 개수, 가격에 대한 긍/부정 표현 각각의 개수를 출력해.'
    ]
    
    answers = []  # 요약된 답변을 저장할 리스트
    
    for review in review_data_list:
        # 리뷰와 쿼리 설명을 결합하여 쿼리 생성
        query = str([query_instructions, "{", review, "}"])
        
        # 시스템 메시지 설정
        messages = [
            {"role": "system", "content": "너는 음식점 리뷰 문장에서 맛(taste), 서비스(service), 가격(price)에 관련된 표현을 추출하고\
             그 표현의 긍/부정 극성을 판별하는 일을 할 거야. 네가 요약할 리뷰는 '{}'에 감싸져 있고 문장은 '/'로 나눠져 있어. 지정해준 쿼리 형식대로 출력해."},
            {"role": "user", "content": query}
        ]
        
        # ChatGPT API 호출
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        
        # 요약된 답변 추출 및 저장
        summary = response['choices'][0]['message']['content'] + "/////"
        answers.append(summary)
        
        # API 호출 간의 딜레이
        time.sleep(20)
    
    return answers


