import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['an old man', 'a boy', 'a man', 'a magician','a police man']
name = ['Daniel', 'Neil', 'Vedant']
residence = ['Boston','India', 'Germany', 'Switzerland', 'England']
went = ['his friends house','university','cinema', 'school', 'park']
happened = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))