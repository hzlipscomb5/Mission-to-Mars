#Create a new database 
#In terminal
use practicedb

#This created a db named practice db


#Show current database
db 

#Show collections or data
show collections


### Insert Data Syntax

db.collectionName.insert({key:value})

# db refers to the active database, practicedb.
# collectionName is the name of the new collection we're creating (we'll customize it when we practice).
# .insert({ }) is how MongoDB knows we're inserting data into the collection.
# key:value is the format into which we're inserting our data; its construction is very similar to a Python dictionary.


#adding zoo animals to a "zoo" collection
db.zoo.insert({name: 'Cleo', species: 'jaguar', age: 12, hobbies: ['sleeping', 'eating', 'climbing']})

db.zoo.insert({name: 'Banzai', species: 'fox', age: 1, hobbies: ['sleeping', 'eating', 'playing']})




#Documents can also be deleted or dropped. The syntax to do so follows: db.collectionName.remove({}).

#So, if we wanted to remove Cleo from the database, we would update that line of code to:

db.zoo.remove({name: 'Cleo'}).

#We can also empty the collection at once, instead of one document at a time. For example, to empty our pets collection, we would type: 
db.zoo.remove({}) #. Because the inner curly brackets are empty, Mongo will assume that we want everything in our pets collection to be removed.

# Additionally, to remove a collection all together, we would use 
db.zoo.drop() #. After running that line in the shell, our pets collection will no longer exist at all.

#And to remove the test database, we will use this line of code: 
db.dropDatabase().
