import os
import psycopg2
import sqlite3 as lite

def check_result_send_mess():
    '''
    This function looks up the values stored in the SQL database
    and compares them to the crawled jobs and sends out any jobs
    not in the db to the telegram bot
    Args: None
    Returns: None
    '''
