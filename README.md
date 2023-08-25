# FindMyPy 🥧🐍🕵️
Inspired by tools like https://gem.wtf/ and http://ghub.io/ for quickly redirecting to the repository of a ruby gem or npm package, but this time for Python packages.

## How It Works
* Append a PyPI package to findmypy.io/ to be redirected to the package's Github repo (if it has one).
* This is done by:
    * Calling pypi's `/json` API route to get a payload of pypi package info
    * If there's a github URL listed under `homepage` or `repository` links, it'll redirect you
    * Otherwise, it'll just take you to the pypi project homepage
* If you just go to findmypy.io, you'll be redirected here -- because who builds frontends anyways?

## Examples
* [pandas](https://findmypy.io/pandas)
* [fastapi](https://findmypy.io/fastapi)
* [flask](https://findmypy.io/flask)

## CLI usage
```bash
# start up the FastAPI endpoint with gunicorn:
$ cd src && gunicorn --bind :8829 \
--workers 1 \
--worker-class uvicorn.workers.UvicornWorker \
--threads 2 \
--timeout 0 \
--log-level=info \
app:app

# then, in a new terminal:
$ curl -XGET localhost:8829/p/python-openetl
>>> {"github_url":"https://github.com/tmccall8829/python-openetl"}
```
