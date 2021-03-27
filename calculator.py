from converter import *

class SoundSize(): # Calculates sound size 
  def __init__(self, sound_resolution, sample_rate, seconds):
    self.sound_resolution = sound_resolution
    self.sample_rate = sample_rate
    self.seconds = seconds

    # Calculation for sound size is sound resolution * sample rate * second
    bits = (int(sound_resolution) * int(sample_rate) * int(seconds))

    print(bits, "bits")

    user_input = input("Would you like to convert from bits to different values?  \n1. Yes \n2. No \n\nYour Option: ")

    if user_input == "1":
      convertion(input("Convert to: \n\n1. Nibbles \n2. Bytes \n3. Kilobytes \n4. Megabytes \n5. Gigabytes \n6. Terabytes \n7.Petabytes \nYour Option: "), bits)   

    elif user_input == "2":
      print("Thanks for using our service!")


class ImageSize(): # Calculates image size 
  def __init__(self, colour_depth, height, width):
    self.colour_depth = colour_depth
    self.height = height
    self.width = width

    # Calculations for image size 
    bits = int(colour_depth) * int(height) * int(width)

    print(bits, " bits\n\n")
    
    user_input = input("Would you like to convert from bits to different values?  \n1. Yes \n2. No \n\nYour Option: ")

    if user_input == "1":
      convertion(input("Convert to: \n\n1. Nibbles \n2. Bytes \n3. Kilobytes \n4. Megabytes \n5. Gigabytes \n6. Terabytes \n7.Petabytes \nYour Option: "), bits)   

    elif user_input == "2":
      print("Thanks for using our service!")
  

class convertion(): # converts bits to larger values 
  def __init__(self, file_data_type, value):
    self.file_data_type = file_data_type
    self.value = value


    if file_data_type == "1":
      print(value / 4, "nibbles")

    if file_data_type == "2":
      print(value / 8, "bytes")

    if file_data_type == "3":
      print(value / 8000, "kilobytes")

    if file_data_type == "4":
      print(value / 8000000 , "megabytes")

    if file_data_type == "5":
      print(value / 8000000000, "gigabytes")

    if file_data_type == "6":
      print(value / 8000000000000, "tb")

    if file_data_type == "7":
      print(value / 8000000000000000, "petabytes")

class Selection(): # Selects which calculator you actually want to use 
  def __init__(self, convertion_tool):

    self.convertion_tool = convertion_tool
    
    if convertion_tool == "1":
      ImageSize(input("Input Colour Depth: "), input("Input image height: "), input("Input image width: "))
    
    if convertion_tool == "2":
      SoundSize(input("Input Sound Resolution:  "), input("Input Sample Rate: "), input("Input seconds: "))

    if convertion_tool == "3":
      BinarySelection(input("\nWhich one would you like to convert to? \n\n1. Text to binary \n2. Text to hexidecimal \n3. Binary to Text \n4. Binary to hexidecimal \n5. hexidecimal to text \n6. hexidecimal to binary \n\nYour Option: "))
      


class BinarySelection(): # I didn't want to do this but looks better
  def __init__(self, user_option):
    self.user_option = user_option

    if user_option == "1":
      texttobinary(input("Input text: "))

    if user_option == "2":
      texttohex(input("Input text: "))

    if user_option == "3":
      binarytotext(input("Input binary: "))
    
    if user_option == "4":
      binarytohex(input("Input binary:  "))

    if user_option == "5":
      hextotext(input("Input hexidecimal: "))

    if user_option == "6":
      hextobinary(input("Input hexidecimal: "))
