from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movie_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie) -> None:
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()

    
    def update_movie(self, id: int,  data: Movie) -> None:
        movie = self.db.query(MovieModel).filter(Movie.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.title
        movie.category = data.category
        self.db.commit()


    def delete_movie(self, id) -> None:
        result = self.get_movies(id).delete()
        self.db.commit()