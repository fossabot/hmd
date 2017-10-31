# Syntax

**Hierarchial Multiple Dictionary (HMD)** is like a template for [egrep](https://wikipedia.org/wiki/Grep) with custom logic behaviors.

## Schema

```
category_1  category_2  ..  category_i  (definition)
```

## Definition

- **single term** - *detect lines containing term "a"*:

```
(a)
```

- **multiple terms** - *detect lines containing term "a", "b", or "c"*:

```
(a|b|c)
```

- **chained terms** - *detect lines containing terms ("a", "b", or "c") and "d"*:

```
(a|b|c)(d)
```

## Sequence

- **after** - *detect lines with term "b" always after "a"*:

```
(a)(@b)
```

- **within ~n** - *detect lines with term "b" within ~n terms from "a"*:

```
(a)(+3b)
(a)(-11b)
```

## Negation

- **not** - *detect lines that does not contain term "a"*:

```
(!a)
```

## Wildcard

- **prefix** - *detect any valid/invalid prefix of "a"*:

```
(a %)
```

- **suffix** - *detect any valid/invalid suffix of "a"*:

```
(% a)
```

## Variable

- **variable** - *define variables*:

```
$a=(a)
$b= (b)
$c =(b)
$d = (d)
$e =    (e)(f|g)
```

## Comment

- **comment** - *comment if leading character is "#"*:

```
# hello this is a comment ###
```
