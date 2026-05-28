# 조명
# - key light, fill light, backlight, (golden hour, blue hour)
# - soft diffused light (부드럽게 퍼지는 빛)
# - harsh direct light (직사광)
# - studio lighting, even lighting, soft shadow
# - 정확하게 보여주는 것. 대표적 조합 (studio lighting, even lighting, soft shadows) 
# 인물, 풍경(분위기) golden hour 조명, 피부를 따뜻하게 보이게 해서 감성적인 분위기를 만든다.
# golden hour를 흰색 제품에 사용하면 제품 노랗게 보이고, 검정 제품은 어두워져서 색상 정보가 왜곡 되는 문제.

from openai import OpenAI
from dotenv import load_dotenv
import fal_client
import base64
from pathlib import Path
import requests

load_dotenv()
client=OpenAI()
Path("outputs").mkdir(exist_ok=True)

base = "화이트 색상 무선 이어폰, 미니멀 디자인, 충전 케이스"

lighting_variants=[
    ("studio", f"{base}, studio lighting with soft shadows, even lighting, white background"),
    ("golden hour", f"{base}, golden hour warm lighting, bokeh background"),
    ("harsh", f"{base}, harsh direct sunlight, strong contrast shadows, outdoor setting"),
]

for light_name, prompt in lighting_variants:
    output_path=f"outputs/earbuds_{light_name}.png"
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
        
    print(f"{light_name} 제품 사진 생성 완료. -> {output_path}")

print("제품 카탈로그 이미지 생성 완료")

# 렌즈
# 화각 24mm, 50mm 표준, 85mm, (16, 35, 138, 200...)
# 24mm (넓게 담음, 원근 왜곡 발생)
# 50mm, 80mm 숫자가 클수록 망원 (좁게 담음, 배경 압축효과, 미화)
# 85mm 인물이나 제품을 납작하게 압축해 더 고급스러워 보이게 해주는 효과(배경압축)
# macro 실제 크기 이상으로 극대화 (확대), 표면 질감이나 세부 묘사를 할 수 있다.
