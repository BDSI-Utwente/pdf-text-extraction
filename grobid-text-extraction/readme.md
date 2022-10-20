# Text extraction with GROBID

## How to use

1. Start the containerized GROBID web service: `docker compose up -d`
2. Activate the python environment: `cd client && pipenv shell`
3. Use the CLI tool to parse a folder of pdf documents: `grobid_client --in <dir> --out <dir>`

## Postprocessing

Grobid spits out `.xml` documents containing raw text as well as metadata, the `postprocess.py` script creates `.txt` files with a metadata header in `yaml` format, and the raw text.

4. Postprocess a folder of `.xml` documents: `python postprocess.py <dir>`

Done!