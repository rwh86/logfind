# logfind

[Projects The Hard Way](http://projectsthehardway.com/) [Project 1](http://projectsthehardway.com/2015/06/16/project-1-logfind-2/)

Logfind is nothing more than a simple version of grep.  The purpose of logfind
is to make it easier for someone on a computer to quickly scan all their log
files without having to explicitly declare every file on the command line.

```
usage: logfind [-h] [-o] [-e] string [string ...]

Find string(s) in logfiles. Logfiles to search are specified as filename globs
in ~/.logfind.

positional arguments:
  string      string to find in the log files

optional arguments:
  -h, --help  show this help message and exit
  -o          use OR semantics (default: use AND)
  -e          strings are treated as Perl regular expressions
```

Given a list of filename globs to search for in the ~/.logfind file, logfind
will search each of the files for a list of strings specified as command line
arguments.  The default behaviour is to use AND, i.e. require a match of all of
the specified strings, but you can pass the -o option to change this to OR.
You can also choose to treat the strings to search for as Perl regular
expressions by passing the -e option.

## testing

To run unit tests, change to the root directory of the source repository and
run `nosetests`.
