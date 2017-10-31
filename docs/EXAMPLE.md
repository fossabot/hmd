# Example

Below are some examples of new HMD features:

## Schema

There can be arbitrary number of categories. However, you can [declare a limit](https://github.com/initbar/hmdc/blob/388fb0b30b0b452351efcba762ba27b9aceead81/hmdc/__main__.py#L78-L85) and manually override the total category number:

```
(category)  ..  (category)	(definition)
```

## Comment

Comments are indicated by `#`.

```bash
# categories can be single.
A    (a)
B    (b)

## or multiple. ###
C    D  (e)

#
##
### comments can also be nested.
##
#
```

## Variable

When declaring a variable, there can be infinite or no spaces between declaration `=` and definition.

```bash
$x =(a)
$y =    (b)
$z = (c)
A B	(a)$x
C D	(a)$y
E F	(a)$z
G H	$x
I J	$y
K L	$z
M N	$x$x
O P	$x$y$z
```

You don't need to declare everything on the top. **hmdc** is flexible that you can declare variables on-the-go:

```bash
$x= (a)
A B	(a)$x
G H	$x

$y = (b)
C D	(a)$y
I J	$y

$z=(c)
E F	(a)$z
K L	$z

M N	$x$x
O P	$x$y$z

# but below will throw an exception
Q R   $s
```

## Spaces

Rules can be declared with arbitrary number of leading and trailing spaces/tabs:

```bash
A	A	(a)
 A	B	(a)
  A	C	(a)
   A	D	(a)
    A	E	(a)
     A	F	(a)
      A	G	(a)
```

## Sorting

If rules are not organized, you can set **hmdc** to sort the output result using [sort](https://github.com/initbar/hmdc/blob/388fb0b30b0b452351efcba762ba27b9aceead81/hmdc/__main__.py#L87-L91) flag:

```bash
# before
C (c)
B (b)
A (a)
A (b)

# after
A (a)
A (b)
B (b)
C (c)
```

In addition, sorting also takes place inside the lists to improve legibility:

```bash
# before
A	(b|a)(e|@d|c)
B	(a)(b)(z|x|y)

# after
A	(a|b)(@d|c|e)
B	(a)(b)(x|y|z)
```

## Unique

If you accidentally copy-and-paste identical rules, you can set **hmdc** to de-dup the results using [unique](https://github.com/initbar/hmdc/blob/388fb0b30b0b452351efcba762ba27b9aceead81/hmdc/__main__.py#L93-L97) flag:

```bash
# before
A (a)
B (b)
C (c)
A (a)
A (a)

# after
A (a)
B (b)
C (c)
```
