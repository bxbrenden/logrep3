# logrep3

This is my python3 implementation of a python script called `logrep.py` from [Linux Pro Magazine's](https://www.linuxpromagazine.com) 2020 special edition magazine "[LibreOffice](https://www.linux-magazine.com/Resources/Special-Editions/40-LibreOffice-2020-Edition)".

The magazine includes a python 2.7 script, but considering python 2.7 was EOL as of January 1, 2020, I think it makes sense for the script to be updated to python3.


## Requirements

The only requirements are:
- a python 3 interpreter must be installed
- a bash prompt to run the python script from
- a LibreOffice Writer doc saved in `.odt` format


## Usage
Usage instructions for running from a bash prompt:

1. Ensure the `logrep3.py` script is executable by running `chmod +x logrep3.py`.
2. Decide on the 2 arguments you'll supply to `logrep3.py`:
  1. The pattern you want to match, e.g. "Hello"
  2. One or more `.odt` files in which to search for the pattern
3. Run the script, for example:
```bash
./logrep3.py "Hello" "Hello-World.odt"
```

## Example Output

The second instance of the word "Hello" will be red in the real output:
```
HelloWorld.odt, <text:p text:style-name="P1">Hello, World!</text:p>
```
