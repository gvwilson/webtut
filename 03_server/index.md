# A Server

## Overview

<figure id="server-concept-map">
  <img src="server_concept_map.svg" alt="concept map of Flask server"/>
  <figcaption>Figure 1: Concept Map</figcaption>
</figure>

<p id="terms"></p>

## Outline

-   [`server_hello.py`](./server_hello.py): return HTML

```{data-file="server_hello.py"}
"""Hello server."""

from flask import Flask

HELLO = """\
<html>
<body>
<h1>Hello</h1>
</body>
</html>
"""


app = Flask("hello")


@app.route("/")
def root():
    return HELLO
```

-   Go to http://127.0.0.1:5000 to view (5000 being [Flask][flask]'s default port)
    -   Or use [`fetch.py`](./fetch.py) to fetch and display data

```{data-file="fetch.py"}
"""Fetch HTML from URL and display."""

import argparse
import httpx


HOST = "127.0.0.1"
PORT = 5000
RESOURCE = "/"


def main():
    """Main driver."""
    opt = parse_args()
    url = f"http://{opt.host}:{opt.port}{opt.resource}"
    response = httpx.get(url)
    print(response.status_code)
    print(response.text)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default=HOST, help="server address")
    parser.add_argument("--port", type=int, default=PORT, help="server port")
    parser.add_argument("--resource", type=str, default=RESOURCE, help="resource path")
    return parser.parse_args()


if __name__ == "__main__":
    main()
```

-   [`server_func.py`](./server_func.py) creates the application and configures [routes](g:route) in a function
    -   Get path to staff CSV from `DATA` [environment variable](g:env-var)
    -   Read and convert to HTML with [PrettyTable][prettytable]

> **CORS**
>
> -   Ignore `CORS` for now
> -   Allows the browser to fetch resources from sites other than the one the page came from
> -   Permission needed to prevent some kinds of attacks (which we will discuss later).

```{data-file="server_func.py:keep"}
def create_app():
    """Build application and configure routes."""
    app = Flask("func")
    CORS(app)

    @app.get("/")
    def root():
        """Display home page as HTML."""
        return util.as_html()

    return app
```

-   [`server_routes.py`](./server_routes.py) configures several routes
    -   Use [query parameters](g:query-parameter) or [URL fragments](g:url-fragment)
        to select individual row or column
    -   Use [Polars][polars] to get a [dataframe](g:dataframe) and [Flask][flask] to convert to JSON

```{data-file="server_routes.py:keep"}
def create_app():
    """Build application and configure routes."""
    app = Flask("routes")
    CORS(app)

    @app.get("/")
    def root():
        return util.as_html()

    @app.get("/col/<name>")
    def column(name):
        data = util.as_dataframe()
        return jsonify(list(data[name]))

    @app.get("/row/<staff_id>")
    def row(staff_id):
        staff_id = int(staff_id)
        data = util.as_dataframe()
        row = data.filter(pl.col("staff_id") == staff_id).row(0, named=True)
        return jsonify(row)

    return app
```

-   Some endpoints return HTML, some return JSON
    -   No endpoint should return both
-   [`server_err.py`](./server_err.py) handles errors
    -   Check row and column and raise exception if not there
    -   Rely on [Flask][flask] to handle nonexistent routes

```{data-file="server_err.py:keep"}
def create_app():
    """Build application and configure routes."""
    app = Flask("err")
    CORS(app)

    @app.get("/")
    def root():
        return util.as_html()

    @app.get("/col/<name>")
    def column(name):
        try:
            data = util.as_dataframe()
            return jsonify(list(data[name]))
        except Exception as exc:
            abort(util.HTTP_400_BAD_REQUEST, str(exc))

    @app.get("/row/<staff_id>")
    def row(staff_id):
        try:
            staff_id = int(staff_id)
            data = util.as_dataframe()
            row = data.filter(pl.col("staff_id") == staff_id).row(0, named=True)
            return jsonify(row)
        except Exception as exc:
            abort(util.HTTP_400_BAD_REQUEST, str(exc))

    return app
```
