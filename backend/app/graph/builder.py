from functools import partial

from langgraph.graph import END, StateGraph

from app.graph.nodes.analyze_gap import analyze_gap_node
from app.graph.nodes.analyze_jd import analyze_jd_node
from app.graph.nodes.analyze_resume import analyze_resume_node
from app.graph.nodes.export_markdown import export_markdown_node
from app.graph.nodes.generate_interview import generate_interview_node
from app.graph.nodes.generate_resumes import generate_resumes_node
from app.graph.nodes.review_resumes import review_resumes_node
from app.graph.state import ResumeGraphState
from app.llm import LLMClient
from app.services.exporter import MarkdownExporter


def build_resume_graph(llm: LLMClient, exporter: MarkdownExporter):
    graph = StateGraph(ResumeGraphState)

    graph.add_node("analyze_jd", partial(analyze_jd_node, llm=llm))
    graph.add_node("analyze_resume", partial(analyze_resume_node, llm=llm))
    graph.add_node("analyze_gap", partial(analyze_gap_node, llm=llm))
    graph.add_node("generate_resumes", partial(generate_resumes_node, llm=llm))
    graph.add_node("review_resumes", partial(review_resumes_node, llm=llm))
    graph.add_node("generate_interview", partial(generate_interview_node, llm=llm))
    graph.add_node("export_markdown", partial(export_markdown_node, exporter=exporter))

    graph.set_entry_point("analyze_jd")
    graph.add_edge("analyze_jd", "analyze_resume")
    graph.add_edge("analyze_resume", "analyze_gap")
    graph.add_edge("analyze_gap", "generate_resumes")
    graph.add_edge("generate_resumes", "review_resumes")
    graph.add_edge("review_resumes", "generate_interview")
    graph.add_edge("generate_interview", "export_markdown")
    graph.add_edge("export_markdown", END)

    return graph.compile()
