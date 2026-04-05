# DS / ML / DL / NLP Bootcamp — User Guide

This repository is a **learning workspace**: Jupyter notebooks, small Python apps, and sample data for data science, classical machine learning, deep learning, and NLP. It is **not** a single installable application; you open notebooks and scripts in your editor and run them with Python.

## Prerequisites

- **Python** 3.9 or newer (3.10 works well with the examples here).
- **Git** (to clone the repo).
- A **code editor** with notebook support (VS Code, Cursor, or Jupyter Lab).

Optional but recommended:

- **GPU** with CUDA for some deep learning notebooks (CPU often works, but training is slower).

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd DS_ML_DL_NLP_BOOTCAMP
```

### 2. Create and activate a virtual environment

Using the standard library (macOS/Linux):

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows (Command Prompt):

```bash
python -m venv venv
venv\Scripts\activate
```

If you prefer Conda, see `commands.txt` in this folder for `conda create` / `conda activate` examples.

### 3. Install dependencies

From the **repository root**:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install ipykernel jupyter
```

The root `requirements.txt` covers many notebooks (NumPy, pandas, scikit-learn, TensorFlow 2.15, Flask, Streamlit, NLTK, etc.).

**Extra packages for some notebooks**

- **BERT** (`Deep Learning/BERT/implementation.ipynb`): install PyTorch and Hugging Face Transformers when you reach that notebook, for example:

  ```bash
  pip install torch transformers
  ```

  (Use the [official PyTorch install page](https://pytorch.org/get-started/locally/) if you need a specific CUDA build.)

- **`Deep Learning/project/`**: there is a separate `requirements.txt` inside that folder if you work only in that project.

### 4. Register the environment for Jupyter (optional)

With your venv activated:

```bash
python -m ipykernel install --user --name=ds-ml-bootcamp --display-name="DS ML Bootcamp"
```

Then choose the **“DS ML Bootcamp”** kernel when opening `.ipynb` files.

### 5. Run Jupyter

```bash
jupyter lab
```

Or open any `.ipynb` file in Cursor/VS Code and select your interpreter / kernel pointing at this `venv`.

## Running small apps (not notebooks)

Examples live under `PythonBasics/`:

- **Streamlit**: from `PythonBasics/Streamlit/`, with venv activated:

  ```bash
  streamlit run app.py
  ```

- **Flask**: from `PythonBasics/Flask/flask/` (or the app’s directory, depending on the file you use), run the relevant `app.py` or `main.py` with `python`.

Paths and entry files vary by subfolder; open the `.py` file and run the one that defines the app.

## How to read and navigate the codebase

### Top-level layout

| Folder | What it is |
|--------|------------|
| `PythonBasics/` | Python language fundamentals, data structures, pandas/numpy, SQLite, logging, threading, Streamlit/Flask samples, and `practice/` assignments. |
| `MLCore/` | Classical ML by topic (e.g. regression, logistic regression, trees, ensembles, SVM, clustering, PCA, NLP basics). Each subfolder usually holds one or more `.ipynb` notebooks and sometimes `data/`. |
| `Deep Learning/` | Neural networks with TensorFlow/Keras (e.g. RNN, LSTM, practicals), BERT/Transformers material, and a `project/` folder for end-to-end experiments. |
| `DL/` | Extra bundled material (`The-Grand-Complete-Data-Science-Materials`). |
| `requirements.txt` | Default pip dependencies for most of the repo. |
| `commands.txt` | Quick notes on Conda/venv and Jupyter kernel setup. |

### Suggested order for learners

1. **`PythonBasics/`** — control flow, data structures, file I/O, then **DataAnalysis** (NumPy, pandas, plotting).
2. **`MLCore/`** — pick algorithms in any order, but regression → classification → ensembles → clustering is a common path.
3. **`Deep Learning/Practicals/`** then **SimpleRNN / LSTM / BI-RNN** as you move into sequences.
4. **`Deep Learning/BERT`** and **`Deep Learning/Transformers`** after you are comfortable with tensors and training loops.

### How notebooks are organized

- Most teaching content is in **`.ipynb`** files; **open the notebook** and run cells top to bottom.
- **Data** for a lesson is usually in the same folder or a `data/` subfolder; if a path fails, set your working directory to that notebook’s folder or adjust paths in the first cells.
- Some notebooks download models or corpora (e.g. NLTK, Hugging Face); the first run may need internet access.

### Notes about `Notes/` and `venv/`

- **`venv/`** is listed in `.gitignore`. Create your own virtual environment locally; do not rely on a `venv` folder from Git.
- **`Notes/`** is also ignored by Git in this project. If you do not see it after cloning, that is expected for a fresh clone; course PDFs or duplicate notebooks may exist only on the machine where they were added.

## Troubleshooting

- **Import errors**: install missing packages with `pip install <package>` or add them to a personal `requirements-local.txt`. Check the notebook’s import cell first.
- **TensorFlow / GPU**: TensorFlow 2.15 is pinned in `requirements.txt`. GPU support depends on your OS and drivers; CPU-only installs are fine for learning.
- **Wrong Python**: ensure the terminal where you run `pip`/`jupyter` is the same environment where you installed packages (`which python` / `python -c "import sys; print(sys.executable)"`).

This README is for **using and studying** the materials. For changes to the repo itself, use your usual Git workflow (branches, commits, pull requests) as your team prefers.
