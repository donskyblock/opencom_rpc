# opencom-rpc

`opencom-rpc` is a small Python client for the OpenCom RPC server.

It provides:

- `OpenComRPCClient` for talking to the local OpenCom RPC endpoints
- `Activity` and `ActivityButton` models for building payloads

## Installation

```bash
python -m pip install opencom-rpc
```

## Usage

```python
from opencom_rpc import Activity, OpenComRPCClient

activity = Activity(
    name="Listening to music",
    details="Example Track",
    state="Example Artist",
)

with OpenComRPCClient() as client:
    client.set_activity(activity)
```

## Local development

This repository also includes a top-level `main.py` script used for local media bridge experiments. It is not part of the package itself.

For local development:

```bash
python -m pip install -e .
```

## Build

Install the packaging tools if needed:

```bash
python -m pip install build twine
```

Build source and wheel distributions with:

```bash
python -m build
```

This creates files in `dist/`.

## Upload

Upload to PyPI with Twine:

```bash
python -m twine upload dist/*
```

For TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```
