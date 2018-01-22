#!/bin/bash
figlet "      arXiv"
echo "====================================="
echo "Searching the arXiv for the new stuff"
echo "http://arxiv.org/list/quant-ph/new"
echo "====================================="
echo "keyword: $1"
echo "====================================="
curl -s http://arxiv.org/list/quant-ph/new | grep "Title" | grep -i "$1" | sed 's/.*<span class="descriptor">Title:<\/span> /- /g' > results.txt
numarticles=$(wc -l < results.txt | sed 's/ //g')
echo "Articles found: $numarticles"
cat results.txt
echo "====================================="
rm results.txt