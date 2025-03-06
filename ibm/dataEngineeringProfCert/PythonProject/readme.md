# Karmak-Coupa Integration

This project integrates the Coupa procurement system with the Karmak accounting system, automating the process of transferring approved invoices from Coupa to Karmak.

## Overview

The application is an Azure Function that runs on a schedule to:

1. Fetch approved invoices from Coupa that haven't been exported yet
2. Process and format the invoice data for Karmak
3. Post the formatted data to Karmak's API
4. Mark the successfully posted invoices as exported in Coupa
5. Log all API operations to a database for tracking and troubleshooting

## Project Structure

```
karmak-coupa-integration/
├── main.py               # Main entry point and Azure Function definition
├── config.py             # Configuration, constants, and environment variables
├── database.py           # Database operations for API logging
├── coupa_api.py          # Coupa API integration
├── karmak_api.py         # Karmak API integration
├── requirements.txt      # Project dependencies
├── data/                 # Directory for database files
│   └── api_logs.db       # SQLite database for API logging
└── .env                  # Environment variables (not in version control)
```

## Module Descriptions

### main.py

The main entry point for the Azure Function. This file:

- Registers the Azure Function
- Coordinates the overall flow of operations
- Calls the appropriate module functions in sequence
- Logs the overall execution

### config.py

Centralizes all configuration and constants:

- Loads and validates environment variables
- Defines constants used across the application
- Contains branch mapping and account lists
- Configures the logging system

### database.py

Handles database operations for logging API calls:

- Creates and initializes the SQLite database
- Defines the schema for API logging
- Provides functions to log API calls with detailed information

### coupa_api.py

Contains all Coupa API related functionality:

- Authentication with Coupa via OAuth2
- Retrieving approved invoices
- Processing invoice data for Karmak
- Marking invoices as exported in Coupa

### karmak_api.py

Contains all Karmak API related functionality:

- Posting invoice data to Karmak's API
- Handling API responses and errors
- Tracking successfully posted invoices

## Database Schema

The application logs all API operations to a SQLite database with the following schema:

**Table: api_logs**
| Column | Type | Description |
|----------------|---------|----------------------------------------------|
| id | INTEGER | Primary key |
| timestamp | TEXT | When the API call was made |
| source_file | TEXT | File that made the API call |
| api_call | TEXT | Function or endpoint name |
| status | TEXT | Success, error, or other status |
| request_data | TEXT | JSON string of request data |
| response_data | TEXT | JSON string of response data |
| error_message | TEXT | Any error message |
| execution_time | REAL | Time taken to execute the call in seconds |

## Installation and Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the required environment variables:
   ```
   COUPA_TOKEN_URL=<your_token_url>
   COUPA_SAND_CLIENT_ID=<your_client_id>
   COUPA_SAND_CLIENT_SECRET=<your_client_secret>
   COUPA_SAND_URL=<your_coupa_api_url>
   KARMAK_DEV_ACCT_NUMBER=<your_karmak_account>
   KARMAK_DEV_KEY_2=<your_karmak_api_key>
   ```

## Deployment

To deploy this function to Azure:

1. Make sure you have the Azure Functions Core Tools installed
2. Run the following commands:

```
func azure functionapp publish <YourFunctionAppName>
```

## Monitoring and Troubleshooting

The application logs all operations in two ways:

1. **Standard Logging**: Logs are written to `karmak_coupa_integration.log`
2. **Database Logging**: Detailed API call information is stored in `data/api_logs.db`

To review logs:

- Check the log file for general operation information
- Query the database for detailed API call information:
  ```sql
  SELECT * FROM api_logs ORDER BY timestamp DESC LIMIT 100;
  ```
- Filter for errors:
  ```sql
  SELECT * FROM api_logs WHERE status = 'error' ORDER BY timestamp DESC;
  ```

## Environment Variables

| Variable                 | Description                        |
| ------------------------ | ---------------------------------- |
| COUPA_TOKEN_URL          | URL for Coupa OAuth token requests |
| COUPA_SAND_CLIENT_ID     | Coupa sandbox client ID            |
| COUPA_SAND_CLIENT_SECRET | Coupa sandbox client secret        |
| COUPA_SAND_URL           | Base URL for Coupa sandbox API     |
| KARMAK_DEV_ACCT_NUMBER   | Karmak developer account number    |
| KARMAK_DEV_KEY_2         | Karmak API subscription key        |

## Function Schedule

The Azure Function runs on a schedule defined in `main.py`:

- Schedule: Every 5 minutes (`0 */5 * * * *`)
- Also runs on startup (`run_on_startup=True`)

## Error Handling

The application implements robust error handling:

- All API calls are wrapped in try/except blocks
- Errors are logged to both the log file and database
- Failures in one part of the process don't stop the entire execution
- Detailed error information is recorded for troubleshooting

## API Flow

### 1. Coupa to Karmak Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Fetch      │    │  Process    │    │  Post to    │
│  Coupa      │───>│  Invoice    │───>│  Karmak     │
│  Invoices   │    │  Data       │    │  API        │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             v
                                      ┌─────────────┐
                                      │  Mark as    │
                                      │  Exported   │
                                      │  in Coupa   │
                                      └─────────────┘
```

### 2. API Logging Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  API Call   │    │  Format     │    │  Store in   │
│  Execution  │───>│  Log Data   │───>│  SQLite     │
│             │    │             │    │  Database   │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Best Practices Implemented

1. **Modular Design**: Each component is isolated in its own file
2. **Error Handling**: Robust error handling throughout the code
3. **Logging**: Comprehensive logging for troubleshooting
4. **Configuration Management**: Centralized configuration
5. **Code Documentation**: Functions have descriptive docstrings
6. **Database Logging**: Detailed API operation tracking
7. **Function Purity**: Functions focus on single responsibilities
8. **Environment Variables**: Sensitive information stored in environment variables
