from state_machine import StateMachine
from database import Database
from ai_engine import AIEngine


class Chatbot:

    def __init__(self):
        self.state_machine = StateMachine()
        self.database = Database("chatbot.db")
        self.ai_engine = AIEngine()

    def handle_message(self, user_id, message_type, message_content):
        return message_content
        # # 1. ユーザーIDを使って、データベースから現在のユーザー状態を取得
        # current_state = self.database.get_user_state(user_id)

        # # 2. カスタム状態マシンを使って、状態遷移を管理
        # new_state, action_result = self.state_machine.process_event(
        #     user_id, message_type, message_content, current_state
        # )

        # # 3. 状態遷移に応じて、適切なアクションを実行（例：AIエンジンとのやりとり、データベースへの保存）
        # if action_result["action"] == "generate_diary_entry":
        #     topic = action_result["topic"]
        #     user_data = action_result["user_data"]
        #     past_diary_data = self.database.get_past_diary_data(user_id, topic)
        #     generated_text = self.ai_engine.generate_diary_entry(
        #         topic, user_data, past_diary_data)
        #     response_message = generated_text

        # elif action_result["action"] == "refine_diary_entry":
        #     feedback = action_result["feedback"]
        #     generated_text = action_result["generated_text"]
        #     refined_text = self.ai_engine.refine_diary_entry(
        #         feedback, generated_text)
        #     response_message = refined_text

        # else:
        #     response_message = action_result["response_message"]

        # # 4. 応答メッセージを生成
        # # (前のステップで応答メッセージが生成されています)

        # # 5. 新しい状態をデータベースに保存
        # self.database.set_user_state(user_id, new_state)

        # # 6. 応答メッセージを返す
        # return response_message
