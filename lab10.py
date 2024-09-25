#Charles Bryan Antolijao, 301290232, Cnet232-lab10


def UserInfo():
    info = ['Charles', 'Antolijao', '301290232']
    sep = " "
    print("\nName: ".ljust(20) + info[0] + sep + info[1])
    print("ID: ".ljust(19) + info[2])


def create_marks():
    with open('C:\\Lab10\\marks.txt', 'w') as file:
        file.write(input("\nEnter 10 marks: "))
    with open('C:\\Lab10\\marks.txt', 'r') as file:
        for marks in file:
            print("The entered marks are: " + marks, end=' ')




def find3Max():
    with open('C:\\Lab10\\marks.txt', 'r') as file:
        marks = file.read().split()
        highest_marks = sorted(map(int, marks), reverse=True)
        ascending_marks = sorted(map(int, marks))
        print()
        print("\nThe sorted received marks are: ", ascending_marks)
        return highest_marks[:3]


def output(marks):
    print("\nThe highest 3 marks are:", *marks)


def main():
    UserInfo()
    create_marks()
    top_marks = find3Max()
    output(top_marks)


main()