#!/bin/sh

echo '<?xml version="1.0" encoding="utf-8"?>' > app/src/main/res/values/iconpack.xml
echo '<resources>' >> app/src/main/res/values/iconpack.xml
echo '  <string-array name="icon_pack" translatable="false">' >> app/src/main/res/values/iconpack.xml
for ICON in icons/*; do
  ICON=$(echo "${ICON}" | sed 's;icons/\(.*\)\..*;\1;');
  echo "    <item>${ICON}</item>" >> app/src/main/res/values/iconpack.xml
done
echo '  </string-array>' >> app/src/main/res/values/iconpack.xml
echo '</resources>' >> app/src/main/res/values/iconpack.xml
