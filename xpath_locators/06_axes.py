# Get parent div of the element div with id="row1"
parent_div_of_row1 = '$x("//div[@id="row1"]/parent::div")'

# Get all the children of the div with id="row1"
children_of_row1 = '$x("//div[@id="row1"]/child::*)'

# Get all the descendants of the div with id="row1"
descendants_of_row1 = '$x("//div[@id="row1"]//child::*)'
descendants_of_row1_1 = '$x("//div[@id="row1"]/descendant::*)'

# Get all the ancestors of the div with id="row1"
ancestors_of_row1 = '$x("//div[@id="row1"]/ancestor::*)'

# Get list item #2 directly following h5 Test case 2
list_item_2_following_h5 = '$x("//h5[contains(text(), "Test case 2")]/following-sibling::ol[1]/li[2]")'

# Get list item #2 following h5 Test case 2
list_item_2_following_h5 = '$x("//h5[contains(text(), "Test case 2")]/following::ol[1]/li[2]")'
