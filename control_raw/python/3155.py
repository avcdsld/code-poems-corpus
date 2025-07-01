def find_elements_by_id(self, id_):
        """
        Finds multiple elements by id.

        :Args:
         - id\\_ - The id of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            ::

                elements = driver.find_elements_by_id('foo')
        """
        return self.find_elements(by=By.ID, value=id_)