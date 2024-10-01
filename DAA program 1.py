words=["abd","car","ara","cool"]
palindrome=next((word for word in words if word== word[::-1]),"")
print("the first palindrome  is",palindrome)
