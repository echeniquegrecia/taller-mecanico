client_table = "CREATE TABLE IF NOT EXISTS client (" \
                          "id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "name text NOT NULL," \
                          "last_name text NOT NULL," \
                          "identification_number text," \
                          "email text," \
                          "phone text," \
                          "address text NOT NULL" \
                          ");"

vehicle_table = "CREATE TABLE IF NOT EXISTS vehicle (" \
                           "id integer PRIMARY KEY UNIQUE NOT NULL," \
                           "client_id integer NOT NULL," \
                           "repair_id integer UNIQUE NOT NULL," \
                           "model text NOT NULL," \
                           "year integer NOT NULL," \
                           "identification_number  NOT NULL," \
                           "mileage REAL NOT NULL," \
                           "FOREIGN KEY (client_id) REFERENCES client (id)," \
                           "FOREIGN KEY (repair_id) REFERENCES repair (id)" \
                           "); """

repair_table = "CREATE TABLE IF NOT EXISTS repair (" \
                          "id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "vehicle_id integer NOT NULL," \
                          "details_pre_repair text NOT NULL," \
                          "details_post_repair text NOT NULL," \
                          "date TEXT NOT NULL," \
                          "price REAL NOT NULL," \
                          "FOREIGN KEY (vehicle_id) REFERENCES vehicle (id)   " \
                          "); """
