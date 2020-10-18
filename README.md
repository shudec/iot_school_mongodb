# iot_school_mongodb

**Ex 0**

Load data students.json into `students` collection

**Ex 1**

Insert the following documents into `students` collection:

- `{"name":"Guy Brossard","scores":[{"score":87.5,"type":"exam"},{"score":58.6,"type":"quiz"},{"score":60.8,"type":"homework"}]}`
- `{"name":"Patrick Folrui","scores":[{"score":47.5,"type":"exam"},{"score":28.6,"type":"quiz"},{"score":80.8,"type":"homework"}]}`
- `{"name":"Yann Dubois","scores":[{"score":57.5,"type":"exam"},{"score":88.6,"type":"quiz"},{"score":68.8,"type":"homework"}]}`

**Ex 2**

Query the `students` collection to:
- show all documents
- show all documents with name set to "Jessika Dagenais"
- show all documents which score of exam is greater than 50
- show all documents which score of homework is between 50 and 70

**Ex 3**

- add a note of type "terminal exam" to all students
- add the mean of notes to all students

**Ex 4**

Delete documents with an empty name

**Ex 5**

Create a collection `subjects` and add the following documents:

- `{"name":"Mathematics", "level":2, "Professor":"Mrs Pythagore"}`
- `{"name":"Physics", "level":3, "Professor":"Mr Einstein"}`
- `{"name":"Computer Sciences", "level":5, "Professor":"Mr Keyboard"}`

Add the id of subject mathematics to the first third of the scores, Physics to the second third and Computer Sciences to the last third of the scores.

Query the database to:
- show the scores of Physics
- show the scores of Mr Keyboard's students

**Ex 6**

- Calculate the mean of each suject and add it to the `subjects` collection
- Calculate the mean of each suject by type and add it to the `subjects` collection