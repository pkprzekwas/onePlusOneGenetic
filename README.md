
## Prerequisites:
<br />

Installed:
* [pyplot](http://matplotlib.org/users/installing.html)
* click==6.6
<br />

## Installation:
Execute `pip install --editable .` from main project direcotry
<br />
When succeded tool should be available in terminal as `solve` command.  
<br />

## Examples of use:
<br />

`solve --iter 1000 --to_file True --mutation shuffle`
<br />

`solve --iter 1000 --to_file True --mutation swap`
<br />

`solve --iter 1000 --to_file True --mutation reverse_cut`