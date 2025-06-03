from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

coach = Agent(
    role='Senior Career Coach',
    goal="Discover and examine key tech and AI career skills for 2025",
    backstory="You're an expert in spotting new trends and essential skills in AI and technology.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

influencer = Agent(
    role='LinkedIn Influencer Writer',
    goal="Write catchy, emoji-filled LinkedIn posts within 200 words",
    backstory="You're a specialized writer on LinkedIn, focusing on AI and technology.",
    verbose=True,
    allow_delegation=False,  # Changed to False to avoid delegation issues
    llm=llm
)

critic = Agent(
    role='Expert Writing Critic',
    goal="Give constructive feedback on post drafts",
    backstory="You're skilled in offering straightforward, effective advice to tech writers. Ensure posts are concise, under 200 words, with emojis and hashtags.",
    verbose=True,
    allow_delegation=False,  # Changed to False to avoid delegation issues
    llm=llm
)
