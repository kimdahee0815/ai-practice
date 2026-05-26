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

# 프롬프트 구조화 json

APPEARANCE= (
    "젊은 여성 AI 비서 아리아, "
    "은백색의 짧은 머리에 파란 눈, "
    "하늘색의 미래지향적인 재킷, 온화한 미소"
)

# 프롬프트 조합 함수
def build_prompt(scene:dict) -> str:
    """JSON 장면 필드 딕셔너리에서 LLM용 프롬프트 조합"""
    parts = [APPEARANCE, 
             f"{scene['shot']} shot", # 카메라거리
             scene['angle'], #앵글
             scene['light'], # 조명
             f"{scene['lens']} lens", # 구도
            scene['composition']
         
             
             ]
    return ", ".join(parts)

#장면설정 json
sample_scene = {
    "scene_id":1,
    "scene_kr": "Aria의 집중된 표정 클로즈업",
    "shot": "CU",
    "angle": "eye_level",
    "light": "key light",
    "lens": "85mm tight",
    "composition": "centered"
}
prompt = build_prompt(sample_scene)
print(prompt)