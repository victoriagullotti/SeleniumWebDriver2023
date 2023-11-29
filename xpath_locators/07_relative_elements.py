# Any relative div element of any input element
parent_div_of_input = "$x('//div[./input]')"

# Same as above
parent_div_of_input_1 = "$x('//input/parent::div')"

# Same as above
parent_div_of_input_2 = "$x('//input[parent::div]')"

# Input inside a div row1
input_inside_div_row1 = '$x("//input[parent::div[@id="row1"]]")'

# Same thing
input_inside_div_row1_1 = '$x(\'//div[@id="row2"]/input\')'
