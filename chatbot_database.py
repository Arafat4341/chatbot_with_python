import sqlite3
import json
from datetime import datetime

timeframe = '2005-12'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))

def create_table():
	c.execute(""" CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY,
				 comment_id TEXT UNIQUE, parent TEXT, subreddit TEXT, unix INT, score INT) """)

if __name__ == '__main__':
	create_table()
	row_counter = 0
	paired_rows = 0

	with open("D:\git\chatbot_with_python\RC_2005-12".format(timeframe.split('-')))