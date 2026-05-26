from app.graph.state import ResumeGraphState


class MarkdownExporter:
    def export(self, state: ResumeGraphState) -> str:
        language = state["language"]
        if language == "zh":
            headings = {
                "title": "简历优化结果",
                "analysis": "岗位与匹配分析",
                "versions": "三版优化简历",
                "interview": "面试题预测",
                "warnings": "风险提示",
            }
        else:
            headings = {
                "title": "Resume Optimization Result",
                "analysis": "Role and Fit Analysis",
                "versions": "Three Optimized Resume Versions",
                "interview": "Interview Question Predictor",
                "warnings": "Risk Notes",
            }

        jd = state["jd_analysis"]
        gap = state["gap_analysis"]
        review = state["review"]

        lines: list[str] = [
            f"# {headings['title']}",
            "",
            f"## {headings['analysis']}",
            "",
            f"- Role: {jd.role_title or 'N/A'}",
            f"- Match score: {gap.match_score}/100",
            f"- ATS score: {review.ats_score}/100",
            f"- Language score: {review.language_score}/100",
            "",
        ]

        if gap.strong_matches:
            lines.append("### Strong Matches")
            lines.extend(f"- {item}" for item in gap.strong_matches)
            lines.append("")
        if gap.optimization_suggestions:
            lines.append("### Optimization Suggestions")
            lines.extend(f"- {item}" for item in gap.optimization_suggestions)
            lines.append("")

        lines.append(f"## {headings['versions']}")
        lines.append("")
        for index, version in enumerate(state["resume_versions"], start=1):
            lines.append(f"### {index}. {version.name}")
            lines.append("")
            lines.append(f"Strategy: {version.strategy}")
            lines.append("")
            lines.append(version.resume_markdown.strip())
            lines.append("")

        lines.append(f"## {headings['interview']}")
        lines.append("")
        for index, question in enumerate(state["interview_questions"], start=1):
            lines.append(f"### Q{index}. {question.question}")
            lines.append("")
            lines.append(question.why_it_matters)
            lines.append("")
            if question.answer_framework:
                lines.append("Answer framework:")
                lines.extend(f"- {item}" for item in question.answer_framework)
                lines.append("")
            if question.evidence_to_prepare:
                lines.append("Evidence to prepare:")
                lines.extend(f"- {item}" for item in question.evidence_to_prepare)
                lines.append("")

        warnings = state.get("warnings", [])
        if warnings:
            lines.append(f"## {headings['warnings']}")
            lines.append("")
            lines.extend(f"- {warning}" for warning in warnings)
            lines.append("")

        return "\n".join(lines).strip() + "\n"
