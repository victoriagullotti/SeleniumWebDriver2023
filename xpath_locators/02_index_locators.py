# Get first H5 element on the page. In XPath index starts from 1, not 0!!!
first_h5_locator = '//h5[1]'

# Get all elements with H5 except the first one
all_h5_except_first_locator = '//h5[position() > 1]'
all_h5_except_first_locator_1 = '//h5[position() != 1]'
all_h5_except_first_locator_2 = '//h5[position() >= 2]'

# Get last H5 element on the page
last_h5_element_locator = '//h5[last()]'

# Get second row from the table
second_row_locator = '//div[@class="row"])[2]'

# Get second button inside second row
second_button_inside_second_row = '(//div[@class="row"])[2]/button[2]'