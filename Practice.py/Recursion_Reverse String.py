print("Display a Reverse String to use a Recursion.")
String = input("Enter a String to Reverse: ")

def len_Str(String):
    # 1. 'str' ki jagah 'String' variable istemal kiya
    if len(String) <= 1:
        return String
    # 2. Subtraction (-) ki jagah slicing [1:] istemal ki
    # 3. Multiplication (*) ki jagah concatenation (+) istemal ki
    return len_Str(String[1:]) + String[0]
# 4. Fazol extra call hata kar direct variable mein store kiya
Reverse = len_Str(String)
print("Reversed String:", Reverse)