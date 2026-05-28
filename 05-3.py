from typing import Literal

shot_type= Literal["close-up", "macro", "medium_shot", "full_shot"]

# 제품 크기 카테고리 -> 권장 샷 매핑
shot_map: dict[str, shot_type] = {
    "small": "macro", # 이어폰, 반지, 시계
    "medium": "close-up", # 텀블러, 키보드, 책
    "large": "full_shot" # 가방, 신발, 소형 가전
}

products=[
    {
        "name": "earbuds",
        "desc": "화이트 색상, 미니멀 디자인, 충전 케이스 포함",
        "size": "small"
    },
    {
        "name": "tumbler",
        "desc": "매트 블랙, 스테인리스 소재, 450ml 용량",
        "size": "medium"
    }, 
    {
        "name": "keyboard",
        "desc": "기계식, 화이트 키캡, RGB 백라이트, 텐키리스",
        "size": "medium"
    }
]

for product in products:
    shot = shot_map[product["size"]]
    # print(shot)
    prompt = (
        f"{product['desc']}, {shot}, "
        "중앙 배치, 깔끔한 흰색 배경, "
        "부드러운 그림자가 있는 스튜디오 조명"
    )
    print(f"{product['name']}: 샷={shot}: {prompt}")
    
# 앵글
# - eye-level : 길쭉한 제품 (텀블러)
# - low-angle : (인물: 위엄, 웅장함), 특이한 케이스 (특별한 분위기 연출)
# - high-angle : (인물: 귀여움), 납작한 제품 (키보드)
# 앵글만 바뀌더라도 같은 제품이 완전히 다른 인상을 준다.

base = "매트 블랙 스테인리스 텀블러 450ml"

angles=[
    ("eye_level", f"{base}, eye-level angle, close-up, clean white background, studio lighting"),
    ("slight_high_angle", f"{base}, slight high angle view, close-up, clean white background, studio lighting"),
    ("bird_eye", f"{base}, bird's eye view top-down, clean white background, studio lighting, 8k detail")
]

for angle_name, prompt in angles:
    print(angle_name, " | ", prompt)

