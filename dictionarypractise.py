#Write a program to read through the mailbox.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

newdict = dict()
bigname = None
bignumber = None
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("From "):
        continue

    else:
      name = line.split()[1]
      newdict[name] = newdict.get(name,0) + 1
for name,number in newdict.items():
    if bignumber is None or number > bignumber:
        bigname = name
        bignumber = number
print(bigname, bignumber)
