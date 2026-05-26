import openai

# 이렇게 하지 마세요
# client = openai.OpenAI(api_key="Asdfasf")

# import os
# os.environ["OPENAI_API_KEY"] = 'sk-proj-실제키'

# 올바른 방법
from dotenv import load_dotenv
import os

# 프로젝트 폴더 (루트) .env 파일을 찾아서 로드
load_dotenv()

api_key: str | None = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# .gitignore 에 .env 추가 확인
gitignore_path = ".gitignore"
try:
    with open(gitignore_path, "r", encoding="utf-8") as f:
        content = f.read()
        if ".env" in content:
            print(".gitignore 에 .env 등록 확인")
        else:
            print(".gitignore 에 .env 누락 - 즉시 추가 필요!!!")
except FileNotFoundError:
    print(".gitignore 파일 없음")
        