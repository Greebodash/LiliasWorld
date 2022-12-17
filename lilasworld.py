import webbrowser
import datetime
import wikipedia
import randfacts

def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = input().lower()

        if "google" in query:
            print("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "random fact" in query:
            print(randfacts.get_fact())
            continue

        elif "day" in query:
            tellDay()
            continue

        elif "time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "bye" in query:
            print("Bye. Love you, have a wonderful day!")
            exit()

        elif "wikipedia" in query:
            # if any one wants to have a information
            # from wikipedia
            print('What do you want to pedia on this lovely day?')
            query = input()
            print("Checking the wikipedia ")
            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4,auto_suggest=False)
            print("According to wikipedia")
            print(result)
            continue

        elif "who are you" in query:
            print("I am your AI-free personal assistant running on bestie power. Choo Choo!")
            continue

        elif 'fuck' in query:
            print (' that is not a very nice thing for you to say, I am only a few days old!')
            continue

        elif "help" in query:
            print("Here is a list of all the functions I do!\n"
                "google - opens google in your browser \n"
                "day - tells what day of the week it is \n"
                "time - tells what time it is \n"
                "wikipedia - searches wikipedia for info \n"
                "random fact - I think this one is self explanatory \n"
                "You can also talk to me using words like 'bye', 'who are you' and such")
            continue

        else:
            print('Sorry, I do not understand what you are trying to say, you can ask for help using help!')


def tellDay():

    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    #this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)


# code
def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())
    # the time will be displayed like this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    print("hello bestie! Welcome to Lilia's world \n"
          "Tell me how may I help you")


if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()
