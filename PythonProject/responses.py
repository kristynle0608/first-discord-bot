from random import choice, randint

oogway = [
    '"Whoever holds this long stick is gay."',
    '"You may wish for an apple or an orange, but you will get a peach.',
    'Quit, don\'t quit. Noodles, don\'t noodles. You are too concerned with what was and what will be."',
    '"Mmmmh, monke..."',
    '"My time has come."',
    '"Yesterday is history, Tomorrow is a mystery but Today is a gift. That is why it is called the present."',
    '"One often meets his destiny on the road that he takes to avoid it."'
]

inspire = [
    'No matter what anybody tells you, words and ideas can change the world.',
    'With great power comes great responsibility.',
    'You are who you chose to be.',
    'Life\'s like a movie, write your own ending.',
    'All we have to decide is what to do with the time that is given to us.',
    'A true master is an eternal student.'
]

encourage = [
    'Do or do not. There is no try.',
    'Life is pain, highness. Anyone who says differently is selling something.',
    'What is broken can be reforged.'
    'Sometimes icy heart just needs warm smile.',
    'The darker the night, the brighter the stars.',
    'Never give up. You\'re a trash can, not a trash cannot.',
    'You can do it!',
    'Go and make some mistakes, you live and you learn.'
]

help: str = ( "```!oogway: shows Oogway quotes.\n"
    "!inspire: shows inspiring quotes.\n"
    "!encourage: shows encouraging quotes.\n"
    "!death: shows the infamous Yasuo quote.\n"
    "!hello: bot greets back.\n"
    "!how are you: bot answers good.\n"
    "!bye: bot says goodbye.\n"
    "!roll dice: roll a dice.```"
)

def get_response(user_input: str, username: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'oogway':
        return choice(oogway) + ' - Oogway'
    elif 'inspire' in lowered:
        return choice(inspire)
    elif 'encourage' in lowered:
        return choice(encourage)
    elif 'death' in lowered:
        return 'Death is like the wind, always by my side.'
    elif 'helpme' in lowered:
        return help
    elif 'hello' in lowered:
        return 'Hello, username!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...', 'What are you talking about?'])