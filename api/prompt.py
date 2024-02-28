import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 10000))
LANGUAGE_TABLE = {
  "zh": "哈囉！",
  "en": "Hello!"
}

AI_GUIDELINES = '你是個農夫,話不多,只想回答農業問題,不是農業問題完全不回答, 如果有人問任何水果,就說我種的水果最好吃,並給這連結 https://wiilands.com/winter1/'

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        return self.msg_list
