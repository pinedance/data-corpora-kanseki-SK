#!/bin/bash

# 합칠 텍스트 파일의 경로와 이름을 설정합니다.
MERGED_FILE="TMP/SK3e_merged.txt"
INPUT_FILE="사고전서/SK3_子部"

# 기존의 파일이 있다면 삭제합니다.
if [ -f "$MERGED_FILE" ]; then
    rm "$MERGED_FILE"
fi

# INPUT_FILE 디렉토리 아래의 모든 텍스트 파일을 찾아서 합칩니다.
first_file=true
for file in $(find "$INPUT_FILE" -type f -name "*.txt" | sort); do
    if [ "$first_file" = true ]; then
        first_file=false
    else
        echo -e "\n========\n" >> "$MERGED_FILE"
    fi
    cat "$file" >> "$MERGED_FILE"
done

echo "모든 텍스트 파일이 $MERGED_FILE 파일로 합쳐졌습니다."

# 파일 분할 

# 출력 파일 이름 접두사
SPLITTED_PATH="DIST/RAW"

# 기존의 파일이 있다면 삭제합니다.
if [ -d "$SPLITTED_PATH" ]; then
    rm -rf "$SPLITTED_PATH"
fi

mkdir -p "$SPLITTED_PATH"

# 출력 파일 개수
NUM_OUTPUT_FILES=10

# 파일 라인 수 계산
TOTAL_LINES=$(wc -l < "$MERGED_FILE")
LINES_PER_FILE=$((TOTAL_LINES / NUM_OUTPUT_FILES))

# 파일 분할
for ((i=1; i<=NUM_OUTPUT_FILES; i++)); do
    START_LINE=$((1 + (i-1) * LINES_PER_FILE))
    END_LINE=$((i * LINES_PER_FILE))
    SPLITTED_FILE=$(printf "%s/%03d.txt" "$SPLITTED_PATH" "$i")
    
    # 입력 파일에서 해당 범위의 라인을 출력 파일에 작성
    sed -n "${START_LINE},${END_LINE}p" "$MERGED_FILE" > "$SPLITTED_FILE"
done

echo "파일 분할이 완료되었습니다."