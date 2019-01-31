# -*- coding: UTF-8 -*-
#Python libraries that we need to import for our bot
import logging
import random
import os
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'ACCESS_TOKEN'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

#CalculatorRecogValues
ADD = ['+', 'plus', 'added']
SUBTRACT = ['-', 'minus', 'subtracted']
MULTIPLY = ['x', 'times', 'multiplied']
DIVIDE = ['/', 'divided']

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    userMessage = message['message'].get('text').lower()
                    response_sent_text = get_message_type(userMessage)
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

#chooses a random message to send to the user
def get_message_type(userMessage):
    if 'joke' in userMessage:
        response = joke_request()
    elif 'quote' in userMessage:
        response = quote_request()
    elif self.ADD in userMessage:
        response = calculator_request(add, userMessage)
    else:
        response = 'Please Try Again'
    # return selected item to the user
    return response

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def calculator_request(operationType, userMessage):
	return "Adding"


def joke_request():
    jokes = [
        "What happens to a frog's car when it breaks down?\nIt gets toad away.",
        "Why was six scared of seven?\nBecause seven \"ate\" nine.",
        "How do astronomers organize a party?\nThey planet.",
        "Want to hear a Potassium joke?\nK.",
        "A photon walks into a hotel. The desk clerk says, \"Welcome to our hotel. Can we help you with your luggage?\"\nThe photon says, \"No thanks, I'm traveling light.\"",
        "What did the 30 degree angle say to the 90 degree angle?\n\"You think you're always right!\"",
        "Wife: \"I look fat. Can you give me a compliment?\"\nHusband: \"You have perfect eyesight.\"",
        "I changed my password to \"incorrect\". So whenever I forget what it is, the computer will say \"Your password is incorrect\".",
        "When an employment application asks who is to be notified in case of emergency, I always write, \"A very good doctor\".",
        "If you think nobody cares whether you're alive, try missing a couple of payments.",
        "I hate when I am about to hug someone really sexy and my face hits the mirror.",
        "Did you hear about the guy whose whole left side was cut off?\nHe's all right now.",
        "Two atoms are walking down the street. One says, \"Oh no! I lost an electron!\", The other asks him, \"Are you sure?\", The first one says, \"Yeah, I'm positive\"",
        "What time did the man go to the dentist?\nTooth hurt-y.",
        "Astronomers got tired of watching the moon go round the earth for 24 hours, so they decided to call it a day.",
        "What do you call a fish with no eyes?\nFsh.",
        "What did the green grape say to the purple grape?\nBreathe, you fool, breathe!",
        "I'm reading a book about anti-gravity.\nIt's impossible to put down.",
        "I wondered why the baseball was getting bigger.\nThen it hit me.",
        "I used to be a banker, but I lost interest.",
        "Why do seagulls fly over the sea?\nBecause they aren't bay-gulls!",
        "Why was the javascript developer sad?\nBecause he didn't Node how to Express himself.",
        "How did the hipster burn the roof of his mouth?\nHe ate the pizza before it was cool.",
        "How did Darth Vader know what Luke was getting for Christmas?\nHe felt his presents.",
        "What's red and bad for your teeth?\nA Brick.",
        "What's orange and sounds like a parrot?\nA Carrot.",
        "How many tickles does it take to tickle an octopus?\nTen-tickles!",
        "At the rate law schools are turning them out, by 2050 there will be more lawyers than humans.",
        "Why did the turkey cross the road?\nTo prove he isn't a chicken.",
        "Why was 6 afraid of 7?\nBecause 7 8 9.",
        "A mom picks her son from school\nMom: What did you learn at school today?\nSon: Apparently not enough, I have to go back tomorrow.",
        "I introduced my girlfriend to my family today\nThe kids really liked her, but my wife seemed mad.",
        "Why can't atheists solve exponential problems?\nBecause they don't believe in higher powers.",
        "Mike, do you think I'm a bad mother?\nMy name is Paul.",
        "When I see lovers' names carved in a tree, I don't think it's sweet. I just think it's surprising how many people bring a knife on a date.",
        "Why did the shark keep swimming in circles?\nIt had a nosebleed.",
        "Pessimist: Things just can't get any worse!\nOptimist: Nah, of course they can!",
        "What goes up and down, but never moves?\nThe stairs.",
        "A family of mice were surprised by a big cat. Father Mouse jumped and and said, \"Bow-wow!\" The cat ran away.\n \"What was that, Father?\" asked Baby Mouse. \n\"Well, son, that's why it's important to learn a second language.\"",
        "Patient: Doctor, I have a pain in my eye whenever I drink tea.\nDoctor: Take the spoon out of the mug before you drink.",
        "Mother: \"Did you enjoy your first day at school?\"\nGirl: \"First day? Do you mean I have to go back tomorrow?",
        "What did the hot-dog say when he needed to use the bathroom?\nMust-Turd",
        "What kind of bagel can fly?\nA Plain Bagel.",
        "Where do animals go when their tails fall off?\nA retail store ;)",
        "What was Forrest Gump's password?\n1Forrest1."
      ]
    return random.choice(jokes)

def quote_request():
    quote = [
    "Don't cry because it's over, smile because it happened. ― Dr. Seuss",
    "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best. ― Marilyn Monroe",
    "You've gotta dance like there's nobody watching, Love like you'll never be hurt, Sing like there's nobody listening, And live like it's heaven on earth. ― William W. Purkey",
    "You only live once, but if you do it right, once is enough. ― Mae West",
    "In three words I can sum up everything I've learned about life: it goes on. ― Robert Frost",
    "To live is the rarest thing in the world. Most people exist, that is all. ― Oscar Wilde",
    "Insanity is doing the same thing, over and over again, but expecting different results. ― Narcotics Anonymous",
    "It is better to be hated for what you are than to be loved for what you are not. ― André Gide, Autumn Leaves",
    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle. ― Albert Einstein",
    "Life is what happens to you while you're busy making other plans. ― Allen Saunders",
    "It does not do to dwell on dreams and forget to live. ― J.K. Rowling, Harry Potter and the Sorcerer's Stone",
    "Good friends, good books, and a sleepy conscience: this is the ideal life. ― Mark Twain",
    "I may not have gone where I intended to go, but I think I have ended up where I needed to be. ― Douglas Adams, The Long Dark Tea―Time of the Soul",
    "Sometimes the questions are complicated and the answers are simple. ― Dr. Seuss",
    "Everything you can imagine is real. ― Pablo Picasso",
    "Today you are You, that is truer than true. There is no one alive who is Youer than You. ― Dr. Seuss, Happy Birthday to You!",
    "I'm not afraid of death; I just don't want to be there when it happens. ― Woody Allen",
    "Sometimes people are beautiful. Not in looks. Not in what they say. Just in what they are. ― Markus Zusak, I Am the Messenger",
    "Life isn't about finding yourself. Life is about creating yourself. ― George Bernard Shaw",
    "Some infinities are bigger than other infinities. ― John Green, The Fault in Our Stars",
    "Things change. And friends leave. Life doesn't stop for anybody. ― Stephen Chbosky, The Perks of Being a Wallflower",
    "The only way out of the labyrinth of suffering is to forgive. ― John Green, Looking for Alaska",
    "When someone loves you, the way they talk about you is different. You feel safe and comfortable. ― Jess C. Scott, The Intern",
    "I'm the one that's got to die when it's time for me to die, so let me live my life the way I want to. ― Jimi Hendrix, Jimi Hendrix - Axis: Bold as Love",
    "But better to get hurt by the truth than comforted with a lie. ― Khaled Hosseini",
    "The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time. ― Mark Twain",
    "We are what we pretend to be, so we must be careful about what we pretend to be. ― Kurt Vonnegut, Mother Night",
    "The one you love and the one who loves you are never, ever the same person. ― Chuck Palahniuk, Invisible Monsters",
    "I speak to everyone in the same way, whether he is the garbage man or the president of the university. ― Albert Einstein",
    "If you don't know where you're going, any road'll take you there. ― George Harrison",
    "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared. ― Buddha",
    "To be happy, we must not be too concerned with others. ― Albert Camus",
    "The moments of happiness we enjoy take us by surprise. It is not that we seize them, but that they seize us. ― Ashley Montagu",
    "Perhaps they are not stars, but rather openings in heaven where the love of our lost ones pours through and shines down upon us to let us know they are happy. ― Eskimo Proverb",
    "Sometimes your joy is the source of your smile, but sometimes your smile can be the source of your joy. ― Thich Nhat Hanh",
    "Love is that condition in which the happiness of another person is essential to your own. ― Robert A. Heinlein",
    "Happy people plan actions, they don't plan results. ― Dennis Waitley",
    "Happiness is when what you think, what you say, and what you do are in harmony. ― Mahatma Gandhi",
    "The only joy in the world is to begin. ― Cesare Pavese",
    "Some cause happiness wherever they go; others whenever they go. ― Oscar Wilde",
    "Time you enjoy wasting is not wasted time. ― Marthe Troly-Curtin",
    "Nobody can be uncheered with a balloon. ― Winnie the Pooh",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. ― Herman Cain",
    "What you do not want done to yourself, do not do to others. ― Confucius",
    "Happiness is not something ready-made. It comes from your own actions. ― Dalai Lama",
    "When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us. ― Helen Keller",
    "Happiness depends upon ourselves. ― Aristotle",
    "It is more fitting for a man to laugh at life than to lament over it. ― Seneca",
    "It's been my experience that you can nearly always enjoy things if you make up your mind firmly that you will. ― L.M. Montgomery",
    "Most people would rather be certain they're miserable, than risk being happy. ― Dr. Robert Anthony",
    "The unhappy derive comfort from the misfortunes of others. ― Aesop",
    "For many men, the acquisition of wealth does not end their troubles, it only changes them. ― Seneca",
    "A table, a chair, a bowl of fruit and a violin; what else does a man need to be happy?. ― Albert Einstein",
    "Of all forms of caution, caution in love is perhaps the most fatal to true happiness. ― Bertrand Russell",
    "I'd far rather be happy than right any day. ― Douglas Adams",
    "Everyone wants to live on top of the mountain, but all the happiness and growth occurs while you're climbing it. ― Andy Rooney",
    "The foolish man seeks happiness in the distance, the wise grows it under his feet. ― James Oppenheim",
    "Action may not always bring happiness; but there is no happiness without action. ― Benjamin Disraeli",
    "Happiness is nothing more than good health and a bad memory. ― Albert Schweitzer",
    "Our envy always lasts longer than the happiness of those we envy. ― Heraclitus",
    "Happiness is a how; not a what. A talent, not an object. ― Herman Hesse",
    "No act of kindness, no matter how small, is ever wasted. ― Aesop",
    "Just because it didn't last forever, doesn't mean it wasn't worth your while. ― Unknown",
    "Your work is discover your world and then with all your heart give yourself to it. ― Buddha",
    "That man is richest whose pleasures are cheapest. ― Henry David Thoreau",
    "Happiness always looks small while you hold it in your hands, but let it go, and you learn at once how big and precious it is. ― Maxim Gorky",
    "Gratitude is a vaccine, an antitoxin, and an antiseptic. ― John Henry Jowett",
    "No one can make you feel inferior without your consent. ― Eleanor Roosevelt",
    "And remember, no matter where you go, there you are. ― Confucius",
    "If you are too busy to laugh, you are too busy. ― Proverb",
    "Security is mostly a superstition. It does not exist in nature…. Life is either a daring adventure or nothing. ― Helen Keller",
    "Real integrity is doing the right thing, knowing that nobody’s going to know whether you did it or not. ― Oprah Winfrey",
    "It’s not that I’m so smart, it’s just that I stay with problems longer. ― Albert Einstein",
    "Obstacles are those frightful things you see when you take your eyes off your goal. ― Henry Ford",
    "The problem with the world is that the intelligent people are full of doubts, while the stupid ones are full of confidence. ― Charles Bukowski",
    "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that. ― Martin Luther King, Jr.",
    "Those who are not looking for happiness are the most likely to find it, because those who are searching forget that the surest way to be happy is to seek happiness for others. ― Martin Luther King, Jr.",
    "We must develop and maintain the capacity to forgive. He who is devoid of the power to forgive is devoid of the power to love. There is some good in the worst of us and some evil in the best of us. When we discover this, we are less prone to hate our enemies. ― Martin Luther King, Jr.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. ― Martin Luther King, Jr.",
    "Faith is taking the first step even when you can't see the whole staircase. ― Martin Luther King, Jr.",
    "Science without religion is lame, religion without science is blind. ― Albert Einstein",
    "The person who follows the crowd will usually go no further than the crowd. The person who walks alone is likely to find himself in places no one has ever seen before. ― Albert Einstein",
    "I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world. ― Albert Einstein",
    "I have no special talents. I am only passionately curious. ― Albert Einstein",
    "The most beautiful experience we can have is the mysterious. It is the fundamental emotion that stands at the cradle of true art and true science. ― Albert Einstein",
    "Everything must be made as simple as possible. But not simpler. ― Albert Einstein",
    "Education is the most powerful weapon which you can use to change the world. ― Nelson Mandela",
    "A good head and good heart are always a formidable combination. But when you add to that a literate tongue or pen, then you have something very special. ― Nelson Mandela",
    "No one is born hating another person because of the color of his skin, or his background, or his religion. People must learn to hate, and if they can learn to hate, they can be taught to love, for love comes more naturally to the human heart than its opposite. ― Nelson Mandela",
    "One of the things I learned when I was negotiating was that until I changed myself, I could not change others. ― Nelson Mandela",
    "A leader is like a shepherd. He stays behind the flock, letting the most nimble go out ahead, whereupon the others follow, not realizing that all along they are being directed from behind. ― Nelson Mandela",
    "The best preparation for tomorrow is doing your best today. ― H. Jacksn Brown Jr",
    "I can't change the direction of the wind, but I can always adjust my sails to always reach my destination. ― Jimmy Dean",
    "My mission in life is not merely to survive, but to thrive; and to do so with some passion, compassion, humour, and some style. ― Maya Angelou"
      ]
    return random.choice(quote)

if __name__ == "__main__":
    app.run()