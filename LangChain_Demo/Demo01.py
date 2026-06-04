import os

from langchain.chat_models import init_chat_model
from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# api_key = os.getenv("ZP_API_KEY")
# base_url = os.getenv("ZP_BASE_URL")
# print(base_url)
# (1)硅基流动方法一
# llm = ChatOpenAI(
#     model = "Qwen/Qwen2.5-7B-Instruct",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# res =llm.invoke("介绍一下你自己").content
# print(res)
# (2)硅基流动方法二
# llm = init_chat_model(
#     model = "Pro/zai-org/GLM-5",
#     model_provider ="openai",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# messages = [
#     {"role":"system","content":"你是一个美妆博主！"},
#     {"role": "user", "content": "我想要知道完美的韩妆教程！"}
# ]
# res = llm.invoke(messages).content
# print(res)

# (3)智普清言方法一

# llm = init_chat_model(
#     model="glm-5.1",
#     model_provider="openai",
#     api_key=os.getenv("ZP_API_KEY"),
#     base_url=os.getenv("ZP_BASE_URL")
# )
# messages = [
#     {"role":"system","content":"你是一个美食博主！"},
#     {"role": "user", "content": "我想要做一份正宗的东北锅包肉！"}
# ]
# res = llm.invoke(messages).content
# print(res)

# (4)智谱清言方法二
# llm = ChatOpenAI(
#     model="glm-5.1",
#     api_key=os.getenv("ZP_API_KEY"),
#     base_url=os.getenv("ZP_BASE_URL")
# )
# res = llm.invoke("请你夸一夸我今天的穿搭吧！").content
# print(res)