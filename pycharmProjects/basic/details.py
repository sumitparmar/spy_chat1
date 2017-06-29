from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('sumit parmar', 'Mr.', 21, 4.7)

friend_one = Spy('manish', 'Mr.', 4.7, 21)
friend_two = Spy('rajnish', 'Mr.', 4.7, 21)
friend_three = Spy('rajender', 'Mr.', 4.7, 21)


friends = [friend_one, friend_two, friend_three,]