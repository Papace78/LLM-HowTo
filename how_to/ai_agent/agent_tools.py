from datetime import datetime
from langchain_core.tools import tool
from langchain_community.agent_toolkits.polygon.toolkit import PolygonToolkit
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def polygon_tools() -> list:
    polygon = PolygonAPIWrapper()
    toolkit = PolygonToolkit.from_polygon_api_wrapper(polygon)
    return toolkit.get_tools()

def wikipedia_tools() -> list:
    wikipedia = WikipediaAPIWrapper()
    return [WikipediaQueryRun(api_wrapper=wikipedia)]

def custom_tools() -> list:
    @tool(parse_docstring=True)
    def get_today() -> str:
        """Return today's date."""
        return datetime.today().strftime("%Y-%m-%d")
    return [get_today]
