Hex Replace project. Takes part of a files binary and patches it over existing region of original_path's file. A new file is generated so original file will not be amended. 

Example:
Let's take basic_hex.txt:
```
hello world i like dogs
```

And replace small_hex.txt into basic_hex.txt at offset 0x6:
```
buddy
```

The output file will be the same size as the original file, but will contain the entire new binary files contents beginning at offset specified.

```
>>> import hex_replace as hex
>>> hex.replace_hex(r"C:\Projects\basic_hex.txt",r"C:\Projects\small_hex.txt",0x6)
File saved to C:\Projects\HEX_Replace-2018-11-11--22-16-09.bin.
```

HEX_Replace-2018-11-11--22-16-09.bin now contains:
```
hello buddy i like dogs
```
