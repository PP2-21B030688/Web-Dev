def make_out_word(out, content):
    leftOut = out[:int(len(out)/2)]
    rightOut = out[int(len(out)/2):len(out)]
    return leftOut + content + rightOut

print(make_out_word("<<>>", "Bobby"))