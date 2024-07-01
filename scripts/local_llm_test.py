# Test Llama3 integration
from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

llm = Ollama(
    model="llama3"
)
print(llm.invoke("The first man on the moon was ..."))