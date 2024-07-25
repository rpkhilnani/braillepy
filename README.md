# braillepy

This is a library to convert text to braille in python using unicode. This includes all the key characters on a Standard English Keyboard.

## Installation

You can install the package using pip:

```bash
pip install braillepy
```

## Example usage

from braillepy import BrailleConverter

result = BrailleConverter.text_to_braille("Hello, World!")
print(result)
