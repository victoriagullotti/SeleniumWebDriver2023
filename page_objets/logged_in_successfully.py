def is_log_out_button_present(self) ->:
    try:
        self.driver.find_element_by_xpath(self.log_out_button_xpath).is_displayed()
        return True
    except:
        return False