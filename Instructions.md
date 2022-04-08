## Adding icons
We have a LOT of icons to go still.

In this example, we will add Catima's icon (which is already in here).

1. Choose a filename. It must start with `acryl_`. For example: `acryl_catima.jpg`
2. Save the icon in `icons`
3. Use the app [Turtl](https://f-droid.org/en/packages/org.xphnx.iconsubmit/) to figure out the activity name. In Catima's case, this is `me.hackerchick.catima/protect.card_locker.MainActivity`
4. Add the icon to `app/src/main/res/xml/appfilter.xml` with the correct activity name
5. If you are not running in CI, you will have to manually run the scripts in `scripts`

![Turtl Catima example](turtl_catima_example.jpg)
Turtl shows 2 lines for Catima: `me.hackerchick.catima` and `protect.card_locker.MainActivity`. To calculate the activity name we need for `appfilter.xml` we just put those after each other with a `/` in between, so it becomes `me.hackerchick.catima/protect.card_locker.MainActivity`
