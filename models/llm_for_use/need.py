from openai import OpenAI

def conversation(inputs):
    result =[]
    client = OpenAI(api_key="your-api-key-here") # 如果想在代码中设置Api-key而不是全局变量就用这个代码
    messages = [
    {"role": "system", "content": "请用大幅上升，上升，无影响，下降，大幅下降回答以下问题，其中大幅上升上升幅度为超过50%，上升为上升幅度在0到50%，大幅下降为下降幅度超过50%，下降为下降幅度0-50%，并"},
    ]
    for input in inputs:
        messages.append({"role": "user", "content": input})
        completion = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=messages)
        answer = completion.choices[0].message.content
        print('System:', answer)
        messages.append({"role": "system", "content": answer})
        result.append(answer)
    return result
