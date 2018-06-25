#!/usr/bin/env bash
while read p; do
  echo $p
  wget $p
done < File_URLs.txt
