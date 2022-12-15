def decimal_to_dms(decimal):
  degrees = int(decimal)

  minutes = (decimal - degrees) * 60

  seconds = (minutes - int(minutes)) * 60

  return str(degrees) + "° " + str(int(minutes)) + "' " + str(int(seconds)) + "''"

def main():
  coordinate = float(input("Enter a decimal degree coordinate: "))

  print("DMS: " + decimal_to_dms(coordinate))

main()

