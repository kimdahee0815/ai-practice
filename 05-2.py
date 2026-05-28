from openai import OpenAI
from dotenv import load_dotenv
import fal_client
import base64
from pathlib import Path
import requests

load_dotenv()
client = OpenAI()
Path("outputs").mkdir(exist_ok=True)

products=[
    {
        "name": "earbuds",
        "desc": "화이트 색상, 미니멀 디자인, 충전 케이스 포함"
    },
    {
        "name": "tumbler",
        "desc": "매트 블랙, 스테인리스 소재, 450ml 용량"
    }, 
    {
        "name": "keyboard",
        "desc": "기계식, 화이트 키캡, RGB 백라이트, 텐키리스"
    }
]
base_desc="화이트 색상 무선 이어폰, 미니멀 디자인, 충전 케이스 포함"

shot_variants = [
    ("close-up", f"{base_desc}, close-up, 50mm macro lens, studio lighting, white background"),
    ("macro", f"{base_desc}, extreme close-up macro, surface texture detail, studio lighting, white background"),
    ("medium-shot", f"{base_desc}, medium shot, product on table, lifestyle setting, soft natural light")  
]

for shot_name, prompt in shot_variants:
    output_path=f"outputs/earbuds_{shot_name}.png"
    response = client.images.generate(
        model="gpt-image-1.5",
        prompt=prompt,
        size="1024x1024",
        quality="auto",
        n=1,
        output_format="png"
    )
    b64_data=response.data[0].b64_json
    
    img_data = base64.b64decode(b64_data)
    with open(output_path, "wb") as f:
        f.write(img_data)
        
    print(f"{shot_name} 제품 사진 생성 완료. -> {output_path}")

print("제품 카탈로그 이미지 생성 완료")