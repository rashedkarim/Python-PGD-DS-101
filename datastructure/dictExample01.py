import frequency as f

txt = '''Fruits have pericardia developed from ovary walls and seeds developed from fertilized ovules-generally the ovary alone grows into a fruit. But in some cases calyx and thalamus are involved to form false fruits like Dillenia, cashew nut and apple. Simple fruits developed from single ovary, is the character of fruits. Aggregate fruits are developed from numerous ovaries as in jackfruit and pineapple.

Bangladesh abounds with a large variety of tropical and sub-tropical fruits. The most widely cultivated fruits are mango, jackfruit, black berry, pineapple, banana, litchi, lemon, guava, custard apple, wood apple, elephant apple, golden apple, Indian berry, papaya, tamarind, melon, watermelon, cashew nut, pomegranate, palmyra, plum, rose apple, Indian olive, and Indian jujube. There are many minor edible fruits that are locally available in the wild and are also cultivated, such as latkan, monkey jack, uriam, rattan, river ebony, garcinia, water coconut, wild date palm, etc.

May, June and July are specially treated as fruit festival months in Bangladesh when almost all the major and minor fruits are matured and available. A few fruits are available throughout the year. These are the papaya, sapodilla, coconut and banana. The common imported fruits are orange, apple, pomegranate, grape, date, and mandarin.

In Bangladesh the cultivation of temperate fruits has been unsuccessful, except for grapes in some places. Oranges are cultivated only in a very limited areas in Sylhet and in remote areas of Rangamati (Sajeek) and Bandarban (Ruma) districts.'''


# print(txt)


# fruitSet = set()
#
# for x in txt.replace(',', '').replace('.', '').split(" "):
#     if x in myFruits:
#         fruitSet.add(x)
# print(fruitSet)

# fruit frequency
def fruitFrequency(txt):
    myFruits = ['apple', 'banana', 'guava', 'olive']
    fruitsDict = dict()
    for x in txt.replace(',', '').replace('.', '').split(" "):
        if x in myFruits:
            if x in fruitsDict.keys():
                fruitsDict[x] = fruitsDict[x] + 1
            else:
                fruitsDict[x] = 1
    print(fruitsDict)


result = dict()
result = f.characterFrequency(txt, ['a', 'e', 'i', 'o', 'u'])
for k, v in result.items():
    print(f"{k} : {v} times")

result = f.wordFrequency(txt, ['apple', 'banana', 'guava', 'olive'])
