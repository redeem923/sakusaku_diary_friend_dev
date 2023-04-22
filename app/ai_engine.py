import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class AIEngine:

    def __init__(self, temperature=0.7):
        self.temperature = temperature

    def generate_diary_entry(self, topic, user_data, past_diary_data):
        prompt = f"ユーザーに関する情報: {user_data}\n過去の日記: {past_diary_data}\n今日のトピック: {topic}\n\n日記のエントリ:"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].text.strip()

    def refine_diary_entry(self, feedback, generated_text):
        prompt = f"元のテキスト: {generated_text}\nフィードバック: {feedback}\n\n改善されたテキスト:"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].text.strip()
