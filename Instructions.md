## Adding icons
In this example, we will add Catima's icon (which is already in here).

1. Choose a filename. It must start with `acryl_`. For example: `acryl_catima.jpg`
2. Save the icon in [icons](https://codeberg.org/mondstern/AndroidAcrylicIconPack/src/branch/main/icons) with the correct filename (you can use "Add File" -> "Upload File" on that page)
3. Use the app [Turtl](https://f-droid.org/en/packages/org.xphnx.iconsubmit/) to figure out the activity name. In Catima's case, this is `me.hackerchick.catima/protect.card_locker.MainActivity`
4. Add the icon to [app/src/main/res/xml/appfilter.xml](https://codeberg.org/mondstern/AndroidAcrylicIconPack/src/branch/main/app/src/main/res/xml/appfilter.xml) with the correct activity name and filename.

![Turtl Catima example](turtl_catima_example.jpg)
Turtl shows 2 lines for Catima: `me.hackerchick.catima` and `protect.card_locker.MainActivity`. To calculate the activity name we need for `appfilter.xml` we just put those after each other with a `/` in between, so it becomes `me.hackerchick.catima/protect.card_locker.MainActivity`

## Releasing an update
1. Make sure to increase `versionCode` and `versionName` in https://codeberg.org/mondstern/AndroidAcrylicIconPack/src/branch/main/app/build.gradle
2. Make sure the following badge is green. If not, something is wrong. Click the top result on the page and see which check on the left is failing. Then click the check and see why (you may have to scroll down):
[![Sanity checks status](https://ci.codeberg.org/api/badges/mondstern/AndroidAcrylicIconPack/status.svg)](https://ci.codeberg.org/mondstern/AndroidAcrylicIconPack/branches/main)
3. If the badge is green, [click here to start creating a new release](https://codeberg.org/mondstern/AndroidAcrylicIconPack/releases/new). Put the new versionName in the "Tag name" and "Title" field. Optionally write a description of what you changed in "Content" and then press "Publish Release"
4. Wait a few days for F-Droid to pick up your update.