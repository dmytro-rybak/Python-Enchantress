import pytest
from hen_class import HenHouse, ErrorTimesOfYear


class TestClass:
    @classmethod
    def setup_class(cls):
        cls.hen_house = HenHouse(10)

    def test_init_with_less_than_min(self):
        with pytest.raises(ValueError):
            self.hen_house = HenHouse(1)

    @pytest.fixture()
    def set_winter(self, monkeypatch):
        monkeypatch.setattr("hen_class.HenHouse.season", "winter")

    @pytest.fixture()
    def set_spring(self, monkeypatch):
        monkeypatch.setattr("hen_class.HenHouse.season", "spring")

    @pytest.fixture()
    def set_summer(self, monkeypatch):
        monkeypatch.setattr("hen_class.HenHouse.season", "summer")

    @pytest.fixture()
    def set_autumn(self, monkeypatch):
        monkeypatch.setattr("hen_class.HenHouse.season", "autumn")

    def test_season_winter(self, set_winter):
        assert self.hen_house.season == "winter"

    def test_season_spring(self, set_spring):
        assert self.hen_house.season == "spring"

    def test_season_summer(self, set_summer):
        assert self.hen_house.season == "summer"

    def test_season_autumn(self, set_autumn):
        assert self.hen_house.season == "autumn"

    def test_productivity_index_spring(self, set_spring):
        assert self.hen_house._productivity_index() == 0.75

    def test_productivity_index_autumn(self, set_autumn):
        assert self.hen_house._productivity_index() == 0.5

    def test_productivity_index_incorrect_season(self, monkeypatch):
        monkeypatch.setattr("hen_class.HenHouse.season", "")
        with pytest.raises(ErrorTimesOfYear):
            self.hen_house._productivity_index()

    def test_get_eggs_daily_in_autumn(self, set_autumn):
        assert self.hen_house.get_eggs_daily(10) == 5

    def test_get_max_count_for_soup_in_winter(self, set_winter):
        assert self.hen_house.get_max_count_for_soup(1) == 4

    def test_get_max_count_for_soup_in_spring(self, set_spring):
        assert self.hen_house.get_max_count_for_soup(5) == 2

    def test_get_max_count_for_soup_in_summer_returns_zero(self, set_summer):
        assert self.hen_house.get_max_count_for_soup(10) == 0
