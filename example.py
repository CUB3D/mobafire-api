import mobafire

if __name__ == "__main__":
    while True:
        championName = input("Enter a champion name: ")
        guides = mobafire.get_guides(championName)
        print("Found", len(guides), "guides for", championName)
        print("Top 3 guides:")
        for i in range(3):
            print("{}: {}".format(i+1, guides[i]))
