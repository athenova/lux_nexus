from simple_blogger import SimpleBlogger
from datetime import datetime

class Project(SimpleBlogger):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            text_ai_token_name='OPENAI_API_KEY',
            ai_text_model='chatgpt-4o-latest',
            text_base_url='https://api.openai.com/v1',
            first_post_date=datetime(2025, 3, 3),
            **kwargs)

    def _task_converter(self, item):
        return { 
                "category": f"{item['category']}",
                "description": f"{item['description']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{item['category']}'",
                "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{item['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
            }
    