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

def get_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("OPEN_API_KEY")
    if not api_key:
        raise RuntimeError("OPEN_API_KEY가 .env에 없습니다.")
    return OpenAI()
    
# client = get_client()

def get_scene_prompt()->str:
    # extract_scene 결과에서 prompt_en을 꺼냅니다.
    scene={
        "scene_kr": "아리아가 비 오는 오후 카페 창가에서 낡은 지도를 바라보고 있는 장면입니다.",
        "prompt_en": "Aria gazes at an old map by the cafe window on a rainy afternoon."
    }
    return scene["prompt_en"]

def generate_one_image(client: OpenAI, prompt:str):
    return client.images.generate(
    model="gpt-image-1.5",
    prompt=prompt,
    size="1024x1024",
    quality="low",
    n=1,
    output_format="png" # gpt-image-2 모델 항상 base64 반환
)
    
def save_image(response):
    image_b64=response.data[0].b64_json
    image_bytes=base64.b64decode(image_b64)

    output_dir=Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path=output_dir/"aria_03_6.png"
    output_path.write_bytes(image_bytes)
    
    print(f"[저장완료] {output_path}")
    
if __name__ == "__main__":
    client=get_client()
    prompt=get_scene_prompt()
    response=generate_one_image(client=client, prompt=prompt)
    # json b64 encoding 데이터를 바이트 데이터로 변환
    save_image(response)