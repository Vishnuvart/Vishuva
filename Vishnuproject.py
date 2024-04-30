Project in Python - Movie Website using Functions
[Should be done on jupyter notebook locally download Anaconda and Jupyter Notebooks]
So lets Assume you want to make a movies website, a very basic one with a lot of posters and their respective names on the main page and when you click on any one of them the trailer associated with that particular movie should start playing.

Lets make a program that will do so.

If you were to make this program what steps will you take to write this program pls write in the live CHAT?
[ don't worry about the code, in plane english just identify the steps that you will take to make this work eg - step1 do this , step2 do that ]

One possible ANSWER
we will crete 2 functions one to show the trailer of the movie
and an other to show the poster and the name of the movie.
CODE:
Lets start with writing the code for this project. First lets declare the function and lets continue from there step by step.


def show_trailer():
  # Open Browser and play trailer

def show_info():
  # Print movie information
     
So now imagine we want to run this program and we want to play a movies trailer. Well but which movies trailer, so in order to make that work we will need to supply in the arguments to the function so that we can tell the program which movie as well as what trailer we need to the played.

So lets feed in the arguments that is needed.


def show_trailer(title, youtube_url):
  # Open Browser and play trailer

def show_info():
  # Print movie information
     
now lets try to do the same thing with show_info. again as we dont know which movies info, we will need to supply in the function with some arguments.


def show_trailer(title, youtube_url):
  # Open Browser and play trailer

def show_info(title, storyline, release_date, rating, youtube_url, director, box_office):
  # Print movie information
     
Now as it is evident that even with such a little info the fuction show_info() has already become too convoluted.

What we need to do is to create a template for a movie and record all the data that needs to go into that template. Data like title and storyline as well as functions like show_trailer() and show_info().

And then simply say that Avengers is a movie and similarly iron man is a movie. and then have the ability to say show me Iron Man trailer or show me details of Avengers, with no arguments necessary. Now this is someting that we are going to study next under OOPS ie. classes etc.

But what if we still want to do it using only functions is to take a template that we have defined and make multiple copies of it.

so we will have to make:

1> avengers.py

title = "avenger"
youtube_url = "www.youtube.com"
storyline = "A band of heros come together against all odds to save the earth"
rating = "10/10"


def show_trailer():
  # Open Browser and play trailer

def show_info():
  # Print movie information
after we have done this for each and every movie we will can then call the functions to play their trailer or show their info.

what if we want to rename our functions or add more data for each movie we will have to edit each and every python files that are present for each movie. This is not a smart work.

so at the end of the day what we need is a way to make copies of a template without making multiple files. We can just create a template and just say that Avengers is a type of that template. And this new template is what we call as a class. We will be learning more about classes in the next module.
