from openhands.sdk import LLM


def test_sdk_import() -> None:
    """Verify the SDK can be imported."""
    assert LLM is not None
