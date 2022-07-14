# uwufier algorithm by PiciAkk, do not touch!

class Utils:
    vowels = "aáeéiíoóöőuúüűy"
    consonants = "bccsddzdzsfggyhjkllymnnypqrsszttyuvwxyzzs"
    
    def windowed(lst):
        return list(zip(lst[0:-1], lst[1:len(lst)]))

def uwufy(text):
    # uwufy a word
    return "".join([
        "ij" if (char == "i" and next_char in Utils.vowels)
        else "j" if (char == "l" and next_char in Utils.vowels)
        else "w" if (char in ["l", "r"])
        else f"{char}y" if (char in ["t", "n"] and next_char != "y")
        else char

        for char, next_char in Utils.windowed(text)
    ]).lower() + text[-1]

# "szija! '╰(☆▽¯)／' üdvözöwwek a fiwc nyapjóban! uwu"
