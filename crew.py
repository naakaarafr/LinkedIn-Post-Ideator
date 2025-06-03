from crewai import Crew, Process
from tasks import task_search, task_post, task_critique
from agents import coach, influencer, critic

def main():
    crew = Crew(
        agents=[coach, influencer, critic],
        tasks=[task_search, task_post, task_critique],
        verbose=2,
        process=Process.sequential
    )
    
    try:
        # Get your crew to work!
        result = crew.kickoff()
        
        print("=" * 50)
        print("FINAL RESULT:")
        print("=" * 50)
        print(result)
        
        return result
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    main()
