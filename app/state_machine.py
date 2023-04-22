class State:
    INIT = "init"
    GENERATING_DIARY = "generating_diary"
    REFINING_DIARY = "refining_diary"


class Event:
    TEXT_MESSAGE = "text_message"
    DIARY_GENERATED = "diary_generated"
    DIARY_REFINED = "diary_refined"


class StateMachine:

    def __init__(self):
        # 初期状態を設定
        self.state = State.INIT

    def process_event(self, user_id, message_type, message_content, current_state):
        # 1. メッセージタイプとコンテンツに基づいて、適切なイベントを特定
        event = self._identify_event(message_type, message_content)

        # 2. 現在の状態とイベントを使って、次の状態を決定
        new_state = self._determine_next_state(current_state, event)

        # 3. 必要に応じて、適切なアクションを実行（例：AIエンジンとのやりとり、データベースへの保存）
        action_result = self._execute_action(user_id, event, message_content)

        # 4. 新しい状態とアクションの結果を返す
        return new_state, action_result

    def _identify_event(self, message_type, message_content):
        if message_type == "text":
            return Event.TEXT_MESSAGE
        elif message_type == "diary_generated":
            return Event.DIARY_GENERATED
        elif message_type == "diary_refined":
            return Event.DIARY_REFINED
        else:
            return None

    def _determine_next_state(self, current_state, event):
        if current_state == State.INIT and event == Event.TEXT_MESSAGE:
            return State.GENERATING_DIARY
        elif current_state == State.GENERATING_DIARY and event == Event.DIARY_GENERATED:
            return State.REFINING_DIARY
        elif current_state == State.REFINING_DIARY and event == Event.DIARY_REFINED:
            return State.INIT
        else:
            return current_state

    def _execute_action(self, user_id, event, message_content):
        if event == Event.TEXT_MESSAGE:
            return {"action": "generate_diary", "topic": message_content}
        elif event == Event.DIARY_GENERATED:
            return {"action": "refine_diary", "feedback": message_content}
        elif event == Event.DIARY_REFINED:
            return {"action": "save_diary", "diary_entry": message_content}
        else:
            return None
