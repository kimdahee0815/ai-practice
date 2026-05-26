import sys
import importlib

def main():
    print("Hello from ai-basic!")
    for pkg in ["python-dotenv", "openai", "fal-client", "replicate", "transformers", "diffusers", "Pillow"," requests"]:
        try:            
            mod = importlib.import_module(pkg) 
            ver = getattr(mod, "__version__", "버전 정보 없음")
            print(f"{pkg}: {ver}")      
        except ImportError:
            print(f"{pkg} Import 실패")

if __name__ == "__main__":
    main()
