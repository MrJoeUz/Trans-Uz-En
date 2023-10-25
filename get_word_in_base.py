from .mainbase.finder import find

def get_word_in_mainbase(fl, tl, w):
    if(str(type(w)) == "<class 'str'>"):
        first_letter = w[0].lower()
        base_folder = f"{fl}-{tl}"
        return find(base_folder, first_letter)
    else:
        return False
