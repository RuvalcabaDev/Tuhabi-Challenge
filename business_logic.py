from Connections import ConnectionMySQL
from fastapi import FastAPI
from schemas import PropertiesRequestModel


app = FastAPI(title='findProperties',
              version='1.0')


@app.get('/findProperties')
async def find_properties(properties: PropertiesRequestModel):
    query_status_history = 'SELECT max(update_date), property_id FROM status_history ' \
                           'WHERE (status_id = 5) OR (status_id = 4) OR (status_id = 3) ' \
                           'GROUP BY property_id'
    try:
        database_connection = ConnectionMySQL()
        database_connection.mysql_connect()
        response_properties_id = database_connection.clean_properties(query_status_history)
        if properties.city == "" and properties.year == "":
            response_data = database_connection.select_properties(response_properties_id)
            if response_data:
                database_connection.mysql_close()
                return response_data
        elif properties.city or properties.year:
            response_with_arguments = database_connection.select_properties_with_arguments(
                response_properties_id,
                properties.city,
                properties.year
            )
            if response_with_arguments:
                database_connection.mysql_close()
                return response_with_arguments
    except Exception as e:
        print("Error: ", e)
        return e

