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

scene={
    "scene_kr": "비 오는 오후, 작은 카페의 창가에 앉아 있는 아리아가 낡은 지도를 발견하는 장면",
    "prompt_en": "A girl named Aria discovers an old map while sitting by the window of a small cafe on a rainy afternoon. The rain is lightly falling outside, creating a cozy atmosphere inside the cafe.",
    "shot": "medium shot",
    "angle": "eye level",
    "light": "soft, diffused light from the cloudy sky"
}

REQUIRED_FIELDS={"scene_kr", "prompt_en", "shot", "angle", "light"}

def validate_scene(scene:dict)->None:
    missing=REQUIRED_FIELDS - set(scene)
    if missing:
        print("없는 필드: ", missing)
        
    # prompt_en 에 시각 정보가 있는지 확인
    prompt = scene["prompt_en"].lower()
    visual_words = ["shot", "angle","light", "close-up", "wide"]
    if not any(word in prompt for word in visual_words):
        print("prompt_en에 샷, 앵글, 조명 등의 표현이 부족합니다.")
        

validate_scene(scene)