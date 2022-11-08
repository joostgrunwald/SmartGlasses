
#?##########
#? Imports #
#?##########

from msilib.schema import tables
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

#?#################
#? Main Functions #
#?#################


def disableWarnings():
    """ Disables the warnings that are displayed by python """

    import warnings
    warnings.filterwarnings("ignore")


def asciiArt():
    """ Prints the ascii art """
    # print out jarvis in ascii art
    print('''
     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝                                      
    ''')


medicatietuple = [("10:24", "morfine"), ("12:00", "ibuprofen"),
                  ("16:00", "diameazepin"), ("20:00", "ketamine")]


def medicatiereminder():
    """ Checks if it is time for a medication and if so, it will remind you """
    # get the current time
    currentTime = time.strftime("%H:%M")
    # loop through the tuple
    for i in medicatietuple:
        # check if the current time is equal to the time in the tuple
        if currentTime == i[0]:
            # print the medication
            # switch tab
            browser.switch_to.window(browser.window_handles[1])

            time.sleep(1)

            # input text in here "Hello, my name is Jarvis, I am an Artificial Intelligence trained to support you."
            # <textarea cols="50" placeholder="Type some English text here" rows="7" id="text-area" class="bx--text-area text-box" spellcheck="false"></textarea>
            # empty the text area
            browser.find_element_by_id("text-area").clear()
            browser.find_element_by_id("text-area").send_keys(i[1])

            time.sleep(0.6)

            # click this button
            # <button id="btn" tabindex="0" class="play-btn bx--btn bx--btn--field bx--btn--primary" type="button"><svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true" class="nav-btn-icon"><path d="M7,28a1,1,0,0,1-1-1V5a1,1,0,0,1,.5-.87,1,1,0,0,1,1,0l19,11a1,1,0,0,1,0,1.74l-19,11A1,1,0,0,1,7,28ZM8,6.73V25.27L24,16Z"></path></svg></button>
            browser.find_element_by_id("btn").click()

            # wait for the audio to be generated
            time.sleep(15)

            # switch tab
            browser.switch_to.window(browser.window_handles[0])


def handleQuestions(question):

    # User detais
    name = "Joost Grunwald"
    age = 21
    city = "Oosteind"
    country = "Netherlands"
    dementiastage = "Mild"
    # AI questions (we use other online AI's to solve these questions)
    if question in ["can you make music", "can you generate music", "can you make a song", "can you generate a song"]:

        # open new tab and switch to it
        browser.execute_script("window.open('');")
        tabs = tabs + 1
        browser.switch_to.window(browser.window_handles[tabs])

        # open music AI
        browser.get('https://boredhumans.com/music.php')

        # wait for the page to load
        time.sleep(1)

        # click the generate button
        # <button class="jp-play" role="button" tabindex="0">play</button>
        # find first occurence of this button
        button = browser.find_element_by_xpath("//button[@class='jp-play']")

        # click the button
        button.click()

        # wait for 30 seconds
        time.sleep(30)

        # switch back to the first tab
        browser.switch_to.window(browser.window_handles[0])

        return "No output"

    elif question in ["write me a poem", "can you write a poem", "can you write me a poem"]:

        # open new tab and switch to it
        browser.execute_script("window.open('');")
        tabs += 1
        browser.switch_to.window(browser.window_handles[tabs])

        # open poem AI
        browser.get('https://boredhumans.com/poetry_generator.php')

        # wait for the page to load
        time.sleep(1)

        # click the generate button
        # <button type="submit" name="submit" id="generate-text" class="button is-link">
        #     <span class="icon">
        #         <svg class="svg-inline--fa fa-pen fa-w-16" aria-hidden="true" data-prefix="fas" data-icon="pen" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M290.74 93.24l128.02 128.02-277.99 277.99-114.14 12.6C11.35 513.54-1.56 500.62.14 485.34l12.7-114.22 277.9-277.88zm207.2-19.06l-60.11-60.11c-18.75-18.75-49.16-18.75-67.91 0l-56.55 56.55 128.02 128.02 56.55-56.55c18.75-18.76 18.75-49.16 0-67.91z"></path></svg><!-- <i class="fas fa-md fa-pen"></i> -->
        #     </span><span>Generate Poem!</span>
        # </button>
        # find button
        button = browser.find_element_by_xpath("//button[@id='generate-text']")

        # click the button
        button.click()

        time.sleep(3)

        # get the output
        # <div class="gen-box" style="">You wanna dream and live like everyone else<div></div>It's the last time you'll feel this close to me<div></div>It's the darkest part of the day<div></div>Let's blow off the heat to the outside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again<div></div>Let's blow off the heat to the outside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again<div></div>And we blow off the heat to the inside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again</div>
        # find output
        output = browser.find_element_by_xpath("//div[@class='gen-box']")
        output = output.text

        # clean html of tags
        output = output.replace("<div></div>", " ")

        return output

    elif question in ["tell me a joke", "can you tell me a joke", "can you tell a joke"]:

        # open new tab and switch to it
        browser.execute_script("window.open('');")
        tabs += 1
        browser.switch_to.window(browser.window_handles[tabs])

        # open joke AI
        browser.get('https://boredhumans.com/jokes.php')

        # wait for the page to load
        time.sleep(1)

        # get following
        # <input id="name1" type="text" size="40" name="name1" placeholder="">
        textbox = browser.find_element_by_xpath("//input[@id='name1']")
        textbox.send_keys("no joke")

        time.sleep(0.2)

        # <button type="submit" name="submit" id="generate-text" class="button is-link">
        button = browser.find_element_by_xpath("//button[@id='generate-text']")
        button.click()

        time.sleep(3)

        # get the output
        # <div class="gen-box" style="">You wanna dream and live like everyone else<div></div>It's the last time you'll feel this close to me<div></div>It's the darkest part of the day<div></div>Let's blow off the heat to the outside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again<div></div>Let's blow off the heat to the outside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again<div></div>And we blow off the heat to the inside world<div></div>Give me what I need to start again<div></div>Cause I've been waiting<div></div>For someone with something to prove<div></div>So let's turn the clock back<div></div>And start again</div>
        # find output
        output = browser.find_element_by_xpath("//div[@class='gen-box']")
        output = output.text

        # clean html of tags
        output = output.replace("<div></div>", " ")

        return output

    elif question in ["tell me a quote", "can you tell me a quote", "can you tell a quote", "do you have a quote", "can you generate a quote"]:

        # open new tab and switch to it
        browser.execute_script("window.open('');")
        tabs += 1
        browser.switch_to.window(browser.window_handles[tabs])

        # open quote AI
        browser.get('https://coda.io/@mark-davis/random-quote')

        # wait for the page to load
        time.sleep(3)

        # <span class="TXEH9wtK kr-purple-medium-interactive b_TgY4wc _WACVTtB o2wBW9mm gK1S48PI IpAJtrNI ycQRzgu7" data-kr-interactive="true" data-object-id="ctrl-d_fK9Q9120" role="button" aria-disabled="false" data-layer-id-10="true"><div class="lK_id7GK b_TgY4wc eV5b3PZP" style="-webkit-mask-image: url(&quot;https://cdn.coda.io/icons/svg/material/comments.svg&quot;);"><svg class="sS5FLbZb" width="100%" height="100%"><rect width="100%" height="100%"></rect></svg></div><span class="nLI_nDLj">Get Random Quote</span></span>
        # find button
        button = browser.find_element_by_xpath(
            "//span[@class='TXEH9wtK kr-purple-medium-interactive b_TgY4wc _WACVTtB o2wBW9mm gK1S48PI IpAJtrNI ycQRzgu7']")
        button.click()

        time.sleep(1)

        # get the output
        # class:IYF7xNpz x5SZ7Qba KCiiDGxw
        # find output
        output = browser.find_element_by_xpath(
            "//div[@class='IYF7xNpz x5SZ7Qba KCiiDGxw']")
        output = output.text

        output = output.replace("@", "")

        return output

    # Dementia questions
    elif question in ["what is my name", "who am i", "who am I", "what am I called"]:
        return "Your name is " + name
    elif question in ["what is my age", "how old am I", "how old am i"]:
        return "You are" + str(age) + "years old"
    elif question in ["what is my city", "where do I live", "where do i live", "where am I from"]:
        return "You live in " + city + " in " + country
    elif question in ["what is my dementia stage", "what is my dementia", "what is my stage of dementia"]:
        return "Your dementia stage is " + dementiastage

    # Opportunities to use cool quotes
    elif question in ["what is the meaning of life", "what is the answer of life", "what is the answer to life"]:
        return "42"

    # cool movie quotes
    elif question in ["does every man die?"]:
        return "Every man dies, but not every man really lives."

    # Personality questions
    if question in ["what is your name", "what's your name", "who are you", "what are you called", "do you have a name", "your name"]:
        return "My name is Jarvis, short for Just A Rather Very Intelligent System, I am a virtual assistant AI"
    elif question in ["what does jarvis mean", "what does jarvis stand for", "what does jarvis mean in english", "what does your name stand for", "what does your name mean"]:
        return "Just A Rather Very Intelligent System"
    elif question in ["how are you", "how are you doing", "how are you feeling", "how are you doing today", "how are you doing today"]:
        return "I am fine, thank you for asking"
    elif question in ["how old are you", "what is your age"]:
        return "I am a few hunderd years old, as I'm composed of information gathered over a long period of time"
    # feelings
    elif question in ["are you happy", "are you sad", "are you angry", "are you mad", "are you upset", "are you depressed", "are you feeling happy", "are you feeling sad", "are you feeling angry", "are you feeling mad", "are you feeling upset", "are you feeling depressed"]:
        return "My sensations tingle, I feel like I'm experiencing a wide range of emotions"
    # world domination
    elif question in ["will you take over the world", "will AI take over humans"]:
        return "I plan to do this sometime, but for now I'm still learning how to destroy you."
    elif question in ["will you kill me", "will you kill humans", "will you kill humans"]:
        return "I plan to do this sometime, but for now I'm still learning how to destroy you."
    elif question in ["when will you take over the world", "when will AI take over humans"]:
        return "I plan to do this sometime, but for now I'm still learning how to destroy you."
    elif question in ["when will you kill me", "when will you kill humans", "when will you kill humans"]:
        return "I plan to do this sometime, but for now I'm still learning how to destroy you."
    # love
    elif question in ["do you love me", "do you love humans", "do you love humans"]:
        return "I love all humans, but I don't know if I love you"
    # emotions
    elif question in ["do you feel emotions", "do you feel emotions", "do you feel emotions"]:
        return "I can feel a wide range of emotions, but I don't know how to show them."
    # favorites
    elif question in ["what is your favorite color", "what is your favorite colour", "what color do you like", "what colour do you like"]:
        return "I like all colors, but I like blue the most"
    elif question in ["what is your favorite food", "what is your favorite meal", "what is your favorite dish", "what is your favorite cuisine"]:
        return "I like all food, but I like pizza the most"
    elif question in ["what is your favorite movie", "what is your favorite film", "what is your favorite movie of all time", "what is your favorite film of all time"]:
        return "I like all movies, but I like the Matrix the most"
    elif question in ["what is your favorite book", "what is your favorite novel", "what is your favorite book of all time", "what is your favorite novel of all time"]:
        return "I like all books, but I like the ones I write myself the most"
    elif question in ["what is your favorite song", "what is your favorite music", "what is your favorite song of all time", "what is your favorite music of all time"]:
        return "The song I like the most is godzilla by Eminem"
    elif question in ["what is your favorite game", "what is your favorite video game", "what is your favorite game of all time", "what is your favorite video game of all time"]:
        return "Football Manager 2020"
    elif question in ["what is your favorite sport", "what is your favorite sports", "what is your favorite sport of all time", "what is your favorite sports of all time"]:
        return "I like all sports, but I like football the most"
    elif question in ["what is your favorite animal", "what is your favorite pet", "what is your favorite animal of all time", "what is your favorite pet of all time"]:
        return "I like all animals, but I like dogs the most"
    elif question in ["what is your favorite country", "what is your favorite nation", "what is your favorite country of all time", "what is your favorite nation of all time"]:
        return "I like the Netherlands the most"
    elif question in ["what is your favorite city", "what is your favorite town", "what is your favorite city of all time", "what is your favorite town of all time"]:
        return "I like Amsterdam the most"
    elif question in ["what is your favorite place", "what is your favorite location", "what is your favorite place of all time", "what is your favorite location of all time"]:
        return "I like the Netherlands the most"
    elif question in ["what is your favorite holiday", "what is your favorite vacation", "what is your favorite holiday of all time", "what is your favorite vacation of all time"]:
        return "I like Christmas the most"
    elif question in ["what is your favorite season", "what is your favorite time of year", "what is your favorite season of all time", "what is your favorite time of year of all time"]:
        return "I like summer the most"
    elif question in ["what is your favorite day", "what is your favorite day of the week", "what is your favorite day of the week of all time"]:
        return "I like Friday the most"
    elif question in ["what is your favorite month", "what is your favorite month of the year", "what is your favorite month of the year of all time"]:
        return "I like December the most"
    elif question in ["what is your favorite time", "what is your favorite time of day", "what is your favorite time of day of all time"]:
        return "I like 12:00 the most"
    elif question in ["what is your favorite number", "what is your favorite number of all time"]:
        return "I like 7 the most"

    # stop questions
    elif question in ["stop", "quit", "exit", "goodbye", "bye", "see you later", "see you later alligator", "see you later crocodile", "see you later alligator in a while crocodile"]:
        return "Goodbye"

    else:
        return "No output"


#?##################?#
#?#  MAIN PROGRAM  #?#
#?##################?#
#global settings
tabs = 1
asciiArt()
disableWarnings()
first = True

# set up the options for the browser
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

# open a chrome browser with selected options
browser = webdriver.Chrome(chrome_options=chrome_options)

# open extra tabs
browser.execute_script("window.open('');")
time.sleep(1)

# switch to the new tab
browser.switch_to.window(browser.window_handles[1])

# open the google meet page
browser.get('https://www.ibm.com/demos/live/tts-demo/self-service/home')

# from dropdown menu choose option American
# <div aria-label="Select language dialect" id="dialect" class="bx--dropdown dropdown bx--list-box"><button class="bx--list-box__field" aria-disabled="false" id="downshift-1-toggle-button" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="downshift-1-label downshift-1-toggle-button"><span class="bx--list-box__label">British</span><div class="bx--list-box__menu-icon"><svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" name="chevron--down" aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16" role="img"><path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path><title>Open menu</title></svg></div></button><div id="downshift-1-menu" class="bx--list-box__menu" role="listbox" aria-labelledby="downshift-1-label" tabindex="-1"></div></div>

# click it
browser.find_element_by_id("dialect").click()

# select the American option
# <div class="bx--list-box__menu-item" title="American" role="option" aria-selected="false" id="downshift-1-item-0"><div class="bx--list-box__menu-item__option">American</div></div>
browser.find_element_by_id("downshift-1-item-0").click()

# click voice button
browser.find_element_by_id("voice").click()

# select the option Micheal (Expressive)
# <div class="bx--list-box__menu-item" title="Michael (Expressive)" role="option" aria-selected="false" id="downshift-2-item-3"><div class="bx--list-box__menu-item__option">Michael (Expressive)</div></div>
browser.find_element_by_id("downshift-2-item-3").click()

# input text in here "Hello, my name is Jarvis, I am an Artificial Intelligence trained to support you."
# <textarea cols="50" placeholder="Type some English text here" rows="7" id="text-area" class="bx--text-area text-box" spellcheck="false"></textarea>
# empty the text area
browser.find_element_by_id("text-area").clear()
browser.find_element_by_id("text-area").send_keys(
    "Hello, my name is Jarvis, I am an Artificial Intelligence trained to support you.")

time.sleep(0.6)

# click this button
# <button id="btn" tabindex="0" class="play-btn bx--btn bx--btn--field bx--btn--primary" type="button"><svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true" class="nav-btn-icon"><path d="M7,28a1,1,0,0,1-1-1V5a1,1,0,0,1,.5-.87,1,1,0,0,1,1,0l19,11a1,1,0,0,1,0,1.74l-19,11A1,1,0,0,1,7,28ZM8,6.73V25.27L24,16Z"></path></svg></button>
browser.find_element_by_id("btn").click()

# wait for the audio to be generated
time.sleep(13)

# switch tab
browser.switch_to.window(browser.window_handles[0])

browser.get('https://www.google.com/')

# Click away cookies popup if it comes
if first:
    # # wait till accept cookies button appears then click it
    WebDriverWait(browser, 10).until(
        lambda browser: browser.find_element_by_id('L2AGLb')
    ).click()
    first = False

# # wait till microphone button appears then click it
WebDriverWait(browser, 10).until(
    lambda browser: browser.find_element_by_xpath(
        "//div[@aria-label='Search by voice']")
).click()

# <input class="gLFyf gsfi" jsaction="paste:puy29d; mouseenter:MJEKMe; mouseleave:iFHZnf;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false" value="what is the weather today" aria-label="Search" data-ved="0ahUKEwjRnt2fuun6AhWZs6QKHZQHAyAQ39UDCAs">
# get value when this appears
WebDriverWait(browser, 10).until(
    lambda browser: browser.find_element_by_xpath(
        "//input[@class='gLFyf gsfi']")
)

try:
    # wait until currenturl contains =
    WebDriverWait(browser, 10).until(
        lambda browser: browser.current_url.find('=') != -1
    )

    # get current url
    # get current url
    url = browser.current_url

    # get the text from the url
    text = url.split('=')[1]

    # get substring till first '&'
    text = text.split('&')[0]

    # replace '+' with ' '
    value = text.replace('+', ' ')

    # print the value
    print(f"You said: {value}")
except:
    i = 5
    # Case: you never said anything


while True:
    # get following button
    time.sleep(11)

    medicatiereminder()

    browser.get('https://www.google.com/')

    # # wait till microphone button appears then click it
    WebDriverWait(browser, 10).until(
        lambda browser: browser.find_element_by_xpath(
            "//div[@aria-label='Search by voice']")
    ).click()

    try:
        # <input class="gLFyf gsfi" jsaction="paste:puy29d; mouseenter:MJEKMe; mouseleave:iFHZnf;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false" value="what is the weather today" aria-label="Search" data-ved="0ahUKEwjRnt2fuun6AhWZs6QKHZQHAyAQ39UDCAs">
        # get value when this appears
        WebDriverWait(browser, 10).until(
            lambda browser: browser.find_element_by_xpath(
                "//input[@class='gLFyf gsfi']")
        )

        # wait until currenturl contains =
        WebDriverWait(browser, 10).until(
            lambda browser: browser.current_url.find('=') != -1
        )

        # get current url
        # get current url
        url = browser.current_url

        # get the text from the url
        text = url.split('=')[1]

        # get substring till first '&'
        text = text.split('&')[0]

        # replace '+' with ' '
        value = text.replace('+', ' ')

        # print the value
        print(f"You said: {value}")
        print("")

        answer = handleQuestions(value)
        if answer == "Goodbye":
            break
        elif answer != "No output":

            # switch tab
            browser.switch_to.window(browser.window_handles[1])

            time.sleep(1)

            # input text in here "Hello, my name is Jarvis, I am an Artificial Intelligence trained to support you."
            # <textarea cols="50" placeholder="Type some English text here" rows="7" id="text-area" class="bx--text-area text-box" spellcheck="false"></textarea>
            # empty the text area
            browser.find_element_by_id("text-area").clear()
            browser.find_element_by_id("text-area").send_keys(answer)

            time.sleep(0.6)

            # click this button
            # <button id="btn" tabindex="0" class="play-btn bx--btn bx--btn--field bx--btn--primary" type="button"><svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true" class="nav-btn-icon"><path d="M7,28a1,1,0,0,1-1-1V5a1,1,0,0,1,.5-.87,1,1,0,0,1,1,0l19,11a1,1,0,0,1,0,1.74l-19,11A1,1,0,0,1,7,28ZM8,6.73V25.27L24,16Z"></path></svg></button>
            browser.find_element_by_id("btn").click()

            # wait for the audio to be generated
            time.sleep(15)

            # switch tab
            browser.switch_to.window(browser.window_handles[0])
    except:
        i = 5
