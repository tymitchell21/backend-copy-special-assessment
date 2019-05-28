#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
from os import listdir
from os.path import isfile, join
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Tyler Ward"

# +++your code here+++
# Write functions and modify main() to call them
def find_special_files(my_path):
    files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    special_files = []
    for filename in files:
        if re.search('__(.[A-Za-z]*)__', filename):
            special_files.append(filename)
    return special_files

def print_filenames(filenames, my_path):
    for file in filenames:
        print(my_path)
        print(file)

def copy_to_dir(filenames, my_path):
    for file in filenames:
        shutil.copy(file, my_path)

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('directory')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    print(args.directory)

    if not args.directory:
        print('Must enter a directory to search')
        return

    # +++your code here+++
    # Call your functions
    if args.directory == '.':
        my_path = os.getcwd()
        special_files = find_special_files(my_path)
    else:
        my_path = os.getcwd() + '/' + args.directory
        special_files = find_special_files(my_path)
    
    if args.todir:
        copy_to_dir(special_files, args.todir)
    
    if args.tozip:
        special_files_str = " ".join(special_files)
        subprocess.call('zip -j ' + args.tozip + ' ' + special_files_str, shell=True)

    print_filenames(special_files, my_path)
if __name__ == "__main__":
    main()