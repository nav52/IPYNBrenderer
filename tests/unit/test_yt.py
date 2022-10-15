from webbrowser import get
import pytest
from IPYNBrenderer import get_time_info
from IPYNBrenderer.custom_exception import InvalidURLException

good_URL_data = [
    ("https://youtu.be/1-68pFs_HIE", 0),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE", 0),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&t=60s", 60),
]

bad_URL_data = [
    ("https://www.youtube.com/watch?v=1-68pFs_HIEwe3fdsa"),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&t"),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&t==50s"),
    ("https://www.youtube.com/watch?v==1-68pFs_HIE&t=50s"),
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


@pytest.mark.parametrize("URL", bad_URL_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
