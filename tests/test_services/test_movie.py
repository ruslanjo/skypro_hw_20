from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Wolf of Wall-Street')
    movie_2 = Movie(id=2, title='Harry Potter')
    movie_3 = Movie(id=3, title='Social Network')

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_create(self):
        movie_d = {"title": "Pirates of the Caribbean"}

        new_movie = self.movie_service.create(movie_d)

        assert new_movie.id is not None

    def test_update(self):
        movie_d = {"id": 3, "title": "new_title"}
        self.movie_service.update(movie_d)

    def test_delete(self):
        self.movie_service.delete(1)
