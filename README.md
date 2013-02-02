# poem2anki

_Create flashcards from text files of poems._

Poem2anki is a small Python script designed to convert lines of poetry into flash cards into the Open Source [Anki](http://ankisrs.net/anki2.html) system created by Damien Elmes.  

## The Idea

It's easy to find most classic poems on the web and copy and paste them into a text editor.  Save the result as plain text -- not Rich Text, HTML, or Word format -- and then run this script on it, and it will produce a tab-separated text file suitable for import into Anki as a new card deck.  

The basic idea is that Anki will prompt you with a few lines of a poem and you need to respond with the next line.  For example:

_Question:_

    This day is call’d the feast of Crispian.  
    He that outlives this day, and comes safe home,  
    Will stand a tip-toe when this day is nam’d,

_Answer_:

    And rouse him at the name of Crispian.

On the next card, everything will have moved down one line:

_Question:_:

    He that outlives this day, and comes safe home,  
    Will stand a tip-toe when this day is nam’d,  
    And rouse him at the name of Crispian.

_Answer_:

    He that shall live this day, and see old age,

By default, after the first couple of cards, there are three lines of poem on the front (question) part of the card, and the following line then forms the 'answer' on the back.   You can change how many lines are in the question and answer by using the _-q_ and _-a_ options when running the script.

For best effect, read the lines out loud to yourself when studying the cards.  Spoken words are much more memorable than read ones, especially when it comes to poetry.

## Using poem2anki

You need a reasonably recent version of python and the argparse library.  (argparse seems to get installed along with Python by default on Windows).

Exactly _how_ you run a Python script on your machine will depend on your operating system.  On a Mac or Linux machine, you should do something like:

    ./poem2anki.py < sonnet18.txt > sonnet18.tsv

or perhaps

    python poem2anki.py < sonnet18.txt > sonnet18.tsv

in a terminal window to convert the sample _Shall I compare thee?_ file.

On Windows, you'll need to install [Python](http://www.python.org) first (which isn't hard) and then do something like:

    c:\python27\python.exe poem2anki.py < sonnet18.txt > sonnet18.tsv

at a command prompt.

You can import the result into Anki using the desktop client, after which you can sync it to [AnkiWeb](https://ankiweb.net/decks/).

* In the desktop Anki, click 'Deck' to take you to the list of decks, then click 'Import'

* Pick the file you just generated and make sure that the type is set to 'Text file separated by tabs or semicolons' and open it.

* Click on the 'Deck' button to choose the deck to which they should be added, or to create a new one.

* When that's done, check that Anki has detected that the fields are separated by tabs, select the option to allow HTML in the fields (if your Anki has that option) because we use it for line breaks, and click _Import_.



## Author

poem2anki was created by [Quentin Stafford-Fraser](http://qandr.org/quentin).

