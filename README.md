# Multi-Language Invoice Extractor

The Multi-Language Invoice Extractor is an application that uses Google Gemini Pro's large language model (LLM) to process and extract relevant information from invoices written in multiple languages. This powerful tool streamlines the invoice processing workflow by automatically parsing invoices and providing structured data for further processing.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

The Multi-Language Invoice Extractor leverages the advanced capabilities of Google Gemini Pro's LLM to understand and extract information from invoices written in different languages. The application automatically processes invoices and provides structured data, saving time and reducing manual effort.

## Features

- **Multi-Language Support**: Extracts information from invoices written in multiple languages.
- **Invoice Parsing**: Parses invoices and extracts relevant data such as invoice number, date, items, quantities, and totals.
- **Structured Data Output**: Provides extracted data in a structured format for easy integration into other systems.
- **User-Friendly Interface**: Offers an intuitive interface for uploading and processing invoices using Streamlit.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Libraries**: The project requires the following Python libraries:
    - `streamlit`: For the web interface.
    - `google-generativeai`: For using Google Gemini Pro's LLM.
    - `python-dotenv`: For managing environment variables.
    - `langchain`: For natural language processing and interaction.
    - `chromadb`: For managing data storage and retrieval.
    - `PyPDF2`: For PDF file handling and parsing.

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:

    ```bash
    cd multi-language-invoice-extractor
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Google Gemini Pro**: Set up your API access to Google Gemini Pro's LLM.

## Usage

1. **Prepare your invoices**: Collect the invoices you wish to process.
2. **Run the application**:

    ```bash
    streamlit run app.py
    ```

3. **Upload invoices**: Use the application's interface to upload invoices you want to process.
4. **View extracted data**: Review the extracted data in the application's output.

## License

This project is licensed under the Apache-2.0 License.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any features, improvements, or bug fixes.

## Contact

For any inquiries or support, please [contact us](mailto:yashraj3376@gmail.com).

Happy extracting!
