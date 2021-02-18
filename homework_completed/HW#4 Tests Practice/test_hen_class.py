import unittest
from unittest.mock import patch
from hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # optional method, may be used to initialize hen_house instance
        cls.hen_house = HenHouse(10)

    def test_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised
        with self.assertRaises(ValueError):
            self.hen_house = HenHouse(1)

    def test_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch("hen_class.HenHouse.season", "winter"):
            self.assertEqual(self.hen_house.season, "winter")
        with patch("hen_class.HenHouse.season", "spring"):
            self.assertEqual(self.hen_house.season, "spring")
        with patch("hen_class.HenHouse.season", "summer"):
            self.assertEqual(self.hen_house.season, "summer")
        with patch("hen_class.HenHouse.season", "autumn"):
            self.assertEqual(self.hen_house.season, "autumn")

    def test_productivity_index(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        with patch("hen_class.HenHouse.season", "winter"):
            self.assertEqual(self.hen_house._productivity_index(), 0.25)
        with patch("hen_class.HenHouse.season", "spring"):
            self.assertEqual(self.hen_house._productivity_index(), 0.75)
        with patch("hen_class.HenHouse.season", "summer"):
            self.assertEqual(self.hen_house._productivity_index(), 1)
        with patch("hen_class.HenHouse.season", "autumn"):
            self.assertEqual(self.hen_house._productivity_index(), 0.5)

    def test_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called
        with patch("hen_class.HenHouse.season", ""):
            with self.assertRaises(ErrorTimesOfYear):
                self.hen_house._productivity_index()

    def test_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked
        with patch("hen_class.HenHouse._productivity_index", return_value=0.25):
            self.assertEqual(self.hen_house.get_eggs_daily(10), 2)

    def test_get_max_count_for_soup(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch("hen_class.HenHouse.season", "winter"):
            self.assertEqual(self.hen_house.get_max_count_for_soup(1), 4)
        with patch("hen_class.HenHouse.season", "spring"):
            self.assertEqual(self.hen_house.get_max_count_for_soup(5), 2)
        with patch("hen_class.HenHouse.season", "summer"):
            self.assertEqual(self.hen_house.get_max_count_for_soup(8), 2)
        with patch("hen_class.HenHouse.season", "autumn"):
            self.assertEqual(self.hen_house.get_max_count_for_soup(3), 4)

    def test_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch("hen_class.HenHouse._productivity_index", return_value=0.5):
            self.assertEqual(self.hen_house.get_max_count_for_soup(10), 0)

    def test_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type
        with patch("hen_class.requests.get") as mocked_request:
            mocked_request.return_value.status_code = 200
            mocked_request.return_value.text = "6543513511212"
            self.assertEqual(self.hen_house.food_price(), 2)
            self.assertIsInstance(self.hen_house.food_price(), int)

    def test_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called
        with patch("hen_class.requests.get") as mocked_request:
            mocked_request.return_value.status_code = 404
            with self.assertRaises(ConnectionError):
                self.hen_house.food_price()


if __name__ == '__main__':
    unittest.main()
