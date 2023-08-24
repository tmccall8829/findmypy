from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from models.package import PackageURL
from utils.api import FindMyPy

app = FastAPI()


@app.get("/")
def index():
    return (
        "Append a PyPI package name to this base URL to get their GitHub Project URL."
    )


@app.get("/{package_name}", response_model=PackageURL)
def return_package_github_url(package_name: str):
    url = FindMyPy.get_github_url(package_name=package_name)

    if not url:
        raise HTTPException(
            status_code=404, detail=f"Github repo URL for {package_name} not found."
        )

    return RedirectResponse(url)
