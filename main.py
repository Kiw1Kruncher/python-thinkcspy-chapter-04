from chat import chat

def responce(t):
    n = 1
    prompt = "who are you"
    print('### Temperature {}.0'.format(t))
    for i in range(5):
        print('Response {}:'.format(n), end =" ")
        print(chat(prompt, t))
        print('\n')
        n = n + 1

t = 1
for i in range(5):
    responce(t)
    t = t + 1
