# src/main.py
import logging
from config.config import Config
from src.salesforce import SalesforceAPI
from src.postgres import PostgreSQL
from src.redis_cache import RedisCache


def setup_logging():
    logging.basicConfig(level=Config.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    setup_logging()
    salesforce = SalesforceAPI()
    postgres = PostgreSQL()
    redis_cache = RedisCache()

    # fetching data of conf table from postgres to query data from salesforce 
    table_queries = postgres.fetch_table_queries()
    

    for table_name, query in table_queries:
        # fetching data from salesforce using it's instance
        query_records = salesforce.fetch_data(query)

        # creating table in postgres data in order to save it saperatly
        postgres.create_table(table_name)

        # inserting data in respected table
        postgres.insert_data(table_name, query_records['records'])

        # gettign list of ids from saved data on postgres
        ids = postgres.get_ids_from_db(table_name)

        # Cache fetched records
        redis_cache.set_cache(f"{table_name}_records", str(query_records['records']))

        # deleting data from salesforce
        salesforce.delete_records(ids, table_name)

    # closing postgres connection 
    postgres.close_connection()


if __name__ == "__main__":
    main()
