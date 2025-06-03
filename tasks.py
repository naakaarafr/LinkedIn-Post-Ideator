from crewai import Task
from tools import search_tool
from agents import coach, influencer, critic

task_search = Task(
    description="""
    Research and compile a comprehensive report on the top 5-7 emerging AI and technology skills 
    that will be most valuable for tech professionals in 2025. 
    
    Your report should include:
    - Skill name and brief description
    - Why it's becoming important
    - Specific applications or use cases
    - How professionals can start learning it
    
    Present findings in a clear, structured format with bullet points.
    """,
    agent=coach,
    tools=[search_tool],
    expected_output="A detailed report with at least 5 AI/tech skills in bullet point format"
)

task_post = Task(
    description="""
    Using the research from the career coach, create an engaging LinkedIn post about 
    the top emerging AI and tech skills for 2025.
    
    Requirements:
    - Eye-catching headline (under 30 characters)
    - Maximum 200 words total
    - Include relevant emojis
    - Add 3-5 relevant hashtags
    - Make it engaging and shareable
    - Focus on actionable insights for professionals
    """,
    agent=influencer,
    context=[task_search],  # This ensures the task gets input from task_search
    expected_output="A LinkedIn post under 200 words with headline, emojis, and hashtags"
)

task_critique = Task(
    description="""
    Review and refine the LinkedIn post to ensure it meets all requirements:
    
    - Headline is engaging and under 30 characters
    - Total word count is under 200 words
    - Emojis are used effectively (not too many, not too few)
    - Hashtags are relevant and trending
    - Content is engaging and provides value
    - Call-to-action is clear
    
    Provide the final polished version of the post.
    """,
    agent=critic,
    context=[task_post],  # This ensures the task gets input from task_post
    expected_output="A refined, final LinkedIn post ready for publishing"
)