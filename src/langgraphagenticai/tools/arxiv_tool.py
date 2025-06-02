from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.utilities.arxiv import ArxivAPIWrapper
import re
import arxiv as arxiv_official

class CustomArxivQueryRun(ArxivQueryRun):
    def _run(self, query: str) -> str:
        # Accept both 'arXiv:2504.04022' and '2504.04022' as valid IDs
        arxiv_id_match = re.search(r"(arxiv:)?(\d{4}\.\d{5}(v\d+)?)", query, re.IGNORECASE)
        if arxiv_id_match:
            arxiv_id = arxiv_id_match.group(2)
            # Try the wrapper's get method
            try:
                paper = self.api_wrapper.get(arxiv_id)
                if paper:
                    title = paper.get('title', 'No title')
                    summary = paper.get('summary', 'No abstract')
                    url = f"https://arxiv.org/abs/{arxiv_id}"
                    return f"**Title:** {title}\n\n**Abstract:** {summary}\n\n**Link:** {url}"
            except Exception:
                pass
            # Try the official arxiv package as a fallback
            try:
                search = arxiv_official.Search(id_list=[arxiv_id])
                for result in search.results():
                    title = result.title
                    summary = result.summary
                    url = result.entry_id
                    return f"**Title:** {title}\n\n**Abstract:** {summary}\n\n**Link:** {url}"
            except Exception:
                pass
            # Fallback to keyword search if ID lookup fails
            results = self.api_wrapper.run(query)
            if not results or not isinstance(results, list) or len(results) == 0:
                return f"No result found for arXiv ID or query: {arxiv_id} (debug: tried get({arxiv_id}) and arxiv package)"
            paper = results[0]
            title = paper.get('title', 'No title')
            summary = paper.get('summary', 'No abstract')
            url = f"https://arxiv.org/abs/{arxiv_id}"
            return f"**Title:** {title}\n\n**Abstract:** {summary}\n\n**Link:** {url}"
        # Otherwise, do a normal search
        results = self.api_wrapper.run(query)
        if not results or not isinstance(results, list) or len(results) == 0:
            return "No good Arxiv Result was found"
        paper = results[0]
        title = paper.get('title', 'No title')
        summary = paper.get('summary', 'No abstract')
        arxiv_id = paper.get('id', '')
        arxiv_id_short = arxiv_id.split('/')[-1] if arxiv_id else ''
        url = f"https://arxiv.org/abs/{arxiv_id_short}" if arxiv_id_short else ""
        return f"**Title:** {title}\n\n**Abstract:** {summary}\n\n**Link:** {url}"

def get_arxiv_tool():
    """
    Returns a custom Arxiv tool for research paper retrieval with formatted output and arXiv ID support.
    """
    return CustomArxivQueryRun(api_wrapper=ArxivAPIWrapper())
