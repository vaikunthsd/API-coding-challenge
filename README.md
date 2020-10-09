# API-coding-challenge

## Requirements:

* Use Python 3.8 as base version
* Create a class for all API interactions with methods for all interactions with the API
* Use pythonic practices as much as possible, including formatting matching PEP-8
standards
* Bonus Points - Include pytest based unit tests

## Scenario:

The JSONPlaceholder website allows for testing against a sample set of data, description here: (http://jsonplaceholder.typicode.com/)

Notice that examples are in JavaScript, you will have to translate what is expected to Python. 

(Full endpoint API docs here: (http://jsonplaceholder.typicode.com/guide.html))

Using the API to interact with the JSONPlaceholder website, accomplish the following goals:

<ol type="1">
  <li>Print the value of the title for post number 99</li>
  <li>Inject a field called time into the results for post number 100 and print the whole JSON
record</li>
<ol type="a">
  <li>Use the datetime library to perform this action with a UTC timestamp matching the following format DD/MM/YYYY HH:MM:SS</li>
 </ol>
  <li>Create a new /posts entry which the following values</li>
  <ol type="a">
  <li>Title: Security Interview Post</li>
   <li>UserID: 500</li>
   <li>Body: This is an insertion test with a known API</li>
 </ol>
  <li>Determine if your post was successful, and if it was, create a tuple of the 3 following values</li>
    <ol type="a">
  <li>The “id” field of the new record</li>
   <li>The status code returned from the POST</li>
   <li>The value of the “x-Powered-By” field in the headers</li>
 </ol>
  <li>Print the tuple from #4</li>
  <li>Delete the record you created in #3, by referencing the new “id”. Print the return status code and the x-content-type-options from the returned object</li>
</ol>
