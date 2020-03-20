#!/usr/bin/python3

import os
import sys
import re
import eyed3

def main():
  for arg in sys.argv[1:]:
    basepath = arg
    print("Processing files in directory: \"%s\"" % (basepath))
    print("================================")
    for fname in os.listdir(basepath):
      # ITERATING OVER DIRECTORY CONTENT
      fpath=os.path.join(basepath, fname)
      if not os.path.isdir(fpath) and not fname.startswith('.') and fname.endswith('.mp3'):
        # ITERATING OVER MP3s
        audiofile = eyed3.load(fpath)
        artist, title = getFormatedTags(audiofile)
        audiofile.tag.artist = artist
        audiofile.tag.title = title
        audiofile.tag.save()
        print("Successfully tagged: {}".format(fname))

def getFormatedTags(af):
  if hasattr(af, 'tag'):
    # check existence tags
    if all(hasattr(af.tag, attr)\
    for attr in ["artist", "title"]):
      artist = af.tag.artist
      title = af.tag.title
      newTitle = title.replace('[', '(').replace(']', ')')
      newArtist = artist.replace('[', '(').replace(']', ')')

      # remove unnecessary title infos
      newTitle = re.sub(r'(?: \(Remix\)| \(Remixes\)| \(New Remixes\)| \(Original Mix\)| \(Extended Mix\)| \(Club Mix\)| \(Extended Explicit Mix\) | \(Extended Explicit Mix\)| \(Deluxe Mix\))', '', newTitle)
      # replace few title formatings
      newTitle = re.sub(r'(?:Extended Remix\)|Club Remix\))', 'Remix)', newTitle)
      newTitle = re.sub(r'(?:Original Mix\)|Club Mix\)|Extended Mix\))', 'Mix)', newTitle)

      # replace artist featuring formating
      newArtist = re.sub(r'(?:feat\.|FEAT\.|featuring|Featuring)', 'ft.', newArtist)

      # move featuring artists from title to artist tag
      ftMatchRegex = r'\((?:feat\.|FEAT\.|featuring|Featuring|ft.) (.*?)\)'
      titleFeatStrs = re.findall(ftMatchRegex, newTitle)
      if len(titleFeatStrs) > 0:
        newTitle = re.sub(ftMatchRegex, '', newTitle)
        newArtist += ' ft. ' + ' & '.join(titleFeatStrs)

      return newArtist, newTitle

if __name__ == "__main__":
  main()