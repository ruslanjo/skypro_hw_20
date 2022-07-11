from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    dir_1 = Director(id=1, name='Nolan')
    dir_2 = Director(id=2, name='Kubrick')
    dir_3 = Director(id=3, name='Stanislavskiy')

    director_dao.get_all = MagicMock(return_value=[dir_1, dir_2, dir_3])
    director_dao.get_one = MagicMock(return_value=dir_1)
    director_dao.create = MagicMock(return_value=Director(id=4))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        dir_d = {"name": "Mihalkov"}
        new_dir = self.director_service.create(dir_d)

        assert new_dir.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        dir_d = {
            "id": 3,
            "name": "Koen"
        }
        self.director_service.update(dir_d)



