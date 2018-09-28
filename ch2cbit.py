from bitstring import BitArray
from tkinter.filedialog import askopenfilename

fn = askopenfilename(filetypes =(("chicken File", "*.ch"),("All Files","*.*")), title = "Select a chicken file")
f = open(fn, 'r')
in_string = f.read()
in_string = ((in_string.replace('chicken', '1')).replace(' ', '')).replace('\n', '0')
bit_array = BitArray(bin=in_string)
#print(bit_array.bin)
out_file = open(fn[:-2] + 'cbit', 'wb')
bit_array.tofile(out_file)
out_file.close()
