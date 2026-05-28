# 제품 형태에 따라 권장 되는 앵글 있다. -> 앵글 매핑
angle_map = {
    "tall": "eye-level angle", # 텀블러, 긴 병
    "flat": "slight high angle view", # 키보드, 책, 태블릿
    "small": "bird's eye view to-down" # 이어폰, 반지, 동전
}


products=[
    {
        "name": "earbuds",
        "desc": "화이트 색상, 미니멀 디자인, 충전 케이스 포함",
        "form":"small"
    },
    {
        "name": "tumbler",
        "desc": "매트 블랙, 스테인리스 소재, 450ml 용량",
        "form": "tall"
    }, 
    {
        "name": "keyboard",
        "desc": "기계식, 화이트 키캡, RGB 백라이트, 텐키리스",
        "form": "flat"
    }
]

for product in products:
    angle = angle_map[product["form"]]
    prompt=(
        f"{product['desc']}, {angle}"
        "중앙 배치, 깔끔한 흰색 배경, "
        "부드러운 그림자가 있는 스튜디오 조명"
    )
    print(f"{product['name']}: 앵글={angle}: {prompt}")

