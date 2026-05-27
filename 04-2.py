import fal_client
from dotenv import load_dotenv
import time
from fal_client import Completed, InProgress, Queued

load_dotenv()

# 비동기 방식
model_id = "fal-ai/kling-video/v2/master/image-to-video"
handler = fal_client.submit(
    model_id,
    arguments={
        "prompt":"static shot, gentle smile, subtle breathing, cinematic lighting",
        "image_url":"https://pbs.twimg.com/media/HImlEStXcAAQwYb.jpg",
        "duration":"5"
    }
)
print(handler.request_id)
request_id = handler.request_id
print(f"[1단계] 제출완료: {request_id}")

print(f"[2단계] 진행 상태 점검")
while True:
    status = handler.status(with_logs=True)
    if isinstance(status, Completed): 
        break
    print("진행중...", status)
    time.sleep(0.5)

print("[3단계] 작업 결과물 가져오기")
result = handler.get()
print(result["video"]["url"])
# request_id: 019e6772-3abd-7d93-9751-0d3f964c344