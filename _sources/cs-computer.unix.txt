Unix-related
""""""""""""
.. contents:: `Table of contents`
   :depth: 2
   :local:

###############################################
terminal, shell, tty, console...the difference?
###############################################
http://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con

In unix terminology, the short answer is that

- **terminal** = tty = text input/output environment
- **console** = physical terminal
- **shell** = command line interpreter


Terminal is synonymous to tty (tty is what's running on each of my tab)

.. rubric:: shell

- A **shell** is the primary interface that users see when they log in, whose primary purpose is to start other programs.
- In unix circles, **shell** has specialized to mean a command-line shell, centered around entering the name of the application one wants to start, followed by the names of files or other objects that the application should act on