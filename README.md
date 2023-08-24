# FindMyPy
Inspired by tools like https://gem.wtf/ and http://ghub.io/ for quickly redirecting to the repository of a ruby gem or npm package, but this time for Python packages.

## Example
```bash
# start up the FastAPI endpoint with gunicorn:
$ cd src && gunicorn --bind :8829 \
--workers 1 \
--worker-class uvicorn.workers.UvicornWorker \
--threads 8 \
--timeout 0 \
--log-level=info \
app:app

# then, in a new terminal:
$ curl -XGET localhost:8829/p/python-openetl
>>> {"github_url":"https://github.com/tmccall8829/python-openetl"}
```
