# uvws-demo: uv workspaces demo

A simple demo of the new [workspaces][ws] feature in `uv` 0.3.0.

[ws]: https://docs.astral.sh/uv/concepts/workspaces/

## Usage

0. (Optional) Create a conda environment to encapsulate the package installation

```sh
conda create -n uvwsdemo python=3.10 -y && conda activate uvwsdemo
```

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

3. Run the CLI entrypoint `two_plus_two` which adds 2+2 = 4, using the workspace package `tpt` (from
   `packages/tpt`)

```sh
$ two_plus_two
4
```
