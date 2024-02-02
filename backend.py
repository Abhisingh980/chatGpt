import openai


class ChatBot:
    def __init__(self):
        # your own apikey
        openai.api_key = "sk-uDi1dUPHVJZ148Pp5y0TT3BlbkFJ2WCU..."

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-16k",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chat = ChatBot()
    response = chat.get_response("today joke")
    print(response)

