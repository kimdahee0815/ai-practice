import base64
import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import json

# API KEY 로드 되었는지 확인
load_dotenv()

api_key: str | None = os.getenv("OPENAI_API_KEY")
print(f"[환경확인] OPENAI_API_KEY 첫 12자: {api_key[:13] if api_key else 'None - .env 위치 확인 필요!!'}")

# OpenAI 클라이언트 생성 (키 자동 탐지)
client = OpenAI()

def json_mode():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type":"json_object"}, # 요청포맷
        messages=[
            {
                "role":"system",
                "content":(
                    "당신은 한 줄 문장을 JSON 객체로 변환하는 도우미입니다."
                    "반드시 다음 형식으로만 답하세요:"
                    '{"title": "제목 한 줄", "word_count": "단어수(정수)"}'
                )
            },
            {
                "role":"user",
                "content": "아리아가 도서관에서 책을 읽고 있습니다."
            }
        ]

    )
        
    result = json.loads(response.choices[0].message.content)
    print(result)
    print(type(result))
    
def no_json_mode():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        # response_format={"type":"json_object"}, # 요청포맷
        messages=[
            {
                "role":"system",
                "content":(
                    # "당신은 한 줄 문장을 JSON 객체로 변환하는 도우미입니다."
                    # "반드시 다음 형식으로만 답하세요:"
                    # '{"title": "제목 한 줄", "word_count": "단어수(정수)"}'
                )
            },
            {
                "role":"user",
                "content": "아리아가 도서관에서 책을 읽고 있습니다."
            }
        ]

    )
        
    result = json.loads(response.choices[0].message.content)
    print(result)
    print(type(result))
    
    
def response_json():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type":"json_object"}, # 요청포맷
        messages=[
            {
                "role":"system",
                "content":(
                    "당신은 한 줄 문장을 JSON 객체로 변환하는 도우미입니다."
                    "반드시 다음 형식으로만 답하세요:"
                    '형식: {"name": "이름", "age": "나이"}'
                )
            },
            {
                "role":"user",
                "content": "아리아의 이름과 나이를 알려주세요"
            }
        ]

    )
        
    result = json.loads(response.choices[0].message.content)
    print(result)
    print(type(result))
    
if __name__ == "__main__":
    response_json()

