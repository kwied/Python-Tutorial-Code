formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
# %formatter does not actually get typed out only what is actually in the parenthesis
# % is represented by what is in the parenthesis
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#pritned %r after each of these since that was represented by the variable
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
#commas made it all on one line
# everything in parenthesis is then written in only one quotation mark
