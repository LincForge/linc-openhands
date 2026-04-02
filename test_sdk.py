import os

import structlog
# Import tools to trigger registration
import openhands.tools.file_editor  # noqa: F401
import openhands.tools.terminal  # noqa: F401
from openhands.sdk import LLM, Agent, Conversation, Tool

# Configure structlog
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.ConsoleRenderer(),
    ],
)
logger = structlog.get_logger()


def main() -> None:
    """Run a simple OpenHands SDK verification task."""

    # 1. Configure the LLM
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error(
            "api_key_missing",
            message="Please set GOOGLE_API_KEY environment variable",
        )
        return

    # Using Gemini 2.5 Flash - confirmed working in diagnostics
    llm = LLM(model="gemini/gemini-2.5-flash", api_key=api_key)

    # 2. Define the Agent with tools
    logger.info("agent_init", model=llm.model)
    agent = Agent(
        llm=llm,
        tools=[
            Tool(name="terminal"),
            Tool(name="file_editor"),
        ],
    )

    # 3. Start a Conversation in the current directory
    workspace_path = os.getcwd()
    logger.info("conversation_start", workspace=workspace_path)
    conversation = Conversation(agent=agent, workspace=workspace_path)

    # 4. Run a task
    task_message = (
        "Create a file named HELLO_OPENHANDS.md with the text "
        "'Hello from OpenHands SDK!' and include the current system time."
    )
    logger.info("sending_message", task=task_message)

    try:
        conversation.send_message(task_message)
        conversation.run()
        logger.info("task_completed")
    except Exception as e:
        logger.error("task_failed", error=str(e))


if __name__ == "__main__":
    main()
