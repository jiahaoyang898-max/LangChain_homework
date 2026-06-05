import asyncio
import aiohttp
import os

from langchain_core.callbacks import get_usage_metadata_callback
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

# (1)
llm = ChatOpenAI(
    model="Pro/zai-org/GLM-5",
    api_key=os.getenv("GJLD_API_KEY"),
    base_url=os.getenv("GJLD_BASE_URL")
)
async def main():
    with get_usage_metadata_callback() as cb:
        response = await llm.ainvoke("写一首快乐的歌曲")
        print(response.content)
        print(cb.usage_metadata)
asyncio.run(main())
# (2)
# llm = ChatOpenAI(
#     model="Pro/zai-org/GLM-5",
#     api_key=os.getenv("GJLD_API_KEY"),
#     base_url=os.getenv("GJLD_BASE_URL")
# )
# que =[
#     "中国的首都是哪里？",
#     "北京有什么好玩的？",
#     "制定一份三天两晚的北京旅行！"
# ]
# with get_usage_metadata_callback() as cb:
#     response = llm.batch(que)
#     for q,r in zip(que,response):
#         print(f"问题：{q}")
#         print(f"回答：{r.content}")
#         print(cb.usage_metadata)

# (3)
# llm = ChatOpenAI(
#     model="Pro/zai-org/GLM-5",
#     api_key=os.getenv("GJLD_API_KEY"),
#     base_url=os.getenv("GJLD_BASE_URL")
# )
# talk =[
#     SystemMessage(content="你是一个探店博主"),
#     HumanMessage(content="郑州的有哪些好吃的蛋糕房"),
#     AIMessage(content="推荐觉醒"),
#     HumanMessage(content="在什么地方呢？")
# ]
# with get_usage_metadata_callback() as cb:
#     response = llm.invoke(talk)
#     print(response.content)
#     print(cb.usage_metadata)
