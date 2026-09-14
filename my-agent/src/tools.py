import logging
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun

logger = logging.getLogger("agent")

@function_tool
async def search_web(context: RunContext, query: str):
    """Use this tool to search the web for information.

    Args:
        query: The search query to look up on the web.
    """
    try:
        result = DuckDuckGoSearchRun().run(tool_input=query)
        logger.info(f"Web search result for query '{query}': {result}")
        return result
    except Exception as e:
        logger.error(f"Error during web search for query '{query}': {e}")
        raise

