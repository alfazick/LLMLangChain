
# Mini Project: Using RAG To implement Question Answering
Example serves as a proof of concept

pdf is obtained from https://pages.cs.wisc.edu/~remzi/OSTEP/

## Operating Systems: Three Easy Pieces
Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau (University of Wisconsin-Madison)
##
Probably the best book about Systems Programming and Operating Systems.

## Chapter4: The Abstraction: The Process ##
https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf

### Steps ToDO:

1) Load the document
2) Split the document into chunks
3) Embed the documents to vector store
4) Define the retriever
5) Setup chat dialog with completion, which uses provided document
### 

***
Technology stack:
LangChain + Chroma
LLM used OpenAI
***

Sample output:

***
The Abstraction: The Process
In this chapter, we discuss one of the most fundamental abstract ions that
the OS provides to users: the process . The deﬁnition of a process, infor-
mally, is quite simple: it is a running program.
***

``` Enter your query: what is a process? ```

```
In the context of the document provided, a process is defined as 
a running program.
```

``` Enter your query: what is running program```

```
A running program in the context of the document provided refers 
to a program that is actively executing on a computer system. 
It is mentioned that one often wants to run more than one program at once, 
such as a web browser, mail program, game, music player, etc. 
The document also discusses understanding the machine state of a program, 
which includes what parts of the machine are important to the execution of 
the program at any given time.
```

```Enter your query: what is a computer system```

```
In the context of the document provided, a computer system refers to a system that can seemingly 
run tens or even hundreds of processes at the same time, making it easy to use without 
the need to be concerned about CPU availability. The challenge highlighted is to manage and 
optimize the running of multiple processes efficiently.
```

```Enter your query: what is CPU availability```

```
In the context of the document provided, CPU availability refers to the challenge of 
providing the illusion of many CPUs despite having only a few physical CPUs available. 
The document discusses the technique of time-sharing the CPU to allow users 
to run multiple concurrent processes, even though there are limitations in physical CPU resources.
```

```
Enter your query: exit
```
