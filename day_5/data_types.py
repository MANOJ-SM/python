# 1) List    # mutable 

# my_list = [ 1,2,3, "apple","banana",3];
# print(my_list)


# 2) Tuple   # immutable   # ordered  #Allow duplicates 

# my_tuple = [ 1,2,3, "apple","banana",3];
# print(len(my_tuple));  

# my_tuple1 = [ 1,2,3, "apple","banana",3];                               // wrrrrooonng              
# my_tuple2 = [ 4,5,6, "guava","orange",3];
# result = my_tuple1 + my_tuple2 ;
# print(result);


# 3) Dictinary   #  mutable   #unordered  #unique key 

# my_dict  = { 
    
#     "name" : "manu",
#     "age"  : "50",
#     "city" : "mumbai",
    
# }

# print(my_dict["name"])                          #   accesing values 

# my_dict["email"] = "example@gmail.com"          #   adding/ updateing values 

# print(my_dict);

# my_dict.pop("email");                           #   deleting items in dict 

# print(my_dict);

# preety -print the dict 

# w3scools 

# 4) sets    # mutable #unordered 

# my_set = { 1,2,3,"apple","banana",3}
# print(my_set);

# my_set.add("orange");
# print(my_set);

# my_set.remove("orange");
# print(my_set);


# print(my_set[0]);          // cant access 

# write a python script that :

#1. create a list of student names 

students = [ "manu" , "abhi", "megha","chandu","suman","kasturi"];

# 2.dict with student name as key and score as value 

scores = { " satya" : "35" , "manu": "89"};

# 3.add new name and score 

scores["deepika"] = 90

# 4. print the updated dict 

print(scores);


