# uvws-demo: uv workspaces demo

A simple demo of the new [workspaces][ws] feature in `uv` 0.3.0.

[ws]: https://docs.astral.sh/uv/concepts/workspaces/

## Usage

1. Install the workspace top level package

- It has one dependency, Pydantic

```sh
uv pip install -e .
```

2. Run the CLI entrypoint `greet` which says hello with one optional argument

```sh
$ greet
Hello world from workspaces!
$ greet uv
Hello uv from workspaces!
```
