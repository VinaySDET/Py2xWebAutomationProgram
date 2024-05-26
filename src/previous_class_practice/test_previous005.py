# * out of these, which one is faster:

# class By:
#     """Set of supported locator strategies."""
#
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"

# * answer: 1st: ID, 2nd: Name, 3rd: CLASS_NAME, 4th: LINK_TEXT, 5th: PARTIAL_LINK_TEXT, 6th: CSS_SELECTOR and 7th: XPATH
# * people say CSS_SELECTOR is faster than XPATH   -- it is sometimes True/False, depend on the OS and browser

# * Locators:
# 1. Unique
# 2. Stable in nature - they shouldn't change often
# 3. Avoid dynamic locators, ex: class = "_123_april2024"  --> if class gets change day by day, it doesn't make sense to use this
# 4. Find the stable and unique locators which will survive the automation scripts for the longer run.

# * How to check stable and not stable :
# <
# input type="text"    ----> not stable
# spellcheck="false"  ----> not stable
# name="autosuggestBusSRPSrcHomeName" ----> not stable
# aria-autocomplete="list"  ----> not stable
# aria-labelledby="downshift-1-label"       ---> not stable
# autocomplete="off"  ---> not stable
# id="autosuggestBusSRPSrcHome"    ---> it is stable
# placeholder="Enter Source"   ---> stable
# value=""     ---> not stable
# fdprocessedid="7koigq"  ---> stable
# >




# * stable: whatever u use locator, they should be 1 element found with locator & you're 100% sure that it'll not change

# XPATH and CSS_SELECTOR?
# * ID, CLASS_NAME, NAME --> attributes
# *  TAG_NAME --> HTML
# * LINK_TEXT, PARTIAL_LINK_TEXT --> Text of the anchors
# * XPATH --> query language to find a tag in HTML
# * CSS_SELECTOR --> way to find an element in HTML
