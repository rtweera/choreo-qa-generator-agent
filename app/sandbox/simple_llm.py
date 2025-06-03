from langchain_core.prompts import ChatPromptTemplate
import getpass
import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_core.messages import ChatMessage, ChatMessageChunk

load_dotenv(override=True, verbose=True)

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash-preview-04-17", model_provider="google_genai")

system_template = "Translate the following from English into {language}"

# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template), ("user", "{text}")]
# )
prompt_template = ChatPromptTemplate.from_messages(
    [SystemMessage(content=system_template), HumanMessage(content="{text}")]  # type: ignore[call-arg]
)
prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

response = model.invoke(prompt)
print(response.content)