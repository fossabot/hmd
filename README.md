[![Build Status](https://travis-ci.org/initbar/hmd.svg?branch=master)](https://travis-ci.org/initbar/hmd)

# hmd

**hmd** is the next-generation Hierarchial Multiple Dictionary (HMD) compiler, pattern matching, and text traversal engine.

## Features

- Modular to support additional syntax and definitions.
- Backward-compatible with the older version **hmd_split.py**.
- Optimized to sort and de-duplicate listed keywords in results (".matrix").
- Optimized to sort and de-duplicate listed rules in results (".matrix").
- Convert dictionary terms into lemma using NLP engine.
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

## Documentations

See [syntax](./docs/SYNTAX.md) or some [examples](./docs/EXAMPLE.md).

## Design

**hmd** is a monolith engine that contains HMD compiler and pattern matching engine.

### Compiler

The modified compiler component has similarities to conventional compilers. All user input goes into `FACTORY`, a singleton-wrapper instance that spawns and dies with the program's lifetime, and outputs as compiled matrix:

![](./docs/images/design.png)

By default, `LEXER` will only tokenize a string into primitive characters, numbers, and symbols. If a user provides custom rules (as [regular expression](https://wikipedia.org/wiki/Regular_expression)), it will use that instead.

Since the syntax of Hierarchial Multiple Dictionary (HMD) does not resemble that of a conventional programming language, custom language grammar was defined as inheritable abstractions of [deterministic finite automata](https://wikipedia.org/wiki/Deterministic_finite_automaton):

![](./docs/images/automata.png)

`PARSER` also uses similar technique as the [Shunting Yard algorithm](https://wikipedia.org/wiki/Shunting-yard_algorithm) to split the operator and scalar values. However, it has heavily modified the algorithm to accomodate variables and comments:

![](./docs/images/shuntingyard.svg)

`GENERATOR` is an overridable class that can be defined with custom compiling implementations.

### Pattern Matching and Text Traversal Engine

## License

**hmd** is under [MIT License](./LICENSE.md).
