import os
import re
import xml.etree.ElementTree as ET

try:
    import requests
except ImportError as error:
    print(f"Could not find requests, is it installed? {error}")

RES_ROOT = os.path.join('app', 'src', 'main', 'res')
XML_ROOT = os.path.join(RES_ROOT, 'xml')
DRAWABLE_ROOT = os.path.join(RES_ROOT, 'drawable')
ICONPACK_PATH = os.path.join(RES_ROOT, 'values', 'iconpack.xml')

errors = 0
warnings = 0

print("Checking appfilter.xml...")

tree = ET.parse(os.path.join(XML_ROOT, 'appfilter.xml'))
items = tree.getroot()


def check_drawable_name(drawable_name):
    return drawable_name.startswith("acryl_")


def check_drawable_exists(drawable_name):
    return os.path.isfile(os.path.join(DRAWABLE_ROOT, f"{drawable_name}.jpg"))


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
        if not check_drawable_name(drawable_name):
            print(f"[ERROR] {drawable_name} should start with acryl_ but it doesn't!")
            errors += 1
            continue

        if not check_drawable_exists(drawable_name):
            print(f"[ERROR] {drawable_name}.jpg doesn't exist in {DRAWABLE_ROOT}!")
            errors += 1
            continue

        if not check_drawable_iconpack(drawable_name):
            print(f"[ERROR] {drawable_name} doesn't exist in {ICONPACK_PATH}!")
            errors += 1
            continue

if errors > 0:
    print("[FATAL] One or more broken icons found. Fix them first, then run the script again to check packages.")
    exit(1)

for item in items:
    if item.tag == 'item':
        component = item.attrib['component']
        component_data = re.search(r"ComponentInfo{(.*)/(.*)}", component)
        if len(component_data.groups()) != 2:
            print(f"[ERROR] Component value {component} does not seem to be formatted correctly!")
            errors += 1
            continue

        package_name = component_data.group(1)
        activity_name = component_data.group(2)

        if not check_package_fdroid(package_name) and not check_package_izzyondroid(package_name):
            print(f"[ERROR] Could not find {package_name} on either F-Droid or IzzyOnDroid")
            warnings += 1
            continue

print(f"Found {errors} errors and {warnings} warnings.")
print("Please remember this script can't find every error!")
