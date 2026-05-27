import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import fal_client
import requests
import base64

load_dotenv()

# 테스트 프롬프트
STYLE_PREFIX = (
    "아리아, 젊은 한국인 남성, 짧은 머리, 따뜻한 미소, "
    "따뜻한 느낌의 수채화 일러스트 스타일"
)

def _save_b64_to_png(b64_data: str, save_path: Path) -> str:
    """base64 이미지 데이터를 디코딩 해서 PNG 이미지로 저장한다"""
    save_path.parent.mkdir(parents=True, exist_ok=True) # ./outputs/abc.png
    save_path.write_bytes(base64.b64decode(b64_data))
    return str(save_path)

def _save_url_to_png(url: str, save_path: Path) -> str:
    save_path.parent.mkdir(parents=True, exist_ok=True)
    result = requests.get(url, timeout=30)
    result.raise_for_status() # 다운로드 문제 여부 확인
    save_path.write_bytes(result.content)
    return str(save_path)

def generate_gpt(client: OpenAI, prompt: str, save_path: str) -> str:
    """gpt-imageX 이미지를 생성하고 저장 경로를 반환합니다"""
    full_prompt = STYLE_PREFIX + prompt
    result = client.images.generate(
        model="gpt-image-1.5",
        prompt=full_prompt,
        size="1024x1024",
        quality="auto",
        n=1,
        output_format="png"
    )
    b64_data=result.data[0].b64_json
    return _save_b64_to_png(b64_data, save_path)

def generate_fal(prompt:str, save_path:Path, seed: int=55):
    """fal.ai FLUX 이미지를 생성하고 저장 경로를 반환합니다."""
    full_prompt=STYLE_PREFIX+prompt
    result = fal_client.run(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": full_prompt,
            "seed": seed, # 캐릭터 일관성을 위한 시드 고정
            "num_images": 1,
            "image_size": "square_hd"
        }
    )
    image_url = result["images"][0]["url"]
    return _save_url_to_png(image_url, save_path)

def generate_image(scene: dict, backend: str = 'fal') -> str:
    """
    장면 한 항목을 받아 이미지를 생성한다. 경로 정보 반환
    ARGS:
        scene: {"scene_id": int, "scene_kr": str, "prompt_en", str}
        backend: "gpt" -> generate_gpt, "fal" -> generate_fal
    RETURN:
        저장된 이미지 파일의 경로
    """
    scene_id = scene.get("scene_id", 1)
    prompt = scene.get("prompt_en", "")
    save_path = Path("outputs")
    save_path = save_path / f"aria_scene_{scene_id}.png"
    print("이미지 생성중...")
    if backend == "gpt":
        client = OpenAI()
        return generate_gpt(client, prompt, save_path)
    else:
        return generate_fal(prompt, save_path)
    
    