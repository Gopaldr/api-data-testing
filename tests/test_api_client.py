
from unittest.mock import Mock, patch
from api_client import fetch_posts

@patch("api_client.requests.get")
def test_fetch_posts(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [{"id": 1, "title": "Test"}]
    mock_get.return_value = mock_response

    assert fetch_posts() == [{"id": 1, "title": "Test"}]
