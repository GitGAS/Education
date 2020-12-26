# Task_2

class Road():
    weight = 25

    def __init__(self,length,width):
        self._length = int(length)
        self._width = int(width)

    def mas(self, height = 5):
        result = self._length * self._width * self.weight * height / 1000
        return result

out = Road(5000, 20)

print(f"Масса асфальта составит: {out.mas():0.0f} т.")