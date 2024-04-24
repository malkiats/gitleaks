import json
import sys

def generate_html(data):
    html_start = '''
<html>
<head>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 10px;
      }

      table {
        width: 100%;
        border-collapse: collapse;
        display: block;
        max-width: -moz-fit-content;
        max-width: fit-content;
        margin: 0 auto;
        overflow-x: auto;
        white-space: nowrap;
        border-right: 1px solid #ddd;
        /* Add right border to the table */
      }

      th,
      td {
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
      }

      th {
        background-color: #d3d3d3;
        /* Light gray background for the table header */
        color: black;
      }

      td {
        border-left: 1px solid #ddd;
        /* Consistent left border for table data cells */
      }

      .report-header {
        background-color: #09caf5;
        /* Sky blue background */
        color: white;
        padding: 10px;
        text-align: center;
        border-radius: 5px;
        /* Rounded corners */
        margin-bottom: 10px;
        /* Extra space below the header */
      }
    </style>
</head>
<body>
    <div class="report-header">
        <h1>Gitleaks Scanning Result</h1>
    </div>
    <table>
        <thead>
        <tr>
            <th>Description</th>
            <th>File</th>
            <th>Commit</th>
            <th>Author</th>
            <th>Email</th>
            <th>Message</th>
            <th>Match</th>
            <th>Secret</th>
        </tr>
    </thead>
    <tbody>
    '''
    html_end = '''
    </tbody></table></body></html>
    '''
    rows = ''
    for item in data:
        rows += f"<tr><td>{item['Description']}</td><td>{item['File']}</td><td>{item['Commit']}</td><td>{item['Author']}</td><td>{item['Email']}</td><td>{item['Message']}</td><td>{item['Match']}</td><td>{item['Secret']}</td></tr>\n"

    return html_start + rows + html_end

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as file:
        json_data = json.load(file)

    html_content = generate_html(json_data)
    with open(output_file, 'w') as file:
        file.write(html_content)
