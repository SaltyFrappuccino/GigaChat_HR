import mysql.connector

DATABASE_CONFIG = {
    'host': 'eow.h.filess.io',
    'port': '3307',
    'user': 'gigachat_asleepfrog',
    'password': 'c7db1316db5f9dea0153255c225d003d4d433074',
    'database': 'gigachat_asleepfrog'
}


def get_database_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)
