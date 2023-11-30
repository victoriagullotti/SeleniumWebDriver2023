# Rools are different for SVG elements
rect = '$x('//rect[@y="11"]")' # Won't work
rect = '$x('//*[@y="11"]")' # Correct!!!

# Or. Get all elements with the name of 'rect'
rect = '$x("//*[name()=\'rect\']")'

# Get element with y=11
rect = '$x("//*[name()=\'rect\' and @y=\'11\']")'

# Get amazon logo
amazon_logo = '$x(\'//*[name()="symbol" and @id="icon-amazon"]\')'

# Get path from amazon logo
path_amazon_logo = '$x(\'//*[name()="symbol" and @id="icon-amazon"]/*[name()="path"]\')'
