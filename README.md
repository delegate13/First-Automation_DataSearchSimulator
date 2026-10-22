# Data Search Simulator

A Python console application that demonstrates a simple search workflow using
a small in-memory dataset. It validates search input, simulates retrieval with
a short delay, performs a case-insensitive search across record fields, and
prints a result summary.

## Requirements

- Python 3.9 or newer
- No third-party packages; all functionality uses the Python standard library

## Run the application

Open the `First Automation_DataSearchSimulator` project in PyCharm, then run
`main.py`. Alternatively, open a terminal in this directory and run:

```powershell
python main.py
```

Enter a word or phrase when prompted. Blank input is rejected and the
application continues prompting until a search term is provided.

## Project files

- `main.py` starts the application and coordinates the workflow.
- `data.py` stores ten mock records in the `RECORDS` constant.
- `search.py` provides case-insensitive substring search across record fields.
- `utils.py` contains the welcome display, input validation, delay, and output
  helpers.
- `requirements.txt` documents that no external dependencies are required.
