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

prompt="Aria sitting by the cafe window on a rainy afternoon, examining an old map."

response = client.images.generate(
    model="gpt-image-1.5",
    prompt=prompt,
    size="1024x1024",
    quality="low",
    n=1,
    output_format="png" # gpt-image-2 모델 항상 base64 반환
)

# json b64 encoding 데이터를 바이트 데이터로 변환
image_b64=response.data[0].b64_json
image_bytes=base64.b64decode(image_b64)

output_dir=Path("outputs")
output_dir.mkdir(exist_ok=True)
output_path=output_dir/"aria_03_5.png"
output_path.write_bytes(image_bytes)
print(f"[저장완료] {output_path}")