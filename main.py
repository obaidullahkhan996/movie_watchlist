movies = [
    {"name": "Inception", "genre": "Sci-Fi", "status": "watched"},
    {"name": "Avatar", "genre": "Action", "status": "unwatched"},
    {"name": "Titanic", "genre": "Romance", "status": "watched"}
]

while True:
    print("\n=== MOVIE WATCHLIST ===")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Mark as Watched")
    print("5. Delete Movie")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")



    if choice == "1":
        name = input("enter movie name: ")
        genre = input("enter movie genre: ")

        movie = {
        "name": name,
        "genre": genre,
        "status": "unwatched"
    }

        movies.append(movie)
        print("Movie added successfully!")


    elif choice == "2":
        if not movies:
            print("No movies in your watchlist.")
        else:
            for movie in movies:
                print(f"Name: {movie['name']} | Genre: {movie['genre']} | Status: {movie['status']}")


    elif choice == "3":
        search_name = input("Enter movie name to search: ").strip().lower()
        found = False

        for movie in movies:
            if search_name in movie["name"].lower():
                print(f"Name: {movie['name']} | Genre: {movie['genre']} | Status: {movie['status']}")
                found = True

        if not found:
            print("Movie not found.")



    elif choice == "4":
             name = input("Enter movie name to mark as watched: ").strip().lower()
             found = False

             for movie in movies:
                  if movie["name"].lower() == name:
                 
                   movie["status"] = "watched"
                   found = True
                   print("status changed")

             if not found:
                 print("movie not found")       


    elif choice == "5":
        name = input("Enter movie name to delete: ").strip().lower()
        found = False  # <-- add this

        for movie in movies:

            if movie["name"].lower() == name:
           
                movies.remove(movie)
                found = True
                print("movie deleted succesfully")
                break


        if not found:
            print("movie not found")   


    elif choice == "6":
        total_movies = len(movies)
        watched_count = 0
        unwatched_count = 0

        for movie in movies:
            if movie["status"] == "watched":
                watched_count += 1

        for movie in movies:
            if movie["status"] == "unwatched":
               unwatched_count += 1  

        print("Total movies:", total_movies)
        print("Watched movies:", watched_count)
        print("Unwatched movies:", unwatched_count)   



    elif choice == "7":
        print("Goodbye!")
        break    







     