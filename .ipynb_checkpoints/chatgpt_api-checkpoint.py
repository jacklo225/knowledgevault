import openai

client = openai.OpenAI(api_key = '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')

def query_gpt(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)
    return response

def query_gpt_conversation(model="gpt-3.5-turbo"):

    messages = []
    while True:
        message = input("User:" )
        if message == "": break
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(model=model, messages=messages, temperature=0)

        reply = response.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

    return messages
