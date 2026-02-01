#!/usr/bin/env sh

mkdir -p data
exec curl -L https://github.com/mifunetoshiro/kanjium/raw/refs/heads/master/data/kanjidb.sqlite --output data/kanjidb.sqlite
