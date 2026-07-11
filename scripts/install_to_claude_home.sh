#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest_root="${CLAUDE_HOME:-$HOME/.claude}/skills"
mkdir -p "$dest_root"

if [ "$#" -eq 0 ]; then
  set -- "$repo_dir"/skills/*
fi

for src in "$@"; do
  if [ ! -d "$src" ]; then
    echo "skip: $src" >&2
    continue
  fi
  name="$(basename "$src")"
  dest="$dest_root/$name"
  if [ -e "$dest" ]; then
    echo "refusing to overwrite existing skill: $dest" >&2
    exit 1
  fi
  cp -R "$src" "$dest"
  echo "installed $name -> $dest"
done
