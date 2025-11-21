class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats_sorted = sorted(seats)
        students_sorted = sorted(students)
        ret = [abs(seat - student) for seat, student in zip(seats_sorted, sorted(students_sorted))]
        return sum(ret)

