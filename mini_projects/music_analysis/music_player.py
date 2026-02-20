import pandas as pd
import matplotlib.pyplot as plt

player = pd.read_csv('music_playlist_sample.csv')
avg_duration = player["Duration"].mean()
most_common_genre = player["Genre"].mode()[0]


plt.figure(figsize=(10,6))
plt.bar(player["Song Name"], player["Duration"])
plt.xticks(rotation=45)
plt.title("Duration per Song")
plt.xlabel("Song")
plt.ylabel("Duration (seconds)")
plt.show()
player["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Genre Distribution")
plt.ylabel("")
plt.show()


print(player.info())
print("Average Duration:", avg_duration, "seconds")
print("Most Common Genre:", most_common_genre)


# INSIGHTS
# 1. Most songs in my playlist belong to the Pop genre, so that is my preferred music style.
# 2. The average duration of my songs shows that I prefer shorter tracks.
# 3. Most songs are from recent years, showing I listen mainly to modern music.
