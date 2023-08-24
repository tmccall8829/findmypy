from fastapi import FastAPI
from pydantic import BaseModel
from utils.api import FindMyPy

app = FastAPI()


class PackageURL(BaseModel):
    github_url: str | None


@app.get("/")
def index():
    return (
        "Append a PyPI package name to this base URL to get their GitHub Project URL."
    )


@app.get("/{package_name}", response_model=PackageURL)
def return_package_github_url(package_name: str):
    url = FindMyPy.get_github_url(package_name=package_name)

    return {"github_url": url}
