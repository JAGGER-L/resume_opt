from app.graph.state import ResumeGraphState
from app.services.exporter import MarkdownExporter


def export_markdown_node(state: ResumeGraphState, exporter: MarkdownExporter) -> ResumeGraphState:
    return {"markdown_export": exporter.export(state)}
