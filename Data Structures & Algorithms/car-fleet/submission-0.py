class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_state = []
        for i in range(len(position)):
            car_state.append((target-position[i],speed[i]))
        car_state.sort()
        car_stack = []
        fleets = 0
        for i in range(len(car_state)):
            time = car_state[i][0]/car_state[i][1]
            while car_stack and car_stack[-1] < time:
                car_stack.pop()
            if len(car_stack) == 0:
                fleets += 1
            car_stack.append(time)
        return fleets