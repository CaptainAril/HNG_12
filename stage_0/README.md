# HNG Stage 0 Backend Task: Public API for Basic Information Retrieval

This repository contains the implementation of a public API that retrieves basic information, including the registered email address, current datetime in ISO 8601 format, and the GitHub URL of the project's codebase. The API is designed to meet the requirements of the HNG Stage 0 Backend Task.

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
The goal of this project is to develop a public API that returns the following information in JSON format:
- **Email**: The registered email address used to sign up for the HNG12 Slack workspace.
- **Current Datetime**: The current datetime in ISO 8601 format (UTC).
- **GitHub URL**: The URL of the GitHub repository hosting the project's codebase.

The API is designed to handle GET requests and is deployed to a publicly accessible endpoint. It also includes proper CORS handling to ensure cross-origin requests are supported.

---

## Technology Stack
- **Programming Language/Framework**: Python (Flask)
- **Deployment Platform**: [pythonanywhere](https://pythonanywhere.com/)
- **Version Control**: GitHub

---

## API Specification
### Endpoint
- **Method**: `GET`
- **URL**: `https://eblaze.pythonanywhere.com/api/basic-info/`

### Response Format (200 OK)
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Example Usage
```bash
curl -X GET https://eblaze.pythonanywhere.com/api/basic-info/
```

### Response Example
```json
{
  "email": "john.doe@example.com",
  "current_datetime": "2023-10-05T14:30:00Z",
  "github_url": "https://github.com/johndoe/hng-stage0-backend"
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
   git clone https://github.com/yourusername/hng-stage0-backend.git
   cd stage_0
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
5. The API will be accessible at `http://127.0.0.1:8000/api/basic-info`.

---

## API Documentation
### Endpoint Details
- **Endpoint**: `/api/basic-info`
- **Method**: `GET`
- **Response Format**: JSON
- **Fields**:
  - `email`: Registered email address.
  - `current_datetime`: Current datetime in ISO 8601 format (UTC).
  - `github_url`: GitHub repository URL.

### Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/basic-info
```

### Example Response
```json
{
  "email": "john.doe@example.com",
  "current_datetime": "2023-10-05T14:30:00Z",
  "github_url": "https://github.com/johndoe/hng-stage0-backend"
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