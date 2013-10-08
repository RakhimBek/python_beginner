def ConvertDegree(a):
    return a + 273.15,a*(9.0/5.0) + 32.0

class InputException(Exception):
    pass

def main():
    try:
        a = float(input("\nEnter degree(Celsius) : "))
        if a < -273.15:
            raise InputException("\nThe value must not be less than -273.15 degrees")
        c,d = ConvertDegree(a)
        print("\n\nKelvin : {0} \nFahrenheit : {1}\n".format(round(c,9),round(d,9)))
    except ValueError:
        print("\n Input just number values ")
    except InputException as e:
        print(e)
        
if __name__ == "__main__":
    main()
