year = int(input("Enter a year: "))


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap(year))

# Results C:\Users\Ragner\AppData\Local\Microsoft\WindowsApps\python3.11.exe "C:\Users\Ragner\Desktop\.vscode\project 1.py" 
#Enter a year: 1990
#False

#Process finished with exit code 0
