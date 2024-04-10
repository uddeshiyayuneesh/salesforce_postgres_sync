# src/redis_cache.py
import redis
import logging
from config.config import Config

class RedisCache:
    def __init__(self):
        self.connection = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            password=Config.REDIS_PASSWORD
        )
        self.logger = logging.getLogger(__name__)

    def set_cache(self, key, value):
        try:
            self.connection.set(key, value)
        except Exception as e:
            self.logger.error(f"Error setting cache in Redis for key {key}: {str(e)}")

    def get_cache(self, key):
        try:
            return self.connection.get(key)
        except Exception as e:
            self.logger.error(f"Error getting cache from Redis for key {key}: {str(e)}")
            return None
