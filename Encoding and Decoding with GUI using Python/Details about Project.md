This is a simple but useful projects using python 3.8
The working of the script is :
  You have to input your messege and the secret key and then press encode button to encode your messege.
  Then you can send the result.(you tell the secret key secretly to your friend)
  Your friend input your messege and the secret key to retrive your original messege


You need to install two library which we are using there one is tinkter and other one is base64
Tinkter is for the GUI and the base74 is for encoding

Some breakdown of the funtions which are used in code are mentioned in the code
I just explain here the Encode and Decode algo:
  Encode:
enc = [] is an empty list
We run loop till the length of the message
i% of len(key) gives the remainder of division between i and len(key) and that remainder used as an index of key the value of key at that index is stored in key_c
ord() function takes string argument of a single unicode character and return its integer unicode value
chr() function takes an integer argument and returns the string.
ord (message[i]) convert the value of message at index i into the integer value
ord(key_c) converts the key_c value to integer value
ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) and ord( key_c) with 256 and passes that remainder to chr() function
chr() function converts that integer value to string and store to enc
base64.urlsafe_b64encode encode a string.
The join() method joins each element of list, string, and tuple by a string separator and returns the concatenated string.
encode() method returns utf-8 encoded message of the string.
decode() method decodes the string.
return gives the result of the encoded string.


Decode:

enc = [] is an empty list
We run loop till the length of the message
i% of len(key) gives the remainder of division between i and len(key) and that remainder used as an index of key the value of key at that index is stored in key_c
ord() function takes string argument of a single unicode character and return its integer unicode value
chr() function takes an integer argument and returns the string.
ord (message[i]) convert the value of message at index i into the integer value
ord(key_c) converts the key_c value to integer value
ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) and ord( key_c) with 256 and passes that remainder to chr() function
chr() function converts that integer value to string and store to enc
base64.urlsafe_b64encode encode a string.
The join() method joins each element of list, string, and tuple by a string separator and returns the concatenated string.
encode() method returns utf-8 encoded message of the string.
decode() method decodes the string.
return gives the result of the encoded string.
