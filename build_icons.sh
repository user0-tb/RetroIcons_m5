#!/bin/sh

for ICON in icons/*; do
  mogrify -resize "192x192" -path "app/src/main/res/drawable/" "$ICON"
done
