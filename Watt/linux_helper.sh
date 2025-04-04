#!/bin/bash

CURRENT_DIR=$(pwd)
FOR_PATH="$CURRENT_DIR/wat/target"

export PATH="$PATH:$FOR_PATH"

if [ -n "$ZSH_VERSION" ]; then
    PROFILE_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    PROFILE_FILE="$HOME/.bashrc"
else
    PROFILE_FILE="$HOME/.profile"  # Запасной вариант
fi

if ! grep -qxF "export PATH=\"\$PATH:$FOR_PATH\"" "$PROFILE_FILE"; then
    echo "export PATH=\"\$PATH:$FOR_PATH\"" >> "$PROFILE_FILE"
    added "added $FOR_PATH to $PROFILE_FILE"
else
    echo "already added to $PROFILE_FILE"
fi

source "$PROFILE_FILE"

echo "added to path!"
