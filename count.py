def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

def main():
    user_input = input("Enter a sentence: ")
    vowels, consonants = count_vowels_consonants(user_input)
    print(f"\nVowels: {vowels}")
    print(f"Consonants: {consonants}")

if __name__ == "__main__":
    main()
