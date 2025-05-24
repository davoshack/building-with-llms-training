# Building software on top of Large Language Models

## Prerequisites

If you are attending this tutorial you will need a **laptop with a browser** and a **GitHub account**. The tutorial can be entirely completed using [GitHub Codespaces](https://github.com/features/codespaces), a free online development environment.

If you would prefer to run everything on your own machine you will need a **Python 3.9 or higher** local development environment with the ability to create a virtual environment and install packages using `pip`.

You can pre-install the packages we will be using like this:

```bash
mkdir building-with-llms
cd building-with-llms
python -m venv venv
venv/bin/pip install -r requirements.txt
```

## Workshop description

Large Language Models such as GPT-4o, Claude and Google Gemini provide APIs that can be used to develop features that were almost impossibly difficult to build in the past, spanning areas that include human language understanding, image recognition and structured data extraction.

Building software that uses these APIs reliably and responsibly is a topic with a great deal of depth and a lot of hidden traps.

In this workshop we'll explore a range of proven techniques for building useful software on top of this wildly powerful but unreliable substrate.

Topics we will cover include:

* A review of the best currently available models
* Using multi-modal LLMs to analyze images, audio and video
* Use-cases that LLMs can be effectively applied to
* How to access the most capable models via their various APIs
* Prompt engineering
* Retrieval Augmented Generation (RAG)
* LLM tool usage
* Effective LLM Workflows


## Syllabus

- [Setup](docs/setup.md)
- [Prompting with LLM](docs/prompting-with-llm.md)
- [Prompting with Python](docs/prompting-with-python.ipynb)
- [Structured data extraction](docs/structured-data-extraction.md)
- [Structured data extraction with pydantic](docs/structured_data_with_pydantic.py)
- [Semantic search and RAG](docs/semantic-search-and-rag.md)
- [Tool usage](docs/tools.md)
- [Effective LLM Workflows](docs/effective-llm-workflows/README.md)


## Presentation
- [Slides](slides.pdf)