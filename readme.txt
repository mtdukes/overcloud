OverCloud
OverCloud is a basic Python script to automatically prepare document sets for the Associated Press analysis tool Overview (http://overview.ap.org/) using the document management application DocumentCloud (http://www.documentcloud.org). After extracting text data from projects associated with a logged in DocumentCloud user, it formats the information into a CSV compatible with Overview.

OverCloud was developed by Charlie Szymanski and Tyler Dukes at Reporters' Lab, a research project at Duke University's DeWitt Wallace Center for Media and Democracy.

Code contributed to this project is provided under the MIT license (for more details, see below).

IMPORTANT NOTES
• OverCloud will only work on public projects in DocumentCloud.
• More on joining DocumentCloud: https://www.documentcloud.org/contact
• Instructions for installing Overview: http://overview.ap.org/blog/2012/02/getting-started-with-the-overview-prototype/
• See requirements.txt for necessary Python modules.

INSTRUCTIONS
1. Start a new project in DocumentCloud.
 
2. Upload your documents to DocumentCloud.

3. After your documents are processed, use DocumentCloud's API to access your project's JSON feed. Copy the project ID by clicking the edit button next to the project you want to use in the left rail. The project ID is under the description field.

In your browser, fetch the JSON file using the following URL, with your project ID inserted. If there are more than 100 documents in your projects (DocumentCloud's default value), specify a larger page count (up to 1,000).

https://www.documentcloud.org/api/search.json?q=projectid:INSERTPROJECTID&per_page=101

4. Click "Save as…" on the resulting page, making sure to end the filename in the ".json".

5. Open your command line interface and run OverCloud, specifying the path of your JSON file.

python overcloud.py directory/my-project.json

6. The text of your project should now be in an Overview-compatible CSV, along with the URLs for each individual document viewer.

Questions? Need help troubleshooting? Contact Tyler Dukes at tyler@reporterslab.org.

LICENSE
Copyright (c) 2012 Reporters' Lab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.