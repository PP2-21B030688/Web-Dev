def cat_dog(s):
    cat = s.count("cat")
    dog = s.count("dog")
    return (True if cat == dog else False)

print(cat_dog("catdof"))