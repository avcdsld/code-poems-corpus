def update_employee_keyword_categories(data=nil,generate_objects=false)
            uri = URI.parse(@uri + "/EmployeeKeywordCategories")
            put(uri,data,generate_objects)
        end