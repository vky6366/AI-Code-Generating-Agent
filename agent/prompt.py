def prompt(user_input: str)->str:
    prompt = f"""
    You are a PLANNER AGENT. Convert user input to a FULLY FUNCTIONAL engineering project plan

    user input: {user_input}
    """

    return prompt