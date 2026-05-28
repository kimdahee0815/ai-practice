from openai import OpenAI
from dotenv import load_dotenv
import fal_client
import base64
from pathlib import Path
import requests

load_dotenv()
client = OpenAI()


def _agent_designer(character: dict) -> str:
    """디자이너: 캐릭터 dict -> 시각화 프롬프트 문자열로 반환"""
    # return f"{character['appearance']}, cinematic lighting, photorealistic"
    appearance=(
        f"{character['role']}, {character['appearance']}, "
        f"{character['outfit']}, {character['mood']}"
    )
    print(appearance)
    shot = "bust shot, 50mm lens, eye-level, soft key light, cinematic lighting, photorealistic"
    return f"{appearance, shot}"

def _agent_photographer(prompt: str) -> str:
    """사진작가: prompt -> 이미지 생성 -> url"""
    # return f"https://example.com/images/{prompt[2:10].replace(' ','_')}.png"
    r = client.images.generate(
        model="gpt-image-1.5",
        prompt=prompt,
        size="1024x1024",
        quality="auto",
        n=1,
        output_format="png"
    )
    return r.data[0].b64_json

# agent_photographer(agent_designer(aria))

def _agent_video_director(image_b64:str, name:str) -> str:
    """영상감독: 이미지 url -> 영상 url"""
    # return f"https://example.com/videos/{name}_intro.mp4"
    camera_work = (
        f"static shot, {name} gentle smile, eye blink, "
        "slight head turn, cinematic lighting"
    )
    r = fal_client.subscribe(
        "fal-ai/kling-video/v2/master/image-to-video",
        arguments={
            "prompt": camera_work,
            "image_url": f"data:image/png;base64,{image_b64}",
            "duration":"5"
        }
    )
    return r["video"]["url"]


def _save_video(video_url:str, name:str) -> str:
    """영상 url -> 로컬 저장"""
    output_dir=Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{name.lower()}_card.mp4"
    response = requests.get(video_url, timeout=30)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)
    size_kb = output_path.stat().st_size // 1024
    print(f" 저장 경로: {output_path} ({size_kb})KB")
    return str(output_path)

def character_pipeline(character:dict) -> dict:
    """파이프라인: 3개의 에이전트를 순서대로 전부 호출"""
    print(f"캐릭터 카드 제작 시작 : {character['name']}")
    prompt = _agent_designer(character)
    image_b64 = _agent_photographer(prompt)
    video_url = _agent_video_director(image_b64, character["name"])
    video_path = _save_video(video_url, character["name"])
    return {
        "name":character["name"],
        "image_url": image_b64,
        "video_url": video_url,
        "video_path": video_path
    }
    
    