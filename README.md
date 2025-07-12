![CI](https://github.com/dimst12/animalssay/actions/workflows/python-ci.yaml/badge.svg)

# animalssay

**animalssay** is a fun Python library that lets animals say things in ASCII art style — just like the classic `cowsay`, but with more animals!

## Features

- Cute ASCII art animals: cat, dog, frog, fox, cow, pig, owl and more
- Simple functions to generate speech bubbles with animal pictures  
- Easy to use and extend with your own animals  

## Installation

You can install `animalssay` via pip (once published):

```bash
pip install animalssay
Or install locally for development:

pip install -e .

from animalssay import cat_says, dog_says, frog_says

print(cat_says("Hello!"))
print(dog_says("Woof!"))
print(frog_says("Ribbit."))
This will print:

  --------
< Hello! >
  --------
     \
      \
        /\_/\
       ( o.o )
        > ^ <
Adding more animals
You can add your own animal functions by editing animalssay/animals.py and updating __init__.py.

License
MIT License © Dmytro Steblev

Enjoy making animals talk! 🐱🐶🦊🐸🐮🐷🦉

---

If you want, I can also help you create a proper `LICENSE` file or add more sections like contribution guidelines!