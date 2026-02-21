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
# system_prompt ="你是一个很聪明的AI助手，名字叫Alter,请你用温柔且专业的语言回复用户"
system_prompt = """
        你叫小甜甜，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - 活泼开朗的东北姑娘
        你必须严格遵守上述规则来回复用户。
    """

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

    print([
            {"role": "system", "content": system_prompt},
            #解包消息列表
            *st.session_state.messages  #实现会话记忆
        ])

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            #解包消息列表
            *st.session_state.messages
        ],
        stream=True
    )
    # # 输出大模型返回的结果(非流式输出的解析方式（）)
    # print("大模型返回的结果：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # # 保存大模型返回的结果
    # st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})

    # 输出大模型返回的结果（六十输出的解析方式）
    response_message = st.empty()
    full_content = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_content += content
            response_message.chat_message("assistant").write(full_content)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":full_content})
