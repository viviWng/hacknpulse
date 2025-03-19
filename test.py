import autogen

config_list = [
    {
        "model": "gpt-4",
        "api_key": "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"
    }
]

llm_config={
    #"request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0 # values between 0 and 1. The higher the value, the more creative the text
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
    # system_message= "" to be defined if you have multiple assistant agents defined
)

# creating an agent that acts on behalf of the user
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    #any files that it creates or writes, it will be into this folder
    code_execution_config={
        "work_dir": "web",
        "use_docker": False},
    max_consecutive_auto_reply=10, #if you set it too high, the agents might get into an infinite loop
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)


task = """
Can you summarise the article in the following link : https://artificialintelligenceact.eu/article/5/
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)