import order_request
import data

def test_positive_assert():
    # Проверяется, что код ответа равен 200
    assert order_request.response_details.status_code == 200
