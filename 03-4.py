import base64
import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import json # LLM 호출하는 라이브러리
import fal_client 

load_dotenv()
client = OpenAI() # fal_client

REQUIRED_FIELDS={"scene_kr", "prompt_en", "shot", "angle", "light"}
SYSTEM_PROMPT = """
너는 그림일기 정면 추출 담당자 입니다.
반드시 JSON 개체로만 답합니다.
최상위 키는 scenes입니다.
각 장면은 scene_kr, prompt_en, shot, angle, light를 포함합니다.
prompt_en 은 영어로 쓰고, 샷, 앵글, 조명 표현을 포함합니다.
장면은 최대 3개입니다.
"""

def validate_scene(scene:dict)->list[dict]:
    missing=REQUIRED_FIELDS - set(scene)
    if missing:
        print("없는 필드: ", missing)
        return ValueError(f"누락 필드: {sorted(missing)}")

def extract_scenes(text:str) -> list[dict]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT,
        },
        {
            "role":"user",
            "content":text
        },
        ],
        response_format={"type":"json_object"}
    )
    
    content=response.choices[0].message.content
    data=json.loads(content)
    scenes=data.get("scenes",[])[:3]
    
    for scene in scenes:
        validate_scene(scenes)
    return scenes

if __name__ == "__main__":
    diary = "아리아는 비 오는 오후 카페 창가에서 낡은 지도를 발견했다."
    for item in extract_scenes(diary):
        print(item["scene_kr"])
        print(item["prompt_en"])