students = [
    {"name": "Homayoon", "job": "Front-End Dev", "ID": 1101},
    {"name": "Maryam", "job": "Front-End Dev", "ID": 1102},
    {"name": "Hesam", "job": "Security Engineer", "ID": 1103},
    {"name": "Mahdyar", "job": "Project Manager", "ID": 1104},
    {"name": "Matin", "job": "Data Engineer", "ID": 1105},
]

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #aa043c;
  color: white;
}
</style>
</head>
<body>

<h1>Students Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Job</th>
    <th>ID</th>
  </tr>
"""

for person in students:
    html_content += f"""
      <tr>
        <td>{person['name']}</td>
        <td>{person['job']}</td>
        <td>{person['ID']}</td>
      </tr>
    """

html_content += """
</table>
</body>
</html>
"""

open("Table.html","w").write(html_content)
print("Done")
