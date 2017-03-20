import os, csv, sqlite3

def add_path(f, folder):
    return folder + '/' + f

# It returns all CSV files from a directory
def getCSVFiles(directory):
    CSVFiles = []
    for x in os.walk(directory):
        for csv in x[2]:
            if os.path.splitext(csv)[1] == '.csv':
                full_path = add_path(csv, x[0])
                CSVFiles.append(full_path)
        for folder in x[1]:
            other_files = [add_path(p, x[0]) for p in getCSVFiles(folder)]
            CSVFiles.extend(other_files)
    return CSVFiles

def insert_sql(name_table, name_csv):
    with open (name_csv, 'r') as f:
        reader = csv.reader(f)
        columns = map(lambda x: x.replace(" ",""), next(reader))

        query_create_table = 'CREATE TABLE {0}({1});'
        query_create_table = query_create_table.format(name_table, ','.join(columns))
        print query_create_table

        query = 'insert into {0}({1}) values ({2})'
        query = query.format(name_table, ','.join(columns), ','.join('?' * len(columns)))

        try:
            connection = sqlite3.connect(":memory:")
            cursor = connection.cursor()
            cursor.execute(query_create_table)
            for data in reader:
                cursor.execute(query, data)
            cursor.commit()
        except:
            print "Failed on {0}".format(query)

def main():

    # Search all the folders in datos
    # For each PDF I find
    # Convert it into XLS with the same name
    for csv in getCSVFiles('../datos'):
        new_name = os.path.basename(csv).split('.')[0]
        print "CSV {0} converted into {1}".format(csv, new_name)
        insert_sql(new_name, csv)

if __name__ == "__main__":
    main()
