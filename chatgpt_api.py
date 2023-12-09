import openai

client = openai.OpenAI(api_key = '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')

def query_gpt(prompt, model="gpt-3.5-turbo", temp=0.2):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)
    return response

def query_gpt_conversation_interactive(model="gpt-3.5-turbo", temp=0.2):

    messages = []
    while True:
        message = input("User:" )
        if message == "": break
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(model=model, messages=messages, temperature=temp)

        reply = response.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

    return messages

def query_gpt_conversation(user_messages, model="gpt-3.5-turbo", temp=0.2):

    all_messages = []
    for u_msg in user_messages:
        all_messages.append({"role": "user", "content": u_msg})

        response = client.chat.completions.create(model=model, messages=all_messages, temperature=temp)
        reply = response.choices[0].message.content
        all_messages.append({"role": "assistant", "content": reply})

    return all_messages
