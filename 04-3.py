def agent_designer(character: dict) -> str:
    """디자이너: 캐릭터 dict -> 시각화 프롬프트 문자열로 반환"""
    return f"{character['appearance']}, cinematic lighting, photorealistic"

def agent_photographer(prompt: str) -> str:
    """사진작가: prompt -> 이미지 생성 -> url"""
    return f"https://example.com/images/{prompt[:10].replace(' ','_')}.png"

def agent_video_director(image_url:str, name:str) -> str:
    """영상감독: 이미지 url -> 영상 url"""
    return f"https://example.com/videos/{name}_intro.mp4"

def character_pipeline(character:dict) -> dict:
    """파이프라인: 3개의 에이전트를 순서대로 전부 호출"""
    prompt = agent_designer(character)
    image_url = agent_photographer(prompt)
    video_url = agent_video_director(image_url, character["name"])
    return {
        "name":character["name"],
        "image_url": image_url,
        "video_url": video_url
    }
    
# 실행
aria = {"name": "Aria", "appearance":"short black hair, warm brown eyes, friendly smile"}
result = character_pipeline(aria)
print(result)