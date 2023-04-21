from linebot.models import CarouselTemplate, CarouselColumn, TemplateSendMessage, PostbackAction, TextMessage

def create_carousel_message(user_id: str) -> TemplateSendMessage:
    """
    Create a carousel message containing diary templates for the user to choose from.
    Args:
        user_id: The user ID to generate the diary templates for.
    Returns:
        A TemplateSendMessage object containing the carousel message.
    """
    diary_templates = get_diary_templates_for_user(user_id)

    carousel_columns = []

    for template in diary_templates:
        column = CarouselColumn(
            title=template.title,
            text=template.description,
            actions=[
                PostbackAction(
                    label="Choose",
                    display_text="Choosing template",
                    data=f"action=choose_template&template_id={template.id}"
                )
            ]
        )
        carousel_columns.append(column)

    carousel_template = CarouselTemplate(columns=carousel_columns)
    carousel_message = TemplateSendMessage(alt_text="Diary templates", template=carousel_template)

    return carousel_message

def create_preview_message(generated_diary: str) -> TextMessage:
    """
    Create a message containing the preview of the generated diary.
    Args:
        generated_diary: The generated diary text.
    Returns:
        A TextMessage object containing the diary preview.
    """
    preview_message = TextMessage(text=f"Here is your generated diary:\n\n{generated_diary}\n\nDo you want to make any changes? Reply with your feedback or 'OK' to approve.")

    return preview_message
