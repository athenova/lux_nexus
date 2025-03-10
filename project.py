from simple_blogger import Journalist
from datetime import datetime

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 3, 4),
            send_text_with_image=True,
            topic_word_limit=100,
            **kwargs)

    def _task_converter(self, item):
        return { 
                "topic": f"{item['topic']}",
                "category": f"{item['category']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{item['topic']}' из области '{item['category']}'",
                "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{item['topic']}' из области '{item['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
            }
    
   