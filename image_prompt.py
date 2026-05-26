# 영상 프롬프트 기본 구조
# 이미지 프롬프트는 감상문이 아니다. 촬영 지시서이다.
# prompt = f"{캐릭터 외모}, {샷 사이즈}, {렌즈}, {앵글}, {조명}, {스타일 마무리}"

# 기본 프롬프트
APPEARANCE={
    "젊은 여성 AI 비서 아리아, "
    "은백색의 짧은 머리에 파란 눈, "
    "하늘색의 미래지향적인 재킷, 온화한 미소"
}

# 6종 샷 사이즈 레퍼런스 카드
# 샷 의미 : 카메라와 피사체 간의 거리
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
    'fill light' # 보조광 - 그림자 완화, 자연스러움
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

prompt = f"{APPEARANCE}, {SHOT_SIZES['BS'][0]}, {ANGLES[1]}, {LIGHTING_SETUPS[0]}, {LENSES[0]}, {DEPTHS[0]}, {COMPOSITIONS[0]}"
print("최종 프롬프트: ", prompt)

