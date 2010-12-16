## SNOW Obtained from: http://wordlist.sourceforge.net/
##    Except for the special word lists the files follow the following
##    naming convention:
##      <spelling category>-<classification>.<size>
##    Where the spelling category is one of
##      english, american, british, british_z, canadian, 
##      variant_0, varaint_1, variant_2
##    Classification is one of
##      abbreviations, contractions, proper-names, upper, words
##    And size is one of
##      10, 20, 35 (small), 40, 50 (medium), 55, 60, 70 (large), 
##      80 (huge), 95 (insane)
##    The special word lists follow are in the following format:
##      special-<description>.<size>
##    Where description is one of:
##      roman-numerals, hacker
import os
import re
import string
import urllib2
word_lists = []
root_path = "C:\\Users\\Nick\\Downloads\\scowl-6\\final"
for root, dirs, files in os.walk(root_path):
    for filename in files:
        word_lists.append(filename)
for i, word_list in enumerate(word_lists):
    file_path = os.path.join(root_path, word_list)
    f = open(file_path, "r")
    words = f.readlines()
    f.close()
    words = [string.replace(word, '\n','') for word in words]
    word_count = len(words)
    meta = re.compile(r'([^-]*)[-]([^\.]*)[\.](.*)').match(word_list)
    spelling_category, classification, list_size = meta.group(1), meta.group(2), meta.group(3)
    word_lists[i] = {"word_list": word_list, "category": spelling_category, "classification": classification, "size": list_size, "words": words, "count": word_count}
word_lists.sort(key=lambda x: x["size"])
##sizes = []
##categories = []
##classifications = []
##for word_list in word_lists:
##    size = word_list["size"]
##    category = word_list["category"]
##    classification = word_list["classification"]
##    if size not in sizes:
##        sizes.append(size)
##    if category not in categories:
##        categories.append(category)
##    if classification not in classifications:
##        classifications.append(classification)
##sizes.sort()
##for category in categories:
##    word_count = 0
##    for size in sizes:
##        for word_list in word_lists:
##            if (word_list["size"] == size) and (word_list["category"] == category):
##                word_count += word_list["count"]
##                print word_list["count"], "\t", word_count, "\t", word_list["word_list"]
#tlds = ["com", "net", "org", "edu"]
tlds = urllib2.urlopen("http://data.iana.org/TLD/tlds-alpha-by-domain.txt").readlines()
tlds = [string.replace(tld,'\n','') for tld in tlds]
for tld in tlds:
    if re.search("\A[a-zA-Z]*\Z", tld):
        f = open(tld + "-wordlist.txt", "w")
        for word_list in word_lists:
            if word_list["classification"]=="words":
                for word in word_list["words"]:
                    if re.search(tld + "$", word, re.IGNORECASE):
                        f.write("." + tld + "\t" + word + "\n")
        f.close()                    
            
            
    
        
