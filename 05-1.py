# 업무 전환 -> 제품 카탈로그 사진

character = {
    "name": "아리아",
    "appearance": "은발의 파란 눈, 모험적인",
    "emotion": "단호한",
    "mood": "차가운 느낌의 사무실"
}

# 제품 카탈로그 도메인 프롬프트
product = {
    "name": "무선 이어폰",
    "desc": "화이트 색상, 미니멀 디자인, 충전 케이스 포함"
}

# 달라지는 것 : input dict 구조, prompt 어휘, 저장하는 파일명 패턴
# 유지되는 것 : generate_image() 호출 방식, load_getenv() 보안, outputs/ 폴더

# 우선 간단0한 MVP 전략, 코드 작성
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

def build_product_prompt(desc: str) -> str:
    """제품 설명을 카탈로그 스타일 프롬프트로 변환"""
    return (
        f"{desc}, 제품 사진, "
        "중앙 배치, 깔끔한 흰색 배경, "
        "부드러운 그림자가 있는 스튜디오 조명, "
        "클로즈업, 50mm 매크로 렌즈, 8k 화질, 상업용 카탈로그 스타일"
    )
    
for product in products:
    prompt = build_product_prompt(product["desc"])
    output_path = f"outputs/product_{product['name']}.png"
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
        
    print(f"{product['name']} 제품 사진 생성 완료. -> {output_path}")
    
print("제품 카탈로그 이미지 생성 완료")

# show
# 캐릭터 카드 : BS 기본
# 제품사진:
# - 이어폰, 반지 작은 크기 제품: macro close-up, extreme detail
# - 텀블러, 키보드 중간 크기 제품: close-up, medium shot, product in center
# - 가구, 대형가전 대형 크기 제품: full shot, studio environment
# - 상세페이지, 대표 이미지: CU, 세부 설명을 위한 이미지 ECU

base_desc="화이트 색상 무선 이어폰, 미니멀 디자인, 충전 케이스 포함"

shot_variants = [
    {"close-up": f"{base_desc}, close-up, 50mm macro lens, studio lighting, white background"},
    {"macro": f"{base_desc}, extreme close-up macro, surface texture detail, studio lighting, white background"},
    {"medium-shot": f"{base_desc}, medium shot, product on table, lifestyle setting, soft natural light"}   
]

for shot_name, prompt in shot_variants:
    pass