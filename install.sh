#!/usr/bin/env bash

if [[ "$EUID" -ne 0 ]]; then
    echo "Please run as root (use sudo)"
    exit 1
fi

file='./JWTKeyCracker.py'
name="$(basename "${file%.py}")"

cp -r $file /bin/$name
echo "Done."

