import binascii

class texttobinary():
  def __init__(self, text):
    self.text = text 
    print(' '.join(format(ord(x), 'b') for x in text))

class texttohex():
  def __init__(self, text):
    self.text = text
    text = text.encode('utf-8')
    print(text.hex())

class binarytotext():
  def __init__(self, text):
    self.text = text
    ascii_string = "".join([chr(int(binary, 2)) for binary in text.split(" ")])
    print(ascii_string)
    
class binarytohex():
  def __init__(self, text):
   self.text = text
   text = int(text)
   print(hex(text))

class hextotext():
  def __init__(self, text):
    self.text = text
    text = bytes.fromhex(text).decode('utf-8') 
    print(text)

class hextobinary():
  def __init__(self, text):
    self.text = text
    binary_string = binascii.unhexlify(text)
    print(binary_string.decode())