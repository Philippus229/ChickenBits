from bitstring import BitArray
from tkinter.filedialog import askopenfilename

fn = askopenfilename(filetypes =(("ChickenBits File", "*.cbit"),("All Files","*.*")), title = "Select a ChickenBits file")
f = open(fn, 'rb')
bit_array = BitArray(bytes=f.read())
bit_string = bit_array.bin
#print(bit_string)
bit_string = ((bit_string.replace("10", "chicken\n")).replace("0", "\n")).replace("1", "chicken ")
nfn = fn[:-4] + "ch"
nf = open(nfn, 'w')
nf.write(bit_string)
nf.close()
