import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
# (1)
# client = OpenAI(
#     base_url=os.getenv("ZP_BASE_URL"),
#     api_key=os.getenv("ZP_API_KEY")
# )
# completion =client.chat.completions.create(
#     model="glm-5.1",
#     messages=[{"role": "user", "content": "帮我规划一份在校减肥计划加上配套食谱"}]
# )
# print(completion.choices[0].message.content)
# (2)
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# llm = ChatOpenAI(model = "Qwen/Qwen2.5-7B-Instruct",
#                 api_key = os.getenv("GJLD_API_KEY"),
#                 base_url = os.getenv("GJLD_BASE_URL")
#                  )
# response = llm.invoke([
#     SystemMessage(content="你是一个专业的Python编程助手"),
#     HumanMessage(content="什么是装饰器？")
# ])
# print(response.content)

#(3)
# from dotenv import load_dotenv
# load_dotenv()
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage
llm = ChatOpenAI(
    model = "Pro/zai-org/GLM-5",
    api_key = os.getenv("GJLD_API_KEY"),
    base_url = os.getenv("GJLD_BASE_URL")
)
# response = llm.invoke([HumanMessage(content="你好")])
# print(response.content)

# (4)

# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# conversation = [
#     SystemMessage (content="你是一位资深美食博主。"),
#     HumanMessage (content="郑州有什么好吃的蛋糕房。")
# ]
# response = llm.invoke(conversation)
# print(response.content)

# (5)
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# responses =llm.invoke(
#     [   HumanMessage(content="怎么说漂亮话？"),
#         SystemMessage(content="你是一个精通高情商发言的ai助手"),
#         HumanMessage(content="在职场呢？")
#     ]
# )
# print(responses.content)

# (6)
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# tuple_messages = [
#     ("system","你是一个专业的Python编程助手"),
#     ("user","什么是装饰器？")
# ]
# dict_messages = [
#     {"role":"system","content":"你是一个专业的Python编程助手"},
#     {"role":"user","content":"什么是装饰器？"}
# ]
# print(llm.invoke(tuple_messages))
# print(llm.invoke(dict_messages))

# (7)
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# prompt_template = [
#     {"role":"system","content":"你是一个{role}"},
#     {"role":"user","content":"请解释{topic}"}
# ]
# messages = [
#     {
#         "role":t["role"],"content":t["content"].format(role="翻译助手",topic="机器翻译")
#     }
#     for t in prompt_template
# ]
# print(llm.invoke(messages).content)

# (8)
import asyncio
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# async def call_llm_async():
#         response = await llm.ainvoke("什么是LangChain?")
#         print(response.content)
# asyncio.run(call_llm_async())

# (9)
# import time
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key = os.getenv("GJLD_API_KEY"),
#     base_url = os.getenv("GJLD_BASE_URL")
# )
# res = [
#     "用一句话介绍一下北京",
#     "用一句话介绍一下上海",
#     "用一句话介绍一下广州",
#     "用一句话介绍一下深圳",
#     "用一句话介绍一下杭州"
# ]
#
# def test_sync_invoke():
#     print("=====同步=====")
#     start_time = time.time()
#     for i,prompt in enumerate(res):
#         print(f"[同步] 正在发送第 {i + 1} 个请求...")
#         respont = llm.invoke(prompt)
#         print(respont.content)
#     print(f"总耗时: {time.time() - start_time:.2f} 秒\n")
#
#
# async def test_async_ainvoke():
#     print("=== 异步 ainvoke ===")
#     start_time = time.time()
#     print("  [异步] 瞬间派发 5 个请求...")
#     tasks = [llm.ainvoke(prompt) for prompt in res]
#     results = await asyncio.gather(*tasks)
#     for r in results:
#         print(f"回答: {r.content[:20]}...")
#     print(f"总耗时: {time.time() - start_time:.2f} 秒\n")
# async def main():
#     test_sync_invoke()
#     await test_async_ainvoke()
# asyncio.run(main())

# (10)
# def streaming_example():
#     llm = ChatOpenAI(
#         model = "Pro/zai-org/GLM-5",
#         api_key = os.getenv("GJLD_API_KEY"),
#         base_url = os.getenv("GJLD_BASE_URL")
#     )
#     print("AI回答：")
#     full_message = None
#     for chunk in llm.stream("请写一首五字绝句，关于爱情的。"):
#         full_message = chunk if full_message is None else full_message + chunk
#         print(chunk.content,end="",flush=True)
#     print(f"\n\n完整消息:\n{full_message.content}")
# streaming_example()

# (11)
# async def stream_events():
#     llm = ChatOpenAI(
#         model="Pro/zai-org/GLM-5",
#         api_key=os.getenv("GJLD_API_KEY"),
#         base_url=os.getenv("GJLD_BASE_URL")
#     )
#     async for event in llm.astream_events("你好"):
#         if event["event"] == "on_chat_model_start":
#             print("开始！")
#         elif event["event"] == "on_chat_model_stream":
#             print("进行中！")
#         elif event["event"] == "on_chat_model_end":
#             print(f"\n完成!")
# asyncio.run(stream_events())

# (12)
# def batch_example():
#     llm = ChatOpenAI(
#         model="Pro/zai-org/GLM-5",
#         api_key=os.getenv("GJLD_API_KEY"),
#         base_url=os.getenv("GJLD_BASE_URL")
#     )
#     que = [
#         "什么是Python？",
#         "什么是JavaScript？",
#         "什么是Go语言？"
#     ]
#     res = llm.batch(que)
#     for q,r in zip(que, res):
#         print(f"Q: {q}")
#         print(f"A: {r.content}\n")
# batch_example()

# (13)
# async def batch_async():
#     questions = [
#         "什么是LangChain？",
#         "LangChain的核心组件有哪些？",
#         "如何使用LangChain构建Agent？"
#     ]
#     responses = await llm.abatch(questions)
#     for q, r in zip(questions, responses):
#         print(f"Q: {q}\nA: {r.content}\n")
#
# asyncio.run(batch_async())

# (14)
# llm = ChatOpenAI(
#     model = "Pro/zai-org/GLM-5",
#     api_key=os.getenv("GJLD_API_KEY"),
#     base_url=os.getenv("GJLD_BASE_URL")
# )
# res = llm.invoke(
#     "讲一个笑话",
#     config = {
#         "tags": ["humor", "demo"],          # 标签
#         "metadata": {"user_id": "123"},
#     }
# )
# print(res.content)















