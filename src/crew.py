from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task


def run_crew(topic: str):
    """Run the AI news generation workflow."""

    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )

    try:
        result = crew.kickoff(
            inputs={"topic": topic}
        )

        print("\n" + "=" * 60)
        print(f"REPORT GENERATED FOR: {topic}")
        print("=" * 60)
        print(result)

        return result

    except Exception as e:
        print(f"Error running crew: {e}")
        return None


if __name__ == "__main__":
    run_crew("AI in Healthcare")