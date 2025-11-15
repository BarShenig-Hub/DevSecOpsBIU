#the script counts and presents details of a file
# the file is the $1 input
# For example: /etc/hosts
line_count=`cat $1> >(wc -l)`
word_count=`cat $1> >(wc -w)`
file_size=`cat $1> >(wc -c)`
export line_count
export word_count
export file_size
printf "File: %s\nLines: %s\nWords: %s\nSize: %s bytes\n" "$1" "$line_count" "$word_count" "$file_size"
