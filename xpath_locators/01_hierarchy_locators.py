# Get xpath in console of browser
# $x('//*[@id="login"]/ul/li[2]/b[2]')

# Get input field inside parent div with id 'row2'
input_field_in_row2_locator = '//div[@id='row2']/input'

# //
# Anywhere on a page
button_anywhere_locator = '//button'

# Descendants of div with id 'rows'
input_inside_rows_locator = '//div[@id="rows"]//input'

# /
# Root of the current element.
body_absolute_locator = '/html/body'
input_inside_div = '//div[@id='row2"]/input'

# .//
# From the current element only
input_text_from_current_element = './/input/text'

# For loop to get all rows from table and then search for the input field inside each row
for row in driver.find_elements_by_xpath('//table[@id="table1"]/tbody/tr'):
    input_text = row.find_element_by_xpath('.//input/text').text
