import pandas as pd
employee_service = pd.DataFrame({"employee": ["Chiva", "Otis", "Bella"], "years_service":[2,14,9], "number_of_roles": [2,3,2]})
employee_service.groupby(["number_of_roles"]).sum()