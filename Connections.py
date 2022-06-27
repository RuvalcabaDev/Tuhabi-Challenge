import pymysql
import os


class ConnectionMySQL:
    cursor = None
    connection = None

    def mysql_connect(self):
        self.connection = pymysql.connect(
            host=os.environ.get('DATABASE_HOST'),
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            port=int(os.environ.get('DATABASE_PORT')),
            db=os.environ.get('DATABASE_NAME')
        )
        self.cursor = self.connection.cursor()
        print("Conexión establecida!")

    def select_properties(self, properties_id):
        response_data = {}
        property_data = []
        sql_query = 'SELECT * FROM property WHERE id IN(' + ','.join((str(n) for n in properties_id)) + ')'
        try:
            self.cursor.execute(sql_query)
            response = self.cursor.fetchall()
            for property_info in response:
                if property_info[3] != 0:
                    property_detail = {
                        "address": property_info[1],
                        "city": property_info[2],
                        "price": property_info[3],
                        "description": property_info[4]
                    }
                    property_data.append(property_detail)
                else:
                    continue
            response_data["properties"] = property_data
            print("logs: ", response_data)
            return response_data
        except Exception as e:
            print("Error: ", e)
            return e

    def select_properties_with_arguments(self, properties_id, city, year):
        response_data_with_arguments = {}
        property_data = []
        if city != "" and year != "":
            sql_query = 'SELECT * FROM property ' \
                        'WHERE id IN(' + ','.join((str(n) for n in properties_id)) + ') AND city = (%s) AND year = (%s)'
            try:
                self.cursor.execute(sql_query, city, year)
            except Exception as e:
                print("Error: ", e)
                return e
        elif city != "":
            sql_query = 'SELECT * FROM property WHERE id IN(' + ','.join(
                (str(n) for n in properties_id)) + ') AND city = (%s)'
            try:
                self.cursor.execute(sql_query, city)
            except Exception as e:
                print("Error: ", e)
                return e
        elif year != "":
            sql_query = 'SELECT * FROM property WHERE id IN(' + ','.join(
                (str(n) for n in properties_id)) + ') AND year = (%s)'
            try:
                self.cursor.execute(sql_query, year)
            except Exception as e:
                print("Error: ", e)
                return e
        try:
            response = self.cursor.fetchall()
            for property_info in response:
                if property_info[3] != 0:
                    property_detail = {
                        "address": property_info[1],
                        "city": property_info[2],
                        "price": property_info[3],
                        "description": property_info[4]
                    }
                    property_data.append(property_detail)
                else:
                    continue
            response_data_with_arguments["properties"] = property_data
            print("logs: ", response_data_with_arguments)
            return response_data_with_arguments
        except Exception as e:
            print("Error: ", e)
            return e

    def clean_properties(self, sql_query):
        properties_id = []
        try:
            self.cursor.execute(sql_query)
            response = self.cursor.fetchall()
            for status_history in response:
                properties_id.append(status_history[1])
            print("logs: ", properties_id)
            return properties_id
        except Exception as e:
            print("Error: ", e)
            return e

    def mysql_close(self):
        print("Conexión cerrada!")
        self.connection.close()
