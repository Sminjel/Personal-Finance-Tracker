# Personal Finance Tracker

## Project Overview

The Personal Finance Tracker is a Python application designed to help users manage their income, expenses, and savings. 
It offers functionalities to add transactions, categorize expenses, generate financial reports, and visualize data. 
The project also demonstrates file handling for persisting data and includes error handling to ensure robust operation.

## Features

- **Add Income**: Allows users to add income transactions.
- **Add Expense**: Allows users to add expense transactions.
- **Generate Report**: Provides a summary of income, expenses, and savings, with optional visualization.
- **Data Persistence**: Saves transactions to a file and loads them when the application starts.
- **Error Handling**: Includes mechanisms to handle invalid inputs and file-related exceptions.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Matplotlib (optional for data visualization).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/smangelent@gmail.com/personal-finance-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd personal-finance-tracker
    ```

3. Install required packages (if any):

    ```bash
    pip install matplotlib
    ```

### Usage

1. Run the application:

    ```bash
    python file_handling_assignment.py
    ```

2. Follow the prompts to add income, add expenses, and generate reports.

### Code Explanation

- **Step 1: Print Statement**: Displays a welcome message and instructions.
- **Step 2: Variables**: Defines variables to store income, expenses, savings, and transactions.
- **Step 3: Data Types**: Uses appropriate data types for storing financial data.
- **Step 4: Input and Output**: Manages user input and output.
- **Step 5: Functions**: Implements functions to add income, add expenses, and calculate savings.
- **Step 6: Conditional Statements**: Provides a menu for user interaction.
- **Step 7: File Handling**: Handles saving and loading transaction data from a file.
- **Step 8: Categories and Reports**: Generates and displays financial reports.
- **Step 9: Data Visualization**: (Optional) Creates visual representations of financial data.
- **Step 10: Error Handling and Validation**: Ensures robustness with error handling.
- **Step 11: Test and Refine**: Tests the application and refines based on feedback.
- **Step 12: Conclusion**: Displays a closing message.

## JSON Introduction

JSON (JavaScript Object Notation) is used for data interchange. The project uses JSON to save and load transaction data.

- **JSON Syntax**: Key-value pairs enclosed in curly braces `{}`, with keys as strings and values as strings, numbers, arrays, or nested objects.
- **Python and JSON**: Python’s `json` library is used for serializing and deserializing JSON data.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by modern financial tracking tools.
- Uses Matplotlib for optional data visualization.
