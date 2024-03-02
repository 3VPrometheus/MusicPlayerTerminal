from dLoaderLibsTerminal import SearchYoutube
from time import sleep

search_term = input("Enter the search term: \n")
num_results = int(input("Enter the number of results to display: \n"))

video_link = SearchYoutube(search_term, num_results)

for i in range(7):
    print(".")
    sleep(1)

print("Printing video link...\n\n")
print(video_link)