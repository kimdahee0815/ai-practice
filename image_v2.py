import base64
import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# API KEY 로드 되었는지 확인
load_dotenv()

api_key: str | None = os.getenv("OPENAI_API_KEY")
print(f"[환경확인] OPENAI_API_KEY 첫 12자: {api_key[:13] if api_key else 'None - .env 위치 확인 필요!!'}")

# OpenAI 클라이언트 생성 (키 자동 탐지)
client = OpenAI()

# 캐릭터 생성 프롬프트
BASE_PROMPT = (
    "한국인 여성 20대 중반 아리아, 은은한 하이라이트가 들어간 짧은 검은 머리, 따뜻한 갈색 눈, "
    "파란색 포인트가 들어간 흰색 테크 의상, 친근한 미소, "
    "50mm 렌즈, 눈높이, 영화 같은 조명, 사실적인 표현"
)

SHOT_SIZES={
    "ECU":("extreme close-up", "감정 미세변화, 눈빛 강조"),
    "EU": ("close-up", "얼굴 중심, SNS 프로필"),
    "BS": ("bust shot", "표준 포트레이트 - 캐릭터 카드 기준"),
    "MS": ("medium shot", "제스처, 옷차림 포함"),
    "FS": ("full shot", "전신, 의상 카탈로그"),
    "WS": ("wide shot", "환경, 세계관 등 강조")
}

# 앵글 3종
ANGLES=[
    'eye-level', # 기본 - 친근하고 자연스러운 
    'low angle', # 올려보기 - 위엄, 파워, 영웅 등장
    'high angle' # 내려보기 - 귀엽고, 관찰되는 느낌
]

LIGHTING_SETUPS=[
    'key light', # 주광 - 밝고 상업적
    'fill light', # 보조광 - 그림자 완화, 자연스러움
    'back light' # 후면광 - 윤곽 강조, 드라마틱
]

LENSES = [
    "24mm wide",
    "50mm portrait",
    "85mm tight",
    "200mm",
    "400mm"
]

DEPTHS = [
    "shallow depth of field",
    "deep focus, sharp background",
    
]

# 구도
COMPOSITIONS =[
    "rule of thirds",
    "centered composition",
    "negative space, minimalist"
]

prompt = f"{BASE_PROMPT}, {SHOT_SIZES['FS']}, {ANGLES[0]}, {LIGHTING_SETUPS[2]}, {LENSES[1]}, {DEPTHS[0]}, {COMPOSITIONS[1]}"

print("GPT-IMAGE-2 호출 시작 = 약 5 ~ 15초 소요 예상...")

# gpt-image-2 동기 호출 : 응답이 올 때까지 기다려야 한다.
response = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1024",
    quality="low",
    n=1,
    output_format="png" # gpt-image-2 모델 항상 base64 반환
)

# 응답 구조 확인 : b64_json 구조
image_b64 = response.data[0].b64_json
print(f"[응답구조] response.data[0].b64_json={image_b64[:60]}")

# base 64 디코딩 후 저장
output_dir=Path("outputs")
output_dir.mkdir(exist_ok=True)
image_bytes=base64.b64decode(image_b64)

output_path=output_dir/"aria_v7.png"
output_path.write_bytes(image_bytes)
print(f"[저장완료] {output_path}")
