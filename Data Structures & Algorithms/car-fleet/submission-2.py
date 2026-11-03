class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i, v in enumerate(position):
            car_data = (position[i], speed[i])
            cars.append(car_data)

        cars.sort(key=lambda car: car[0], reverse=True)
        groupStack = []

        for pos, spd in cars:
            arrival = (target - pos) / spd

            if not groupStack or arrival > groupStack[-1]:
                groupStack.append(arrival)

        return len(groupStack)