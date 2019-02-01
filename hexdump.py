# Author: Jacob Goldman
# Usage: python hexdump.py [filename]
# Produces same output as hexdump -Cv
import sys
with open(sys.argv[1], 'rb') as f:
    offset = 0
    data = f.read(16)
    while data:
        offset_str = f'{offset:0{8}x}'
        values = [data[i:i+1].hex() for i in range(0, len(data), 1)]
        values = '  '.join([' '.join(values[:8]), ' '.join(values[8:])])
        perusal = ''.join([chr(byte) if byte >= 0x20 and byte <= 0x7E else '.' for byte in data ])

        print(f'{offset_str}  {values:<48}  |{perusal}|')
        
        offset += len(data)
        data = f.read(16)
    if offset > 0:
        print(f'{offset:0{8}x}')