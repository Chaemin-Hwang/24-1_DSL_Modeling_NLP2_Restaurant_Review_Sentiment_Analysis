pip install pandas openpyxl

import pandas as pd
from openpyxl import Workbook
df = pd.read_excel("file_name")

import random
import pickle
import re

wordnet = {}
with open("wordnet.pickle", "rb") as f:
	wordnet = pickle.load(f)
	
# 한글만 남기고 나머지는 삭제
def get_only_hangul(line):
	parseText= re.compile('/ ^[ㄱ-ㅎㅏ-ㅣ가-힣]*$/').sub('',line)

	return parseText

########################################################################
# Random deletion
# Randomly delete words from the sentence with probability p
########################################################################
def random_deletion(words, p):
	if len(words) == 1:
		return words

	new_words = []
	for word in words:
		r = random.uniform(0, 1)
		if r > p:
			new_words.append(word)

	if len(new_words) == 0:
		rand_int = random.randint(0, len(words)-1)
		return [words[rand_int]]

	return new_words

########################################################################
# Random swap
# Randomly swap two words in the sentence n times
########################################################################
def random_swap(words, n):
	new_words = words.copy()
	for _ in range(n):
		new_words = swap_word(new_words)

	return new_words

def swap_word(new_words):
	random_idx_1 = random.randint(0, len(new_words)-1)
	random_idx_2 = random_idx_1
	counter = 0

	while random_idx_2 == random_idx_1:
		random_idx_2 = random.randint(0, len(new_words)-1)
		counter += 1
		if counter > 3:
			return new_words

	new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
	return new_words

def EDA(sentence, alpha_sr=0.1, alpha_ri=0.1, alpha_rs=0.1, p_rd=0.1, num_aug=9):
	sentence = get_only_hangul(sentence)
	words = sentence.split(' ')
	words = [word for word in words if word != ""]
	num_words = len(words)

	augmented_sentences = []
	num_new_per_technique = int(num_aug/4) + 1

	n_rs = max(1, int(alpha_rs*num_words))

	# rs
	for _ in range(num_new_per_technique):
		a_words = random_swap(words, n_rs)
		augmented_sentences.append(" ".join(a_words))

	# rd
	for _ in range(num_new_per_technique):
		a_words = random_deletion(words, p_rd)
		augmented_sentences.append(" ".join(a_words))

	augmented_sentences = [get_only_hangul(sentence) for sentence in augmented_sentences]
	random.shuffle(augmented_sentences)

	if num_aug >= 1:
		augmented_sentences = augmented_sentences[:num_aug]
	else:
		keep_prob = num_aug / len(augmented_sentences)
		augmented_sentences = [s for s in augmented_sentences if random.uniform(0, 1) < keep_prob]

	augmented_sentences.append(sentence)

	return augmented_sentences


import pandas as pd

def apply_eda_to_excel(input_file, output_file):
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file)
    
    # 새로운 데이터프레임 생성
    new_rows = []

    # 각 문장에 대해 EDA 적용
    for index, row in df.iterrows():
        augmented_sentences = EDA(row['Sentence'])  # 여기서 EDA는 예시로 사용된 함수입니다.
        for aug_sen in augmented_sentences:
            new_rows.append({'Sentence': aug_sen, 'Label': row['Label']})

    # 새로운 데이터프레임 생성
    new_df = pd.DataFrame(new_rows)
    
    # 결과를 새로운 엑셀 파일에 저장
    new_df.to_excel(output_file, index=False)


# 경로 설정 후 함수 호출
apply_eda_to_excel('file_path')

# 'augmented_train.xlsx' 파일을 읽어옵니다.
df = pd.read_excel('augmented_train.xlsx')

# 'Sentence' 컬럼에서 중복된 행을 제거합니다.
df_unique = df.drop_duplicates(subset='Sentence', keep='first')

# 중복이 제거된 데이터프레임을 새로운 엑셀 파일에 저장합니다.
#df_unique.to_excel('augmented_train_unique.xlsx', index=False)
df_unique

#중복제거전 -> 중복제거후 리뷰개수
print(len(df))
print(len(df_unique))