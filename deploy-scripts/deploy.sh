#!/usr/bin/env bash
# This file can be used by CNDLS Developers with SSH access to the UIS servers to deploy changes to the website.
source config.sh

cd "${LOCAL_DIR}"

pwd

git checkout master

git pull origin master

git status

# Activate the virual environment
source "${VENV_DIR}bin/activate"

# Compile the static site files using frozen-flask
python freeze.py

# Use rsync to transfer the files to server
#      -r: Recurse into subdirectories
#      -v: Increase verbosity
#      -e: Specify the remote shell to use
#      -I: Ignore times: don't skip files that match size and time, i.e. overwrite all files at destination
# --perms: Preserve file permissions
# --group: Preserve group
# A trailing / on a source name means "copy the contents of this directory".
# Without a trailing slash it means "copy the directory".
# In this case, we want to copy the entire directory.

rsync -rvI -e 'ssh' "${LOCAL_BUILD_DIR}" "${SERVER_USERNAME}@${SERVER}:${SERVER_BUILD_DIR}"

# Connect to the server using ssh and change file permissions and groups
ssh -v "${SERVER_USERNAME}@${SERVER}" "
  echo 'Changing to server build directory'
  cd ${SERVER_BUILD_DIR}
  pwd

  echo 'Listing files in the server build directory before changing groups and permissions'
  ls -al

  echo 'Changing permissions'
  find . -type d -exec chmod 775 {} \;
  find . -type f -exec chmod 664 {} \;

  echo 'Changing groups and permissions'
  find . -type d -exec chown ${SERVER_USERNAME}:${SERVER_GROUP} {} \;
  find . -type f -exec chown ${SERVER_USERNAME}:${SERVER_GROUP} {} \;

  echo 'Listing files in the server build directory after changing groups and permissions'
  ls -al
  "

  # Delete the build directory locally
  rm -r "${LOCAL_BUILD_DIR}"



