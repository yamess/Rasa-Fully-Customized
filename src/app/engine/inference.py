from rasa.core.agent import load_agent
from rasa.core.channels import UserMessage


async def predict_intent(text: str, model_path):
    agent = await load_agent(model_path=model_path)
    result = await agent.handle_message(message=UserMessage(text=text))
    print(result)
