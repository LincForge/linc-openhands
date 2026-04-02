import os
import pytest
from openhands.sdk import LLM, Agent, Conversation, Tool

def test_agent_conversation_run_fails_registration() -> None:
    """Test that Conversation fails to run if tools are not registered."""
    api_key = os.getenv("LLM_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        pytest.skip("LLM_API_KEY or ANTHROPIC_API_KEY not found")
        
    llm = LLM(model="anthropic/claude-3-5-sonnet-20240620", api_key=api_key)
    agent = Agent(
        llm=llm,
        tools=[
            Tool(name="TerminalTool"),
            Tool(name="FileEditorTool"),
        ],
    )
    
    workspace_path = os.getcwd()
    conversation = Conversation(agent=agent, workspace=workspace_path)
    
    # We expect this to fail with registration error based on previous test_sdk.py run
    with pytest.raises(Exception, match="ToolDefinition .* is not registered"):
        conversation.send_message("Just say hi")
        conversation.run()
