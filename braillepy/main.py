# The Unicode block Braille Patterns (U+2800..U+28FF) contains all 256 possible patterns of an 8-dot braille cell, including the complete 6-dot cell range. using this the below code is developed to recognize Latin English text and convert to braille.

braille_dict = {
    # Uppercase letters 
    'A': '\u2820\u2801', 'B': '\u2820\u2803', 'C': '\u2820\u2809', 'D': '\u2820\u2819', 'E': '\u2820\u2811',
    'F': '\u2820\u280B', 'G': '\u2820\u281B', 'H': '\u2820\u2813', 'I': '\u2820\u280A', 'J': '\u2820\u281A',
    'K': '\u2820\u2805', 'L': '\u2820\u2807', 'M': '\u2820\u280D', 'N': '\u2820\u281D', 'O': '\u2820\u2815',
    'P': '\u2820\u280F', 'Q': '\u2820\u281F', 'R': '\u2820\u2817', 'S': '\u2820\u280E', 'T': '\u2820\u281E',
    'U': '\u2820\u2825', 'V': '\u2820\u2827', 'W': '\u2820\u283A', 'X': '\u2820\u282D', 'Y': '\u2820\u283D',
    'Z': '\u2820\u2835',
    
    # Lowercase letters
    'a': '\u2801', 'b': '\u2803', 'c': '\u2809', 'd': '\u2819', 'e': '\u2811',
    'f': '\u280B', 'g': '\u281B', 'h': '\u2813', 'i': '\u280A', 'j': '\u281A',
    'k': '\u2805', 'l': '\u2807', 'm': '\u280D', 'n': '\u281D', 'o': '\u2815',
    'p': '\u280F', 'q': '\u281F', 'r': '\u2817', 's': '\u280E', 't': '\u281E',
    'u': '\u2825', 'v': '\u2827', 'w': '\u283A', 'x': '\u282D', 'y': '\u283D',
    'z': '\u2835', 

    # numbers
    "1": "\\u283C\\u2801", "2": "\\u283C\\u2803", "3": "\\u283C\\u2809", 
    "4": "\\u283C\\u2819", "5": "\\u283C\\u2811", "6": "\\u283C\\u280B",
    "7": "\\u283C\\u281B", "8": "\\u283C\\u2813", "9": "\\u283C\\u280A",
    "0": "\\u283C\\u281A"

    # Spacers
    ' ': ' ', '\n': '\n',
    # symbol
    "!": "\\u2816", "@": "\\u2808\\u2801", "#": "\\u2838\\u2839",
    "$": "\\u2808\\u280E", "%": "\\u2805\\u2834", "^": "\\u2808\\u2822", 
    "&": "\\u2808\\u282F", "*": "\\u2810\\u2814", "(": "\\u2810\\u2823",
    ")": "\\u2810\\u281C", "{": "\\u2838\\u2823", "}": "\\u2838\\u281C",
    "-": "\\u2824", "_": "\\u2828\\u2824", "+": "\\u2810\\u2816",
    "=": "\\u2810\\u2836", "[": "\\u2828\\u2823", "]": "\\u2828\\u281C", 
    ":": "\\u2812", ";": "\\u2806", "“": "\\u2826",
    "”": "\\u2834", "‘": "\\u2820\\u2826", "’": "\\u2820\\u2834",
    "<": "\\u2808\\u2823", ">": "\\u2808\\u281C", "\\": "\\u2802",
    ".": "\\u2832", "/": "\\u2838\\u280C", "\\": "\\u2838\\u2821",
    "?": "\\u2826", "|": "\\u2838\\u2833", "`": "\\u2820\\u2826",
    "~": "\\u2808\\u2814", "£": "\\u2808\\u2807", "©": "\\u2818\\u2809", 
    "°": "\\u2818\\u281A", "÷": "\\u2810\\u280C", "€": "\\u2808\\u2811",
    "¶": "\\u2818\\u280F", "®": "\\u2818\\u2817", "™": "\\u2818\\u281E",
    "¥": "\\u2808\\u283D", "×": "\\u2810\\u2826"
}


    # Braille contractions
braille_contractions = {

}

def char_to_braille(text):
    return ''.join(braille_dict.get(char, char) for char in text)

def words_to_braille(text):
    # Convert contractions first
    for contraction, braille in sorted(braille_contractions.items(), key=lambda x: -len(x[0])):
        if contraction in text:
            text = text.replace(contraction, braille)
    
    # Convert remaining characters
    braille_text = ''.join(braille_dict.get(char, char) for char in text)
    
    return braille_text

# Example usage
#if __name__ == "__main__":
    # text = "Hello, World! 123 €£¥"
    # braille_text = text_to_braille(text)
    # print(braille_text)