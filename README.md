# Gemini API 3.5 Python Project

This is a simple Python project demonstrating how to call the Gemini API version 3.5 to fetch data.

## Requirements

- Python 3.x
- `requests` library (specified in `requirements.txt`)

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Notes

- Replace the base URL and endpoint in `app.py` with the actual Gemini API endpoints and adjust authentication if needed.
- This script currently makes a simple GET request to fetch market data as an example.

