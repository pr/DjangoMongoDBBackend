from sample_mflix.models import Movie, Award, Viewer
from django.utils import timezone
from datetime import datetime


movie_awards = Award(wins=122, nominations=245, text="Won 1 Oscar")

movie = Movie.objects.create(
   title="Test Title",
   plot="Test Plot",
   runtime=100,
   released=timezone.make_aware(datetime(2025, 1, 1)),
   awards=movie_awards,
   genres=["Drama", "Comedy"]
)

viewer = Viewer.objects.create(
   name="Peter",
   email="test@peter.net",
   password="<PASSWORD>",
)
