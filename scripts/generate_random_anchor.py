import random
import string

def generate_short_code(length=7, underscore=True):
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(length))
    if underscore:
        code += '_'
    return code

def main():
    print("生成随机平台短码示例：")
    for platform in ["ZH", "WX", "GH", "MED", "TW"]:
        print(f"{platform}~{generate_short_code()}")

if __name__ == "__main__":
    main()