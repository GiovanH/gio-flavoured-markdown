### SuperFences

Inline code `is like this`.

Highlight

```python hl_lines="1 3"
# This line is emphasized
# This line isn't
# This line is emphasized
```

No language

```
# Line 1
# Line 2
```

Text

```text
# Line 1
# Line 2
```

Python

```python
# Line 1
def line2():
    print("string", 3)
    return
```

Python without line numbering (1)

```python linenums="0"
# Line 1
def line2():
    print("string", 3)
    return
```

Python without line numbering (2)

```{.python .no-line-nums}
# Line 1
def line2():
    print("string", 3)
    return
```
Mermaid

```mermaid
graph TD
    A[Hard] -->|Text| B(Round)
    B --> C{Decision}
    C -->|One| D[Result 1]
    C -->|Two| E[Result 2]
```

```markdeep

*************************************************************************************************
*.-------------------.                           ^                      .---.                   *
*|    A Box          |__.--.__    __.-->         |                      |   |                   *
*|                   |        '--'               v                      |   |                   *
*'-------------------'                                                  |   |                   *
*                       Round                                       *---(-. |                   *
*  .-----------------.  .-------.    .----------.         .-------.     | | |                   *
* |   Mixed Rounded  | |         |  / Diagonals  \        |   |   |     | | |                   *
* | & Square Corners |  '--. .--'  /              \       |---+---|     '-)-'       .--------.  *
* '--+------------+-'  .--. |     '-------+--------'      |   |   |       |        / Search /   *
*    |            |   |    | '---.        |               '-------'       |       '-+------'    *
*    |<---------->|   |    |      |       v                Interior                 |     ^     *
*    '           <---'      '----'   .-----------.              ---.     .---       v     |     *
* .------------------.  Diag line    | .-------. +---.              \   /           .     |     *
* |   if (a > b)     +---.      .--->| |       | |    | Curved line  \ /           / \    |     *
* |   obj->fcn()     |    \    /     | '-------' |<--'                +           /   \   |     *
* '------------------'     '--'      '--+--------'      .--. .--.     |  .-.     +Done?+-'      *
*    .---+-----.                        |   ^           |\ | | /|  .--+ |   |     \   /         *
*    |   |     | Join                   |   | Curved    | \| |/ | |    \    |      \ /          *
*    |   |     +---->  |                 '-'  Vertical  '--' '--'  '--  '--'        +  .---.    *
*    '---+-----'       |                                                            |  | 3 |    *
*                      v                             not:line    'quotes'        .-'   '---'    *
*                  .---+--------.            /            A || B   *bold*       |        ^      *
*                 |   Not a dot  |      <---+---<--    A dash--is not a line    v        |      *
*                  '---------+--'          /           Nor/is this.            ---              *
*************************************************************************************************
[Figure [diagram]: Diagrams can also have captions]


```

But it needs renderdeps!

<script>window.markdeepOptions={mode:"html"};</script>
<style class="fallback">pre.markdeep{white-space:pre;font-family:monospace}</style>
<script src="https://casual-effects.com/markdeep/latest/markdeep.min.js"></script>
<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>

### Asides

::: spoiler
    This is *true* markdown text.
    
    Markdown allows you to be lazy and only put the `>` before the first
    line of a hard-wrapped paragraph:
    
>     This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
    
    Spoilers will happily nest arbitrarily:
    ::: spoiler
        See?

::: spoiler Pesterlog
    This is *true* markdown text.

TOC inside a spoiler:

::: spoiler TOC
    [TOC]

### Footnotes

Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]: A footnote on the label: "@#$%".

A footnote with a complicated definition.[^2]

[^2]:
    The first paragraph of the definition.

    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.

This is a second point, but it has the same footnote. Weird![^2]