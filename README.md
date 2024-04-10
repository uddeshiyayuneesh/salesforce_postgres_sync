# Salesforce Postgres Synchronization

This Python script facilitates synchronization between Salesforce and PostgreSQL databases. It fetches data from Salesforce, saves it into PostgreSQL, and provides functionality to delete records from Salesforce.

## Features

- Fetch data from Salesforce based on specified queries.
- Save fetched data to PostgreSQL tables.
- Delete records from Salesforce based on record IDs.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system (version 3.9 or higher).
- Required Python packages installed (see `requirements.txt`).
- Access to both Salesforce and PostgreSQL databases.
- Proper configuration set up for Salesforce and PostgreSQL connections.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Singh-Sg/salesforce_postgres_synchronization.git
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up configuration files for Salesforce (`config.py`) and PostgreSQL (`config.py`) connections.**

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **The script will automatically fetch data from Salesforce, save it to PostgreSQL, and perform any specified operations.**

3. **Optionally, you can set up cron jobs to run the script at regular intervals for automatic synchronization.**

## Configuration

Ensure that you configure the following settings in the `config.py` file:

```python
# Salesforce credentials
SALESFORCE_USERNAME = 'your_salesforce_username'
SALESFORCE_PASSWORD = 'your_salesforce_password'
SALESFORCE_SECURITY_TOKEN = 'your_salesforce_security_token'

# PostgreSQL connection details
POSTGRES_HOST = 'your_postgres_host'
POSTGRES_PORT = 'your_postgres_port'
POSTGRES_DB = 'your_postgres_database'
POSTGRES_USER = 'your_postgres_username'
POSTGRES_PASSWORD = 'your_postgres_password'

# Redis connection details
REDIS_HOST = 'your_redis_host'
REDIS_PORT = 'your_redis_port'
REDIS_PASSWORD = 'your_redis_password'

# set log info
LOG_LEVEL = logging.INFO