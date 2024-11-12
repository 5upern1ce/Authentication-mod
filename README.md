# Authentication-mod
GetUserDetails() - Normal username and password input

PassHash(passwd) - Inputs the password and hashes it using bcrypt, also generates the salt in the same function

StoreDetails(user, passwd) - Inputs the password (hashed if hashing is being used), connects it to a local host server set up as logins(db) -> users(table) -> username and password (columns)

Requires bcrypt and mysql.connector
