# Homework 00

## Due Date

This assignment is due on Monday January 27, 2020 at 11:59 PM.

## Learning goals

The main goals of this assignment are to become familiar with the homework access and submission system and confirm that you can run the various technologies that we will be using in this class. This includes:

1. Connecting to GitHub Classroom.
1. Cloning a repository of starter code.
1. Running the CS181U Docker.
1. Running python, z3, and NuSMV in Docker.
1. Editing and committing solution files.
1. Submitting a completed assignment. 


## GitHub Classroom

If you do not already have a GitHub Classroom account you will need to create one. You can do so on their website. If you already have a GitHub account, I think that automatically gives you a GitHub Classroom account, so try your GitHub credentials first.

https://classroom.github.com

## Accept the Homework-00 Repository

As long as you have a GitHub Classroom Account, you can accept an invitation to the Homework-00 starter code repository by following this link

https://classroom.github.com/g/3hZ9u3f3

You might first need to add yourself to the classroom and then grant GitHub classroom access to your regular GitHub account by "linking" your accounts. Instructions should be provided when you follow the steps after clicking the link. This will allow GitHub classroom to copy over the template repo of starter code into your account.

If you have any trouble, please remember to post on Piazza!


## Run the CS181U Docker

We will be using Docker so that all of us can run the required software without having to install a bunch of dependencies. Docker is available in the the HMC Computer Science Labs. You might also try installing Docker on your own machine, but this is not necessary. We will offer limited support for getting Docker running on your own machine, since we assume that you can use the labs, or at least one out of two programming partners should be able to use Docker. 

On a lab computer, **signed in as guest**, you can open a terminal (inside of VS Code, if you like) and run the following command. This will download the Docker image for this course, which contains all necessary software and dependencies, and then run it. 

```
docker run -v $(pwd):/home/student/cs181u -it harveymudd/cs181 /bin/zsh
```


- `docker` starts up the Docker program.
- `run` says that you want to run a Docker container (rather than build, tag, push, etc.), downloading it if necessary. 
- `-v` says that we are going to mount a Docker **v**olume, or file system to a location on our local system. The argument to the `-v` flag says that we are going to connect the *present working directory* (pwd) to the `home/student/cs181U` directory inside the running Docker container. This way, you can edit files on your local machine, and run them inside of the Docker virtual environment which has everything that you need already installed. 
- `-i` is for interactive mode, meaning that you will get a command prompt when it starts. 
- `-t` is the Docker tag to run, which in this case is harveymudd/cs181.
- `/bin/zsh` is the terminal shell that will start up in Docker.

## Part a: a python-z3 program

In this part of the assignment, you will run a python-z3 program. Z3 is an automated theorem prover that we will use in this course. You don't need to have a deep understanding of what it does right now, just be able to have a very basic understanding of what it does and how to run it. 

In directory `part-a`, you will find a file named `z3-test.py`. Open this file in a code editor (say, VS Code) and read over the file. You should be able to run this file **inside of the CS181U Docker** with the command

```
python3 z3-test.py
```

Confirm that you get this output:

```
[And(Not(a), b, x > 0, x < 100, x < y)]
sat
[x = 99, y = 100, b = True, a = False]

[And(Not(a), b, x > 0, x < 100, x < y), y < 1]
unsat
```

### To complete this part of the assignment

Inside of the file `answer-a.md`, write a paragraph or two explaining what the code in `z3-test.py` does and how to interpret the meaning of the output.

**After you do this, add, commit, and push to github.**

## Part b: a simple logic language

Inside of directory `part-b`, there is a file called `propositional_logic.py`. Take a look at this file. Again, you don't need a deep understanding right now. Just take note of which classes have been defined: BoolConst, BoolVar, Not, And, etc. 

We are going to use these classes to construct objects that represent propositional formulas. 

**Spoiler alert:**  eventually, we will write a simple satisfiability checker and some other fun procedures for this propositional logic language defined by these classes. In fact, we will take the first steps toward that in Homework-01.

The file `examples.py` makes use of the classes defined in `propositional_logic.py`. Take a look at that file and get an idea of what it is doing. You can run that file like this:

```
python3 examples.py
```

which should produce output like this:

```
And(BoolConst(True), BoolConst(False))
(T & F)

Or(BoolConst(True), BoolConst(True))
(T | T)

Implies(And(BoolConst(True), BoolConst(False)), Not(Or(BoolConst(True), BoolConst(True))))
((T & F) => ~(T | T))

And(And(BoolConst(True), BoolConst(False)), BoolVar(A))
((T & F) & A)

Iff(And(And(BoolConst(True), BoolConst(False)), BoolVar(A)), And(BoolConst(True), BoolConst(False)))
(((T & F) & A) <=> (T & F))

Not(Iff(And(And(BoolConst(True), BoolConst(False)), BoolVar(A)), And(BoolConst(True), BoolConst(False))))
~(((T & F) & A) <=> (T & F))

```

### To complete this part of the assignment

Edit the file `answer-b.py`. Write code using the variables A, B, and C, defined in that file, along with the classes from propositional_logic.py
and the provided `.format()` method to output the expression:

```
(((A => B) & (B => C)) => (A => C))
```

**Don't forget to add, commit, and push!**

## Part c: symbolic model verifier

This is the last part of the assignment. In directory `part-c`, there is a file called `request.smv`. The `.smv` extension stands for **S**ymbolic **M**odel **V**erifier. 

Take a look at the file `request.smv`. This file defines a symbolic model of a very simple request system. 

It defines a module named `main`, a variable `request` that can either be `Yes` or `No`, and a variable `state` that can either be `ready` or `busy`. Next it defines a transition system (a.k.a. finite state machine, kind of like a DFA or NFA) where 

- the initial state is `ready`
- if it is in the ready state and there is a request, then in the `next` time instant, state changes to the busy state (to simulate processing the request)
- otherwise, in the `next` time instant, the state could switch to either `ready` or `busy`, and we just don't know which!

Finally, the last line is a specification to check about the system:

``` 
AG((request = Yes) -> AF state = busy)
```

That last line is a statement in temporal logic:

- `AG` is an operator that roughly translates to 'starting in any possible state the system could ever be in'

- `AF` is an operator that roughly translates to 'eventually, in all possible future system behaviors'


So the whole specification says something like, 'no matter what state the system gets into, if there is a request, then eventually the system becomes busy.'

**Spoiler Alert**: in this class, we will eventually learn some pretty cool algorithms for deciding if a system satisfies a specification written in temporal logic.

For now, we can just use a program called NuSMV to decide if the transition system satisfies this property or not. On the Docker command line, inside of the `part-c` directory:

```
smv request.smv
```

This should generate a big block of text about NuSMV, but at the end, it should give you a single line that tells you if the system satisfies the specification. 


### To complete this part of the assignment

Edit the file `answer-c.md`. Paste in the last line of output from running NuSMV on the file.

**Remember to add, commit, and push!!**

