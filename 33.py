header = input("Enter a header : ")
par = input("Enter a paragraph : ")

html_content = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

open("index.html","w").write(html_content)
print("Done")
