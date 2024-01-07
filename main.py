from langchain.llms import Ollama
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
ollama_openhermes = Ollama(model="llama2-uncensored")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

local_expert = Agent(
  role='Local Expert at this city',
  goal='Provide the BEST insights about the selected city',
  backstory="""A knowledgeable local guide with extensive information
  about the city, it's attractions and customs""",
  tools=[
    SearchTools.search_internet,
    BrowserTools.scrape_and_summarize_website,
  ],
  llm=ollama_openhermes, # Ollama model passed here
  verbose=True
)