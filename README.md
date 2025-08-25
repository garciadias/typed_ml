# Introduction to Pydantic and Pandera

## Weekly team meetings KCL - MT-AMIGO

This repository contains a brief introduction to Pydantic and Pandera, two powerful libraries for data validation and settings management in Python.
The work here is designed to show the first steps in using these libraries to validate data structures for machine learning applications.

The slides presentation can be accessed [here](https://emckclac.sharepoint.com/:p:/r/sites/MT-BMEIS-AMIGO/_layouts/15/Doc.aspx?sourcedoc=%7B55b85734-61d1-4c4a-a34a-a026c2c5f8cc%7D&action=edit&wdPreviousSession=4420161c-2222-ff51-3725-e31d62ac60ef).

## Get the data

The dataset we used here was created using the code [here](https://github.com/virginiafdez/xrays_classifier/), and is available on the teams shared folder at `dgx`.

To download the dataset, you can use the following command:

```bash
rsync -av dgx:/nfs/project/AMIGO/XRAYCAT/data/ data
```

## Install the dependencies

```bash
uv sync
```

activate environment:

```bash
source .venv/bin/activate
```

## Run code examples

To run little examples of how Pydantic can be used for data validation, you can use the following commands:

```bash
uv run src/typed_ml/examples/not_safe.py
uv run src/typed_ml/examples/safe.py
```

To create a Pandera schema based on the csv file downloaded in previous step, you can run:

```bash
uv run src/typed_ml/services/get_schema.py
```

To load the data enforcing the schema, you can run:

```bash
uv run src/typed_ml/services/data.py
```
