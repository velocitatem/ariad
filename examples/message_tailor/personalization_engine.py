from openai import OpenAI
client = OpenAI()

def generate_personalized_message(member_data, info_message):
    name = member_data.get('Name')
    interest = member_data.get('Preferences', {}).get('Interest')

    prompt = f"""Your goal is to send a message to {name}, informing them that {info_message}.
    Their interests are {interest}. You should write a personalized message to them. Do not overly focus on the interests.
    """

    # Initialize the chat models with a system message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the assistant's reply
    assistant_reply = response.choices[0].message.content

    return assistant_reply