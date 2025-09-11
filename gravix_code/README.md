# Gravix Layer API Example

This project demonstrates how to use the Gravix Layer API with a Python script.

## Setup

### 1. Setting up a Virtual Environment (Recommended)

It is recommended to use a virtual environment to manage the project's dependencies.

**Create a virtual environment:**
```bash
python3 -m venv gravix
```

**Activate the virtual environment:**

*   **On Windows:**
    ```bash
    .\gravix\Scripts\activate
    ```
*   **On macOS and Linux:**
    ```bash
    source gravix/bin/activate
    ```

### 2. Create a `.env` file

Create a file named `.env` in the root of the project.

### 3. Add your API key

Open the `.env` file and add your Gravix Layer API key as follows:

```
GRAVIXLAYER_API_KEY=your_api_key_here
```

### 4. Install dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the `llm_usedeploy.py` script to send a request to the Gravix Layer API:

```bash
python llm_usedeploy.py
```