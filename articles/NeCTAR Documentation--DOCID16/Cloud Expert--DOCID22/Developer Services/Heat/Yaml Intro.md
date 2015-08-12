# Just enough YAML to read a template

Heat templates are written in a format named '[YAML](http://yaml.org/)'. This
is a short guide that will, hopefully, give you enough background to be able
to work with heat templates.

## YAML

YAML is a human readable data format.

It's not a markup language: the format of the content gives the meaning. There
are no embedded tags! Hence indentation and justification are important.

Comments are preceded by a hash. A hash can appear anywhere on a line, and will
mark everything to the end of the line as being part of the comment.

```yaml
# this is a comment
```

Data is stored in key value maps, wiht the key value pairs separated by a colon.

```yaml
date: 2014-01-14
```

String values can be indicated by no quotes, single quotes, or double quotes.

```yaml
first-name: 'Verity'
surname: "Stobs"
publication: The Register
```

Hashes in string values demarcated by quotes are not seen as the start of a comment.

```yaml
example: "# this is not a comment" # but this is
```

Double quoted strings can contain escaped characters, such as `'\n'` (newline).

```yaml
example: "This is \n a new line"
```

`'>'` Indicates that the following block of lines is a string value that will
have each line break folded into a space.

````yaml
example: >
    This
    has a value # and it is 'This has a value'
 ```

`'|'` indicates that the following block of lines is a string value that will
have the line breaks preserved.

```yaml
example: |
    This
    has a value # and it is 'This\nhas a value'
````

The value associated with a key can be another map of key value pairs.

If this is the case then don't provide a value: simply indent the new set of
key value pairs on the following lines. So all lines prefixed by more space
than the parent key are contained inside the parent key as a map of key value
pairs.

All lines in the same map have to have the same level of indentation.

```yaml
name:
    first: Verity
    last: Stob
```

Key value pairs have an alternate compact syntax: `{key: value, key: value, ...}`

```yaml
name: {first: Verity, last: Stob}
```

Lists are simply collections of ordered values: hence the values in a list have
no key. But the parent list must belong to a key.

List elements are indicated by a `'-'`.

```yaml
publications:
    - '.EXE'
    - 'Dr. Dobb's Journal'
    - 'The Register'
```

Lists have an alternate compact syntax: `[value, value, value,...]`.

```yaml
publications: ['.EXE', 'Dr. Dobb's Journal', 'The Register']
```

Lists and Maps can be nested in any order.

```yaml
name:
    first: Verity
    last: Stob
    publications:
        - '.EXE'
        - 'Dr. Dobb's Journal'
        - 'The Register'
```
