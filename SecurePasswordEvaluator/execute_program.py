import display_passwd_strength as mod

passwd = input("Enter passwd: ")
result = mod.categorize_passwd(passwd)

print(f"\n- Passwd is {result['rating']}\n- Score: {result['score']}")
print(f"- Entropy: {result['entropy']}\n- Time taken to crack passwd: {result['brute_force_time']} seconds")

if result['issues']:
    print("\n- Potential Weaknesses Found\n")
    for i in result['issues']:
        print("---> ", i)
    print("\n")

else:
    print("- No potential Weaknesses Found\n")

