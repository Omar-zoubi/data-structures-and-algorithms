# import re
def first_word_repeted(sentence):
    val_after_split= []
    save_val = ''
    for word in sentence:
        if word == ' ':
            val_after_split.append(save_val.lower())
            save_val = ''
        else:
            save_val += word
    if save_val:
        val_after_split.append(save_val.lower())
    value_to_check = []
    for repeat in val_after_split:
        if repeat in value_to_check :
            return repeat
        else :
            value_to_check.append(repeat)
    return 'no repeat'
index_one = "It was a queer, sultry summer , the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
index_tow ="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
index_three= "Once upon a time, there was a brave princess who..."
index_four= "hi my name is omar"
print(first_word_repeted(index_one))
print(first_word_repeted(index_tow))
print(first_word_repeted(index_four))
