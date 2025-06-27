# The Webonomicon

This tutorial is a short introduction to web programming using modern tools and practices
for data scientists who are comfortable using Python
but have never built interactive websites before.
All of the material is available under [open licenses](./LICENSE.md),
and contributions through our [GitHub repository][repo] are welcome.
All contributors are required to respect our [Code of Conduct](./CODE_OF_CONDUCT.md).

> **Please note:** this tutorial is still being outlined.
> Most sections will have additional examples (and much more explanation)
> before learners encounter it.
> Suggestions and help are greatly appreciated.

## Learner Persona

-   Sabina, 28, has a master's degree in animal physiology
    and now works for a mid-sized veterinary pharmaceutical company.
-   She learned a bit of R in an undergraduate biostatistics course,
    then picked up Python in grad school.
    She spends several hours a week analyzing data with [Pandas][pandas]
    and visualizing it with [Plotly Express][plotly-express],
    and is comfortable with basic Git commands.
-   Sabina recently became responsible for maintaining a dashboard application built with [Dash][dash].
    She believes a better understanding of how web applications work in general
    will help her debug and extend it.
-   Sabina has tried doing asynchronous online courses a couple of times,
    but strongly prefers learning in real time with other people.

## Syllabus

<div class="chapters" markdown="1">

1.  [Introduction](./01_intro/index.md): what we will learn, how to set up, and the data we will use
1.  [HTTP](./02_http/index.md): how browsers and servers talk to each other
1.  [A Server](./03_server/index.md): building a server with [Flask][flask]

</div>

##  Appendices

<div class="appendices" markdown="1">

1.  [Data Generation](./datagen/index.md)
1.  [License](./LICENSE.md)
1.  [Code of Conduct](./CODE_OF_CONDUCT.md)
1.  [Contributing](./CONTRIBUTING.md)
1.  [Bibliography](./bibliography.md)
1.  [Glossary](./glossary.md)

</div>

## Technologies

| Package                          | Purpose           |
| -------------------------------- | ----------------- |
| [Alpine.js][alpine]              | dynamic HTML      |
| [Beautiful Soup][bs4]            | HTML manipulation |
| [htmx][htmx]                     | interaction       |
| [httpx][httpx]                   | HTTP              |
| [Polars][polars]                 | tabular data      |
| [pytest][pytest]                 | testing           |
| [SQLite][sqlite]                 | database          |

[alpine]: https://alpinejs.dev/
[bs4]: https://beautiful-soup-4.readthedocs.io/
[flask]: https://flask.palletsprojects.com/
[htmx]: https://htmx.org/
[httpx]: https://www.python-httpx.org/
[polars]: https://pola.rs/
[pytest]: https://docs.pytest.org/
[sqlite]: https://www.sqlite.org/
