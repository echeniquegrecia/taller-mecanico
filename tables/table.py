class Table:

    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()


    def create(self, table_schema):
        self.cursor.execute(table_schema)

    def insert_data(self, table_name:str, data:dict):
        list_fields = [*data.keys()]
        list_values = [*data.values()]
        string_fields = ",".join([*data.keys()])
        mark_questions_list= list(map(lambda x: x.replace(x, "?"), list_fields))
        mark_questions_string = ",".join([_ for _ in mark_questions_list])
        sql_command = f"INSERT INTO {table_name}({string_fields}) VALUES({mark_questions_string})"
        self.cursor.execute(sql_command, list_values)
        self.conn.commit()


    def show_all(self, table_name:str):
        self.table_name = table_name
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        print(self.cursor.fetchall())