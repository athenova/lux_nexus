from simple_blogger import Journalist
from datetime import datetime
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.InstagramSender import InstagramSender
from simple_blogger.senders.VkSender import VkSender

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            first_post_date=datetime(2025, 3, 4),
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id=f"@lux_nexus"), 
                     InstagramSender(channel_token_name='LUX_NEXUS_TOKEN'),
                     VkSender(group_id="229822258")],
            topic_word_limit=100,
            **kwargs)

    def _task_converter(self, item):
        return { 
                "topic": f"{item['topic']}",
                "category": f"{item['category']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{item['topic']}' из области '{item['category']}'",
                "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{item['topic']}' из области '{item['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
            }
