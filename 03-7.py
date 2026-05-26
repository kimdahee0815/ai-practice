from module_03_6 import get_client
import base64
import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import json # LLM 호출하는 라이브러리
import fal_client 

if __name__ =="__main__":
    client=get_client()
    print(isinstance(client,OpenAI))