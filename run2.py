from agents.videos import character_pipeline

aria={
    "name":"Aria",
    "role":"젊은 남성 AI PT, 헬스 트레이너",
    "appearance": "짧은 검은 머리, 갈색 눈, 친근한 미소, 태닝한 피부",
    "outfit": "은은한 파란색 포인트가 들어간 흰색 트레이닝복",
    "mood": "친근하고, 전문적이고, 상냥함"
}

result = character_pipeline(aria)