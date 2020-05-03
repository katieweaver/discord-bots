import os

def bee_movie():

    #mydir = 'C:\Users\Katie Weaver\Documents\Builds\discord-bots'
    #myfile = '\bee_script.txt'

    file_name = os.path.join("C:", "Users", "Katie Weaver", "Documents", "Builds", "discord-bots", "bee_script.txt")

    with open(r'C:\Users\Katie Weaver\Documents\Builds\discord-bots\bee-script.txt', 'r') as script:
        for line in script:
            for word in line.split():
                #print(word)
                yield(word)
