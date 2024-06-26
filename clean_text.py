import os
import shutil
import regex as re
from collections import Counter

input_file = os.path.join("TMP", "SK3e_merged.txt")
output_path = os.path.join("DIST", "clean")

# 폴더 존재 여부 확인
if os.path.exists(output_path):
    # 폴더와 하위 파일 삭제
    shutil.rmtree(output_path)

# 폴더 생성
os.makedirs(output_path)

# 파일 읽기
with open(input_file, "r", encoding="utf-8-sig") as fl:
    text = fl.read()
    
# "#"로 시작하는 행 삭제
text = re.sub(r'^#.*\n', '', text, flags=re.MULTILINE)

# "<"로 시작해서 ">"로 끝나는 구절 삭제
text = re.sub(r'^<.*?>', '', text, flags=re.MULTILINE)

#
text = re.sub(r'[\u3000]+', ' ', text)
text = re.sub(r'昏>', '昏', text)
text = re.sub(r'[䷋䷗䷫䷀䷁䷊☵ㄇ]', ' ', text)
text = re.sub(r'[\(\)\[\]\-\+\*\?\!_@ㄙ□○〇/&:;0-9a-zA-Z<>]+', ' ', text)

# 
text = re.sub(r'¶+\s*\n', '', text, flags=re.MULTILINE)
text = re.sub(r'[¶]+', '', text)

# 불필요한 공백 줄 제거
text = re.sub(r'\n\s*\n', '\n', text, flags=re.MULTILINE)

# 공백 합치기
text = re.sub(r'\s+', ' ', text, flags=re.MULTILINE)

# 문서 나누기
text = re.sub(r'\s*========\s*', '\n', text, flags=re.MULTILINE)

# 한자 이외의 기호 알아내기
not_han = re.findall(r'[^\p{Han}]', text )
cnt = Counter( not_han )
print( cnt )

# 출력
N_DOC = 10
text_lst = re.split( r'\s*\n\s*', text, flags=re.MULTILINE )
n_lines = len( text_lst )
print( n_lines )

n_lines_per_doc = int( n_lines / N_DOC ) + 1

sub_text_lst = [ text_lst[i:i+n_lines_per_doc] for i in range(0, n_lines, n_lines_per_doc) ]

for i, sub_text_lst in enumerate( sub_text_lst, start=1):
    output_file = os.path.join( output_path,  f"{i:03}.txt" )
    sub_text = "\n".join( sub_text_lst )
    with open( output_file, 'w', encoding='utf-8') as fl:
        fl.write( sub_text.strip() )
   