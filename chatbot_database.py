import sqlite3
import json
from datetime import datetime

timeframe = '2005-12'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))

def create_table():
	connection.execute(""" CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY,
				 comment_id TEXT UNIQUE, parent TEXT, subreddit TEXT, unix INT, score INT) """)

def format_data(data):
	data = data.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"',"'")
	return data

def find_parent(pid):
	try:
		sql = "SELECT comment from parent_reply where comment_id= '{}' LIMIT 1".format(pid)
		c.execute(sql)
		result = c.fetchone()
		if result != None:
			return result[0]
		else: return False
	except Exception as e:
		return False

if __name__ == '__main__':
	create_table()
	row_counter = 0
	paired_rows = 0

	with open("D:\git\chatbot_with_python\RC_2005-12".format(timeframe.split('-')[0], timeframe), buffering=1000) as f:
		for row in f:
			row_counter += 1
			row = json.loads(row)
			print(row)
			parent_id = row['parent_id']
			body = format_data(row['body'])
			created_utc = row['created_utc']
			score = row['score']
			subreddit = row['subreddit']

			parent_data = find_parent(parent_id)

