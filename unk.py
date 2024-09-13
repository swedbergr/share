# Variable for spaces
one = " "
two = "  "
three = "   "
common = f"{one}*{three}*{one}"

# Row 1
# U (s*sss*s)
print(f"{common}", end="")
# N (s*sss*s)
print(f"{common}", end="")
# K (s*sss*s)
print(f"{common}")

# Row 2
# U (s*sss*s)
print(f"{common}", end="")
# N (s*sss*s)
print(f"{common}", end="")
# K (s*ss*ss)
print(f"{one}*{two}*{two}")

# Row 3
# U (s*sss*s)
print(f"{common}", end="")
# N (s**ss*s)
print(f"{one}**{two}*{one}", end="")
# K (s*s*sss)
print(f"{one}*{one}*{three}")

# Row 4
# U (s*sss*s)
print(f"{common}", end="")
# N (s*s*s*s)
print(f"{one}*{one}*{one}*{one}", end="")
# K (s**ssss)
print(f"{one}**{one}{three}")

# Row 5
# U (s*sss*s)
print(f"{common}", end="")
# N (s*ss**s)
print(f"{one}*{two}**{one}", end="")
# K (s*s*sss)
print(f"{one}*{one}*{three}")

# Row 6
# U (s*sss*s)
print(f"{common}", end="")
# N (s*sss*s)
print(f"{common}", end="")
# K (s*ss*ss)
print(f"{one}*{two}*{two}")

# Row 7
# U (ss***ss)
print(f"{two}***{two}", end="")
# N (s*sss*s)
print(f"{common}", end="")
# K (s*sss*s)
print(f"{common}")