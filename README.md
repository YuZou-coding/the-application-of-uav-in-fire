# the-application-of-uav-in-fire

democsv.csv 为输入的数据
dispatch_log.csv是每次派遣的日志

env_new.py,llm.py,user_prompt_generation.py是需要用到的所有代码
1） user_prompt_generation.py是生成propmt
2） llm.py 是用于调用与大模型对话的api
3） env_new.py 是实验环境以及任务执行

运行该项目启动env_new.py即可


## 改动 2025.3.17

更改了env_new.py以及user_prompt_generation.py
具体为前者中策略提取的正则匹配部分以及后者的prompt文本，避免llm对无人机代理的称呼混淆。

