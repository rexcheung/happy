import sqlite3


class RowBean:
	name = ''
	type = ''
	not_null = True

	def __init__(self, name, type, not_null):
		self.name = name
		self.type = type
		self.not_null = not_null


conn = sqlite3.connect("bt.db")
cursor = conn.cursor()


def buildSQL(table_name, rows):
	sql = 'CREATE TABLE IF NOT EXISTS '
	sql += table_name
	sql += '(_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'

	for i in range(0, len(rows)):
		row = rows[i]
		not_null = ''
		if row.not_null:
			not_null = 'NOT NULL'
		text = row.name + ' ' + row.type + ' ' + not_null + ', '
		sql += text

	sql = sql[0: len(sql) - 3]
	sql += ')'
	return sql


def insert(table, title, url, content):
	sql = 'INSERT INTO '
	sql += table
	sql += ' values (?,?,?,?,?)'
	cursor.execute(sql, (None, title, url, content, None))
	conn.commit()


def main():
	title = RowBean('title', 'TEXT', True)
	url = RowBean('url', 'TEXT', True)
	content = RowBean('content', 'TEXT', True)
	time = RowBean('time', 'INTEGER', False)

	rows = []
	rows.append(title)
	rows.append(url)
	rows.append(content)
	rows.append(time)

	sql = buildSQL('bt1024', rows)
	cursor.execute(sql)

	insert('bt1024', 'test_title11', 'testUrls22', 'testContent33')


main()
