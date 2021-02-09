def CelToFah(t):
    return round(1.8*t+32,6)
def FahToCel(t):
    return round((5/9)*(t-32),6)
print(FahToCel(100))
