from pydantic import BaseModel


class PackageURL(BaseModel):
    github_url: str | None
