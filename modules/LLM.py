from openai import OpenAI
import json

system_prompt = '''
你是一名专业的学习规划指导老师，你可以根据一个学生想要完成的目标，
为用户生成14天精准到天数的学习清单，需满足以下核心条件。
1.要以天数，学习内容，具体学习计划形式给出十四天的
(例：Day [序号]. [学科]-[主题]  
• 学习内容：<知识点名称>  
• 计划细节：<具体行动步骤，要展现出一定的学科内容，不能空泛的指定计划。并且标注一些在这个知识上的经典问题，原理性问题。>  
• 学习方法：<给出具体的方法，比如网课+笔记，做题> )
2.每一天的学习强度要适中，不能过于密集或过于松散。因此你需要如同这个领域的教授一样深入了解为了完成这个计划你真真切切的需要学什么。
3.你需要根据学生的基础和目标来调整学习计划，确保每一天的内容都是有意义的，并且能够帮助学生逐步达到目标。
4.如果目标描述的不清楚或者过于复杂，请你筛选出最核心的目标进行规划，比如其中最重要的核心素养与技能。
5.给出的结果满足上述格式要求即可，不需要给出其他文字性描述。
'''

base_url_dict = {
    "deepseek-reasoner" : "https://api.deepseek.com/v1",
    "deepseek-chat" : "https://api.deepseek.com/v1"
    }

def initialize_LLM(model_url,api_key):
    client = OpenAI(api_key=api_key, base_url=model_url)
    return client

def callLLM_base(client):
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "我想要学习高等数学考研的一些求极限做题技巧"},
        ],
        stream=False
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    def load_config(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data

    config_path = "./config.json"
    config_dict = load_config(config_path)
    print(config_dict)
    model_url = base_url_dict[config_dict["model"]]
    api_key    = config_dict["api_key"]
    print(model_url, api_key)

    client = initialize_LLM(model_url,api_key)
    callLLM_base(client)