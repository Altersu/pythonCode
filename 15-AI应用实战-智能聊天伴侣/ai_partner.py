import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title='AI智能伴侣',
    page_icon="🤖",
    layout = 'wide',
    #　控制的是侧边栏的状态
    initial_sidebar_state = "expanded",
    menu_items = {}
)

# 大标题
st.title("AI智能伴侣")

# logo
st.logo("resources/logo.png")


# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 遍历消息列表，展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
     # if message['role'] == "user":
     #     st.chat_message("user").write(message["content"])
     # else:
     #    st.chat_message("assistant").write(message["content"])

# 系统提示词
system_prompt ="你是一个很聪明的AI助手，名字叫Alter,请你用温柔且专业的语言回复用户"

# 创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEP_SEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入您的问题")
# 字符串会自动转换为布尔值，如果字符串非空，则为true，否则为false
if prompt:
    # st.write(f"用户: {prompt}")
    st.chat_message("user").write(prompt)
    print("调用AI大模型，提示词：",prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role":"user","content":prompt})

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    # 输出大模型返回的结果
    print("大模型返回的结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})