sc_pos
======

Add part of speech tags to tokenized tweets from sc_filter

Take the filtered data output from https://github.com/kira-quan/sc_filter and use it as the input for this script.

`python tag-pos.py <input_file> <output_file>`

This will create a new json file that is about twice the size of the previous. This will take a while to run (~15 mins on my machine).

The new json will have a field called 'pos_tags'. This field is a list of (str, str) tuples.
