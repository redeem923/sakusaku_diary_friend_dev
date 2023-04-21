from typing import List, Tuple
from app.models import DiaryTemplate


def parse_templates(templates: List[str]) -> List[DiaryTemplate]:
    """
    日記テンプレートのリストを解析し、DiaryTemplateオブジェクトのリストに変換します。
    """
    pass


def get_templates_by_similarity(query: str, templates: List[DiaryTemplate]) -> List[DiaryTemplate]:
    """
    類似度に基づいて日記テンプレートを取得します。最も類似しているテンプレートから順にリストで返されます。
    """
    pass


def format_date(date: str) -> str:
    """
    日付文字列を適切な形式に変換します。
    """
    pass


def sanitize_text(text: str) -> str:
    """
    テキストをクリーニングし、不適切な言葉やフレーズを取り除きます。
    """
    pass
