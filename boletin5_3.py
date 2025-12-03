for fahrenheit in range(0, 121, 10):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} ºF = {celsius:.2f} ºC")
