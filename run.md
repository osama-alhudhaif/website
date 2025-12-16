# Project Setup and Running Instructions

This guide provides the necessary steps to set up the environment and run both the backend (Django) and frontend (React/Vite) components of the website.

## 🚀 Step 1: Initialize the Python Environment

First, you need to create and activate a Python virtual environment to manage project dependencies.

1.  **Create your Venv:** Choose a name for your environment (e.g., `myenv`).
    ```bash
    python -m venv NAME_OF_YOUR_VENV
    ```
    *(Replace `NAME_OF_YOUR_VENV` with your preferred name.)*

2.  **Activate the Venv (Windows/PowerShell):**
    ```bash
    .\NAME_OF_YOUR_VENV\Scripts\activate
    ```
    *(For Linux/macOS, use: `source NAME_OF_YOUR_VENV/bin/activate`)*

3.  **Install Python Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Step 2: Install Node Dependencies

Install the necessary packages for the frontend and concurrency tools.

```bash
npm install 
```

## 🛠️ Step 3: run the backend and frontend
``` bash
npm run dev
```
