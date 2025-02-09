# HNG Stage 1 Backend Task: Number Classification API

This repository contains the implementation of a public API that classifies a given number and returns interesting mathematical properties about it, along with a fun fact. The API is designed to meet the requirements of the HNG Stage 1 Backend Task.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Technology Stack](#technology-stack)
3. [API Specification](#api-specification)
4. [Setup Instructions](#setup-instructions)
5. [API Documentation](#api-documentation)
6. [Repository Information](#repository-information)
7. [Backlink](#backlink)

---

## Project Description
The goal of this project is to create an API that takes a number as input and returns the following information in JSON format:
- **Number**: The input number.
- **Is Prime**: Whether the number is a prime number.
- **Is Perfect**: Whether the number is a perfect number.
- **Properties**: A list of mathematical properties of the number (e.g., Armstrong, odd, even).
- **Digit Sum**: The sum of the digits of the number.
- **Fun Fact**: A fun fact about the number fetched from the [Numbers API](http://numbersapi.com/#42).

The API is designed to handle GET requests and is deployed to a publicly accessible endpoint. It also includes proper CORS handling to ensure cross-origin requests are supported.

---

## Technology Stack
- **Programming Language/Framework**: Python (Flask)
- **Deployment Platform**: [PythonAnywhere](https://www.pythonanywhere.com/)
- **Version Control**: GitHub

---

## API Specification
### Endpoint
- **Method**: `GET`
- **URL**: `https://eblaze.pythonanywhere.com/api/classify-number?number=<number>`

### Query Parameter
- **number**: The number to classify (must be a valid integer).

### Response Format (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Response Format (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

### Example Usage
```bash
curl -X GET https://eblaze.pythonanywhere.com/api/classify-number?number=371
```

### Response Example
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

## Setup Instructions
### Prerequisites
- Python 3.x installed
- Git installed

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/CaptainAril/HNG_12.git
   cd stage_1
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create an env file using the sample.env as template

4. Run the Flask application:
   ```bash
   ./run.sh # for linux or macOS
   ```

   or 

   ```bash
    python3 -m src.server # for windows
   ```

5. The API will be accessible at `http://127.0.0.1:8000/api/classify-number?number=<number>`.

---

## API Documentation
### Endpoint Details
- **Endpoint**: `/api/classify-number`
- **Method**: `GET`
- **Query Parameter**: `number` (must be a valid integer)
- **Response Format**: JSON
- **Fields**:
  - `number`: The input number.
  - `is_prime`: Boolean indicating if the number is prime.
  - `is_perfect`: Boolean indicating if the number is perfect.
  - `properties`: List of mathematical properties (e.g., Armstrong, odd, even).
  - `digit_sum`: Sum of the digits of the number.
  - `fun_fact`: Fun fact about the number fetched from the Numbers API.

### Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/classify-number?number=371
```

### Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

## Repository Information
- **GitHub Repository**: [https://github.com/CaptainAril/HNG_12](https://github.com/CaptainAril/HNG_12)
- **Visibility**: Public

---

## Backlink
For more information about hiring Python developers, visit:  
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

This README provides a comprehensive guide to understanding, setting up, and using the API. For any questions or issues, please open an issue on the GitHub repository.