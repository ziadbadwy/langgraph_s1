import datetime
import math
from ddgs import DDGS


def web_search(query: str) -> str:
    results = DDGS().text(query, max_results=4)
    if not results:
        return "No results found."
    combined = ""
    for r in results:
        combined += f"Title: {r['title']}\nSummary: {r['body']}\n\n"
    return combined


def wikipedia_search(query: str) -> str:
    results = DDGS().text(f"site:en.wikipedia.org {query}", max_results=2)
    if not results:
        return "No Wikipedia results found."
    combined = ""
    for r in results:
        combined += f"Title: {r['title']}\nSummary: {r['body']}\n\n"
    return combined


def calculator(expression: str) -> str:
    try:
        allowed = {"sqrt": math.sqrt, "pi": math.pi, "abs": abs, "round": round}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Could not calculate '{expression}': {e}"


def get_current_date() -> str:
    return datetime.datetime.now().strftime("Today is %A, %B %d, %Y")


TOOLS = {
    "web_search": web_search,
    "wikipedia":  wikipedia_search,
    "calculator": calculator,
    "get_date":   get_current_date,
}
