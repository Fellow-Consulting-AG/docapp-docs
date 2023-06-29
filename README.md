
[![Netlify Status](https://api.netlify.com/api/v1/badges/627053ba-8a81-4692-96cb-e57b24979bce/deploy-status)](https://app.netlify.com/sites/aquamarine-taffy-499fd7/deploys)

# DocBits (DOC²) Docs

This repository hosts the documentation for [polydocs](https://polydocs.io/), an extendable workflow automation tool which enables you to connect anything to everything via its open, The documentation is live at [docs.polydocs.io](https://docs.polydocs.io/).


## Previewing and building the documentation locally

### Prerequisites

* Python 3.8 or above
* We recommend using a virtual environment when working with Python, such as [venv](https://docs.python.org/3/tutorial/venv.html).

### Steps

```bash
git clone https://github.com/Fellow-Consulting-AG/docapp-docs/
cd docapp-docs
pip install -r requirements.txt

pip install mkdocs-material
# Serve a local preview
mkdocs serve
# Or build
mkdocs build
```

