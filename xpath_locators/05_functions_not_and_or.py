# Get button with the id of 'edit_btn'
button_with_id = '//button[@id="edit_btn"]'

# Get all buttons except the one with the id of 'edit_btn'
buttons_except_edit_btn = '//button[not(@id="edit_btn")]'

# Get H5 except with the index 1
h5_not_index_one = '$x("//h5[not(position()=1)]")'

# Or function
edit_or_remove_button_locator = '$x("//button[@name="Edit" or @name="Remove"]")'

# Not and Or function
edit_or_remove_button_locator1 = '$x("//button[@class="btn" and not(@style="display: none;")]")'

# Same as above
edit_or_remove_button_locator2 = '$x("//button[@class=\"btn\"][not(@style=\"display: none;\")]")'

# Any * attribute
any_attribute = '$x("//button[@*=\'btn\']")'
