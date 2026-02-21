# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEP_SEEK_API_KEY'),
    base_url="https://api.deepseek.com")
# 与AI大模型进行对话
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个很聪明的AI助手，名字叫Alter,请你用温柔且专业的语言回复用户"},
        {"role": "user", "content": "你是谁"},
    ],
    stream=False
)
#输出大模型返回的结果
print(response.choices[0].message.content)