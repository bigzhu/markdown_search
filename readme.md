# markdown_search

Search markdown file name by key name, order by files created date then write the result in search.md.

Work with my nvim/vim to find my markdown blog article fast

## install

use my [bash_tools](https://github.com/bigzhu/bash_tools)

```bash
install.sh markdown_search.py
```

or manually create link to `/usr/local/bin/`

## work with nvim/vim

Here is my config: https://github.com/bigzhu/nvim/blob/master/markdown.vim

## note

Will auto-add `english/{key}.md` in search.md even search result is nothing.

You can ignore it or modify the `english` subpath to your self path value.

![tty](https://user-images.githubusercontent.com/489815/75991986-49d63500-5f32-11ea-80a7-5d1d9e0f30e7.gif)
