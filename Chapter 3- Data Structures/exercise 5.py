#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.
guest_list = ['ali', 'haider', 'soban', 'usman']
print(f"Unfortunately, {guest_list[2]} can't make it to the dinner.")
guest_list[2] = 'abubakar'
for guest in guest_list:
 print(f"Dear {guest}, please come to dinner at my place on sunday!") 