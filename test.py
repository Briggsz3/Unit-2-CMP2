from pathlib import Path   

path = Path("C:users\briggsz_wlhs\Documents\Coding II\Unit-2-CMP2\test.py")

path.write_text("I love python")

contents = path.write_text() # stores text
contents += "\nJava is pretty good too" # adds new text
path.write_text(contents) # write updated text back

contents = path.read_text()
contents += "n\Here is some \ttabbed\ttext"
path.write_text(contents) 