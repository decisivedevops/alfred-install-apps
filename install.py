#!/usr/bin/env python3

import os
import subprocess
import sys
import shutil


installation_file = sys.argv[1:]


def find_app_name(directory):
    """
    Finds the name of the app in the given directory.
    """
    for root, dirs, files in os.walk(directory):
        if root.endswith('app'):
            return root

        for file in files:
            if file.endswith('pkg'):
                return file


def unzip(source_filename, dest_dir):
    """
    Unzip the source_filename into dest_dir
    """
    subprocess.check_call(['unzip', '-oqq', source_filename,
                           '-d', dest_dir])

def install_from_archive(source_filename):
    """
    Install a app file from zip file and copying its contents
    to /Applications.
    """
    dest_dir = './tmp'
    unzip(source_filename, dest_dir)
    app_name = find_app_name('./tmp')

    if app_name.endswith('pkg'):
        subprocess.call(['open', '-a', 'Installer', f'{dest_dir}/{app_name}'])
    elif app_name.endswith('app'):
        shutil.move(app_name, '/Applications/')
        os.rmdir(dest_dir)

    os.unlink(source_filename)


def install_from_dmg(source_filename):
    """
    Install a dmg file by mounting it and copying its contents
    to /Applications.
    """
    tmp_dir = '/Volumes/install_build'
    # Mount the DMG.
    subprocess.check_call(['hdiutil', 'attach', source_filename, '-nobrowse',
                           '-quiet', '-mountpoint', tmp_dir])

    # Copy the app to /Applications.
    app_name = find_app_name(tmp_dir)
    subprocess.check_call(['cp', '-r', app_name,
                           '/Applications'])

    # Unmount.
    subprocess.check_call(['hdiutil', 'detach', tmp_dir])

    # Delete the source_filename.
    os.unlink(source_filename)


# main
if installation_file[0].endswith('dmg'):
    install_from_dmg(installation_file[0])
if installation_file[0].endswith('zip'):
    install_from_archive(installation_file[0])
