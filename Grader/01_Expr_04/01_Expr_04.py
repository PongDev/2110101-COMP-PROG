import math

WeightKG=float(input())
HeightCM=float(input())
print(math.sqrt(WeightKG*HeightCM)/60)
print(0.024265*(WeightKG**0.5378)*(HeightCM**0.3964))
print(0.0333*(WeightKG**(0.6157-(0.0188*math.log(WeightKG,10))))*(HeightCM**0.3))