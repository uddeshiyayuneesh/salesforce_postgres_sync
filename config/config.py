# config/config.py
import logging


class Config:
    SALESFORCE_USERNAME = "your-username-password"
    SALESFORCE_PASSWORD = "your-salesforce-password"
    SALESFORCE_SECURITY_TOKEN = "your-salesforce-sercurity-token"

    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"
    POSTGRES_DB = "sfdb"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "root"

    REDIS_HOST = "your_redis_host"
    REDIS_PORT = "your_redis_port"
    REDIS_PASSWORD = "your_redis_password"

    LOG_LEVEL = logging.INFO
