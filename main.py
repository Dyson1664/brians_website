# Given the names and grades for each student in a class of  students, store them in a nested list and
# print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.


# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# grades = []
# for g in python_students:
#     grades.append(g[1])
#
# remove_duplicates = sorted(list(set(grades)), reverse=True)
# print(remove_duplicates)
#
# second_lowest_score = remove_duplicates[2:3]
# print(second_lowest_score)
# a = 0
# for i in second_lowest_score:
#     a = i
# print('&&&&&&&&&&&&&&&&&&&&&&&')
# print(a)
# names_list = []
# for list in python_students:
#     print(list)
#     print(list[1])
#     if list[1] == a:
#
#         names_list.append(list)
#
#
# print(names_list)
# names_list.sort()
# for name in names_list:
#     print(name[0])

# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# grades = []
#
# python_students.sort(key=lambda x: x[1], reverse=True)
# print(python_students)
#
# second_lowest = [score[1] for score in python_students]
# sec = sorted(list(set(second_lowest)), reverse=True)
# final_sec = sec[2:3][0]
# print(final_sec, '***************8')
#
# secs = sorted([name for name in python_students if name[1] == final_sec])
# for name in secs:
#     print(name[0])
#
#
# list = [1,2,3,4,5]
#
# new_string = ' '.join(map(str, list))
# print(new_string)

# lst = ['Hello', 'world', 'Python', 'is', 'awesome']
# print(' '.join(lst))

# # List of tuples
# lst = [(1, 'one'), (2, 'two'), (3, 'three')]

# # Convert each tuple to a string and join them with a comma and space
# result = ', '.join(map(str, lst))

# # Print the result
# print(type(result))
# print(result)

import sqlite3


def inspect_database(db_path):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Retrieve the list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in the database.")
        else:
            print(f"Found {len(tables)} table(s):")
            for table in tables:
                print(f"- {table[0]}")

                # Retrieve the number of rows in each table
                cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
                count = cursor.fetchone()[0]
                print(f"  Contains {count} row(s).")

                # Optionally, display the first few rows
                cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
                rows = cursor.fetchall()
                print("  Sample Data:")
                for row in rows:
                    print(f"    {row}")
                print()

        # Close the connection
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    db_file = r"C:\Users\PC\Desktop\Bamboozle_ESL-game-main\vocabulary.db3"  # Ensure this path is correct
    inspect_database(db_file)

