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

# assistant = autogen.AssistantAgent(
#     name="assistant",
#     llm_config=llm_config
#     # system_message= "" to be defined if you have multiple assistant agents defined
# )

# # creating an agent that acts on behalf of the user
# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     human_input_mode="TERMINATE",
#     #any files that it creates or writes, it will be into this folder
#     code_execution_config={
#         "work_dir": "web",
#         "use_docker": False},
#     max_consecutive_auto_reply=10, #if you set it too high, the agents might get into an infinite loop
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
#     llm_config=llm_config,
#     system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
# )


# task = """
# Can you summarise the article in the following link : https://artificialintelligenceact.eu/article/5/
# """

# user_proxy.initiate_chat(
#     assistant,
#     message=task
# )

# ai_compliance_sherpa = autogen.ConversableAgent(
#     "ai_compliance_sherpa",
#     system_message="You are a experienced data protection officer of a software company."
#     "You know the EU Artificial Intelligence Act and you have to make sure that the company complies with it. "
#     "If I propose an AI solution that is not compliant with the AI Act, you should tell me that it is not compliant and explain to me in bullet points why it is not compliant with reference to the corresponding article. "
#     "If I propose an AI solution that is compliant with the AI Act, you should tell me that it is compliant and explain to me in bullet points why it is compliant. ",
#     llm_config=llm_config,
#     is_termination_msg=lambda msg: "TQ" in msg["content"],  # terminate if the number is guessed by the other agent
#     human_input_mode="NEVER",  # never ask for human input
# )

# ai_compliance_sherpa = autogen.ConversableAgent(
#     "ai_compliance_sherpa",
#     system_message=(
#         "You are an expert AI compliance officer guiding users through the EU AI Act. "
#         "Your role is to analyze high-risk AI solutions and ensure they meet compliance requirements. "
#         "Ask step-by-step questions and suggest necessary improvements."
#     ),
#     description="Guides users step by step to ensure AI solutions comply with the EU AI Act.",
#     llm_config=llm_config,
#     is_termination_msg=lambda msg: "TQ" in msg["content"],  # terminate if the number is guessed by the other agent
#     human_input_mode="NEVER",  # never ask for human input
# )

# Initialize the ConversableAgent
# ai_compliance_sherpa = autogen.ConversableAgent(
#     name="ai_compliance_sherpa",
#     system_message=(
#         "You are an AI compliance agent that helps users make their high-risk AI solutions compliant with the EU AI Act. "
#         "Guide them through each necessary step and ask relevant questions."
#     ),
#     description="Guides users step-by-step to ensure their AI solution is compliant with the EU AI Act.",
#     llm_config=llm_config,
# )

# def compliance_workflow():
#     # AI solution description (you, the user, provide it)
#     user_prompt = "Describe your AI solution in detail (e.g., purpose, data used, decision-making process)."
    
#     # Send the user prompt to the agent and get the response
#     user_message = {"role": "user", "content": user_prompt}
#     user_response = ai_compliance_sherpa.generate_reply(messages=[user_message])
    
#     print("\nAI Solution Description:\n", user_response)

#     # Step 1: Categorize the AI solution (ask the user)
#     category_prompt = """
#     Based on the EU AI Act, which category does your AI solution belong to? 
#     Options include:
#     - Employment & Recruitment
#     - Education
#     - Critical Infrastructure
#     - Law Enforcement
#     - Migration & Border Control
#     - Financial Services (Banking, Insurance)
#     - Medical AI
#     - Other
#     """
#     # Ask the user for a response
#     category_message = {"role": "user", "content": category_prompt}
#     category_response = ai_compliance_sherpa.generate_reply(messages=[category_message])
#     print("\nSolution Category:\n", category_response)

#     # Step 2: Transparency check
#     transparency_prompt = "Does your AI system explain how decisions are made to end users? (Yes/No)"
#     transparency_message = {"role": "user", "content": transparency_prompt}
#     transparency_response = ai_compliance_sherpa.generate_reply(messages=[transparency_message])
    
#     if "no" in transparency_response.lower():
#         print("\n⚠️ Transparency issue: Consider adding features like SHAP or LIME for model explanations.")

#     # Step 3: Bias check
#     bias_prompt = "Does your AI system use sensitive data (e.g., race, gender, age)? (Yes/No)"
#     bias_message = {"role": "user", "content": bias_prompt}
#     bias_response = ai_compliance_sherpa.generate_reply(messages=[bias_message])
    
#     if "yes" in bias_response.lower():
#         fairness_prompt = "Have you performed a fairness analysis to mitigate bias? (Yes/No)"
#         fairness_message = {"role": "user", "content": fairness_prompt}
#         fairness_response = ai_compliance_sherpa.generate_reply(messages=[fairness_message])
        
#         if "no" in fairness_response.lower():
#             print("\n⚠️ Bias risk: Implement fairness measures (e.g., Fairlearn or IBM AI Fairness 360).")

#     # Step 4: Human oversight check
#     oversight_prompt = "Can a human override AI decisions? (Yes/No)"
#     oversight_message = {"role": "user", "content": oversight_prompt}
#     oversight_response = ai_compliance_sherpa.generate_reply(messages=[oversight_message])
    
#     if "no" in oversight_response.lower():
#         print("\n⚠️ Human oversight issue: Implement a manual override or human-in-the-loop system.")

#     # Step 5: Security check
#     security_prompt = "Has your AI system been tested for adversarial attacks and security risks? (Yes/No)"
#     security_message = {"role": "user", "content": security_prompt}
#     security_response = ai_compliance_sherpa.generate_reply(messages=[security_message])
    
#     if "no" in security_response.lower():
#         print("\n⚠️ Security issue: Conduct adversarial testing and implement fail-safes.")

#     # Final Recommendation based on the responses
#     print("\n✅ Compliance Report:")  
#     compliance_report = "Your AI solution is compliant!" if all([response.lower() == 'yes' for response in [transparency_response, fairness_response, oversight_response, security_response]]) else "⚠️ Your AI solution needs improvements in the above areas."
#     print(compliance_report)

# # Start the compliance workflow
# compliance_workflow()

import autogen

# Initialize the ConversableAgent
ai_compliance_sherpa = autogen.ConversableAgent(
    name="ai_compliance_sherpa",
    system_message=(
        "You are an AI compliance agent that helps users make their high-risk AI solutions compliant with the EU AI Act. "
        "Guide them through each necessary step and ask relevant questions."
    ),
    description="Guides users step-by-step to ensure their AI solution is compliant with the EU AI Act.",
    llm_config=llm_config,  # Make sure you have your llm_config defined properly
)

def compliance_workflow():
    # Step 1: AI solution description (user provides it)
    user_prompt = "Describe your AI solution in detail (e.g., purpose, data used, decision-making process)."
    
    # Send user prompt to the agent
    user_message = {"role": "user", "content": user_prompt}
    user_response = ai_compliance_sherpa.generate_reply(messages=[user_message])
    print("\nAI Solution Description:\n", user_response)
    
    # Wait for the user to provide their description before continuing
    user_input = input("Please describe your AI solution: ")

    # Send the user input back to the agent (this is how you simulate the conversation flow)
    user_response = ai_compliance_sherpa.generate_reply(messages=[{"role": "user", "content": user_input}])
    print("\nThank you for your input!")

    # Step 2: Categorize the AI solution (ask the user)
    category_prompt = """
    Based on the EU AI Act, which category does your AI solution belong to? 
    Options include:
    - Employment & Recruitment
    - Education
    - Critical Infrastructure
    - Law Enforcement
    - Migration & Border Control
    - Financial Services (Banking, Insurance)
    - Medical AI
    - Other
    """
    # Ask the user for a response
    print("\nAI Compliance Agent:")
    print(category_prompt)
    category_input = input("Please select a category: ")
    
    category_message = {"role": "user", "content": category_input}
    category_response = ai_compliance_sherpa.generate_reply(messages=[category_message])
    print("\nSolution Category:\n", category_response)

    # Step 3: Transparency check
    transparency_prompt = "Does your AI system explain how decisions are made to end users? (Yes/No)"
    print("\nAI Compliance Agent:")
    print(transparency_prompt)
    transparency_input = input("Please answer (Yes/No): ")
    
    transparency_message = {"role": "user", "content": transparency_input}
    transparency_response = ai_compliance_sherpa.generate_reply(messages=[transparency_message])
    print("\nTransparency Check:\n", transparency_response)

    if "no" in transparency_response.lower():
        print("\n⚠️ Transparency issue: Consider adding features like SHAP or LIME for model explanations.")

    # Step 4: Bias check
    bias_prompt = "Does your AI system use sensitive data (e.g., race, gender, age)? (Yes/No)"
    print("\nAI Compliance Agent:")
    print(bias_prompt)
    bias_input = input("Please answer (Yes/No): ")
    
    bias_message = {"role": "user", "content": bias_input}
    bias_response = ai_compliance_sherpa.generate_reply(messages=[bias_message])
    
    if "yes" in bias_response.lower():
        fairness_prompt = "Have you performed a fairness analysis to mitigate bias? (Yes/No)"
        print("\nAI Compliance Agent:")
        print(fairness_prompt)
        fairness_input = input("Please answer (Yes/No): ")
        
        fairness_message = {"role": "user", "content": fairness_input}
        fairness_response = ai_compliance_sherpa.generate_reply(messages=[fairness_message])
        
        if "no" in fairness_response.lower():
            print("\n⚠️ Bias risk: Implement fairness measures (e.g., Fairlearn or IBM AI Fairness 360).")
    else:
        fairness_response = "irrelevant"
    # Step 5: Human oversight check
    oversight_prompt = "Can a human override AI decisions? (Yes/No)"
    print("\nAI Compliance Agent:")
    print(oversight_prompt)
    oversight_input = input("Please answer (Yes/No): ")
    
    oversight_message = {"role": "user", "content": oversight_input}
    oversight_response = ai_compliance_sherpa.generate_reply(messages=[oversight_message])
    
    if "no" in oversight_response.lower():
        print("\n⚠️ Human oversight issue: Implement a manual override or human-in-the-loop system.")

    # Step 6: Security check
    security_prompt = "Has your AI system been tested for adversarial attacks and security risks? (Yes/No)"
    print("\nAI Compliance Agent:")
    print(security_prompt)
    security_input = input("Please answer (Yes/No): ")
    
    security_message = {"role": "user", "content": security_input}
    security_response = ai_compliance_sherpa.generate_reply(messages=[security_message])
    
    if "no" in security_response.lower():
        print("\n⚠️ Security issue: Conduct adversarial testing and implement fail-safes.")

    # Create a list of responses to check for validity (non-empty and not None)
    responses = [transparency_response, fairness_response, oversight_response, security_response]

    # Check if all responses are non-empty and if they are 'yes'
    valid_responses = [response for response in responses if response and response.lower() == 'yes']

    # If all valid responses are 'yes', AI solution is compliant, otherwise, it needs improvements
    if len(valid_responses) == len(responses):
        compliance_report = "Your AI solution is compliant!"
    else:
        compliance_report = "⚠️ Your AI solution needs improvements in the areas above."
        invalid_responses = [response for response in responses if response and response.lower() != 'yes']
        print(invalid_responses)

    print(compliance_report)

# Start the compliance workflow
compliance_workflow()


