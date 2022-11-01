# find -name "*.md"|while read f; do ./add_frontmatter.sh $f; done

# Given a file path as an argument
# 1. get the file name
# 2. prepend template string to the top of the source file
# 3. resave original source file

filepath="$@"
file_name=$(basename "$filepath")

# Getting the file name (title)
md='.md'
title=${file_name%$md}

# Prepend front-matter to files
TEMPLATE="---
title: \"$title\"
---
"

# echo "$TEMPLATE" | cat - "$filepath" > temp
echo "$TEMPLATE" | cat - "$filepath" > temp && mv temp "$filepath"
