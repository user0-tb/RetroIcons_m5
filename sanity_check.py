import os
import re
import xml.etree.ElementTree as ET

try:
    import requests
except ImportError as error:
    print(f"Could not find requests, is it installed? {error}")

RES_ROOT = os.path.join('app', 'src', 'main', 'res')
XML_ROOT = os.path.join(RES_ROOT, 'xml')
APPFILTER_PATH = os.path.join(XML_ROOT, 'appfilter.xml')
DRAWABLE_ROOT = os.path.join(RES_ROOT, 'drawable')
ICONPACK_PATH = os.path.join(RES_ROOT, 'values', 'iconpack.xml')
IGNORE_FILENAME = 'sanity_check_ignored.txt'

errors = 0

print(f"Checking {APPFILTER_PATH}...")

tree = ET.parse(APPFILTER_PATH)
items = tree.getroot()

ignored_items = []
with open(IGNORE_FILENAME) as f:
    for line in f:
        ignored_items.append(line.strip())


def get_drawable_error(drawable_name):
    if not drawable_name.startswith("acryl_"):
        return f"{drawable_name} should start with acryl_ but it doesn't! Check {APPFILTER_PATH}!"

    if not re.match(r"^[a-z0-9_]*$", drawable_name):
        return f"{drawable_name} contains invalid characters, only a-z (lowercase), 0-9 and _ are allowed! Check {APPFILTER_PATH}!"

    if not os.path.isfile(os.path.join(DRAWABLE_ROOT, f"{drawable_name}.jpg")):
        return f"{drawable_name}.jpg doesn't exist in {DRAWABLE_ROOT}!"

    if not check_drawable_iconpack(drawable_name):
        return f"{drawable_name} doesn't exist in {ICONPACK_PATH}!"

    return None


def check_drawable_iconpack(drawable_name):
    for icon in ET.parse(ICONPACK_PATH).getroot()[0]:
        if icon.text == drawable_name:
            return True

    return False


def check_package_fdroid(package_name):
    return requests.get(f"https://gitlab.com/fdroid/fdroiddata/-/raw/master/metadata/{ package_name }.yml").status_code == 200


def check_package_izzyondroid(package_name):
    return requests.get(f"https://apt.izzysoft.de/fdroid/index/apk/{ package_name }").status_code == 200 


# First, check all icons (because no web request needed)
for item in items:
    if item.tag == 'item':
        drawable_name = item.attrib['drawable']
        drawable_error = get_drawable_error(drawable_name)
        if get_drawable_error(drawable_name):
            print(f"[ERROR] {drawable_error}")
            errors += 1

if errors > 0:
    print("[FATAL] One or more broken icons found. Fix them first, then run the script again to check packages.")
    exit(1)

for item in items:
    if item.tag == 'item':
        component = item.attrib['component']
        component_data = re.search(r"ComponentInfo{(.*)/(.*)}", component)
        if len(component_data.groups()) != 2:
            print(f"[ERROR] Component value {component} does not seem to be formatted correctly! Check {APPFILTER_PATH}!")
            errors += 1
            continue

        package_name = component_data.group(1)
        activity_name = component_data.group(2)

        if package_name in ignored_items:
            print(f"[NOTE] Skipped {package_name} because it is in {IGNORE_FILENAME}.")
            continue

        if not check_package_fdroid(package_name) and not check_package_izzyondroid(package_name):
            print(f"[ERROR] Could not find {package_name} on either F-Droid or IzzyOnDroid. Fix the package name in {APPFILTER_PATH} or add it to {IGNORE_FILENAME} if you're sure the name is correct.")
            errors += 1
            continue

print(f"Found {errors} errors.")
print("Please remember this script can't find every error!")

if errors > 0:
    exit(1)
