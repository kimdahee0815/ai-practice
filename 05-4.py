from openai import OpenAI
from dotenv import load_dotenv
import fal_client
import base64
from pathlib import Path
import requests

load_dotenv()
client = OpenAI()
Path("outputs").mkdir(exist_ok=True)

base="매트 블랙, 스테인리스 소재, 450ml 용량"

angles=[
    ("eye_level", f"{base}, eye-level angle, close-up, clean white background, studio lighting"),
    ("slight_high_angle", f"{base}, slight high angle view, close-up, clean white background, studio lighting"),
    ("bird_eye", f"{base}, bird's eye view top-down, clean white background, studio lighting, 8k detail")
]

for angle_name, prompt in angles:
    output_path=f"outputs/tumbler_{angle_name}.png"
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
        
    print(f"{angle_name} 제품 사진 생성 완료. -> {output_path}")

print("제품 카탈로그 이미지 생성 완료")