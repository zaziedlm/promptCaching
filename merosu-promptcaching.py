from openai import OpenAI
import re
import json
import os
from dotenv import load_dotenv

# read .env file
load_dotenv()

with open('hashire_merosu.txt', 'r', encoding='SJIS') as f:
#with open('hashire_merosu-half.txt', 'r', encoding='SJIS') as f:
#with open('hashire_merosu-first.txt', 'r', encoding='SJIS') as f:   
    data = f.read()
    data = re.sub(r'-------------------------------------------------------.*?-------------------------------------------------------\n', '', data, flags=re.DOTALL)
    data = re.sub(r'［＃地から１字上げ[\s\S]*$', '', data)
    data = re.sub("\n\u3000", "", data)
    data = re.sub("《[^》]+》", "", data)

print(data[:100])
print("〜")
print(data[-100:])
print(f"({len(data)})")

system_prompt = f"""\
あなたは与えられた文学作品の分析を得意とするAIアシスタントです。テーマ、キャラクター、文体に関して深い洞察に満ちた解説を提供することがあなたの目標です。

## 対象の文学作品

{data}

"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

while True:
    user_input = input("USER: ")
    if user_input.lower() == '/bye':
        print("チャットを終了します。")
        break
    
    # messages.append({"role": "user", "content": user_input})

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        #model="gpt-4o-2024-08-06",
        model="gpt-4o",
        #model="gpt-4o-mini",
        messages=messages,
        temperature=0.1,
    )
    
    assistant_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    
    print(f"ASSISTANT: {assistant_response}")

    # キャッシュ使用状況を確認
    print("----- Usage -----")
    # print(json.dumps(response.usage.dict(), indent=2))
    print(json.dumps(response.usage.model_dump(), indent=2))
    print("-----------------")