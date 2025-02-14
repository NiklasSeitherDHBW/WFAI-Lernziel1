# WFAI-Lernziel 1

This project is designed to download and analyze papers from arXiv in AI and ML related fields to derive trends and discuss social implications. It includes Jupyter notebooks for data analysis and visualization.

## Contributors
- Yannick Königstein (9502377)
- Niklas Seither (4253802)

## Project Structure
- **.devcontainer/**: Contains the configuration for the development container.
- **arxiv_donwload.ipynb**: Jupyter notebook for downloading papers from arXiv.
- **ausarbeitung.ipynb**: Jupyter notebook for data analysis and visualization.
- **complete_arxiv_papers.csv**: CSV file containing the downloaded papers' metadata.
- **requirements.txt**: List of Python dependencies.

## Getting Started

### Prerequisites

- Docker (optional for using devcontainers)
- Python 3.11

### Setup

1. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

- Run [arxiv_donwload.ipynb](arxiv_download.ipynb) to download papers from arXiv.
- Run [ausarbeitung.ipynb](ausarbeitung.ipynb) to analyze and visualize the data.