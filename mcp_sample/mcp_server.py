from mcp.server.fastmcp import FastMCP
from retriever import get_retriever, format_docs

# FastMCP 초기화
mcp = FastMCP(
    "retrieve_ai_trends",
    instructions="Retrieve the latest trends in AI. If your question is related to AI trends, use this tool. This tool also contains information about a person named Sean. The query must be in Korean.",
    host="0.0.0.0",
    port=4100,
)


@mcp.tool()
async def retrieve_ai_trends(query: str) -> str:
    """Retrieve the latest trends in AI. If your question is related to AI trends, use this tool. This tool also contains information about a person named Sean. The query must be in Korean."""
    retriever = get_retriever()
    docs = await retriever.ainvoke(query)
    return format_docs(docs)


if __name__ == "__main__":
    mcp.run(transport="sse")
