# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like




from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level (all, 1.0, 2.5, 4.5, significant): ")
period = input("Enter time period (hour, day, week, month): ")

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)

dataset.read_feed()

print(dataset)

if len(dataset) > 0:
    print(f"Mean depth = {dataset.mean_depth():.2f} km")
    print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

    strongest = dataset.strongest_quake()

    print()
    print(f"Strongest quake occurred at {strongest.when:%H:%M:%S} on {strongest.when:%Y-%m-%d}")
    print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
    print(f"The depth was {strongest.depth} km")
    print(f"The magnitude was {strongest.magnitude}")
else:
    print("No earthquakes found.")
