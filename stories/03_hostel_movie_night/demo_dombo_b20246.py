"""Dombo's demo of finding entertainment that fits a data bundle."""
from story import (
    FeaturedMovie,
    MovieNight,
    MusicSession,
    StorytellingCircle,
    StreamedMovie,
    available,
)


options = [
    StreamedMovie("Mukono Mystery"),
    MusicSession("Afrobeats break"),
    FeaturedMovie("Mukono Mystery: data saver"),
    StorytellingCircle(),
]
dombo = MovieNight("Dombo", 350)

original_options = options.copy()
starting_data = dombo.bundle.remaining
starting_activities = dombo.activities

fitting_options = available(options, 350)
print("Options that fit 350 MB:")
for option in fitting_options:
    print(f"- {option.title}: {option.data_cost()} MB")
print("The 350 MB data-saver movie fits exactly.")

print("\nOptions that fit 99 MB:")
for option in available(options, 99):
    print(f"- {option.title}: {option.data_cost()} MB")

print("\nRead-only checks:")
print(f"Options unchanged: {options == original_options}")
print(f"Data unchanged: {dombo.bundle.remaining == starting_data} ({dombo.bundle.remaining} MB)")
print(f"Activity history unchanged: {dombo.activities == starting_activities} ({dombo.activities} activities)")
