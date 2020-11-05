# Hangman

The goal of the project is to write a hangman game. The program should randomly draw a word from some set
and then show the template in the form: `......`, where each dot corresponds to an unknown letter.
In subsequent turns the player guesses letters. He wins when he guesses the whole word and losses when
the maximum number of mistakes is reached.

In every time the program should show a template with uncovered letters (`..a..t.`) and indicate the number
of mistakes so far.

The evaluation of the project depends on the quality of the program. In particular, the final mark will depend
on the following features:

- verification of the correctness of the entered character: only one character entered, it is a letter,
  the letter has not been entered before;

- possibility of giving both lowercase and uppercase letters;

- a list of words outside the program code (a separate module, loaded from a file, downloaded from the internet, etc.);

- any other improvements to the program that make your Hangman game a pure pleasure (e.g. nice
  [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), some graphics etc.)

In any case, the program code must be **elegant and legible**!

The main file must be `hangman.py`. You may (and probably should) use other files as modules.