# Import the driver.
import psycopg2

def create_table(database, user, host, port):
	# Connect to the "bank" database.
	conn = psycopg2.connect(database= 'doppelganger', user= 'test', host= 'localhost', port= 26257)

	# Make each statement commit immediately.
	conn.set_session(autocommit=True)

	# Open a cursor to perform database operations.
	cur = conn.cursor()
	# Create the "accounts" table.
	cur.execute("CREATE TABLE IF NOT EXISTS doppelganger.images (url STRING, hash STRING PRIMARY KEY)")
	# Close the database connection.
	cur.close()
	conn.close()


def add_to_db(database_, user_, host_, port_, url_, hash_):
	# Connect to the "bank" database.
	conn = psycopg2.connect(database=database_, user=user_, host=host_, port=port_)

	# Make each statement commit immediately.
	conn.set_session(autocommit=True)

	# Open a cursor to perform database operations.
	cur = conn.cursor()

	# Insert two rows into the "accounts" table.
	cur.execute("INSERT INTO images (url, hash) VALUES('random', %s)" %hash_)

	# Close the database connection.
	cur.close()
	conn.close()

def find_match_from_db():
	return True

if __name__ == "__main__":
	create_table('doppelganger', 'test', 'localhost', 26257)

	add_to_db('doppelganger', 'test', 'localhost', 26257, "random", "010010101")