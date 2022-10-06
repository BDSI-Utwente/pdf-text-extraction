# Text extraction with TIKA

## Prerequisites
Tika requires a Java Runtime Environment (JRE) version 7 or later. 

## How to use
1. Activate the python environment: `pipenv shell`
2. Use the CLI tool to parse documents: `tika-python parse all|meta|text file [file2 ...]`, where 'file' may also point to a directory of files to parse.
3. Output is created as json files in the current working directory. 
    - Note that text is returned in xml format. Using `tika-python parse text file [file2 ...]` returns only the content as raw text, but inconveniently still uses the same auto-generated json filenames, clashing with results of `tika-python parse meta`.

Done!