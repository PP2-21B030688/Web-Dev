rubles = int(input('Rubles? '))
kopeiki = int(input('Kopeiki? '))
apples = int(input('Apples? ')) # apples instead of pirozhki

priceRubles = apples * rubles;
priceKopeiki = apples * kopeiki;

priceRubles += int(priceKopeiki / 100)
priceKopeiki %= 100

print(priceRubles, priceKopeiki)