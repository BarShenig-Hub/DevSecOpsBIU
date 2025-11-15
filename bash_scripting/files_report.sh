# This script counts how many files and directories are in the current folder, calculates its total size, and prints the three largest files
count_files=0
count_dir=0
size=`du -sh`
three_largest_files=`head -3 < <(ls -hS)`
for item in $(ls)
do
 if [ -f $item  ]
 then
  ((count_files++))
fi
 if [ -d $item  ]
 then
  ((count_dir++))
fi
done
echo Number of files: $count_files
echo Number of directories: $count_dir
echo Total size of all directory: $size
echo Three largest files in the directory: $three_largest_files
