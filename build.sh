#!/bin/bash

set -euo pipefail

{
  export PYTHON="$(which python)"

  export SOURCE='hmdc'
  export BUILD='build'
  export BINARY='hmdc'
  export OUTPUT="$(pwd)/${BUILD}/${BINARY}"

  [ -n "$(which zip)" ] || {
    sudo apt-get install -y zip;}

  # clean up
  [ -d "${BUILD}" ] && {
    rm -rfv "${BUILD}";}
  find "${SOURCE}" \
       -type f \
       -iname "*.py[oc]" \
       -exec rm -fv "{}" \;

  # build
  mkdir -pv "${BUILD}"
  (
    cd "${SOURCE}"
    zip -rv "${OUTPUT}.zip" *
    echo "#!${PYTHON}" > "${OUTPUT}"
    cat "${OUTPUT}.zip" >> "${OUTPUT}"
    rm -fv "${OUTPUT}.zip"
    chmod u+x -v "${OUTPUT}"
  )
}
