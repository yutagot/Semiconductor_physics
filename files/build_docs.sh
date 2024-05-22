#!/bin/bash

# Save the current directory
pushd "$(dirname "$0")" >/dev/null

# Command file for Sphinx documentation

if [ -z "$SPHINXBUILD" ]; then
    SPHINXBUILD=sphinx-build
fi
SOURCEDIR=.
BUILDDIR=../docs

if [ -z "$1" ]; then
    $SPHINXBUILD -M help $SOURCEDIR $BUILDDIR $SPHINXOPTS $O
    exit 1
fi

# Check if sphinx-build is installed
if ! command -v $SPHINXBUILD &>/dev/null; then
    echo
    echo "The 'sphinx-build' command was not found. Make sure you have Sphinx"
    echo "installed, then set the SPHINXBUILD environment variable to point"
    echo "to the full path of the 'sphinx-build' executable. Alternatively, you"
    echo "may add the Sphinx directory to PATH."
    echo
    echo "If you don't have Sphinx installed, grab it from"
    echo "https://www.sphinx-doc.org/"
    exit 1
fi

$SPHINXBUILD -b $1 $SOURCEDIR $BUILDDIR $SPHINXOPTS $O

# Return to the original directory
popd >/dev/null
