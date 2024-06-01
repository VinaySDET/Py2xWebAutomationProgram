# We should interact with HTML elements:
# 1. Heading - h1,h2,h3,h4,h5,h6
# 2. paragraphs - p
# 3. Img - <img src=" image-link " alt = " name of image"> ,video,audio
# 4. Div(used as a container for other HTML elements), span
# 5. Table - <tr> - row, td - column
# 6. bold, italic, underline - b, /, _
# 7. input type - password. checkbox, text, file, radio
# 8. select - dropdown list, multiple selection
# 9. Text area
# 10. Button - submit
# 11. form - inputs
# 12. Iframe
# 13. Body, head, title, footer
# 14. List - li, ul

# if you want to interact any of HTML Elements, 2 things you need to pay attention:
# * Recognise HTML Elements -
# 1. BY tag - <h1,h2,title>
# * 2. BY attribute: key-value pair which can help u to find the element, in this example we've 3 attribute(id,href,class)
# <a
# id="btn-make-appointment"
# href="./profile.php#login"
# class="btn btn-dark btn-lg"
# >
# Make Appointment
# </a>

# * Locators in selenium: a locator is a way of identifying an element on a web page so that it can be interacted with.
# There are several different types of locators that can be used
# 1. ID: it uses the unique ID attribute of an element to locate it on the page.
# 2. Name: it uses the name attribute of an element to locate it on page
# 3. Class name: it uses the class attribute of an element to locate it on page
# 4. Tag name: it uses the HTML tag name of an element to locate it on page
# 5. Link text: it uses the text of a link to locate it on page
# 6. Partial link text: it uses part of the text of a link to locate it on the page

# * If the above points don't work. Then we can go towards CSS selector and Xpath
# 7. CSS selector: it uses the CSS selector of an element to locate it on page
# 8. Xpath: it uses a Xpath expression to locate an element on the page