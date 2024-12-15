# -*- coding: utf-8 -*-


from typing import *
import os
import json
from openai import OpenAI
from openai.types.chat.chat_completion import Choice
 
client = OpenAI(
    base_url="https://api.moonshot.cn/v1",
    api_key="your own api",#联网搜索要收费，kimi会送15块，不充值五十，kimiapi的回复频率是一分钟三次，注意修改LLDCG中每次问完的等待时间
)
 
 
# search 工具的具体实现，这里我们只需要返回参数即可
def search_impl(arguments: Dict[str, Any]) -> Any:
    return arguments
 
 
def chat(messages) -> Choice:
    completion = client.chat.completions.create(
        model="moonshot-v1-128k",
        messages=messages,
        temperature=0.3,
        tools=[
            {
                "type": "builtin_function",  
                "function": {
                    "name": "$web_search",
                },
            }
        ]
    )
    return completion.choices[0]
 
 
def response(ques):
    messages = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的最新的理论实事答题助手，你更擅长中文的对话。你会根据网络上最新最权威的文章，为用户提供有帮助，准确的回答，回答选择题时，只回答答案的选项，判断题只回答对或者错，填空题你会判断空的位置，不同的空的答案，用分号隔离开。Moonshot AI 为专有名词，不可翻译成其他语言。"},
    ]

    messages.append({
        "role": "user",
        "content":  ques
    })
 
    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        choice = chat(messages)
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls": 
            messages.append(choice.message) 
            for tool_call in choice.message.tool_calls: 
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(tool_call.function.arguments) 
                if tool_call_name == "$web_search":
                    tool_result = search_impl(tool_call_arguments)
                else:
                    tool_result = f"Error: unable to find tool by name '{tool_call_name}'"
 
             
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result), 
                })
    return choice.message.content 
 
 
if __name__ == '__main__':
    ques = input("你：")
    response(ques)