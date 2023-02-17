import configuration
import requests
import data

#создание нового заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставялем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

#получение трек-номера заказа
response = create_new_order(data.order_body);
json_track_number = str(response.json()["track"]);
print(json_track_number);

#получение информации о заказе по его трек-номеру
def get_order_details():
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH + json_track_number)

response_details = get_order_details()
print(get_order_details());
