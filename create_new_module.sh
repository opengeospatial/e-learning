#!/bin/bash
module_name=$1
cd source
mkdir $module_name
cd $module_name
mkdir img
mkdir text
cd ..
cp -r new/*.rst $module_name/text
sed -i '.orig' 's/module_name/'"$module_name"'/g' $module_name/text/*.rst
rm $module_name/text/*.orig