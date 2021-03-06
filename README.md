[![Build Status](https://travis-ci.org/initbar/hmd.svg?branch=master)](https://travis-ci.org/initbar/hmd)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Finitbar%2Fhmd.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Finitbar%2Fhmd?ref=badge_shield)
<p align="center">
  <img src="./docs/images/logo.png">
</p>

**hmd** is the next-generation Hierarchial Multiple Dictionary (HMD) compiler, pattern matching, and text traversal engine. It's designed to be a monolith construct in order to provide a simpler interface during [import](https://docs.python.org/3/reference/import.html) as a module.

## Features

- Modular to support additional syntax and definitions.
- Backward-compatible with the older version **hmd_split.py**.
- Optimized to sort and de-duplicate listed keywords in matrix.
- Optimized to sort and de-duplicate listed rules in matrix.
- Check dictionary syntax during parsing stage.
- Support variables to store repeated strings.
- Syntax highlighting for definitions.
- Pack to single executable binary.
- Complete test suite.

## Usage

```bash
~$ make && cd ./build
~$ ./hmd -h
```

## Module

When importing, use absolute imports directly from the base repository:

```python
import hmd.src.abstract.automata.automata
import hmd.src.abstract.generator.generator
# ..
```

If you're directly importing the binary builds, then use [zipimport](https://docs.python.org/2/library/zipimport.html) module.

Or, you can also install **hmd** as package using [pip](https://pypi.org).

## Sytax

See [syntax](./docs/SYNTAX.md) and [examples](./docs/EXAMPLE.md).

## Design

There are two major components to the **hmd** code: [compiler](#i-compiler) and [matcher](#ii-pattern-matching-and-text-traversal-engine).

## i. Compiler

The modified compiler component has similarities to a conventional compiler. A text goes into `FACTORY` class, a singleton-wrapper instance that spawns and dies within the program's lifetime, and outputs as a matrix:

![](./docs/images/design.png)

By default, `LEXER` will only tokenize a string into primitive characters, numbers, and symbols. If a user provides custom rules as a [regular expression](https://wikipedia.org/wiki/Regular_expression), it will use that instead.

Since the syntax of Hierarchial Multiple Dictionary (HMD) does not resemble that of a conventional programming language, custom language grammar was defined as inheritable abstractions of [deterministic finite automata](https://wikipedia.org/wiki/Deterministic_finite_automaton):

<img src="./docs/images/automata.png" height="230px">

`PARSER` also uses similar technique as the [Shunting Yard algorithm](https://wikipedia.org/wiki/Shunting-yard_algorithm) to split the operator and scalar values. However, it has heavily modified the algorithm to accomodate variables and comments:

<img src="./docs/images/shuntingyard.svg" height="600px">

`GENERATOR` is an overridable class that can be defined with custom compiling implementations. By itself, it's an empty class.

## License

**hmd** is under [MIT License](./LICENSE.md).


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Finitbar%2Fhmd.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Finitbar%2Fhmd?ref=badge_large)