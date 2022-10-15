import pytest
from IPYNBrenderer import render_YouTube_video
from IPYNBrenderer.custom_exception import InvalidURLException

class TestYTvideoRenderer:
    URL_test_success_data = [
        ("https://youtu.be/1-68pFs_HIE", "success"),
        ("https://www.youtube.com/watch?v=1-68pFs_HIE", "success"),
        ("https://www.youtube.com/watch?v=1-68pFs_HIE&t=60s", "success"),
    ]

    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=1-68pFs_HIEwe3fdsa"),
        ("https://www.youtube.com/watch?v=1-68pFs_HIE&t"),
        ("https://www.youtube.com/watch?v=1-68pFs_Hqw"),
        ("https://www.youtube.com/watch?v=1-68pFs_HIE&t==50s"),
        ("https://www.youtube.com/watch?v==1-68pFs_HIE&t=50s"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_YT_success(self, URL, response):
        assert render_YouTube_video(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)