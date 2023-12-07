#Jordan Lewis:

#Here's everyone in the class
everybody = {"Sakif", "Annie","Jarrod","Joseph",
             "Taylor","Daniel","Nathan","Brian",
             "Margaret","Angel","Andrew","Danielle"}

#Here's the people in class who want to play hopscotch and tag.
hopscotch = {"Taylor","Daniel","Nathan","Brian"}
tag = {"Jarrod","Joseph","Daniel","Nathan","Andrew"}


#Now Let the user to add a new person to the class who wants to plag hopscotch.
#HINT:  new_person1 will need to be added to TWO sets above.
new_person1 = input(("Enter a name of someone new who wants to do hopscotch: "))
everybody.add(new_person1)
hopscotch.add(new_person1)

#Now Let the user to add a new person to the class who wants to plag tag.
#HINT:  new_person2 will need to be added to TWO sets above.
new_person2 = input(("Enter a name of someone new who wants to do tag: "))
everybody.add(new_person2)
print(tag.add(new_person2))



#List the folks who don't want to do either activity
print("\nFolks who don't want to do either activity:")
print(set.difference(hopscotch,tag))


#Find the number of folks who want to do both activities
print("\nThe number of Folks who want to do both:")
print(set.intersection(hopscotch, tag))


#List who wants to do tag but not hopscotch
print("\nThe Folks who want to do tag but not hopscotch:")
print(tag.symmetric_difference(hopscotch))

#Find the percentage of people who want to do at least one of tag/hopscotch.
#The percentage should be shown rounded to 2 decimal places.
print("\nThe % of the class who want to do at least one of the activities:")
print(f"{(len(set.union(hopscotch, tag))) / len(everybody) * 100:.2f}%")
#print((len(set.union(hopscotch, tag))) / len(everybody) * 100)


#List anyone who wants to do one activity but not 2.
print("\nThe folks who want to do hopscotch or tag (but not both):")
print(set.union(hopscotch, tag))

