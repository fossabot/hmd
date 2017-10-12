#!/bin/bash

set -euo pipefail

{
  export PYTHON="$(which python)"
  export BINARY='hmdc'
  export SOURCE='hmdc'
  export BUILD='build'
  export OUTPUT="$(pwd)/${BUILD}/${BINARY}"

  [ -n "$(which zip)" ] || {
    sudo apt-get install -y zip
  }

  # clean up
  find "${SOURCE}" \
       -type f \
       -iname "*.pyc[oc]" \
       -exec rm -fv "{}" \;

  [ -d "${BUILD}" ] && {
    rm -rfv "${BUILD}"
  }

  # build
  mkdir -pv "${BUILD}"
  echo "#!${PYTHON}" > "${OUTPUT}"
  (
    cd "${SOURCE}"
    zip -rv "${OUTPUT}.zip" *
  )
  cat "${OUTPUT}.zip" >> "${OUTPUT}"
  chmod u+x -v "${OUTPUT}"
  rm -fv "${OUTPUT}.zip"
}
