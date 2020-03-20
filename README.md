# Rekordbox Cover Fix

After a quick lookup of my DJ music I noticed, that Pioneer's Rekordbox application will only show album covers
tagged as 'Front' cover. Therefor this hacky Python script will fix this issue by renaming corresponding covertags.

* Related Rekordbox version: 5.8.5

## Getting started (OSX)

Install Python 3
```
brew install python3
```

Install eyeD3
```
pip3 install eyeD3
```

Perform tag formatting on your library
```
python3 retag-mp3.py /path/to/your/library
```

## Dependencies

* Python 3.7
* eyeD3