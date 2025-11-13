# Simple Flask app (Docker-ready)

This repository contains a tiny Flask application with a test, a Dockerfile, and a GitHub Actions CI workflow.

Files added:
- `requirements.txt` — Python dependencies
- `app.py` — minimal Flask app
- `test.py` — pytest test for the root endpoint
- `Dockerfile` — builds a container image running the app with Gunicorn
- `.dockerignore` — files to ignore when building the image
- `.github/workflows/ci.yml` — GitHub Actions workflow to run tests

Quick start (locally):

1. Create a virtual environment and activate it (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
python app.py
```

4. Run tests:

```bash
pytest -q
```

Docker:

Build an image:

```bash
docker build -t simple-flask:latest .
```

Run the container:

```bash
docker run -p 8080:8080 simple-flask:latest
```

CI:

The included GitHub Actions workflow runs the test suite on push and pull requests.

Notes:
- This is intentionally minimal. If you want environment variables, config, or more robust testing, I can add them.
