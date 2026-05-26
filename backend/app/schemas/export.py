from pydantic import BaseModel, ConfigDict


class MarkdownExport(BaseModel):
    model_config = ConfigDict(extra="ignore")

    filename: str
    content: str
