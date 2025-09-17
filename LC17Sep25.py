class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.heap_ratings = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            heappush(self.heap_ratings[cuisine], (-rating, food))
            self.foods[food] = (cuisine, -rating)


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foods[food]
        heappush(self.heap_ratings[cuisine], (-newRating, food))
        self.foods[food] = (cuisine, -newRating)


    def highestRated(self, cuisine: str) -> str:
        while self.foods[self.heap_ratings[cuisine][0][1]][1] != self.heap_ratings[cuisine][0][0]:
            heappop(self.heap_ratings[cuisine])
        return self.heap_ratings[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
