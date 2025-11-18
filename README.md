# My Awesome Python Calculator

This project contains a simple command-line calculator application built with Python and managed using `uv` for dependency management.

## Features

*   Basic arithmetic operations: addition, subtraction, multiplication, and division.
*   User-friendly command-line interface.
*   Error handling for invalid operations and division by zero.

## Setup and Installation

To set up and run this calculator application, follow these steps:

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd calculator_app
    ```
    (Replace `<YOUR_REPOSITORY_URL>` with the actual URL of your GitHub repository, e.g., `https://github.com/bilalwebs/python-calculator.git`)

2.  **Navigate into the project directory:**
    ```bash
    cd calculator_app
    ```

3.  **Create a `uv` virtual environment:**
    ```bash
    uv venv
    ```
    This will create a virtual environment named `.venv` in your project directory.

4.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    Activating the virtual environment ensures that any Python packages you install are isolated to this project.

## How to Run the Calculator

Once the virtual environment is activated, you can run the calculator application:

```bash
python main.py
```

The calculator will prompt you to enter an operation (add, subtract, multiply, divide) and two numbers. You can type `quit` to exit the calculator.

## Deactivating the Virtual Environment

When you are finished using the calculator and want to exit the virtual environment, simply run:

```bash
deactivate
```
