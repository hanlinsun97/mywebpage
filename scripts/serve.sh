#!/bin/sh
# Preview the site locally with the Hugo version Netlify uses (see netlify.toml).
# Newer Hugo releases cannot build the pinned Wowchemy theme.
HUGO_VERSION=0.97.3
HUGO="$HOME/.local/hugo-$HUGO_VERSION/hugo"

if [ ! -x "$HUGO" ]; then
  mkdir -p "$(dirname "$HUGO")"
  case "$(uname -m)" in arm64) ARCH=ARM64 ;; *) ARCH=64bit ;; esac
  curl -sSL "https://github.com/gohugoio/hugo/releases/download/v$HUGO_VERSION/hugo_extended_${HUGO_VERSION}_macOS-$ARCH.tar.gz" \
    | tar xz -C "$(dirname "$HUGO")" hugo
fi

cd "$(dirname "$0")/.." && exec "$HUGO" server -D "$@"
