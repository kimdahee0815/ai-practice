import fal_client
from dotenv import load_dotenv

load_dotenv()

# 동기 방식 - 기다려야 함
result = fal_client.subscribe(
    "fal-ai/kling-video/v2/master/image-to-video",
    arguments={
        "prompt":"static shot, gentle smile, subtle breathing, cinematic lighting",
        "image_url":"https://i.pinimg.com/736x/45/6f/17/456f17614b3a8668864e8ad3aba6898e.jpg",
        "duration":"5"
    }
)
print(result["video"]["url"])
#  result : https://v3b.fal.media/files/b/0a9bd60a/rdtb-TDFh0fcq4GT5PDin_output.mp4