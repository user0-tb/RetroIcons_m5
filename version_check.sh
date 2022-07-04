#!/bin/bash

highestVersionCode=0

tags="$(curl https://codeberg.org/api/v1/repos/mondstern/AndroidAcrylicIconPack/tags 2>/dev/null | jq -r '.[].name')"

if [ -z "${tags}" ]; then
  echo "Something went really wrong: couldn't find any tags."
  exit 1
fi

for tag in ${tags}; do
  versionCode="$(sed -n 's/\s*versionCode \(.*\)/\1/p' <<< "$(curl "https://codeberg.org/mondstern/AndroidAcrylicIconPack/raw/tag/${tag}/app/build.gradle" 2>/dev/null)")"

  if [ "$versionCode" -gt "$highestVersionCode" ]; then
    highestVersionCode="${versionCode}"
  fi
done

versionCode=$(sed -n 's/\s*versionCode \(.*\)/\1/p' app/build.gradle)

if [ "${versionCode}" -le "${highestVersionCode}" ]; then
  echo "Current version code is not higher than the highest tag (current: ${versionCode}, highest: ${highestVersionCode}). Make sure to increase versionCode in app/build.gradle."
  exit 1
fi

versionName=$(sed -n 's/\s*versionName "\(.*\)"/\1/p' app/build.gradle)

if [ "${versionCode}.0" != "${versionName}" ]; then
  echo "Expected versionName to be ${versionCode}.0 but found ${versionName}."
  exit 1
fi
