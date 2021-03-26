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