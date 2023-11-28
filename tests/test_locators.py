

# Get xpath in console of browser
$x('//*[@id="login"]/ul/li[2]/b[2]')

# Get input field from parent div with id row2
//div[@id='row2']/input

# //
# Anywhere on a page
//button # Any button on a page

//div[@id='rows']//input # Discendants of div with id rows

# /
# Root of the current element.
/html/body
//div[@id='row2']/input

# .//
# From the current element only
.//input/text

# Search within the rows
# Get list of all rows
		# List<WebElement> rows = driver.findElements(By.xpath("//div[@id='row2']/*[@id='save_btn']"));
        #
		# String actualText = null;
        #
		# // Iterate over each row in the list
		# for (WebElement row : rows) {
		# 	// Get text from label element for each row
		# 	String label = row.findElement(By.xpath(".//label")).getText();
		# 	System.out.println("Label text is: " + label);
        # .......
