from fastapi import APIRouter

router = APIRouter()

@router.get("/templates")
async def get_templates(user_id: str) -> dict:
    """
    ユーザーに関連する日記テンプレートを取得します。
    """
    pass

@router.post("/templates")
async def create_template(user_id: str, template_data: dict) -> dict:
    """
    ユーザーの日記テンプレートを作成します。
    """
    pass

@router.put("/templates/{template_id}")
async def update_template(user_id: str, template_id: str, template_data: dict) -> dict:
    """
    指定された日記テンプレートを更新します。
    """
    pass

@router.delete("/templates/{template_id}")
async def delete_template(user_id: str, template_id: str) -> dict:
    """
    指定された日記テンプレートを削除します。
    """
    pass
