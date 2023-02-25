import order_request
import data

# Проверяется, что код ответа равен 200
def test_positive_assert():
    response = order_request.get_order_details()
    assert response.status_code == 200

