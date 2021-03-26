from converter import *

class SoundSize():
  def __init__(self, sound_resolution, sample_rate, seconds):
    self.sound_resolution = sound_resolution
    self.sample_rate = sample_rate
    self.seconds = seconds

    bits = (int(sound_resolution) * int(sample_rate) * int(seconds))

    print(bits)

    file_data_type = input("Convert to: ").lower()

    convertion(file_data_type, bits)


class ImageSize():
  def __init__(self, colour_depth, height, width):
    self.colour_depth = colour_depth
    self.height = height
    self.width = width

    bits = int(colour_depth) * int(height) * int(width)
    print(bits, " bits\n\n")

    file_data_type = input("Convert to: ").lower()
    convertion(file_data_type, bits)   
    



class convertion():
  def __init__(self, file_data_type, value):
    self.file_data_type = file_data_type
    self.value = value

    if file_data_type == "bytes":
      print(value / 8, "bytes")

    if file_data_type == "kb":
      print(value / 8000, "kilobytes")

class Selection():
  def __init__(self, convertion_tool):

    self.convertion_tool = convertion_tool
    
    if convertion_tool == "1":
      ImageSize(input("Input Colour Depth: "), input("Input image height: "), input("Input image width: "))
    
    if convertion_tool == "2":
      SoundSize(input("Input Sound Resolution"), input("Input Sample Rate"), input("Input seconds: "))

    if convertion_tool == "3":
      BinarySelection(input("\nWhich one would you like to convert to? \n\n1. Text to binary \n2. Text to hexidecimal \n3. Binary to Text \n4. Binary to hexidecimal \n5. hexidecimal to text \n6. hexidecimal to binary \n\nYour Option: "))
      
    else:
      print("Stupid option!")


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
