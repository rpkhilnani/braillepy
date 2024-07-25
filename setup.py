from setuptools import setup, find_packages

setup(
    name="Roshan Khilnani",
    version="202407-1",
    description="A library to convert text to Braille",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Roshan Khilnani",
    author_email="rpkhilnani@yahoo.in",
    url="https://github.com/rpkhilnani/braillepy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL Version 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


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
        '₿': '\u283F', '¢': '\u2809', '$': '\u2830', '¤': '\u2834',

        # Braille contractions
        'and': '\u2823', 'for': '\u2824', 'the': '\u2835', 'with': '\u2836', 
        'ch': '\u2837', 'sh': '\u2838', 'st': '\u2839', 'th': '\u283A', 
        'wh': '\u283B', 'ou': '\u283C', 'ow': '\u283D', 'ar': '\u283E', 
        'ing': '\u283F', 'ed': '\u2840', 'en': '\u2841', 'er': '\u2842', 
        'ou': '\u2843', 'ow': '\u2844', 'st': '\u2845', 'ch': '\u2846', 
        'gh': '\u2847', 'sh': '\u2848', 'th': '\u2849', 'wh': '\u284A',
        'ble': '\u284B', 'com': '\u284C', 'dd': '\u284D', 'ea': '\u284E', 
        'ff': '\u284F', 'gg': '\u2850', 'in': '\u2851', 'st': '\u2852',
        'ar': '\u2853', 'bb': '\u2854', 'cc': '\u2855', 'dis': '\u2856',
        'ea': '\u2857', 'ff': '\u2858', 'gg': '\u2859', 'in': '\u285A',
        'it': '\u285B', 'll': '\u285C', 'more': '\u285D', 'ness': '\u285E',
        'ound': '\u285F', 'ation': '\u2860', 'ally': '\u2861', 'ance': '\u2862',
        'ence': '\u2863', 'full': '\u2864', 'less': '\u2865', 'ment': '\u2866',
        'ness': '\u2867', 'ong': '\u2868', 'ful': '\u2869', 'ness': '\u286A',
        'rr': '\u286B', 'ship': '\u286C', 'some': '\u286D', 'under': '\u286E',
        'ver': '\u286F', 'wh': '\u2870', 'will': '\u2871', 'ou': '\u2872',
        'where': '\u2873', 'ought': '\u2874', 'sh': '\u2875', 'and': '\u2876',
        'still': '\u2877', 'with': '\u2878', 'gh': '\u2879', 'ing': '\u287A',
        'ble': '\u287B', 'dis': '\u287C', 'en': '\u287D', 'er': '\u287E', 
        'ff': '\u287F'
    }

    @classmethod
    def text_to_braille(cls, text):
        return ''.join(cls.braille_dict.get(char, char) for char in text)

# Example usage
if __name__ == "__main__":
    text = "Hello, World! 123 €£¥"
    braille_text = BrailleConverter.text_to_braille(text)
    print(braille_text)
