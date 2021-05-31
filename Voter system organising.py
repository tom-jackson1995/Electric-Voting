# The voter system needs to have the following:
# 1 We need to have a Class Object which represents a Candidate who can be elected and have votes assigned to them
# 2 We need to have a Class Object which represents a Voting ballot, this must include Identifying information and each vote being cast and transferd.
# 3 We need to be able to loop through every Vote object and assign it to each candidate object
# 4 Once each vote is assigned we must then rank the candidates by number of votes 
# 5 Based on candidate rankings the system must automatically either declare 1 or more candidate(s) as the Winner(s)
# 6 OR the system must run the process again from step 3 until a winner can be declared
# 7 A User must specifiy the conditions needing to be met for a candidate to win
# 8 The conditions should be pre-selected but dynamically updating, e.g. a user might select a total number of votes needed as the conditional from a selection and then dynamically enter the number desired.
# 9 The individual voter ballots and candidate information needs to be held on a seperate database and the number of candidates and voters needs to be scaleable
# 10 The system needs to both read the database to intialising the Class objects and update each ballot and candidate as votes are assigned during a round.
# 11 There needs to be an external voting interface hosted on the web, this service must take in a voters information and add it to the database
# 12 The final result of each step 3 loop and each step 5 winner must output to the User in a clear and useable manner


