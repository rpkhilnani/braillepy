class BrailleConverter:
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
        'z': '\u2835', ' ': ' ', '\n': '\n',

        # Numbers
        '1': '\u2831', '2': '\u2833', '3': '\u2839', '4': '\u283D', '5': '\u2835',
        '6': '\u283B', '7': '\u283F', '8': '\u2837', '9': '\u2836', '0': '\u283A',

        # Punctuation
        '.': '\u2832', ',': '\u2802', ';': '\u2806', ':': '\u2812', '?': '\u2826',
        '!': '\u2816', '(': '\u2836', ')': '\u2836', '-': '\u2824', '"': '\u2822',
        "'": '\u2804', '/': '\u2824', '@': '\u2801', '&': '\u282F', '*': '\u2828',
        '+': '\u2826', '=': '\u2836', '%': '\u2829', '<': '\u2828', '>': '\u2834',
        '[': '\u282E', ']': '\u282E', '{': '\u2824', '}': '\u2824',

        # Additional punctuation
        '#': '\u2820', '$': '\u2830', '^': '\u2824', '_': '\u2835', '\\': '\u2824',
        '|': '\u2824', '~': '\u2836',

        # Various brackets
        '[': '\u282E', ']': '\u282E', '{': '\u2824', '}': '\u2824', 
        '(': '\u2836', ')': '\u2836', '<': '\u2828', '>': '\u2834',

        # Other symbols
        '`': '\u2824', ':': '\u2812', ';': '\u2806', '_': '\u2835', 
        '"': '\u2822', "'": '\u2804', '?': '\u2826', '!': '\u2816', 
        '.': '\u2832', ',': '\u2802', '/': '\u2824', '@': '\u2801', 
        '&': '\u282F', '*': '\u2828', '+': '\u2826', '=': '\u2836', 
        '%': '\u2829', '^': '\u2824', '~': '\u2836', '\\': '\u2824',

        # Currency symbols
        '€': '\u2834', '£': '\u2831', '¥': '\u2839', '₹': '\u2833', '₩': '\u2838', 
        '₪': '\u2835', '₫': '\u2832', '₭': '\u2831', '₮': '\u282D', '₱': '\u283A',
        '₲': '\u2837', '₴': '\u2836', '₵': '\u282B', '₸': '\u2824', '₽': '\u283B',
        '₿': '\u283F', '¢': '\u2809', '$': '\u2830', '¤': '\u2834'
    }

    @classmethod
    def text_to_braille(cls, text):
        return ''.join(cls.braille_dict.get(char, char) for char in text)

# Example usage
#if __name__ == "__main__":
    #text = "Hello, World! 123"
    #braille_text = BrailleConverter.text_to_braille(text)
    #print(braille_text)
