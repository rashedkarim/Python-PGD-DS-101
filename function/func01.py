def my_function(**kid):
   print(kid)
   print("His last name is " + kid["lname"])


d = {"fname": "Tobias", "lname": "Refsnes"}

my_function(fname = "Tobias", lname = "Refsnes")
